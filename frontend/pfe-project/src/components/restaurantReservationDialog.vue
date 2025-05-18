<script setup>
import { ref, computed, watch } from 'vue';
import Dialog from 'primevue/dialog';
import Calendar from 'primevue/calendar';
import InputNumber from 'primevue/inputnumber';
import Button from 'primevue/button';
import api from '@/axios';
import { Toast } from 'primevue';
import { useRoute } from 'vue-router';

const props = defineProps({
  tableInfo: {
    type: Object,
    required: true,
    // must include: { id: Number, capacity: Number, location: String }
  },
  visible: { type: Boolean, default: false }
});
const emit = defineEmits(['update:visible', 'reserved']);

const { params } = useRoute();
const establishmentId = params.id;

const form = ref({
  date: null,
  numberOfPeople: 1
});
const errors = ref({});

// capacity from the table object
const maxGuests = computed(() => props.tableInfo.capacity);

// true whenever the user has entered too many guests
const isOverMax = computed(() => form.value.numberOfPeople > maxGuests.value);

// whenever dialog opens, reset form + errors
watch(() => props.visible, v => {
  if (v) {
    form.value.date = null;
    form.value.numberOfPeople = 1;
    errors.value = {};
  }
});

function close() {
  emit('update:visible', false);
}

async function submit() {
  errors.value = {};

  // client-side guard
  if (isOverMax.value) {
    errors.value.numberOfPeople = `Cannot exceed capacity of ${maxGuests.value} guests.`;
    return;
  }

  try {
    await api.post(
      `reservations/restaurants/${establishmentId}/add`,
      {
        table: props.tableInfo.id,
        date: form.value.date,
        numberOfPeople: form.value.numberOfPeople
      }
    );
    emit('reserved');
    close();
    Toast.add({ severity:'success', summary:'Done', detail:'Table reserved!' });
  } catch (err) {
    const data = err.response?.data || {};
    console.error(err);
    for (let k in data) {
      errors.value[k] = Array.isArray(data[k]) ? data[k][0] : data[k];
    }
  }
}
</script>

<template>
  <Dialog 
    :visible="visible" 
    modal 
    header="Reserve Table" 
    @hide="close"
  >
    <div class="p-fluid grid">
      <div class="field col-12">
        <label>
          Table: {{ props.tableInfo.location }} 
          (max {{ maxGuests }} guests)
        </label>
      </div>

      <div class="field col-12">
        <label for="date">Date</label>
        <Calendar v-model="form.date" dateFormat="yy-mm-dd" />
        <small v-if="errors.date" class="p-error">{{ errors.date }}</small>
      </div>

      <div class="field col-12">
        <label for="num">Guests</label>
        <InputNumber
          v-model="form.numberOfPeople"
          :min="1"
          mode="decimal"
        />
        <!-- real-time warning -->
        <small v-if="isOverMax" class="p-error">
          Cannot exceed capacity of {{ maxGuests }} guests.
        </small>
        <!-- server-side or safety error -->
        <small v-else-if="errors.numberOfPeople" class="p-error">
          {{ errors.numberOfPeople }}
        </small>
      </div>
    </div>

    <template #footer>
      <Button label="Cancel" text @click="close" />
      <Button
        label="Reserve"
        severity="success"
        @click="submit"
        :disabled="isOverMax"
      />
    </template>
  </Dialog>
</template>

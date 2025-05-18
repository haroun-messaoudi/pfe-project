<script setup>
import Fieldset from 'primevue/fieldset';
import Button from 'primevue/button';
import api from '@/axios';

// emit “deleted” if you want to notify the parent
const emits = defineEmits(['deleted']);

const props = defineProps({
  id: { type: Number, required: true },
  reservationType: { type: String, required: true },
  estaName: { type: String, required: true },
  Date: { type: String, required: true },
  status: { type: String, required: true },
  numberOfPeople: { type: Number, required: true },
  tableType: { type: String, required: true },
});

const onCancel = async () => {
  try {
    const response = await api.delete(
      `reservations/${props.reservationType}/${props.id}/delete`
    );
    console.log('deleted:', response);
    // let parent remove it from the list
    emits('deleted');
  } catch (err) {
    console.error('Failed to delete restaurant reservation', err);
  }
};
</script>

<template>
  <div class="py-1">
    <Fieldset>
      <template #legend>
        <div class="flex items-center pl-2 gap-3">
          <span class="font-bold p-2">{{ estaName }}</span>
          <Button
            type="button"
            label="Cancel"
            icon="pi pi-times"
            severity="danger"
            @click="onCancel"
          />
          <Button
            type="button"
            label="Accept"
            icon="pi pi-check"
            severity="success"
          />
        </div>
      </template>
      <div>
        <div class="mb-2">
          <span class="font-semibold">Date of Reservation:</span>
          {{ Date }}
        </div>
        <div class="mb-2">
          <span class="font-semibold">Status:</span> {{ status }}
        </div>
        <div class="mb-2">
          <span class="font-semibold">Number of People:</span>
          {{ numberOfPeople }}
        </div>
        <div>
          <span class="font-semibold">Table Type:</span> {{ tableType }}
        </div>
      </div>
    </Fieldset>
  </div>
</template>

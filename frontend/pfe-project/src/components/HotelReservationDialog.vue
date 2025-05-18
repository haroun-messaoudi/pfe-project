<script setup>
import { ref, watch, computed } from 'vue'
import Dialog from 'primevue/dialog'
import Calendar from 'primevue/calendar'
import InputNumber from 'primevue/inputnumber'
import Button from 'primevue/button'
import api from '@/axios'
import { Toast } from 'primevue'
import { useRoute } from 'vue-router';

const props = defineProps({
  roomInfo : {type : Object},
  visible: { type: Boolean, default: false }
})
const emit = defineEmits(['update:visible', 'reserved'])
const { params } = useRoute();
const establishmentId = params.id;

// form fields
const form = ref({
  check_in_date: null,
  check_out_date: null,
  numberOfPeople: 1
})
const errors = ref({})

// load room details when dialog opens
const roomData = ref(null)
watch(() => props.visible, async v => {
  if (v) {
    resetForm()
    await loadRoom()
  }
})

async function loadRoom() {
  try {
    const { data } = await api.get(`reversations/hotels/rooms/${props.roomId}/`) // fetch single room
    roomData.value = data
  } catch (err) {
    console.error('Failed loading room:', err)
  }
}

function resetForm() {
  form.value.check_in_date = null
  form.value.check_out_date = null
  form.value.numberOfPeople = 1
  errors.value = {}
  roomData.value = null
}

// validations
const maxGuests = computed(() => roomData.value?.capacity || 1)
const isOverMax = computed(() => form.value.numberOfPeople > maxGuests.value)
const isDateInvalid = computed(() => {
  const { check_in_date: ci, check_out_date: co } = form.value
  return ci && co ? new Date(ci) >= new Date(co) : false
})

function close() {
  emit('update:visible', false)
  resetForm()
}

async function submit() {
  errors.value = {}
  if (isOverMax.value) {
    errors.value.numberOfPeople = `Cannot exceed capacity of ${maxGuests.value} guests.`
  }
  if (isDateInvalid.value) {
    errors.value.check_out_date = 'Check-out must be after check-in.'
  }
  if (Object.keys(errors.value).length) return

  try {
    await api.post(
      `reservations/hotels/2/add`,
      {
        room: props.roomInfo.id,
        check_in_date: form.value.check_in_date,
        check_out_date: form.value.check_out_date,
        number_of_people: form.value.numberOfPeople
      }
    )

    // Toast.add({ severity: 'success', summary: 'Done', detail: 'Room booked!' })
    emit('reserved')
    close()
  } catch (err) {
    console.log(err)
    const data = err.response?.data || {}
    for (let k in data) {
      errors.value[k] = Array.isArray(data[k]) ? data[k][0] : data[k]
    }
  }
}
</script>

<template>
  <Dialog :visible="visible" modal header="Book a Room" @hide="close">
    <div class="p-fluid grid">
      <div class="field col-6">
        <label for="checkin">Check-In</label>
        <Calendar v-model="form.check_in_date" dateFormat="yy-mm-dd" />
        <small v-if="errors.check_in_date" class="p-error">{{ errors.check_in_date }}</small>
      </div>
      <div class="field col-6">
        <label for="checkout">Check-Out</label>
        <Calendar v-model="form.check_out_date" dateFormat="yy-mm-dd" />
        <small v-if="errors.check_out_date" class="p-error">{{ errors.check_out_date }}</small>
      </div>
      <div class="field col-12">
        <label for="num">Guests (max {{ maxGuests }})</label>
        <InputNumber v-model="form.numberOfPeople" :min="1" mode="decimal" />
        <small v-if="isOverMax" class="p-error">
          Cannot exceed capacity of {{ maxGuests }} guests.
        </small>
        <small v-else-if="errors.numberOfPeople" class="p-error">
          {{ errors.numberOfPeople }}
        </small>
      </div>
    </div>
    <template #footer>
      <Button label="Cancel" text @click="close" />
      <Button
        label="Book"
        severity="success"
        @click="submit"
        :disabled="isOverMax || isDateInvalid"
      />
    </template>
  </Dialog>
</template>
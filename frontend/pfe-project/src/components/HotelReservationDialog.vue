<script setup>
import { ref, watch } from 'vue'
import  Dialog  from 'primevue/dialog'
import  Button  from 'primevue/button'
import Calendar  from 'primevue/calendar'
import InputNumber  from 'primevue/inputnumber'
import api from '@/axios'
import { Toast } from 'primevue'

// props: the hotel’s ID so we know which hotel/room to reserve
const props = defineProps({
  hotelId: { type: [String, Number], required: true },
  visible:   { type: Boolean, default: false }
})
const emit = defineEmits(['update:visible','reserved'])

const form = ref({
  room: null,
  check_in_date: null,
  check_out_date: null,
  number_of_people: 1
})
const errors = ref({})

// Fetch available rooms when dialog opens
async function loadRooms() {
  try {
    const { data } = await api.get(`/hotels/${props.hotelId}/rooms/available/`)
    rooms.value = data
  } catch (e) { console.error(e) }
}
const rooms = ref([])
watch(() => props.visible, v => v && loadRooms())

function close() {
  emit('update:visible', false)
  form.value = { room: null, check_in_date: null, check_out_date: null, number_of_people: 1 }
  errors.value = {}
}

async function submit() {
  errors.value = {}
  try {
    const payload = { ...form.value }
    await api.post(`/reservations/hotel/create/`, payload)
    emit('reserved')
    close()
    Toast.add({ severity:'success', summary:'Done', detail:'Hotel booked!' })
  } catch (err) {
    // map DRF errors into our `errors` object
    const data = err.response?.data || {}
    for (let key in data) {
      errors.value[key] = Array.isArray(data[key]) ? data[key][0] : data[key]
    }
  }
}
</script>

<template>
  <Dialog :visible="visible" modal header="Book a Room" @hide="close">
    <div class="p-fluid grid">
      <div class="field col-12">
        <label for="room">Room</label>
        <Dropdown v-model="form.room" :options="rooms" optionLabel="room_type" optionValue="id" />
        <small v-if="errors.room" class="p-error">{{ errors.room }}</small>
      </div>
      <div class="field col-6">
        <label for="checkin">Check-In</label>
        <Calendar v-model="form.check_in_date" dateFormat="yy-mm-dd"/>
        <small v-if="errors.check_in_date" class="p-error">{{ errors.check_in_date }}</small>
      </div>
      <div class="field col-6">
        <label for="checkout">Check-Out</label>
        <Calendar v-model="form.check_out_date" dateFormat="yy-mm-dd"/>
        <small v-if="errors.check_out_date" class="p-error">{{ errors.check_out_date }}</small>
      </div>
      <div class="field col-12">
        <label for="num">Guests</label>
        <InputNumber v-model="form.number_of_people" :min="1"/>
        <small v-if="errors.number_of_people" class="p-error">{{ errors.number_of_people }}</small>
      </div>
    </div>
    <template #footer>
      <Button label="Cancel" text @click="close"/>
      <Button label="Book" severity="success" @click="submit"/>
    </template>
  </Dialog>
</template>

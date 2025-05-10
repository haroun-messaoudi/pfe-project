<script setup>
import { ref, watch } from 'vue'
import  Dialog  from 'primevue/dialog'
import Button  from 'primevue/button'
import  Calendar  from 'primevue/calendar'
import  InputNumber  from 'primevue/inputnumber'
import api from '@/axios'
import { Toast } from 'primevue'

// props: restaurant ID for fetching tables
const props = defineProps({
  restaurantId: { type: [String, Number], required: true },
  visible:      { type: Boolean, default: false }
})
const emit = defineEmits(['update:visible','reserved'])

const form = ref({
  table: null,
  date: null,
  numberOfPeople: 1
})
const errors = ref({})
const tables = ref([])

async function loadTables() {
  const { data } = await api.get(`/restaurants/${props.restaurantId}/tables/available/`)
  tables.value = data
}
watch(() => props.visible, v => v && loadTables())

function close() {
  emit('update:visible', false)
  form.value = { table: null, date: null, numberOfPeople: 1 }
  errors.value = {}
}

async function submit() {
  errors.value = {}
  try {
    const payload = { ...form.value }
    await api.post(`/reservations/restaurant/create/`, payload)
    emit('reserved')
    close()
    Toast.add({ severity:'success', summary:'Done', detail:'Table reserved!' })
  } catch (err) {
    const data = err.response?.data || {}
    for (let k in data) errors.value[k] = Array.isArray(data[k]) ? data[k][0] : data[k]
  }
}
</script>

<template>
  <Dialog :visible="visible" modal header="Reserve a Table" @hide="close">
    <div class="p-fluid grid">
      <div class="field col-12">
        <label for="table">Table</label>
        <Dropdown v-model="form.table" :options="tables" optionLabel="location" optionValue="id"/>
        <small v-if="errors.table" class="p-error">{{ errors.table }}</small>
      </div>
      <div class="field col-12">
        <label for="date">Date</label>
        <Calendar v-model="form.date" dateFormat="yy-mm-dd"/>
        <small v-if="errors.date" class="p-error">{{ errors.date }}</small>
      </div>
      <div class="field col-12">
        <label for="num">Guests</label>
        <InputNumber v-model="form.numberOfPeople" :min="1"/>
        <small v-if="errors.numberOfPeople" class="p-error">{{ errors.numberOfPeople }}</small>
      </div>
    </div>
    <template #footer>
      <Button label="Cancel" severity="warn" text @click="close"/>
      <Button label="Reserve" severity="warn" @click="submit"/>
    </template>
  </Dialog>
</template>

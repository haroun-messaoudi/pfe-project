<script setup>
import Fieldset from 'primevue/fieldset'
import Button from 'primevue/button'
import ConfirmDialog from 'primevue/confirmdialog'
import { useConfirm } from 'primevue/useconfirm'
import api from '@/axios'
import { useReservationsStore } from '@/stores/reservations'

const reservationsStore = useReservationsStore()
const confirm = useConfirm()

const props = defineProps({
  estaName: {
    type: String,
    required: true
  },
  id: {
    type: [String, Number],
    required: true
  },
  checkInDate: {
    type: String,
    required: true
  },
  checkOutDate: {
    type: String,
    required: true
  },
  status: {
    type: String,
    required: true
  },
  numberOfPeople: {
    type: Number,
    required: true
  },
  roomType: {
    type: String,
    required: true
  }
})

async function cancelReser() {
  try {
    await api.delete(`reservations/hotels/${props.id}/cancel`)
    await reservationsStore.fetchReservations()
  }
  catch (err) {
    console.error(err)
  }
}

function confirmCancel() {
  confirm.require({
    message: `Do you really want to cancel your stay at "${props.estaName}" from ${props.checkInDate} to ${props.checkOutDate}?`,
    header: 'Please Confirm',
    icon: 'pi pi-exclamation-triangle',
    accept: () => {
      cancelReser()
    },
    reject: () => {
      // no-op
    }
  })
}
</script>

<template>
  <div>
  <!-- mount this once per component tree -->
  <ConfirmDialog />

    <div>
      <Fieldset>
        <template #legend>
          <div class="flex items-center pl-2">
            <span class="font-bold p-2">{{ props.estaName }}</span>
            <Button
              type="button"
              label="Cancel"
              icon="pi pi-times"
              severity="danger"
              @click="confirmCancel"
            />
          </div>
        </template>

        <div>
          <div class="mb-2">
            <span class="font-semibold">Check-In Date:</span>
            {{ props.checkInDate }}
          </div>
          <div class="mb-2">
            <span class="font-semibold">Check-Out Date:</span>
            {{ props.checkOutDate }}
          </div>
          <div class="mb-2">
            <span class="font-semibold">Status:</span> {{ props.status }}
          </div>
          <div class="mb-2">
            <span class="font-semibold">Number of People:</span>
            {{ props.numberOfPeople }}
          </div>
          <div>
            <span class="font-semibold">Room Type:</span> {{ props.roomType }}
          </div>
        </div>
      </Fieldset>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
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
  date: {
    type: String,
    required: true
  },
  status: {
    type: String,
    required: true
  },
  table_location: {
    type: String,
    required: true
  },
  numberOfPeople: {
    type: String,
    required: true
  },
  id: {
    type: [String, Number],
    required: true
  }
})

async function cancelReser() {
  try {
    await api.delete(`reservations/restaurants/${props.id}/cancel`)
    await reservationsStore.fetchReservations()
  }
  catch(err) {
    console.error(err)
  }
}

// new: wrap cancel in confirm dialog
function confirmCancel() {
  confirm.require({
    message: `Do you really want to cancel your reservation at "${props.estaName}"?`,
    header: 'Please Confirm',
    icon: 'pi pi-exclamation-triangle',
    accept: () => {
      cancelReser()
    },
    reject: () => {
      // nothing to do
    }
  })
}
</script>

<template>
  <!-- PrimeVue’s ConfirmDialog must be mounted at root of this component -->
  <div>
  <ConfirmDialog />

  <div>
    <Fieldset>
      <template #legend>
        <div class="flex items-center pl-2">
          <span class="font-bold p-2">{{ props.estaName }}</span>
          <!-- now calls our confirm wrapper -->
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
          <span class="font-semibold">Date Of The Reservation:</span>
          {{ props.date }}
        </div>
        <div class="mb-2">
          <span class="font-semibold">Status:</span> {{ props.status }}
        </div>
        <div class="mb-2">
          <span class="font-semibold">Number of People:</span>
          {{ props.numberOfPeople }}
        </div>
        <div>
          <span class="font-semibold">Table Location:</span>
          {{ props.table_location }}
        </div>
      </div>
    </Fieldset>
  </div>
  </div>
</template>

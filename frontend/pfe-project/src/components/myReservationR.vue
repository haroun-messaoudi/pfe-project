<script setup>
import Fieldset from 'primevue/fieldset';
import Button from 'primevue/button';
import api from '@/axios';

import { useReservationsStore } from '@/stores/reservations'

const reservationsStore = useReservationsStore()

const props= defineProps( {
    estaName:{
        type:String,
        required:true
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
    type: [String, Number], // Match the type you're passing as :key
    required: true
    },
  })

async function cancelReser(){
  try{
    await api.delete(`reservations/restaurants/${props.id}/cancel`)
    await reservationsStore.fetchReservations()
  }catch(errr){
    console.log(errr)
  }
}


</script>

<template>
    <div class="">
        <Fieldset>  
            <template #legend>
                <div class="flex items-center pl-2">
                    <span class="font-bold p-2">{{ props.estaName }}</span>
                    <Button type="button" label="Cancel" icon="pi pi-times"severity="danger" @click="cancelReser"/>
                </div>
            </template>
            <div >
                <div class="mb-2"><span class="font-semibold">Date Of The Reservation:</span> {{ props.date }}</div>
                <div class="mb-2"><span class="font-semibold">Status:</span> {{ props.status }}</div>
                <div class="mb-2"><span class="font-semibold">Number of People:</span> {{ props.numberOfPeople }}</div>
                <div><span class="font-semibold">Table Location:</span> {{ props.table_location }}</div>
            </div>
        </Fieldset>
        


    </div>
</template>
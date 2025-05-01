<script setup>
import Fieldset from 'primevue/fieldset';
import Button from 'primevue/button';
const props= defineProps( {
    estaName:{
        type:String,
        required:true
    },
    checkInDate: {
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
    },
    checkOutDate: {
      type: String,
      required: true
    }
  })

</script>

<template>
    <div class="py-1">
        <Fieldset>  
            <template #legend>
                <div class="flex items-center pl-2 gap-3">
                    <span class="font-bold p-2">{{ props.estaName }}</span>
                    <Button type="button" label="Cancel" icon="pi pi-times"severity="danger" />
                    <Button type="button" label="Accept" icon="pi pi-check"severity="succes" />
                </div>
            </template>
            <div >
                <div class="mb-2"><span class="font-semibold">Check-In Date:</span> {{ props.checkInDate }}</div>
                <div class="mb-2"><span class="font-semibold">Check-Out Date:</span> {{ props.checkOutDate }}</div>
                <div class="mb-2"><span class="font-semibold">Status:</span> {{ props.status }}</div>
                <div class="mb-2"><span class="font-semibold">Number of People:</span> {{ props.numberOfPeople }}</div>
                <div><span class="font-semibold">Room Type:</span> {{ props.roomType }}</div>
            </div>
        </Fieldset>
        


    </div>
</template>
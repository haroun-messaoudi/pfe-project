<script setup>
import Fieldset from 'primevue/fieldset';
import Button from 'primevue/button';
const props= defineProps( {
    estaName:{
        type:String,
        required:true
    },
    Date: {
      type: String,
      required: true
    },
    status: {
      type: String,
      required: true
    },
    tableType: {
      type: String,
      required: true
    },
    numberOfPeople: {
      type: String,
      required: true
    }
  })
</script>

<template>
    <div class="">
        <Fieldset>  
            <template #legend>
                <div class="flex items-center pl-2">
                    <span class="font-bold p-2">{{ props.estaName }}</span>
                    <Button type="button" label="Cancel" icon="pi pi-times"severity="danger" />
                </div>
            </template>
            <div >
                <div class="mb-2"><span class="font-semibold">Date Of The Reservation:</span> {{ props.Date }}</div>
                <div class="mb-2"><span class="font-semibold">Status:</span> {{ props.status }}</div>
                <div class="mb-2"><span class="font-semibold">Number of People:</span> {{ props.numberOfPeople }}</div>
                <div><span class="font-semibold">Table Type:</span> {{ props.tableType }}</div>
            </div>
        </Fieldset>
        


    </div>
</template>
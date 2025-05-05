<script setup>
import { Fieldset } from 'primevue';
const  props = defineProps( {
    reviewerName: {
      type: String,
      required: true,
    },
    rating: {
      type: Number,
      required: true,
      validator: (value) => value >= 0 && value <= 5
    },
    comment: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    }
  }
  )
</script>



<template>
<Fieldset>
    <template #legend>
                <div class="flex items-center pl-2 gap-3">
                    <span class="font-bold p-2">{{ props.reviewerName }}</span>
                </div>
            </template>
    <div class="p-4 border-0 rounded-lg w-full max-w-md">
        <div class="mb-2 flex items-center">
            <span class="font-semibold mr-2">Rating:</span>
            <div class="text-orange-500 text-lg">
                <span v-for="n in 5" :key="n">
                    <span v-if="n <= rating">★</span>
                    <span v-else>☆</span>
                </span>
            </div>
        </div>
        <div class="mb-2"><span class="font-semibold">Comment:</span> {{ comment }}</div>
        <div><span class="font-semibold">Date:</span> {{ date }}</div>
    </div>

</Fieldset>
</template>
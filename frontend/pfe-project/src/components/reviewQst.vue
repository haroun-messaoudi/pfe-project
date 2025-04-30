<script setup>
import Rating from 'primevue/rating'
const props = defineProps({
    question: {
    type: String,
    required: true
  }
});
</script>


<template>
<div class="flex  gap-4 mb-4">
      <label for="rating" class="font-semibold ">{{ props.question }}</label>
      <Rating id="rating"   />
    </div>

    

</template>
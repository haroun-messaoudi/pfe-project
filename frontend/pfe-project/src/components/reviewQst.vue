<script setup>
import Rating from 'primevue/rating'
import { ref, watch } from 'vue'

const props = defineProps({
  question: {
    type: String,
    required: true,
  },
  id: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits(['update-answer'])

const rating = ref(0)

watch(rating, (newRating) => {
  console.log('New Rating in reviewQst:', { questionId: props.id, rating: newRating })
  emit('update-answer', { question: props.id, rating: newRating })
})
</script>

<template>
  <div class="flex gap-4 mb-4">
    <label for="rating" class="font-semibold">{{ props.question }}</label>
    <Rating id="rating" v-model="rating" />
  </div>
</template>
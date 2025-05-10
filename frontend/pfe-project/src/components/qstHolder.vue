<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import reviewQst from './reviewQst.vue'
import { useRoute } from 'vue-router'
import { useSearchStore } from '@/stores/searchStore'
import { useTopEstablishmentsStore } from '@/stores/topestablishments'
import { useQuestionsStore } from '@/stores/questionsStore'
import Textarea from 'primevue/textarea'   // Import Textarea component

// Emit events to parent


const questionsStore = useQuestionsStore()
const route = useRoute()
const searchStore = useSearchStore()
const topEstablishmentsStore = useTopEstablishmentsStore()

const questions = ref([])
const answers = ref([])

const props = defineProps({
  modelValue: {                // this is the v-model prop
    type: String,
    default: ''
  }
})
const emit = defineEmits(['update:modelValue', 'update-answers'])

const reviewText = ref(props.modelValue)
watch(reviewText, val => emit('update:modelValue', val))


onMounted(async () => {
  const establishment = computed(() => {
    const id = route.params.id
    return (
      searchStore.results.find(item => item.objectID === id) ||
      topEstablishmentsStore.bestHotels.hits?.find(item => item.objectID === id) ||
      topEstablishmentsStore.bestRestaurants.hits?.find(item => item.objectID === id)
    )
  })
  if (establishment.value?.type === 'restaurant') {
    await questionsStore.fetchRestaurantQuestions()
    questions.value = questionsStore.restaurantQuestions
  } else if (establishment.value?.type === 'hotel') {
    await questionsStore.fetchHotelQuestions()
    questions.value = questionsStore.hotelQuestions
  } else {
    console.log('No establishment found')
  }
})



function updateAnswer(newAnswer) {
  const index = answers.value.findIndex(a => a.question === newAnswer.question)
  if (index !== -1) answers.value[index].rating = newAnswer.rating
  else answers.value.push(newAnswer)
  emit('update-answers', answers.value)
}

</script>

<template>
  <div>
    <div v-for="(quest, index) in questions" :key="index" class="flex items">
      <reviewQst
        :question="quest.question"
        :id="quest.id"
        @update-answer="updateAnswer"
      />
    </div>

    <div class="flex items-start gap-4 mb-4 mt-4">
      <label for="reviewText" class="font-semibold w-24">Review</label>
      <Textarea
        id="reviewText"
        v-model="reviewText"
        autoResize
        rows="4"
        class="flex-auto"
      />
    </div>
  </div>
</template>

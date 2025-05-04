<script setup>
import { ref, defineProps } from 'vue'
import Rating from 'primevue/rating'
import Galleria from 'primevue/galleria'
import HotelExtra from './hotelExtra.vue'
import Card from './card.vue'
import Panel from 'primevue/panel'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import Textarea from 'primevue/textarea'
import qstHolder from './qstHolder.vue'
import restaurantExra from './restaurantExra.vue'
import SplitButton from 'primevue/splitbutton'
import { useRoute, useRouter } from 'vue-router'
import api from '@/axios'
import { Toast } from 'primevue'

const props = defineProps({
  name: String,
  city: String,
  type: String,
  phone: String,
  email: String,
  location: String,
  images: Array,
  value: Number,
  amenities: Array,
  description: String,
  checkin: String,
  checkout: String,
  stars: Number,
  menuItems: Array,
  cuisineType: String,
})

// Review Dialog state
const reviewDialogVisible = ref(false)
const reviewText = ref('')
const reviewAnswers = ref([])

const route = useRoute()
function CloseReviewDialog() {
  reviewAnswers.value = []
  reviewText.value    = ''
  reviewDialogVisible.value = false
}

async function submitReview() {
  try {
    const id = route.params.id
    const payload = {
      content: reviewText.value,
      answers: reviewAnswers.value.value,
    }

    console.log('Submitting Review Payload:', payload) // Debugging payload

    const response = await api.post(`/reviews/add/${id}/`, payload)
    console.log('Review submitted successfully:', response.data)

    // Reset form
    reviewText.value = ''
    reviewAnswers.value = []
    reviewDialogVisible.value = false
    Toast.add({
      severity: 'success',
      summary: 'Success',
      detail: 'Review submitted successfully!',
      life: 3000,
      
    })
  } catch (error) {
    console.error('Failed to submit review:', error.response?.data || error)
  }
}
</script>

<template>
  <div class="flex gap-4 bg-orange-100 p-5 m-5 border-0 rounded-lg">
    <!-- Carousel Section using Galleria -->
    <div class="w-96">
      <Galleria
        :value="props.images"
        :responsiveOptions="responsiveOptions"
        :numVisible="3"
        :circular="true"
        :showItemNavigators="true"
        :showThumbnails="true"
        containerStyle="max-width: 384px"
      >
        <template #item="slotProps">
          <img
            :src="slotProps.item.itemImageSrc"
            :alt="slotProps.item.alt"
            class="w-full h-96 object-cover rounded-lg"
          />
        </template>
        <template #thumbnail="slotProps" class="p-2">
          <img
            :src="slotProps.item.thumbnailImageSrc"
            :alt="slotProps.item.alt"
            class="object-cover h-20 w-20 rounded-md"
          />
        </template>
      </Galleria>
    </div>

    <!-- Establishment Info Section -->
    <div class="px-10">
      <h1 class="font-serif font-bold text-4xl mb-2">{{ props.name }}</h1>
      <div class="mb-2">{{ props.type }}</div>
      <div class="flex mb-2">
        <div class="font-bold mr-2">Phone Number:</div>
        <div>{{ props.phone }}</div>
      </div>
      <div class="flex mb-2">
        <div class="font-bold mr-2">E-mail:</div>
        <div>{{ props.email }}</div>
      </div>
      <div class="flex mb-2">
        <div class="font-bold mr-2">Location:</div>
        <div>{{ props.location }}</div>
      </div>

      <div class="card flex items-center mt-4">
        <div class="font-bold mr-2">Average Rating:</div>
        <Rating
          :modelValue="props.value"
          readonly
          :style="{ '--p-rating-icon-size': '25px', '--p-rating-icon-active-color': '#E97451' }"
        />
      </div>

      <HotelExtra
        v-if="props.type == 'hotel'"
        :amenities="props.amenities"
        :checkInTime="props.checkin"
        :checkOutTime="props.checkout"
        :stars="props.stars"
      />
      <restaurantExra
        v-if="props.type == 'restaurant'"
        :menu="props.menuItems"
        :cuisineType="props.cuisineType"
      />
    </div>

    <!-- Description and Buttons -->
    <div class="flex flex-col flex-1">
      <Panel class="h-5/6 w-full flex-none min-w-full" header="description">
        <p class="m-0">{{ props.description }}</p>
      </Panel>
      <div class="flex gap-10 py-5 justify-center">
        <Button label="Add A Review" severity="success" raised @click="reviewDialogVisible = true" />
        <SplitButton label="Make a Reservation" :model="reservationItems" raised severity="info" />
      </div>
    </div>

    <!-- Review Dialog -->
    <Dialog v-model:visible="reviewDialogVisible" modal header="Add Your Review" :style="{ width: '30rem' }">
      <template #header>
        <div class="inline-flex items-center justify-center gap-2">
          <i class="pi pi-comment text-xl"></i>
          <span class="font-bold">Leave a Review</span>
        </div>
      </template>

      <span class="text-surface-500 dark:text-surface-400 block mb-4">Tell us what you think about this place.</span>
      <div>
        <qstHolder
          @update-answers="(val) => {
            reviewAnswers.value = val
            console.log('Received Answers in establishementCard:', val)
          }"
          v-model="reviewText"
        />
      </div>
      <template #footer>
        <Button label="Cancel" text severity="secondary" @click="CloseReviewDialog" />
        <Button label="Submit" severity="success" @click="submitReview" />
      </template>
    </Dialog>
  </div>
</template>
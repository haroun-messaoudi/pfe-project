<script setup>
import { ref, defineProps } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Rating from 'primevue/rating'
import Galleria from 'primevue/galleria'
import Panel from 'primevue/panel'
import Dialog from 'primevue/dialog'
import Message from 'primevue/message'
import SplitButton from 'primevue/splitbutton'
import Button from 'primevue/button'
import HotelExtra from './hotelExtra.vue'
import restaurantExtra from './restaurantExra.vue'
import hotelReservationDialog from './hotelReservationDialog.vue'
import restaurantReservationDialog from './restaurantReservationDialog.vue'
import qstHolder from './qstHolder.vue'
import { useUserStore } from '@/stores/user'
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

const userStore = useUserStore()
const route = useRoute()
const router = useRouter()

// --- Review dialog state & methods ---
const reviewDialogVisible = ref(false)
const reviewText = ref('')
const reviewAnswers = ref([])
const errorMessages = ref([])

function CloseReviewDialog() {
  reviewAnswers.value = []
  reviewText.value = ''
  errorMessages.value = []
  reviewDialogVisible.value = false
}

async function submitReview() {
  try {
    const id = route.params.id
    await api.post(`/reviews/add/${id}/`, {
      content: reviewText.value,
      answers: reviewAnswers.value.value,
    })
    CloseReviewDialog()
    Toast.add({ severity: 'success', summary: 'Success', detail: 'Review submitted!', life: 3000 })
  } catch (err) {
    const data = err.response?.data || {}
    errorMessages.value = []
    if (data.content)    errorMessages.value.push('Please type a review.')
    if (data.answers)    errorMessages.value.push('Please fill all the answers.')
    if (data.detail)     errorMessages.value.push(data.detail[0])
    if (!err.response)   errorMessages.value.push('Unexpected error. Please try again.')
  }
}

// --- Navigation & Quick-reservation state & methods ---
const hotelDialogVisible = ref(false)
const restaurantDialogVisible = ref(false)

function navigateToReservation() {
  const id = route.params.id
  if (props.type === 'hotel') {
    router.push({ name: 'roomsList', params: { id } })
  } else {
    router.push({ name: 'tablesList', params: { id } })
  }
}

function quickReservation() {
  if (props.type === 'hotel') {
    hotelDialogVisible.value = true
  } else {
    restaurantDialogVisible.value = true
  }
}

const reservationItems = [
  {
    label: 'Quick Reservation',
    icon: 'pi pi-fast-forward',
    command: quickReservation
  }
]

// optional callback when a quick reservation completes
function onReserved() {
  hotelDialogVisible.value = false
  restaurantDialogVisible.value = false
}
</script>

<template>
  <div class="flex gap-4 bg-orange-100 p-5 m-5 rounded-lg">
    <!-- Carousel -->
    <div class="w-96">
      <Galleria
        :value="props.images"
        :responsiveOptions="responsiveOptions"
        :numVisible="3"
        circular
        showItemNavigators
        showThumbnails
        containerStyle="max-width: 384px"
      >
        <template #item="{ item }">
          <img :src="item.itemImageSrc" :alt="item.alt" class="w-full h-96 object-cover rounded-lg" />
        </template>
        <template #thumbnail="{ item }">
          <img :src="item.thumbnailImageSrc" :alt="item.alt" class="object-cover h-20 w-20 rounded-md" />
        </template>
      </Galleria>
    </div>

    <!-- Info -->
    <div class="px-10">
      <h1 class="font-serif font-bold text-4xl mb-2">{{ props.name }}</h1>
      <div class="mb-2">{{ props.type }}</div>
      <div class="flex mb-2"><span class="font-bold mr-2">Phone:</span>{{ props.phone }}</div>
      <div class="flex mb-2"><span class="font-bold mr-2">E-mail:</span>{{ props.email }}</div>
      <div class="flex mb-2"><span class="font-bold mr-2">Location:</span>{{ props.location }}</div>
      <div class="card flex items-center mt-4">
        <span class="font-bold mr-2">Avg. Rating:</span>
        <Rating
          :modelValue="props.value"
          readonly
          :style="{ '--p-rating-icon-size': '25px', '--p-rating-icon-active-color': '#E97451' }"
        />
      </div>

      <HotelExtra
        v-if="props.type === 'hotel'"
        :amenities="props.amenities"
        :checkInTime="props.checkin"
        :checkOutTime="props.checkout"
        :stars="props.stars"
      />
      <restaurantExtra
        v-else
        :menu="props.menuItems"
        :cuisineType="props.cuisineType"
      />
    </div>

    <!-- Description & Actions -->
    <div class="flex flex-col flex-1">
      <Panel class="h-5/6 w-full" header="Description">
        <p class="m-0">{{ props.description  }}</p>
      </Panel>
      <div class="flex gap-6 py-5 justify-center" v-if="userStore.isAuthenticated">
        <Button label="Add A Review" severity="warn" raised @click="reviewDialogVisible = true" />

        <SplitButton v-if="props.type == 'hotel'"
          label="Make a Reservation"
          icon="pi pi-calendar"
          severity="info"
          raised
          :model="reservationItems"
          @click="navigateToReservation"
        />
        <Button v-else
          label="Make a Reservation"
          icon="pi pi-calendar"
          severity="info"
          @click="navigateToReservation"
        />
      </div>
    </div>

    <!-- Review Dialog -->
    <Dialog v-model:visible="reviewDialogVisible" modal header="Add Your Review" style="width:30rem">
      <template #header>
        <div class="inline-flex items-center gap-2">
          <i class="pi pi-comment text-xl"></i>
          <span class="font-bold">Leave a Review</span>
        </div>
      </template>

      <span class="block mb-4">Tell us what you think about this place.</span>

      <div v-if="errorMessages.length" class="mb-4">
        <Message
          v-for="(msg,i) in errorMessages"
          :key="i"
          severity="error"
          text
        >
          {{ msg }}
        </Message>
      </div>

      <qstHolder @update-answers="val => reviewAnswers.value = val" v-model="reviewText" />

      <template #footer>
        <Button label="Cancel" severity="warn" text @click="CloseReviewDialog" />
        <Button label="Submit" severity="warn" @click="submitReview" />
      </template>
    </Dialog>

    <!-- Quick‐reservation Dialogs -->
    <hotelReservationDialog
      v-model:visible="hotelDialogVisible"
      :establishmentId="route.params.id"
      @reserved="onReserved"
    />
    <restaurantReservationDialog
      v-model:visible="restaurantDialogVisible"
      :establishmentId="route.params.id"
      @reserved="onReserved"
    />
  </div>
</template>

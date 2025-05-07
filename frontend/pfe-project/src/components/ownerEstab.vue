<script setup>
import { ref, defineProps, onMounted, computed } from 'vue'
import Rating from 'primevue/rating'
import Galleria from 'primevue/galleria'
import HotelExtra from './hotelExtra.vue'
import Panel from 'primevue/panel'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import Textarea from 'primevue/textarea'
import restaurantExra from './restaurantExra.vue'
import SplitButton from 'primevue/splitbutton'
import { useRouter } from 'vue-router'
import { useProfileStore } from '@/stores/profile'

const profileStore = useProfileStore()



// ✅ Props preserved exactly with required fields
const props = defineProps({
  name: {
    type: String,
    required: true
  },
  type: {
    type: String,
    required: true
  },
  phone: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true
  },
  location: {
    type: String,
    required: true
  },
  images: {
    type: Array,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  averageRating: {
    type: Number,
    required: true

  },
  menuItems: {
    type: Array,

  },
  cuisineType: {
    type: String,

  },
  amenities:{
    type:Array
  },
  checkin:{
    type : String
  },
  checkout:{
    type:String
  },
  stars:{
    type: Number
  }
})


const amenities  = props.amenities?.map((item,index)=>(item.name ))
console.log('Props:', props)

// Review Dialog state
const reviewDialogVisible = ref(false)
const reviewText = ref('')
const reviewRating = ref(0)

function submitReview() {
  console.log('Review Submitted:')
  console.log('Rating:', reviewRating.value)
  console.log('Review:', reviewText.value)

  // Reset form
  reviewRating.value = 0
  reviewText.value = ''
  reviewDialogVisible.value = false

  // Optional: emit or store the review
}

// Galleria responsive settings
const responsiveOptions = ref([
  {
    breakpoint: '1300px',
    numVisible: 4
  },
  {
    breakpoint: '575px',
    numVisible: 1
  }
])

// SplitButton items
const reservationItems = [
  {
    label: 'Make a Quick Reservation',
    icon: 'pi pi-clock',
    command: () => {
      document.querySelector('#quick-reservation-link')?.click()
    }
  }
]

function goToReservation() {
  document.querySelector('#main-reservation-link')?.click()
}

const galleryImages = computed(() => {
  return props.images?.map((url, index) => ({
    itemImageSrc: url,
    thumbnailImageSrc: url,
    alt: `Image ${index + 1}`
  }))
})


</script>

<template>
  <div class="flex gap-4 bg-orange-100 p-5 m-5 border-0 rounded-lg">
    <!-- Carousel Section using Galleria -->
    <div class="w-96">
      <Galleria
        :value="galleryImages"
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
        <template class="p-2" #thumbnail="slotProps">
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
          :modelValue="props.averageRating"
          readonly
          :style="{ '--p-rating-icon-size': '25px', '--p-rating-icon-active-color': '#E97451' }"
        />
      </div>
      <restaurantExra v-if="props.type=='restaurant'"
      :menu="props.menuItems"
      :cuisineType="props.cuisineType"
      />
      <hotelExtra v-if="props.type=='hotel'"
      :amenities="amenities"
      :checkInTime="props.checkin"
      :checkOutTime="props.checkout"
      :stars="props.stars"
      />
    </div>

    <!-- Description and Buttons -->
    <div class="flex flex-col flex-1">
      <Panel class="h-5/6 w-full flex-none" header="description">
        <p class="m-0">
          {{ props.description }}
        </p>
      </Panel>
      <div class="flex gap-10 py-5 justify-center">
        <RouterLink to="/ownerPage/establishement">
        <Button label="update My Establishement" severity="warn" raised/>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

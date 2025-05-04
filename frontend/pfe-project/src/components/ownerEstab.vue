<script setup>
import { ref, defineProps } from 'vue'
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

const menuItems = [
  {
    name: "Margherita Pizza",
    description: "Classic pizza with tomatoes, mozzarella, and fresh basil.",
    price: 12
  },
  {
    name: "Pasta Carbonara",
    description: "Pasta with creamy sauce, pancetta, and parmesan.",
    price: 15
  },
  {
    name: "Tiramisu",
    description: "Coffee-flavored Italian dessert with mascarpone cream.",
    price: 8
  }
]
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
  value: {
    type: Number,
    required: true
  }
})

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
          :modelValue="props.value"
          readonly
          :style="{ '--p-rating-icon-size': '25px', '--p-rating-icon-active-color': '#E97451' }"
        />
      </div>
      <restaurantExra
      :menu="menuItems"
      cuisineType="Italian"
      />
    </div>

    <!-- Description and Buttons -->
    <div class="flex flex-col flex-1">
      <Panel class="h-5/6 w-full flex-none" header="description">
        <p class="m-0">
          The Panoramic Hotel is a modern, elegant 4-star hotel overlooking the sea, perfect for a romantic, charming vacation, in the enchanting setting of Taormina and the Ionian Sea.
          The rooms at the Panoramic Hotel are new, well-lit and inviting. Our reception staff will be happy to help you during your stay in Taormina, suggesting itineraries, guided visits and some good restaurants in the historic centre.
          While you enjoy a cocktail by the swimming pool on the rooftop terrace, you will be stunned by the breathtaking view of the bay of Isola Bella. Here, during your summer stays, our bar serves traditional Sicilian dishes, snacks and salads.
          At the end of a stairway across from the hotel, the white pebbles on the beach of Isola Bella await you as well as beach facilities with lounge chairs and umbrellas and areas with free access to the pristine clear sea that becomes deep just a few metres from the shore.
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

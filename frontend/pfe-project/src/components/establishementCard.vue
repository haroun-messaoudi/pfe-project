<script setup>
import Rating from 'primevue/rating'
import Galleria from 'primevue/galleria'
import HotelExtra from './hotelExtra.vue'
import { defineProps, ref } from 'vue'
import Card from './card.vue'

// Props for the restaurant details
const props = defineProps({
  name: {
    type: String,
    required: true
  },
  city: {
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
  },
  amenities: {
    type: Array,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  checkin: {
    type: String,
    required: true
  },
  checkout: {
    type: String,
    required: true
  },
  stars: {
    type: Number,
    required: true
  }
})

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

console.log('amenities', props.amenities)


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
        <template #thumbnail="slotProps" class="p-2" >
          <img
            :src="slotProps.item.thumbnailImageSrc"
            :alt="slotProps.item.alt"
            class="object-cover h-20 w-20 rounded-md"
          />
        </template>
      </Galleria>
    </div>

    <!-- Establishment Info Section -->
    <div>
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
        :amenities=props.amenities
        :checkInTime="props.checkin"
        :checkOutTime="props.checkout"
        :stars="props.stars"
      />
    </div>
  </div>
</template>

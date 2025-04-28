<script setup>
import Rating from 'primevue/rating'
import hotelExtra from './hotelExtra.vue'
import { ref } from 'vue'
import HotelExtra from './hotelExtra.vue'

// List of image paths
const images = [
  new URL('/src/assets/img/rest.webp', import.meta.url).href,
  new URL('/src/assets/img/hrn.png', import.meta.url).href,
  new URL('/src/assets/img/rafiki.png', import.meta.url).href
]

const currentImage = ref(0)

const nextImage = () => {
  currentImage.value = (currentImage.value + 1) % images.length
}

const prevImage = () => {
  currentImage.value = (currentImage.value - 1 + images.length) % images.length
}

const value = 4
</script>

<template>
    <div class="flex gap-4 bg-orange-100 p-5 m-5 border-0 rounded-lg">
        <!-- Carousel Section -->
        <div class="relative w-96 h-96 overflow-hidden rounded-lg">
            <img
            :src="images[currentImage]"
            alt="Carousel Image"
            class="w-full h-full object-cover transition-all duration-500"
            />

        <!-- Previous Button -->
            <button
                @click="prevImage"
                class="absolute left-2 top-1/2 transform -translate-y-1/2 bg-white text-black p-2 rounded-full shadow-lg hover:bg-gray-100 transition"
            >
                ‹
            </button>

            <!-- Next Button -->
            <button
                @click="nextImage"
                class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-white text-black p-2 rounded-full shadow-lg hover:bg-gray-100 transition"
            >
                ›
            </button>
        </div>

        <!-- Establishment Info Section -->
        <div>
            <h1 class="font-serif font-bold text-4xl mb-2">Restaurant Name</h1>
            <div class="mb-2">Type Of Establishment</div>
            <div class="flex mb-2">
                <div class="font-bold mr-2">Phone Number:</div>
                <div>0564854784</div>
            </div>
            <div class="flex mb-2">
                <div class="font-bold mr-2">E-mail:</div>
                <div>blaytkurva@gmail.com</div>
            </div>

            <div class="flex mb-2">
                <div class="font-bold mr-2">Location:</div>
                <div>Reghaïa</div>
            </div>

            <div class="card flex items-center mt-4">
                <!-- Rating of the establishment -->
                <div class="font-bold mr-2">Average Rating:</div>
                <Rating
                :modelValue="value"
                readonly
                :style="{ '--p-rating-icon-size': '25px' }"
                class="text-red-400"
                />
            </div>
            <hotelExtra />
        </div>
    </div>
</template>

<template>
    <div class="bg-white rounded-xl shadow p-5 mt-4 w-full max-w-md">
      <h2 class="text-lg font-bold mb-3">Hotel Information</h2>
  
      <!-- Amenities -->
      <div class="mb-3">
        <h3 class="font-semibold text-sm mb-1">Amenities:</h3>
        <ul class="list-disc list-inside text-sm text-gray-700 space-y-1">
          <li v-for="(amenity, index) in amenities" :key="index">
            {{ amenity }}
          </li>
        </ul>
      </div>
  
      <!-- Check-in / Check-out -->
      <div class="flex justify-between text-sm text-gray-700 mb-3">
        <div><span class="font-bold">Check-in:</span> {{ checkInTime }}</div>
        <div><span class="font-bold">Check-out:</span> {{ checkOutTime }}</div>
      </div>
  
      <!-- Stars -->
      <div class="flex items-center text-sm">
        <span class="bold mr-2">Stars:</span>
        <div class="flex">
          <svg
            v-for="n in stars"
            :key="n"
            class="w-4 h-4 text-yellow-400"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path d="M10 15l-5.878 3.09 1.122-6.545L.489 6.91l6.561-.955L10 0l2.95 5.955 6.561.955-4.755 4.635 1.122 6.545z" />
          </svg>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    amenities: {
      type: Array,
      required: true
    },
    checkInTime: {
      type: String,
      required: true
    },
    checkOutTime: {
      type: String,
      required: true
    },
    stars: {
      type: Number,
      required: true
    }
  })
  </script>
<script setup>
const props = defineProps({
  reviewerName:{
    type:String,
    required:true
  },
  reviewerLastName:{
    type:String,
    required:true
  },
  rating: {
    type: Number,
    required: true
  },
  comment: {
    type: String,
    required: true
  },
  reviewDate: {
    type: String,
    required: true
  }
})
</script>

<template>
    <div class="bg-white p-4 rounded-lg shadow-md mb-4">
      <p class="font-bold font-serif">{{ props.reviewerName }}</p>
      <div class="flex items-center mb-2">
        <div class="flex">
          <svg
            v-for="n in props.rating"
            :key="n"
            class="w-5 h-5 text-orange-400"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path d="M10 15l-5.878 3.09 1.122-6.545L.489 6.91l6.561-.955L10 0l2.95 5.955 6.561.955-4.755 4.635 1.122 6.545z" />
          </svg>
        </div>
        <span class="ml-2 text-sm text-gray-500">{{ props.reviewDate }}</span>
      </div>
      <p class="text-sm text-gray-700">{{ props.comment }}</p>
    </div>
  </template>
  

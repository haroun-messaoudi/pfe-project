<template>
    <div class="shadow-lg gap-4 bg-gray-100 p-5 m-5 border-0 rounded-lg">
      <h2 class="text-2xl font-semibold mb-4">Reviews</h2>
  
      <div v-if="reviews && reviews.length===0" class="text-gray-500">
        No reviews yet.
      </div>
  
      <div v-for="(review, index) in reviews" :key="index">
        <SingleReview
          :reviewerName="review.profile"
          :rating="review.rating"
          :comment="review.content"
          :reviewDate="review.date_posted"
        />
      </div>
    </div>
  </template>
  
  <script setup>
  import SingleReview from '@/components/singleReview.vue'
  
  defineProps({
    reviews: {
      type: Array,
      required: true
    }
  })
  </script>
  

  
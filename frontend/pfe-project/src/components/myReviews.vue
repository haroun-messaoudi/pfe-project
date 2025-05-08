<script setup>
import myReview from '@/components/myReview.vue'
import api from '@/axios'
import {ref , onMounted } from 'vue'

const reviews = ref([])

async function fetchReviews(){
  const response = await api.get(`reviews/profile-reviews/`)
  console.log(response)
  reviews.value.push(...response.data)
  console.log(reviews,"reviews")
}



onMounted(async()=>{
  await fetchReviews()}
)

</script>

<template>
    <section class=" px-4 py-10">
      <div class="container-xl border border-gray-500 rounded-lg lg:container m-auto">
        <!-- big title -->
        <h2 class="text-3xl border-b p-5 border-gray-500 font-bold  mb-6 text-center">
          My Reviews
        </h2>
        <!-- cards loop -->
        <div class="flex flex-col  gap-4"> 
          <myReview v-for="(hit, index) in reviews" :key="index" :estaName="hit.establishement"
           :rating="hit.rating"
           :comment="hit.content"
           :date="hit.date_posted"
           />
        </div>
      </div>
</section>
</template>
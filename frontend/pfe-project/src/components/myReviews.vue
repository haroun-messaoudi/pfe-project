<script setup>
import myReview from '@/components/myReview.vue'
const props = defineProps({
  review: {
    type: Array,  // This should be an array of hits (search results)
  },
});
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
          <myReview v-for="(hit, index) in props.review" :key="index" :review="hit"/>
        </div>
      </div>
</section>
</template>
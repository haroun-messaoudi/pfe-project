<script setup>
import Card from '@/components/card.vue';




const props = defineProps({
  cardsInfo: {
    type: Array,  // This should be an array of hits (search results)
  },
});
console.log("hnaa",props.cardsInfo)
</script>

<template>
  <section class="px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <!-- big title -->
      <h2 class="text-3xl font-bold mb-6 text-center">
        Where to?
      </h2>
      <!-- cards loop -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <card v-for="(hit, index) in props.cardsInfo" :key="index" :cardInfo="hit" />
      </div>
    </div>
  </section>
</template>

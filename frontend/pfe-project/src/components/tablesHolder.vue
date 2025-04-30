<script setup>
import tableCard from '@/components/tableCard.vue';




const props = defineProps({
  tablesInfo: {
    type: Array,  // This should be an array of hits (search results)
  },
  title : {
    type: String,
  },
});
console.log("hnaa",props.cardsInfo)
</script>

<template>
  <section class="px-1 py-10 bg-gray-100">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-midium mb-6 text-slate-800">
        {{ props.title }}
      </h2>
      <!-- cards loop -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <tableCard v-for="(hit, index) in props.tablesInfo" :key="index" :tableInfo="hit" /> 
      </div>
    </div>
  </section>
</template>

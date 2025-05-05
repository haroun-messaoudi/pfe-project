<script setup>
import tableCard from '@/components/tableCard.vue';
import roomCard from '@/components/roomCard.vue';



const props = defineProps({
  tables: {
    type: Array,  // This should be an array of hits (search results)
  },
  title : {
    type: String,
  },
});
</script>

<template>
  <section class="px-1 py-10 bg-gray-100 p-5 m-5 border-0 rounded-lg">
    <div class="container-xl lg:container m-auto">
      <!-- <h2 class="text-3xl font-midium mb-6 text-slate-800">
        {{ props.title }}
      </h2> -->
      <!-- cards loop -->
      <div v-if="props.title === 'restaurant'" class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <tableCard v-for="(hit, index) in props.tables" :key="index" :tableInfo="hit" /> 
      </div>
      <div v-if="props.title === 'hotel'" class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <roomCard v-for="(hit, index) in props.tables" :key="index" :tableInfo="hit" /> 
      </div>
    </div>
  </section>
</template>

<script setup>
import card from '@/components/card.vue';
</script>

<template>



<section class=" px-4 py-10">
      <div class="container-xl lg:container m-auto">
        <h2 class="text-3xl font-bold  mb-6 text-center">
          Where to?
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4"> 
          <card v-for="cardInfo in cardsInfo" />
        </div>
      </div>
</section>
</template>
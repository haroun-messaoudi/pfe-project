<script setup>
import { useUserStore } from '@/stores/user'
import cardsholder from '@/components/cardsholder.vue';
import navbar from '@/components/navbar.vue';
import { useSearchStore } from '@/stores/searchStore'
import { useTopEstablishmentsStore } from '@/stores/topestablishments';
import { onMounted } from 'vue';

const topEstablishmentsStore = useTopEstablishmentsStore();

onMounted(() => {
  topEstablishmentsStore.fetchBestHotels(); // Fetch best-rated hotels
  topEstablishmentsStore.fetchBestRestaurants(); // Fetch best-rated restaurants
});


const userStore = useUserStore()
const searchStore = useSearchStore()
console.log("resulta", searchStore.results)
console.log(userStore.isAuthenticated)
</script>

<template>
  <div>
    <navbar page="home" />
      <h2 class="text-3xl font-bold pb-6 text-center bg-gray-100">
        Where to?
      </h2>
      <cardsholder :cardsInfo="topEstablishmentsStore.bestRestaurants.hits" :title="'Best Restaurants'" />
      <cardsholder :cardsInfo="topEstablishmentsStore.bestHotels.hits" :title="'Best Hotels'" />
  </div>
</template>

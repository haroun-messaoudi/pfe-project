<script setup>
import { useRoute } from 'vue-router';
import { useSearchStore } from '@/stores/searchStore';
import profilenav from '@/components/profilenav.vue';
import establishementCard from '@/components/establishementCard.vue';
import { useTopEstablishmentsStore } from '@/stores/topestablishments';
import { computed } from 'vue';

// Access the route and search store
const route = useRoute();
const searchStore = useSearchStore();
const topEstablishmentsStore = useTopEstablishmentsStore()

// Get the establishment data based on the route's id
const establishment = computed(() => {
  const id = route.params.id;
  return (
    searchStore.results.find((item) => item.objectID === id) ||
    topEstablishmentsStore.bestHotels.hits?.find((item) => item.objectID === id) ||
    topEstablishmentsStore.bestRestaurants.hits?.find((item) => item.objectID === id)
  );
});
</script>

<template>
  <div>
    <profilenav :buttonStatus="false" />
    <div v-if="establishment">
      <establishementCard
        :name="establishment.name"
        :type="establishment.type"
        :phone="establishment.phone_number"
        :email="establishment.email"
        :location="establishment.location"
        :amenities="establishment.hotel_amenities"
        :description="establishment.description"
        :checkin="establishment.hotel_check_in_time"
        :checkout="establishment.hotel_check_out_time"
        :stars="establishment.hotel_stars"
        :city="establishment.city"
        :images="[
          { itemImageSrc: '/src/assets/img/logo.png', thumbnailImageSrc: '/src/assets/img/logo.png', alt: 'Image 1' },
          { itemImageSrc: '/src/assets/img/hrn.png', thumbnailImageSrc: '/src/assets/img/hrn.png', alt: 'Image 2' }
        ]"
        :value="establishment.average_rating"
      />
    </div>
    <!-- <div v-else>
      <p>Loading establishment details...</p>
    </div> -->
  </div>
</template>
<script setup>
import { useRoute } from 'vue-router';
import { useSearchStore } from '@/stores/searchStore';
import profilenav from '@/components/profilenav.vue';
import establishementCard from '@/components/establishementCard.vue';
import reviewsHolder from '@/components/reviewsHolder.vue';
import api from '@/axios'
import { ref } from 'vue';
// const reviews = [
//   { 
//     reviewerName:"tahar",
//     reviewerLastName:"irki",
//     rating: 5,
//     comment: "The food was incredible, especially the pasta. Highly recommended!",
//     date: "2025-04-25"
//   },
//   {
//     reviewerName:"haroun",
//     reviewerLastName:"messaoudi",
//     rating: 4,
//     comment: "Nice ambiance and quick service. A bit pricey though.",
//     date: "2025-04-22"
//   },
//   {
//     reviewerName:"rafik",
//     reviewerLastName:"benboaicha",
//     rating: 3,
//     comment: "Food was okay, service could be better.",
//     date: "2025-04-18"
//   }
// ]

import { useTopEstablishmentsStore } from '@/stores/topestablishments';
import { computed, onMounted } from 'vue';

// Access the route and search store

const route = useRoute();
const searchStore = useSearchStore();
const topEstablishmentsStore = useTopEstablishmentsStore()
const reviews = ref([]);
const fetchReviews = async()=>{
  try {
    const response = await api.get('/reviews/establishment/' + route.params.id);
    const data = await response.data;
    reviews.value.push(...data)
  } catch (error) {
    console.error('Error fetching reviews:', error);
    return [];
  }
}

// Get the establishment data based on the route's id
const establishment = computed(() => {
  const id = route.params.id;
  return (
    searchStore.results.find((item) => item.objectID === id) ||
    topEstablishmentsStore.bestHotels.hits?.find((item) => item.objectID === id) ||
    topEstablishmentsStore.bestRestaurants.hits?.find((item) => item.objectID === id)
  );
});

const imageList = computed(() => {
  if (!establishment.value?.images?.length) {
    return []; // or a single default placeholder if you prefer
  }
  return establishment.value.images.map((img, idx) => ({
    itemImageSrc: img.image,
    thumbnailImageSrc: img.image,
    alt: `${establishment.value.name} image ${idx + 1}`,
  }));
});
console.log(imageList.value)

console.log(establishment.value)
onMounted(async () => {
  // Fetch reviews when the component is mounted
  await fetchReviews();
  
  console.log(reviews)
  // Set the fetched reviews to a reactive property or state
  // For example, you can use a ref or reactive object to store the reviews
  // this.reviews = reviews;
});
</script>

<template>
  <div>
    <profilenav :buttonStatus="false" />
    <div v-if="establishment">
      <establishementCard
        :id= "establishment.id"
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
        :images="imageList"
        :value="establishment.average_rating"
        :menuItems="establishment?.restaurant_menu_items"
        :cuisineType="establishment?.restaurant_cuisine"
      />
      <reviewsHolder :reviews="reviews" />
    </div>
    <!-- <div v-else>
      <p>Loading establishment details...</p>
    </div> -->
  </div>
</template>
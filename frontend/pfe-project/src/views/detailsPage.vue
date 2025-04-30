<script setup>
import profilenav from '@/components/profilenav.vue';
import establishementCard from '@/components/establishementCard.vue';
import reviewsHolder from '@/components/reviewsHolder.vue';
const reviews = [
  { 
    reviewerName:"tahar",
    reviewerLastName:"irki",
    rating: 5,
    comment: "The food was incredible, especially the pasta. Highly recommended!",
    date: "2025-04-25"
  },
  {
    reviewerName:"haroun",
    reviewerLastName:"messaoudi",
    rating: 4,
    comment: "Nice ambiance and quick service. A bit pricey though.",
    date: "2025-04-22"
  },
  {
    reviewerName:"rafik",
    reviewerLastName:"benboaicha",
    rating: 3,
    comment: "Food was okay, service could be better.",
    date: "2025-04-18"
  }
]
</script>

<template>
    <div>
        <profilenav :buttonStatus="false"/>
        <establishementCard
    :name="'My Restaurant'"
    :type="'Fine Dining'"
    :phone="'0564854784'"
    :email="'restaurant@example.com'"
    :location="'Downtown'"
    :images="[
      { itemImageSrc: '/src/assets/img/rafiki.png', thumbnailImageSrc: '/src/assets/img/rafiki.png', alt: 'Restaurant Image 1' },
      { itemImageSrc: '/src/assets/img/hrn.png', thumbnailImageSrc: '/src/assets/img/hrn.png', alt: 'Restaurant Image 2' },
      { itemImageSrc: '/src/assets/img/thr.png', thumbnailImageSrc: '/src/assets/img/thr.png', alt: 'Restaurant Image 3' },
      { itemImageSrc: '/src/assets/img/rafiki.png', thumbnailImageSrc: '/src/assets/img/rafiki.png', alt: 'Restaurant Image 4' },
      { itemImageSrc: '/src/assets/img/hrn.png', thumbnailImageSrc: '/src/assets/img/hrn.png', alt: 'Restaurant Image 5' },
      { itemImageSrc: '/src/assets/img/thr.png', thumbnailImageSrc: '/src/assets/img/thr.png', alt: 'Restaurant Image 6' }
    ]"
    :value="4"
  />
      <reviewsHolder :reviews="reviews" />
    </div>
</template>
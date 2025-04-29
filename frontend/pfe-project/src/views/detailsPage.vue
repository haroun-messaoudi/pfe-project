<script setup>
import profilenav from '@/components/profilenav.vue';
import establishementCard from '@/components/establishementCard.vue';
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
      { itemImageSrc: '/src/assets/img/logo.png', thumbnailImageSrc: '/src/assets/img/logo.png', alt: 'Restaurant Image 1' },
      { itemImageSrc: '/src/assets/img/hrn.png', thumbnailImageSrc: '/src/assets/img/hrn.png', alt: 'Restaurant Image 2' }
    ]"
    :value="4"
  />
    </div>
</template>
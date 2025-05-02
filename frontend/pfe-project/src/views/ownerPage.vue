<script setup>
import ownerNav from '@/components/ownerNav.vue';
import ownerEstab from '@/components/ownerEstab.vue';
import tablesHolder from '@/components/tablesHolder.vue';
</script>


<template>
    <div>
    <ownerNav />
    <ownerEstab 
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
    <h2 class="text-3xl font-bold pb-6 text-center bg-gray-100 pt-5">
        My Tables
      </h2>
    <tablesHolder />
    </div>
</template>
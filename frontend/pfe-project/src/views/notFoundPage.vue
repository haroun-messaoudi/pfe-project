<script setup>
import { RouterLink } from 'vue-router';
</script>


<template>


<section class="text-center flex flex-col justify-center items-center h-96">
      <i class="pi pi-exclamation-triangle text-yellow-400 mb-5" style="font-size: 6rem"></i>
      <h1 class="text-6xl font-bold mb-4">404 Not Found</h1>
      <p class="text-xl mb-5">This page does not exist</p>
      <RouterLink
        to="/"
        class="text-white bg-orange-700 hover:bg-orange-900 rounded-md px-3 py-2 mt-4"
        >Go Back
    </RouterLink>
    </section>
</template>
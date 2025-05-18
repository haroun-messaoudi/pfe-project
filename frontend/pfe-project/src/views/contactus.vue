<script setup>
import { RouterLink } from 'vue-router';
import Button from 'primevue/button';
</script>




<template>
  <div class="px-4 py-10 bg-orange-50">
  <div class="flex flex-col items-center">
    <h1 class="text-3xl font-bold  my-6 text-center ">Have questions or want to collaborate? Reach out to our team!</h1>
    <h1 class="text-3xl font-bold  mb-6 text-center">Our Development Team</h1>
    
    <div class="space-y-20">
      <div class="flex space-x-4">
        <img class="h-20 w-auto rounded-lg"  src="@/assets/img/hrn.png" >
        <div>
            <h2>massaoudi haroun</h2>
            <p>messaoudi.haroun@fs.univ-medea.dz</p>
            <p>back-end and front-end specialist</p>
        </div>
      </div>
      
      <div class="flex space-x-4">
        <img class="h-20 w-auto rounded-lg"  src="@/assets/img/rafiki.png" >
        <div>
            <h2>benbouaicha rafik</h2>
            <p>alex.johnson@example.com</p>
            <p>back-end specialist </p>
        </div>
      </div>
      
      <div class="flex space-x-4">
        <img class="h-20 w-auto rounded-lg"  src="@/assets/img/thr1.png" >
        <div>
            <h2>irki tahar</h2>
            <p>taharirki8@gmail.com</p>
            <p>Front-end specialist</p>
        </div>
      </div>
    </div>
    <RouterLink class="my-10" to="/">
      <Button label="return to HomePage" severity="contrast" />
    </RouterLink>
  </div>
</div>
</template>

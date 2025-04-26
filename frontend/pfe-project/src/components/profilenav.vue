<script setup>
import Button from 'primevue/button';
import { RouterLink } from 'vue-router';
</script>

<template>
<div class="h-20 border-b border-gray-800 flex justify-between items-center px-5">
<RouterLink to="/">
<div class="flex space-x-4  border-2 border-gray-500 p-3 rounded-lg">
    <i class="pi-angle-left"></i>
    <p>Home Page</p>
</div>
</RouterLink>
<!-- stay-bite logo -->
<RouterLink to="/">
<img class="h-20 w-auto" src="@/assets/img/logo.png" />
</RouterLink>
<Button label="edit profile" severity="warn" rounded />

</div>    
</template>
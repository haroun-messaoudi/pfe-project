<script setup>
// import { onMounted } from 'vue'
// import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import cardsholder from '@/components/cardsHolder.vue';
import navbar from '@/components/navbar.vue';
// const router = useRouter()
const userStore = useUserStore()
console.log(userStore.isAuthenticated)
</script>
<!-- // onMounted(() => {
//   if (!userStore.isAuthenticated) {
//     router.push('/login')
//   }
// })

// <template>
//   <div>
//     <h1>Welcome to the Homepage</h1>
//     Add your homepage content here -->




<template>
<div>
  <navbar />
  <cardsholder />
</div>
</template>
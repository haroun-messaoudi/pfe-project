<script setup>
// import { onMounted } from 'vue'
// import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import cardsholder from '@/components/cardsholder.vue';
import navbar from '@/components/navbar.vue';
import { useSearchStore } from '@/stores/searchStore'
// const router = useRouter()
const userStore = useUserStore()
const searchStore = useSearchStore()
console.log("resulta",searchStore.results)
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
  <cardsholder :cardsInfo="searchStore.results" />
</div>
</template>
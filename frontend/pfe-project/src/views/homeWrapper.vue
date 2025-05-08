<!-- src/views/HomeWrapper.vue -->
<template>
    <component :is="currentComponent" />
  </template>
  
  <script setup>
  import { computed } from 'vue'
  import { useUserStore } from '@/stores/user'
  
  // import your real pages:
  import homepage from './homepage.vue' 
  import ownerPage from './ownerPage.vue'
  const userStore = useUserStore()
  
  const currentComponent = computed(() => {
    if (!userStore.isAuthenticated) {
      return homepage
    }
  
    // authenticated
    return userStore.profileRole === 'owner'
      ? ownerPage
      : homepage
  })
  </script>
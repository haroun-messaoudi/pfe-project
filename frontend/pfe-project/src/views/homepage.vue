<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
console.log(userStore.isAuthenticated)
onMounted(() => {
  if (!userStore.isAuthenticated) {
    router.push('/login')
  }
})
</script>

<template>
  <div>
    <h1>Welcome to the Homepage</h1>
    <!-- Add your homepage content here -->
  </div>
</template>
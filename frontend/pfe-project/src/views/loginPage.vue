<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
 // Adjust the import path as necessary
const router = useRouter()
const userStore = useUserStore()

const form = ref({
  username: '',
  password: '',
})

const loginUser = async () => {
  try {
    await userStore.login(form.value.username, form.value.password)
    await userStore.fetchUserDetails()
    alert('Login successful!')
    
    router.push('/establishement-create') // Now this works fine
  } catch (error) {
    console.error('Error logging in:', error.response?.data || error.message)
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-md w-full p-6 bg-white shadow-md rounded-md">
      <h2 class="text-2xl font-bold mb-4 text-center">Login</h2>
      <form @submit.prevent="loginUser">
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium">Username</label>
          <input
            id="username"
            v-model="form.username"
            type="text"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
            placeholder="Enter your username"
            required
          />
        </div>
        <div class="mb-4">
          <label for="password" class="block text-sm font-medium">Password</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
            placeholder="Enter your password"
            required
          />
        </div>
        <button
          type="submit"
          class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

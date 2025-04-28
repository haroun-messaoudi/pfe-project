<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Toastify from 'toastify-js' 
import { useUserStore } from '@/stores/user'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Message from 'primevue/message'

const router = useRouter()

const userStore = useUserStore()

const form = ref({
  username: '',
  password: '',
})

const errors = ref({
  username: '',
  password: '',
  general: '',
})

const loginUser = async () => {

  errors.value = {
    username: '',
    password: '',
    general: '',
  }

  try {
    await userStore.login(form.value.username, form.value.password)
    await userStore.fetchUserDetails()
    Toastify({
      text: 'Login successful!',
      duration: 3000,
      gravity: 'top',
      position: 'right',
      backgroundColor: '#4CAF50',
      className: 'toast-success',
    }).showToast()
    router.push('/')
  } catch (error) {
    const responseError = error.response?.data || {}

    // Display toast error message
    Toastify({
      text: responseError.detail || 'An error occurred. Please try again.',
      duration: 3000,
      gravity: 'top',
      position: 'right',
      backgroundColor: '#FF0000',
      className: 'toast-error',
    }).showToast()

    // Field-specific error messages
    if (responseError.errors){
      errors.value = {
        ...errors.value,
        ...responseError.errors,
      }
    }else{
      errors.value.general = 'Invalid username or password'
    }
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-white">
    <div class="w-full max-w-md bg-white p-6 rounded-md shadow-md">
      <h2 class="text-2xl font-bold mb-4 text-center">Login</h2>
      <form @submit.prevent="loginUser" class="space-y-4">
        <!-- Username -->
        <div>
          <label for="username" class="block text-sm font-medium mb-1">Username</label>
          <InputText
            id="username"
            v-model="form.username"
            class="w-full"
            placeholder="Enter your username"
          />
          <Message v-if="errors.username" severity="error">{{ errors.username }}</Message>
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="block text-sm font-medium mb-1">Password</label>
          <Password
            id="password"
            v-model="form.password"
            toggleMask
            :feedback=false
            class="w-full"
            inputClass="w-full"
            placeholder="Enter your password"
          />
          <Message v-if="errors.password" severity="error">{{ errors.password }}</Message>
        </div>

        <!-- General error -->
        <Message v-if="errors.general" severity="error">{{ errors.general }}</Message>

        <!-- Submit button -->
        <Button
          label="Login"
          type="submit"
          class="w-full"
        />


      </form>
      <div class="mt-4 text-center">
        <router-link to="/register" class="text-blue-500 hover:underline">
          Don't have an account? Register here
        </router-link>
      </div>
    </div>
  </div>
</template>

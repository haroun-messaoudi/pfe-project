<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
// PrimeVue components
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Dropdown from 'primevue/dropdown'
import Button from 'primevue/button'
import Message from 'primevue/message'
import Toastify from 'toastify-js'


const router = useRouter()
const userStore = useUserStore()

const roles = [
  { label: 'Client', value: 'client' },
  { label: 'Owner', value: 'owner' },
]

const form = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
  profile: {
    first_name: '',
    last_name: '',
    phone_number: '',
    role: '',
  },
})

const errors = ref({})

const registerUser = async () => {
  errors.value = {}

  if (form.value.password !== form.value.confirmPassword) {
    errors.value.confirmPassword = ['Passwords do not match']
    return
  }

  try {
    // Register the user
    await axios.post('http://127.0.0.1:8000/api/accounts/register/', {
      username: form.value.username,
      email: form.value.email,
      password: form.value.password,
      confirm_password: form.value.confirmPassword,
      profile: form.value.profile,
    })

    // const profileId = response.data.profile.pk
    // userStore.setProfileId(profileId)
    try{
      await userStore.login(form.value.username, form.value.password)
      await userStore.fetchUserDetails()
      Toastify({
        text: 'Registration successful!',
        duration: 3000,
        gravity: 'top',
        position: 'right',
        backgroundColor: '#4CAF50',
        className: 'toast-success',
      }).showToast()
    }catch (error) {
      console.error('Error logging in:', error.response?.data || error.message)
      Toastify({
        text: 'Login failed!',
        duration: 3000,
        gravity: 'top',
        position: 'right',
        backgroundColor: '#F44336',
        className: 'toast-error',
      }).showToast()
    }

    // Login the user automatically
    // const loginResponse = await axios.post('http://127.0.0.1:8000/api/accounts/token/', {
    //   username: form.value.username,
    //   password: form.value.password,
    // })

    // const { access, refresh } = loginResponse.data
    // localStorage.setItem('accessToken', access)
    // localStorage.setItem('refreshToken', refresh)

    // userStore.setAuthenticated(true)

    // Redirect based on role
    const role = form.value.profile.role
    if (role === 'owner') {
      router.push('/establishement-create')
    } else {
      router.push('/')
    }
  } catch (error) {
    errors.value = error.response?.data || {}
  }
}
</script>

<template>
  <div class="max-w-lg mx-auto p-6 bg-white shadow-lg rounded-xl border border-gray-100">
    <h2 class="text-3xl font-bold mb-6 text-center text-slate-700">Create Account</h2>
    <form @submit.prevent="registerUser" class="space-y-5">
      <!-- Username -->
      <div>
        <label for="username" class="block text-sm font-medium mb-1">Username</label>
        <InputText id="username" v-model="form.username" class="w-full" placeholder="Enter username" />
        <Message v-if="errors.username" severity="error" class="mt-2">{{ errors.username[0] }}</Message>
      </div>

      <!-- Email -->
      <div>
        <label for="email" class="block text-sm font-medium mb-1">Email</label>
        <InputText id="email" v-model="form.email" type="email" class="w-full" placeholder="Enter email" />
        <Message v-if="errors.email" severity="error" class="mt-2">{{ errors.email[0] }}</Message>
      </div>

      <!-- Password -->
      <div>
        <label for="password" class="block text-sm font-medium mb-1">Password</label>
        <Password id="password" v-model="form.password" class="w-full" toggleMask placeholder="Password" />
        <Message v-if="errors.password" severity="error" class="mt-2">{{ errors.password[0] }}</Message>
      </div>

      <!-- Confirm Password -->
      <div>
        <label for="confirmPassword" class="block text-sm font-medium mb-1">Confirm Password</label>
        <Password id="confirmPassword" v-model="form.confirmPassword" class="w-full" :feedback=false toggleMask  placeholder="Confirm password" />
        <Message v-if="errors.confirmPassword" severity="error" class="mt-2">{{ errors.confirmPassword[0] }}</Message>
      </div>

      <!-- First Name -->
      <div>
        <label for="firstName" class="block text-sm font-medium mb-1">First Name</label>
        <InputText id="firstName" v-model="form.profile.first_name" class="w-full" placeholder="First name" />
        <Message v-if="errors.profile?.first_name" severity="error" class="mt-2">{{ errors.profile.first_name[0] }}</Message>
      </div>

      <!-- Last Name -->
      <div>
        <label for="lastName" class="block text-sm font-medium mb-1">Last Name</label>
        <InputText id="lastName" v-model="form.profile.last_name" class="w-full" placeholder="Last name" />
        <Message v-if="errors.profile?.last_name" severity="error" class="mt-2">{{ errors.profile.last_name[0] }}</Message>
      </div>

      <!-- Phone Number -->
      <div>
        <label for="phoneNumber" class="block text-sm font-medium mb-1">Phone Number</label>
        <InputText id="phoneNumber" v-model="form.profile.phone_number" class="w-full" placeholder="Phone number" />
        <Message v-if="errors.profile?.phone_number" severity="error" class="mt-2">{{ errors.profile.phone_number[0] }}</Message>
      </div>

      <!-- Role -->
      <div>
        <label for="role" class="block text-sm font-medium mb-1">Role</label>
        <Dropdown
          id="role"
          v-model="form.profile.role"
          :options="roles"
          optionLabel="label"
          optionValue="value"
          placeholder="Select role"
          class="w-full"
        />
        <Message v-if="errors.profile?.role" severity="error" class="mt-2">{{ errors.profile.role[0] }}</Message>
      </div>

      <!-- Submit -->
      <Button label="Register" type="submit" class="w-full p-button-lg"/>
    </form>
    <div class="mt-4 text-center">
      <router-link to="/login" class="text-blue-500 hover:underline">
        Already have an account? Login here
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.p-password input,
.p-inputtext,
.p-dropdown {
  width: 100%;
}
</style>
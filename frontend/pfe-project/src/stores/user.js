import { defineStore } from 'pinia'
import axios from 'axios'
import api from '@/axios' // Your custom Axios instance with interceptors

export const useUserStore = defineStore('user', {
  state: () => ({
    profileId: null,
    isAuthenticated: false,
  }),
  actions: {
    setProfileId(id) {
      this.profileId = id
    },
    setAuthenticated(status) {
      this.isAuthenticated = status
    },
    
    async login(username, password) {
      try {
        const response = await api.post('accounts/token/', {
          username,
          password,
        })
        
        const { access, refresh } = response.data
        
        // Store tokens
        localStorage.setItem('accessToken', access)
        localStorage.setItem('refreshToken', refresh)
        console.log("in user "+access)
        // Immediately set auth header
        api.defaults.headers.common['Authorization'] = `Bearer ${access}`

        return true
      } catch (error) {
        console.error('Login error:', error.response?.data || error.message)
        throw error
      }
    },
    async fetchUserDetails() {
      try {
        const response = await api.get('accounts/details/')
        console.log('User details:', response.data)
        this.setAuthenticated(true)
        return response.data
      } catch (error) {
        console.error('Error fetching user details:', error.response?.data || error.message)
        throw error
      }
    },
    
    async refreshAccessToken() {
      try {
        const refreshToken = localStorage.getItem('refreshToken')
        if (!refreshToken) throw new Error('No refresh token available')

        const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
          refresh: refreshToken,
        })

        const { access } = response.data
        localStorage.setItem('accessToken', access)
        return access
      } catch (error) {
        console.error('Error refreshing access token:', error)
        this.logout() // this is fine, just make sure no router logic inside
      }
    },

    logout() {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
      this.profileId = null
      this.isAuthenticated = false

      // Do NOT use useRouter() here. Handle redirection in the component.
    },
  },
  persist: true, // Enable persistence
})

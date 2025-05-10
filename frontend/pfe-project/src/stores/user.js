import { defineStore } from 'pinia'
import axios from 'axios'
import api from '@/axios' // Your custom Axios instance with interceptors
import { useEstablishementStore } from './establishement'
import { useProfileStore } from './profile'
import router from '@/router' 
import { useReservationsStore } from './reservations'

export const useUserStore = defineStore('user', {
  state: () => ({
    profileId: null,
    isAuthenticated: false,
    profileRole: "",
    refreshToken: null,
    acessToken: null,
  }),
  actions: {
    setProfileId(id) {
      this.profileId = id
    },
    setAuthenticated(status) {
      this.isAuthenticated = status
    },
    setProfileRole(role) {
      this.profileRole = role
    },
    setAcessToken(token) {
      this.acessToken = token
    },
    setRefreshToken(token) {
      this.refreshToken = token
    },
    
    async login(username, password) {
      try {
        const response = await api.post('accounts/token/', {
          username,
          password,
        })
        
        const { access, refresh } = response.data
        
        // Store tokens
        this.acessToken = access
        this.refreshToken = refresh
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
        this.setProfileId(response.data["profile"].pk)
        this.setProfileRole(response.data["profile"].role)
        return response.data
      } catch (error) {
        console.error('Error fetching user details:', error.response?.data || error.message)
        throw error
      }
    },
    
    async refreshAccessToken() {
      try {
        const refreshToken = this.refreshToken // Use the store's state
        if (!refreshToken) throw new Error('No refresh token available')
    
        const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
          refresh: refreshToken,
        })
    
        const { access } = response.data
        this.setAcessToken(access) // Update the store's state
        api.defaults.headers.common['Authorization'] = `Bearer ${access}` // Update Axios headers
        return access
      } catch (error) {
        console.error('Error refreshing access token:', error)
        this.logout()
        throw error
      }
    },

    async logout() {
      try {
        if (this.refreshToken) {
          await api.post('accounts/blacklist/', { refresh: this.refreshToken })
        }
      } catch (err) {
        console.error(err)
      } finally {
        const userStore = useUserStore()
        const profileStore = useProfileStore()
        const estabStore   = useEstablishementStore()
        const reservationStore = useReservationsStore()
    
        // clear tokens + auth state
        userStore.$reset()
    
        // clear your other stores
        profileStore.$reset()
        estabStore.$reset()
        reservationStore.$reset()
        // also clear any default axios headers
        delete api.defaults.headers.common['Authorization']
    
        router.push({ name: 'Home' })
      }
    }
  },
  persist: true, // Enable persistence
})

import axios from 'axios'
import { useUserStore } from './stores/user'
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
})
function decodeJWT(token) {
try {
    const base64Url = token.split('.')[1]
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
    const jsonPayload = decodeURIComponent(
    atob(base64)
        .split('')
        .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    )
    return JSON.parse(jsonPayload)
} catch (e) {
    console.log('Error decoding JWT:', e)
    return null
}
}

function isTokenExpired(token) {
const payload = decodeJWT(token)
return payload?.exp ? Date.now() >= payload.exp * 1000 : true
}
// Helper to check if token is expired


// Request interceptor
api.interceptors.request.use(async (config) => {
  let accessToken = localStorage.getItem('accessToken')

  const refreshToken = localStorage.getItem('refreshToken')
  console.log("at the start"+accessToken)
  if (accessToken && isTokenExpired(accessToken) && refreshToken) {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
        refresh: refreshToken,
      })
      accessToken = response.data.access
      localStorage.setItem('accessToken', accessToken)
    } catch (error) {
      console.error('Failed to refresh access token:', error)
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
    }
  }

  if (accessToken) {
    console.log('Setting Authorization Header with Access Token:', accessToken) // Debugging
    config.headers.Authorization = `Bearer ${accessToken}`
  } else {
    console.log('Access Token available to set Authorization Header') // Debugging
  }

  return config
}, (error) => Promise.reject(error))

// Response interceptor for 401
api.interceptors.response.use(
    response => response,
    async error => {
      const originalRequest = error.config
      
      if (error.response?.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true
        
        try {
          const newAccessToken = await useUserStore().refreshAccessToken()
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
          return api(originalRequest)
        } catch (refreshError) {
          useUserStore().logout()
          return Promise.reject(refreshError)
        }
      }
      
      return Promise.reject(error)
    }
  )

export default api

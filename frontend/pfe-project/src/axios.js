import axios from 'axios'
import { useUserStore } from './stores/user'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
})

// Helper to decode JWT
function decodeJWT(token) {
  try {
    const base64Url = token.split('.')[1]
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map((c) => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    )
    return JSON.parse(jsonPayload)
  } catch (e) {
    console.log('Error decoding JWT:', e)
    return null
  }
}

// Helper to check if token is expired
function isTokenExpired(token) {
  const payload = decodeJWT(token)
  return payload?.exp ? Date.now() >= payload.exp * 1000 : true
}

// Request interceptor
api.interceptors.request.use(
  async (config) => {
    let accessToken = localStorage.getItem('accessToken')
    const refreshToken = localStorage.getItem('refreshToken')

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
        const userStore = useUserStore()
        userStore.logout()
        return Promise.reject(error)
      }
    }

    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`
    }

    return config
  },
  (error) => Promise.reject(error)
)

// Response interceptor for 401
api.interceptors.response.use(
  (response) => response, // Pass through successful responses
  async (error) => {
    const userStore = useUserStore()

    // Check if the error is due to an expired token
    if (error.response?.status === 401 && error.response?.data?.code === 'token_not_valid') {
      try {
        const refreshToken = localStorage.getItem('refreshToken')
        if (!refreshToken) {
          userStore.logout()
          return Promise.reject(error)
        }

        // Attempt to refresh the access token
        const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
          refresh: refreshToken,
        })

        const { access } = response.data

        // Update the access token in localStorage and Axios headers
        localStorage.setItem('accessToken', access)
        api.defaults.headers.common['Authorization'] = `Bearer ${access}`

        // Retry the original request with the new access token
        error.config.headers['Authorization'] = `Bearer ${access}`
        return api.request(error.config)
      } catch (refreshError) {
        console.error('Error refreshing token:', refreshError)
        userStore.logout()
        return Promise.reject(refreshError)
      }
    }

    // If the error is not due to token expiration, reject it
    return Promise.reject(error)
  }
)

export default api
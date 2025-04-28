import axios from 'axios'

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

// Function to set up interceptors dynamically
export function setupInterceptors(userStore) {
  // Request interceptor
  api.interceptors.request.use(
    async (config) => {
      let accessToken = userStore.acessToken
      const refreshToken = userStore.refreshToken

      if (accessToken && isTokenExpired(accessToken) && refreshToken) {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
            refresh: refreshToken,
          })
          accessToken = response.data.access
          userStore.setAcessToken(accessToken)
          userStore.setRefreshToken(response.data.refresh)
          api.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`
        } catch (error) {
          console.error('Failed to refresh access token:', error)
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
      if (error.response?.status === 401 && error.response?.data?.code === 'token_not_valid') {
        try {
          const refreshToken = userStore.refreshToken
          if (!refreshToken) {
            userStore.logout()
            return Promise.reject(error)
          }

          const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
          refresh: refreshToken})

          const { access } = response.data
          userStore.setAcessToken(access)
          api.defaults.headers.common['Authorization'] = `Bearer ${access}`

          error.config.headers['Authorization'] = `Bearer ${access}`
          return api.request(error.config)
        } catch (refreshError) {
          console.error('Error refreshing token:', refreshError)
          userStore.logout()
          return Promise.reject(refreshError)
        }
      }

      return Promise.reject(error)
    }
  )
}

export default api
import { defineStore } from 'pinia'
import api from '@/axios'
import { reactive } from 'vue'
import { useSearchStore } from './searchStore'

export const useEstablishementStore = defineStore('establishement', {
  state: () => ({
    establishement: null,
    // errors for each form: establishment, hotel rooms, restaurant tables, menu items
    errors: reactive({
      name: '',
      location: '',
      email: '',
      phone_number: '',
      city: '',
      description: '',
      hotel: {
        stars: '',
        amenities: '',
        checkInTime: '',
        checkOutTime: ''
      },
      newRoom: {
        room_type: '',
        price_per_night: '',
        amount: '',
        capacity: '',
        image: ''
      },
      updateRoom: {
        room_type: '',
        price_per_night: '',
        amount: '',
        capacity: '',
        image: ''
      },
      newTable: {
        capacity: '',
        description: '',
        amount: '',
        location: '',
        image: ''
      },
      updateTable: {
        capacity: '',
        description: '',
        amount: '',
        location: '',
        image: ''
      },
      newMenuItem: {
        name: '',
        description: '',
        price: ''
      },
      updateMenuItem: {
        name: '',
        description: '',
        price: ''
      }
    }),
    cuisines: [],
    amenities: []
  }),

  actions: {
    // CLEAR ALL ERRORS
    clearErrors() {
      // establishment-level errors
      this.errors.name = ''
      this.errors.location = ''
      this.errors.email = ''
      this.errors.phone_number = ''
      this.errors.city = ''
      this.errors.description = ''
      this.errors.hotel.stars = ''
      this.errors.hotel.amenities = ''
      this.errors.hotel.checkInTime = ''
      this.errors.hotel.checkOutTime = ''

      // clear nested forms errors
      Object.assign(this.errors.newRoom, { room_type: '', price_per_night: '', amount: '', capacity: '', image: '' })
      Object.assign(this.errors.updateRoom, { room_type: '', price_per_night: '', amount: '', capacity: '', image: '' })
      Object.assign(this.errors.newTable, { capacity: '', description: '', amount: '', location: '', image: '' })
      Object.assign(this.errors.updateTable, { capacity: '', description: '', amount: '', location: '', image: '' })
      Object.assign(this.errors.newMenuItem, { name: '', description: '', price: '' })
      Object.assign(this.errors.updateMenuItem, { name: '', description: '', price: '' })
    },

    // MAP BACKEND ERRORS INTO our nested structure
    setErrors(backendErrors) {
      // establishment update
      this.errors.name = backendErrors.name?.[0] || ''
      this.errors.location = backendErrors.location?.[0] || ''
      this.errors.email = backendErrors.email?.[0] || ''
      this.errors.phone_number = backendErrors.phone_number?.[0] || ''
      this.errors.city = backendErrors.city?.[0] || ''
      this.errors.description = backendErrors.description?.[0] || ''

      // hotel update errors
      if (backendErrors.hotel) {
        this.errors.hotel.stars = backendErrors.hotel.stars?.[0] || ''
        this.errors.hotel.amenities = backendErrors.hotel.amenities?.[0] || ''
        this.errors.hotel.checkInTime = backendErrors.hotel.checkInTime?.[0] || ''
        this.errors.hotel.checkOutTime = backendErrors.hotel.checkOutTime?.[0] || ''
      }

      // add room errors (create)
      if (backendErrors.newRoom) {
        this.errors.newRoom.room_type = backendErrors.newRoom.room_type?.[0] || ''
        this.errors.newRoom.price_per_night = backendErrors.newRoom.price_per_night?.[0] || ''
        this.errors.newRoom.amount = backendErrors.newRoom.amount?.[0] || ''
        this.errors.newRoom.capacity = backendErrors.newRoom.capacity?.[0] || ''
        this.errors.newRoom.image = backendErrors.newRoom.image?.[0] || ''
      }
      // update room errors
      if (backendErrors.updateRoom) {
        this.errors.updateRoom.room_type = backendErrors.updateRoom.room_type?.[0] || ''
        this.errors.updateRoom.price_per_night = backendErrors.updateRoom.price_per_night?.[0] || ''
        this.errors.updateRoom.amount = backendErrors.updateRoom.amount?.[0] || ''
        this.errors.updateRoom.capacity = backendErrors.updateRoom.capacity?.[0] || ''
        this.errors.updateRoom.image = backendErrors.updateRoom.image?.[0] || ''
      }

      // add table errors (create)
      if (backendErrors.newTable) {
        this.errors.newTable.capacity = backendErrors.newTable.capacity?.[0] || ''
        this.errors.newTable.description = backendErrors.newTable.description?.[0] || ''
        this.errors.newTable.amount = backendErrors.newTable.amount?.[0] || ''
        this.errors.newTable.location = backendErrors.newTable.location?.[0] || ''
        this.errors.newTable.image = backendErrors.newTable.image?.[0] || ''
      }
      // update table errors
      if (backendErrors.updateTable) {
        this.errors.updateTable.capacity = backendErrors.updateTable.capacity?.[0] || ''
        this.errors.updateTable.description = backendErrors.updateTable.description?.[0] || ''
        this.errors.updateTable.amount = backendErrors.updateTable.amount?.[0] || ''
        this.errors.updateTable.location = backendErrors.updateTable.location?.[0] || ''
        this.errors.updateTable.image = backendErrors.updateTable.image?.[0] || ''
      }

      // add menu item errors (create)
      if (backendErrors.newMenuItem) {
        this.errors.newMenuItem.name = backendErrors.newMenuItem.name?.[0] || ''
        this.errors.newMenuItem.description = backendErrors.newMenuItem.description?.[0] || ''
        this.errors.newMenuItem.price = backendErrors.newMenuItem.price?.[0] || ''
      }
      // update menu item errors
      if (backendErrors.updateMenuItem) {
        this.errors.updateMenuItem.name = backendErrors.updateMenuItem.name?.[0] || ''
        this.errors.updateMenuItem.description = backendErrors.updateMenuItem.description?.[0] || ''
        this.errors.updateMenuItem.price = backendErrors.updateMenuItem.price?.[0] || ''
      }
    },

    // FETCH EXISTING DATA
    async fetchOwnerEstablishement() {
      try {
        const response = await api.get('/establishements/details/')
        this.establishement = response.data
        this.clearErrors()
      } catch (error) {
        console.error('Error fetching establishment:', error.response?.data || error.message)
      }
    },

    async fetchCuisines() {
      try {
        const response = await api.get('/establishements/cuisines/list/')
        this.cuisines = response.data.map(item => ({ label: item.name, value: item.id }))
      } catch (error) {
        console.error('Error fetching cuisines:', error.response?.data || error.message)
        this.cuisines = []
      }
    },
    async searchEstablishements(query = '', filters = []) {
      try {
        // join your array of filter strings into a comma‐separated list
        const filterString = filters.length ? filters.join(',') : ''
        const response = await api.get('/establishements/search/', {
          params: {
            q:       query,        // full-text query
            filters: filterString  // e.g. "type:hotel,city:Algiers"
          }
        })
        // Return the whole body so your setSearchResults can pick off hits, nbHits, etc.
        return response.data
      } catch (err) {
        console.error('Error searching establishments:', err.response?.data || err.message)
        throw err
      }
    },
    async fetchAmenities() {
      try {
        const response = await api.get('/establishements/amenities/list/')
        this.amenities = response.data.map(item => ({ label: item.name, value: item.id }))
        console.log(this.amenities,"fetching")
      } catch (error) {
        console.error('Error fetching amenities:', error.response?.data || error.message)
        this.amenities = []
      }
    },

    // UPDATE ESTABLISHMENT
    async updateEstablishement(data) {
      try {
        this.clearErrors()
        const response = await api.patch('/establishements/update/', data)
        this.establishement = response.data
      } catch (error) {
        // grab either the nested `errors` or the top‐level data
        const backend = error.response?.data.errors
                    || error.response?.data
                    || {}
        this.setErrors(backend)     // ← pass it straight through
        throw error
      }
    },

    // HOTEL UPDATE
    async updateHotel(hotelData) {
      try {
        this.clearErrors()
        const response = await api.patch('/establishements/hotel/update/', hotelData)
        console.log(response,"hnaaa")
        this.establishement.hotel = response.data
      } catch (error) {
        this.setErrors({ updateHotel: error.response?.data || {} })
        throw error
      }
    },

    // RESTAURANT UPDATE
    async updateRestaurant(restaurantData) {
      try {
        this.clearErrors()
        const response = await api.patch('/establishements/restaurant/update/', restaurantData)
        this.establishement.restaurant = response.data
      } catch (error) {
        this.setErrors({ updateRestaurant: error.response?.data || {} })
        throw error
      }
    },

    // ROOM CRUD
    async addRoom(formData) {
      try {
        this.clearErrors()
        const response = await api.post(
          '/establishements/hotel/room/create/',
          formData,
          { headers: { 'Content-Type': 'multipart/form-data' } }
        )
        await this.fetchOwnerEstablishement()
        return response.data
      } catch (error) {
        this.setErrors({ newRoom: error.response?.data || {} })
        throw error
      }
    },

    async updateRoom(roomId, formData) {
      try {
        this.clearErrors()
        await api.patch(
          `/establishements/hotel/room/update/${roomId}/`,
          formData,
          { headers: { 'Content-Type': 'multipart/form-data' } }
        )
        await this.fetchOwnerEstablishement()
      } catch (error) {
        this.setErrors({ updateRoom: error.response?.data || {} })
        throw error
      }
    },

    async deleteRoom(roomId) {
      try {
        await api.delete(`/establishements/hotel/room/delete/${roomId}/`)
        await this.fetchOwnerEstablishement()
      } catch (error) {
        console.error('Error deleting room:', error.response?.data || error.message)
      }
    },

    // TABLE CRUD
    async addTable(formData) {
      try {
        this.clearErrors()
        const response = await api.post(
          '/establishements/restaurant/table/create/',
          formData,
          { headers: { 'Content-Type': 'multipart/form-data' } }
        )
        await this.fetchOwnerEstablishement()
        return response.data
      } catch (error) {
        console.log(error.response.data,"ici")
        this.setErrors({ newTable: error.response?.data || {} })
        throw error
      }
    },

    async updateTable(tableId, formData) {
      try {
        this.clearErrors()
        await api.patch(
          `/establishements/restaurant/table/update/${tableId}/`,
          formData,
          { headers: { 'Content-Type': 'multipart/form-data' } }
        )
        await this.fetchOwnerEstablishement()
      } catch (error) {
        console.log(error.response.data,"ici")
        this.setErrors({ updateTable: error.response?.data || {} })
        throw error
      }
    },

    async deleteTable(tableId) {
      try {
        await api.delete(`/establishements/restaurant/table/delete/${tableId}/`)
        await this.fetchOwnerEstablishement()
      } catch (error) {
        console.error('Error deleting table:', error.response?.data || error.message)
      }
    },

    // MENU ITEM CRUD
    async addMenuItem(data) {
      try {
        this.clearErrors()
        const response = await api.post(
          '/establishements/restaurant/menu/menu-item/create/',
          data
        )
        await this.fetchOwnerEstablishement()
        return response.data
      } catch (error) {
        this.setErrors({ newMenuItem: error.response?.data || {} })
        throw error
      }
    },

    async updateMenuItem(menuItemId, data) {
      try {
        this.clearErrors()
        await api.put(
          `/establishements/restaurant/menu/menu-item/update/${menuItemId}/`,
          data
        )
        await this.fetchOwnerEstablishement()
      } catch (error) {
        this.setErrors({ updateMenuItem: error.response?.data || {} })
        throw error
      }
    },

    async deleteMenuItem(menuItemId) {
      try {
        await api.delete(`/establishements/restaurant/menu/menu-item/delete/${menuItemId}/`)
        await this.fetchOwnerEstablishement()
      } catch (error) {
        console.error('Error deleting menu item:', error.response?.data || error.message)
      }
    }
  }
})

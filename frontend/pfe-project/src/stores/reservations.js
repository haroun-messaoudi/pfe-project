import { defineStore } from 'pinia'
import api from '@/axios'

export const useReservationsStore = defineStore('reservations', {
  state: () => ({
    hotelReservations: [],
    restaurantReservations: []
  }),

  actions: {
    async fetchReservations() {
      try {
        const { data } = await api.get('reservations/client/list')
        this.hotelReservations = data.hotel_reservations
        this.restaurantReservations = data.restaurant_reservations
      } catch (error) {
        console.error('Failed to fetch reservations:', error)
      }
    }
    }
})
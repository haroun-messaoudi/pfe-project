import { defineStore } from 'pinia';
import api from '@/axios'

export const useTopEstablishmentsStore = defineStore('topEstablishments', {
  state: () => ({
    bestHotels: [], // Array to store best-rated hotels
    bestRestaurants: [], // Array to store best-rated restaurants
  }),
  actions: {
    async fetchBestHotels() {
      try {
        const response = await api.get('/establishements/best-hotels/');
        this.bestHotels = response.data; // Store the fetched hotels
        console.log('Best Hotels:', this.bestHotels);
      } catch (error) {
        console.error('Error fetching best hotels:', error.response?.data || error.message);
      }
    },
    async fetchBestRestaurants() {
      try {
        const response = await api.get('/establishements/best-restaurants/');
        this.bestRestaurants = response.data; // Store the fetched restaurants
        console.log('Best Restaurants:', this.bestRestaurants);
      } catch (error) {
        console.error('Error fetching best restaurants:', error.response?.data || error.message);
      }
    },
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'topEstablishmentsStore',
        storage: localStorage, // Persist data in localStorage
      },
    ],
  },
});
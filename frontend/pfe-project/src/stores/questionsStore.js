import { defineStore } from 'pinia';
import api from '@/axios';

export const useQuestionsStore = defineStore('questionsStore', {
  state: () => ({
    hotelQuestions: [],
    restaurantQuestions: [],
  }),
  actions: {
    async fetchHotelQuestions() {
      try {
        const response = await api.get('/reviews/questions/hotel/');
        this.hotelQuestions = response.data;
        console.log('Hotel Questions:', this.hotelQuestions);
      } catch (error) {
        console.error('Error fetching hotel questions:', error.response?.data || error.message);
      }
    },
    async fetchRestaurantQuestions() {
      try {
        const response = await api.get('/reviews/questions/restaurant/');
        this.restaurantQuestions = response.data; // Store the fetched restaurant questions
        console.log('Restaurant Questions:', this.restaurantQuestions);
      } catch (error) {
        console.error('Error fetching restaurant questions:', error.response?.data || error.message);
      }
    },
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'questionsStore',
        storage: localStorage, 
      },
    ],
  },
});
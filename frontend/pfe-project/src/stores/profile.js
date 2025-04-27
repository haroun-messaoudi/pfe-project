import { defineStore } from 'pinia'
import api from '@/axios';

export const useProfileStore = defineStore('profile', {
  state: () => ({
    firstName: '',
    lastName: '',
    phoneNumber: '',
  }),
  actions: {
    async fetchProfileDetails() {
      try {
        const response = await api.get('accounts/profiles/update-details/');
        const data = response.data;

        this.firstName = data.first_name;
        this.lastName = data.last_name;
        this.phoneNumber = data.phone_number;
        console.log('Profile details fetched successfully:', data);
      } catch (error) {
        console.error('Error fetching profile details:', error.response?.data || error.message);
      }
    },
  },
});

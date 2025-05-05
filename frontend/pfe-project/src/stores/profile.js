import { defineStore } from 'pinia'
import api from '@/axios';
import { useUserStore } from '@/stores/user';





export const useProfileStore = defineStore('profile', {
  

  state: () => ({
    firstName: '',
    lastName: '',
    phoneNumber: '',
    establishement : '',
    establishementReviews : [],
    establishementRooms : [],
    establishementTables : [],
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
    async fetchProfileEstablishementDetails(){
      const userStore = useUserStore();
      if(userStore.profileRole==="owner"){
        try {
          const response = await api.get('establishements/details/');
          const data = response.data;
          this.establishement = data;
          console.log('Estab details fetched successfully:', data.details);
        } catch (error) {
          console.error('Error fetching profile details:', error.response?.data || error.message);
        }
      }
    },
    async fetchEstablishementReviews(){
      const userStore = useUserStore();
      if(userStore.profileRole==="owner"){
        try {
          const response = await api.get(`reviews/establishment/${this.establishement.id}/`);
          const data = response.data;
          this.establishementReviews = data;
          console.log('Estab details fetched successfully:', data);
        } catch (error) {
          console.error('Error fetching profile details:', error.response?.data || error.message);
        }
      }
    },
    async fetchEstblishementRoomsAndTables(){
      const userStore = useUserStore();
      if(userStore.profileRole==="owner"){
        if(this.establishement.type == "restaurant"){
          try {
            const response = await api.get(`establishements/tables-and-rooms/`);
            const data = response.data;
            this.establishementTables = data.tables;
            console.log('Estab details fetched successfully:', data);
          } catch (error) {
            console.error('Error fetching profile details:', error.response?.data || error.message);
          }
        } else if(this.establishement.type == "hotel"){
          try {
            const response = await api.get(`establishements/tables-and-rooms/`);
            const data = response.data;
            this.establishementRooms = data.rooms;
            console.log('Estab details fetched successfully:', data);
          } catch (error) {
            console.error('Error fetching profile details:', error.response?.data || error.message);
          }
        }
       }
     }
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'profile',
        storage: localStorage,
      },
    ],
  },
});

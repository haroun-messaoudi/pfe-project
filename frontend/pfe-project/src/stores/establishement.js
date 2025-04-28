import { defineStore } from 'pinia'
import api from '@/axios'
import { reactive } from 'vue'
export const useEstablishementStore = defineStore('establishement', {
  state: () => ({
    establishement: null,
    errors:reactive({ 
      name: '',
      location: '',
      email: '',
      phone_number: '',
      city: '',
      description: '',
      hotel: {
        stars: '',
        amenities: '',
      },
      restaurant: {
        cuisines: '',
      },
      newRoom: {
        room_type: '',
        price_per_night: '',
        amount: '',
      },
      newTable: {
        capacity: '',
        description: '',
        amount: '',
        location: '',
      },
      newMenuItem: {
        name: '',
        description: '',
        price: '',
      }}),
    cuisines: [],
    amenities: [],
}),
  actions: {
    async fetchOwnerEstablishement() {
      try {
        const response = await api.get('/establishements/details/');
        console.log(response.data)
        this.establishement = response.data;
        this.clearErrors();
        
      } catch (error) {
        console.error('Error fetching establishment:', error.response?.data || error.message);
      }
    },
    async updateEstablishement(data) {
      try {
        const response = await api.put(`/establishements/update/`, data);
        this.establishement = response.data;
        this.clearErrors();

      } catch (error) {
        this.setErrors(error.response?.data || {});
      }
    },
    async addRoom(data) {
      try {
        const response = await api.post('/establishements/hotel/room/create/', data);
        await this.fetchOwnerEstablishement();
        return response.data;
      } catch (error) {
        this.setErrors(error.response?.data || {});
        throw error;
      }
    },
    async updateRoom(roomId, data) {
      try {
        await api.put(`/establishements/hotel/room/update/${roomId}/`, data);
        await this.fetchOwnerEstablishement();
      } catch (error) {
        this.setErrors(error.response?.data || {});
      }
    },
    async deleteRoom(roomId) {
      try {
        await api.delete(`/establishements/hotel/room/delete/${roomId}/`);
        await this.fetchOwnerEstablishement();
      } catch (error) {
        this.setErrors(error.response?.data || {});
      }
    },
    async addTable(data) {
      try {
        const response = await api.post('/establishements/restaurant/table/create/', data);
        await this.fetchOwnerEstablishement();
        return response.data;
      } catch (error) {
        this.setErrors(error.response?.data || {});
        throw error;
      }
    },
    async updateTable(tableId, data) {
      try {
        await api.put(`/establishements/restaurant/table/update/${tableId}/`, data);
        await this.fetchOwnerEstablishement();
      } catch (error) {
        this.setErrors(error.response?.data || {});
      }
    },
    async deleteTable(tableId) {
      try {
        await api.delete(`/establishements/restaurant/table/delete/${tableId}/`);
        await this.fetchOwnerEstablishement();
      } catch (error) {
        this.setErrors(error.response?.data || {});
      }
    },
    async addMenuItem(data) {
      try {
        const response = await api.post('/establishements/restaurant/menu/menu-item/create/', data);
        await this.fetchOwnerEstablishement();
        return response.data;
      } catch (error) {
        this.setErrors(error.response?.data || {});
        throw error;
      }
    },
    async updateMenuItem(menuItemId, data) {
      try {
        await api.put(`/establishements/restaurant/menu/menu-item/update/${menuItemId}/`, data);
        await this.fetchOwnerEstablishement();
      } catch (error) {
        this.setErrors(error.response?.data || {});
      }
    },
    async deleteMenuItem(menuItemId) {
      try {
        await api.delete(`/establishements/restaurant/menu/menu-item/delete/${menuItemId}/`);
        await this.fetchOwnerEstablishement();
      } catch (error) {
        this.setErrors(error.response?.data || {});
      }
    },
    async fetchCuisines() {
      try {
        const response = await api.get('/establishements/cuisines/list/');
        this.cuisines = response.data.map((item) => ({
          label: item.name,
          value: item.id,
        }));
      } catch (error) {
        console.error('Error fetching cuisines:', error.response?.data || error.message);
        this.cuisines = [];
      }
    },
    async updateHotel(hotelData) {
      try {
        const response = await api.put('/establishements/hotel/update/', hotelData);
        this.establishement.hotel = response.data; // Update the hotel data in the state
        this.clearErrors(); // Clear errors after a successful update
      } catch (error) {
        console.error('Error updating hotel:', error.response?.data || error.message);
        this.setErrors(error.response?.data || {}); // Set errors from the backend
      }
    },
    async updateRestaurant(restaurantData) {
      try {
        const response = await api.put('/establishements/restaurant/update/', restaurantData);
        this.establishement.restaurant = response.data; // Update the restaurant data in the state
        this.clearErrors(); // Clear errors after a successful update
      } catch (error) {
        console.error('Error updating restaurant:', error.response?.data || error.message);
        this.setErrors(error.response?.data || {}); // Set errors from the backend
      }
    },
    async fetchAmenities() {
      try {
        const response = await api.get('/establishements/amenities/list/');
        console.log("backend response",response.data)
        this.amenities = response.data.map((item) => ({
          label: item.name,
          value: item.id,
        }));
      } catch (error) {
        console.error('Error fetching amenities:', error.response?.data || error.message);
        this.amenities = [];
      }
    },
    async searchEstablishements(query, filters) {
      const filterString = filters.join(" AND ");
      const response = await api.get('/establishements/search/', {
        params: {
          q: query,
          filters: filterString
        }
      });
      console.log("search response",response.data)
      return response.data;
    },    
    setErrors(backendErrors) {
      this.errors.name = backendErrors.name?.[0] || '';
      this.errors.location = backendErrors.location?.[0] || '';
      this.errors.email = backendErrors.email?.[0] || '';
      this.errors.phone_number = backendErrors.phone_number?.[0] || '';
      this.errors.city = backendErrors.city?.[0] || '';
      this.errors.description = backendErrors.description?.[0] || '';
      if (backendErrors.hotel) {
        this.errors.hotel.stars = backendErrors.hotel.stars?.[0] || '';
        this.errors.hotel.amenities = backendErrors.hotel.amenities?.[0] || '';
        this.errors.hotel.checkInTime = backendErrors.hotel.checkInTime?.[0] || ''; // Handle check-in time errors
    this.errors.hotel.checkOutTime = backendErrors.hotel.checkOutTime?.[0] || ''; // Handle check-out time errors
      }
      if (backendErrors.restaurant) {
        this.errors.restaurant.cuisines = backendErrors.restaurant.cuisines?.[0] || '';
      }
      if (backendErrors.newRoom) {
        this.errors.newRoom.room_type = backendErrors.newRoom.room_type?.[0] || '';
        this.errors.newRoom.price_per_night = backendErrors.newRoom.price_per_night?.[0] || '';
        this.errors.newRoom.amount = backendErrors.newRoom.amount?.[0] || '';
      }
      if (backendErrors.newTable) {
        this.errors.newTable.capacity = backendErrors.newTable.capacity?.[0] || '';
        this.errors.newTable.description = backendErrors.newTable.description?.[0] || '';
        this.errors.newTable.amount = backendErrors.newTable.amount?.[0] || '';
        this.errors.newTable.location = backendErrors.newTable.location?.[0] || '';
      }
      if (backendErrors.newMenuItem) {
        this.errors.newMenuItem.name = backendErrors.newMenuItem.name?.[0] || '';
        this.errors.newMenuItem.description = backendErrors.newMenuItem.description?.[0] || '';
        this.errors.newMenuItem.price = backendErrors.newMenuItem.price?.[0] || '';
      }
    },
    clearErrors() {
      setTimeout(() =>{
        this.errors.name = '';
        this.errors.location = '';
        this.errors.email = '';
        this.errors.phone_number = '';
        this.errors.city = '';
        this.errors.description = '';
        this.errors.hotel.stars = '';
        this.errors.hotel.amenities = '';
        this.errors.restaurant.cuisines = '';
        this.errors.newRoom.room_type = '';
        this.errors.newRoom.price_per_night = '';
        this.errors.newRoom.amount = '';
        this.errors.newTable.capacity = '';
        this.errors.newTable.description = '';
        this.errors.newTable.amount = '';
        this.errors.newTable.location = '';
        this.errors.newMenuItem.name = '';
        this.errors.newMenuItem.description = '';
        this.errors.newMenuItem.price = '';

      }
      , 2000);
    },
  },
});
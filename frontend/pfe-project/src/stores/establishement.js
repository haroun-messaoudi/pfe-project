import { defineStore } from 'pinia'
import api from '@/axios'

export const useEstablishementStore = defineStore('establishement', {
  state: () => ({
    establishement: null,
    errors: null,
  }),
  actions: {
    async fetchOwnerEstablishement() {
      try {
        const response = await api.get('/establishements/details/');
        this.establishement = response.data;
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error fetching establishment:', this.errors);
      }
    },
    async updateEstablishement(data) {
      try {
        const response = await api.put(`/establishements/update/${this.establishement.id}/`, data);
        this.establishement = response.data;
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error updating establishment:', this.errors);
      }
    },
    async updateRoom(roomId, data) {
      try {
        await api.put(`/establishements/hotel/room/update/${roomId}/`, data);
        await this.fetchOwnerEstablishement(); // Refresh data
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error updating room:', this.errors);
      }
    },
    async deleteRoom(roomId) {
      try {
        await api.delete(`/establishements/hotel/room/delete/${roomId}/`);
        await this.fetchOwnerEstablishement(); // Refresh data
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error deleting room:', this.errors);
      }
    },
    async updateTable(tableId, data) {
      try {
        await api.put(`/establishements/restaurant/table/update/${tableId}/`, data);
        await this.fetchOwnerEstablishement(); // Refresh data
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error updating table:', this.errors);
      }
    },
    async deleteTable(tableId) {
      try {
        await api.delete(`/establishements/restaurant/table/delete/${tableId}/`);
        await this.fetchOwnerEstablishement(); // Refresh data
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error deleting table:', this.errors);
      }
    },
    async updateMenuItem(menuItemId, data) {
      try {
        await api.put(`/establishements/restaurant/menu/menu-item/update/${menuItemId}/`, data);
        await this.fetchOwnerEstablishement(); // Refresh data
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error updating menu item:', this.errors);
      }
    },
    async deleteMenuItem(menuItemId) {
      try {
        await api.delete(`/establishements/restaurant/menu/menu-item/delete/${menuItemId}/`);
        await this.fetchOwnerEstablishement(); // Refresh data
      } catch (error) {
        this.errors = error.response?.data || error.message;
        console.error('Error deleting menu item:', this.errors);
      }
    },
  },
});
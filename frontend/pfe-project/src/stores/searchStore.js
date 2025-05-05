import { defineStore } from 'pinia';
import api from '@/axios';


export const useSearchStore = defineStore('search', {
  state: () => ({
    results: [], // Array to store search results
    totalHits: 0, // Total number of hits
    processingTime: 0, // Time taken for the search
  }),
  actions: {
    async setSearchResults(data) {
      this.results = data.hits || [];
      this.results = await Promise.all(this.results.map(async (item) => {
        console.log({...item}+"hnaaaa")
        const response = await api.get(`establishements/${item.objectID}/images/`);
        console.log(response)
        const images = response.data;
        item.images = images.map((image) => {
          return {
            id: image.id,
            image: image.image_url            ,
          };
        });
        return item;
      }));
      this.totalHits = data.nbHits || 0;
      this.processingTime = data.processingTimeMS || 0;
    },
    clearSearchResults() {
      this.results = [];
      this.totalHits = 0;
      this.processingTime = 0;
    },
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'searchStore', // Key to store in localStorage
        storage: localStorage, // Use localStorage (or sessionStorage if needed)
      },
    ],
  },
});
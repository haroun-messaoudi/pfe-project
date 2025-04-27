import { defineStore } from 'pinia';

export const useSearchStore = defineStore('search', {
  state: () => ({
    results: [], // Array to store search results
    totalHits: 0, // Total number of hits
    processingTime: 0, // Time taken for the search
  }),
  actions: {
    setSearchResults(data) {
      this.results = data.hits || [];
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
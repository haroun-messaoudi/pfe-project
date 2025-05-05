// src/stores/topestablishments.js
import { defineStore } from 'pinia';
import api from '@/axios';

export const useTopEstablishmentsStore = defineStore('topEstablishments', {
  state: () => ({
    bestHotels: {
      hits: [],
      nbHits: 0,
      processingTimeMS: 0,
    },
    bestRestaurants: {
      hits: [],
      nbHits: 0,
      processingTimeMS: 0,
    },
  }),

  actions: {
    async fetchBestHotels() {
      try {
        // 1) hit your DRF/Algolia-backed endpoint
        const { data } = await api.get('/establishements/best-hotels/');

        // 2) pull out the hits array
        const hits = data.hits || [];

        // 3) fetch & attach images exactly like in your searchStore
        const enriched = await Promise.all(
          hits.map(async (item) => {
            const res = await api.get(
              `/establishements/${item.objectID}/images/`
            );
            const images = res.data || [];
            item.images = images.map((img) => ({
              id: img.id,
              image: img.image_url,
            }));
            return item;
          })
        );

        // 4) commit back to state
        this.bestHotels = {
          hits: enriched,
          nbHits: data.nbHits || enriched.length,
          processingTimeMS: data.processingTimeMS || 0,
        };


      } catch (err) {
        console.error(
          'Error fetching best hotels:',
          err.response?.data || err.message
        );
      }
    },

    async fetchBestRestaurants() {
      try {
        const { data } = await api.get('/establishements/best-restaurants/');
        const hits = data.hits || [];

        const enriched = await Promise.all(
          hits.map(async (item) => {
            const res = await api.get(
              `/establishements/${item.objectID}/images/`
            );
            const images = res.data || [];
            console.log(images)
            item.images = images.map((img) => ({
              id: img.id,
              image: img.image_url,
            }));
            return item;
          })
        );

        this.bestRestaurants = {
          hits: enriched,
          nbHits: data.nbHits || enriched.length,
          processingTimeMS: data.processingTimeMS || 0,
        };
        console.log(this.bestRestaurants.hits,"hits here")
      } catch (err) {
        console.error(
          'Error fetching best restaurants:',
          err.response?.data || err.message
        );
      }
    },
  },

  persist: {
    enabled: true,
    strategies: [
      {
        key: 'topEstablishmentsStore',
        storage: localStorage,
      },
    ],
  },
});

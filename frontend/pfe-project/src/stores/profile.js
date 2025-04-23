import { defineStore } from 'pinia'


export const useProfileStore = defineStore('profile', {
  state: () => ({
    firstName : "blyat",
    lastName : "kurva",
    phoneNumber: "05982554",
  })})
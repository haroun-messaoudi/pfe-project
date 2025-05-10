<script setup>
import myReservations from '@/components/myReservations.vue'
import profilenav from '@/components/profilenav.vue'
import { onMounted } from 'vue'
import { useReservationsStore } from '@/stores/reservations'

const reservationsStore = useReservationsStore()

onMounted(async() => {
  await reservationsStore.fetchReservations()
})
</script>

<template>
  <div>
    <profilenav :buttonText="'Sign Up'" :buttonStatus="false"/>
    <myReservations 
      :hotelReservation="reservationsStore.hotelReservations" 
      :restaurantReservation="reservationsStore.restaurantReservations" 
    />
  </div>
</template>
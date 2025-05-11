<script setup>
import myReservation from '@/components/myReservation.vue'
import myReservationR from './myReservationR.vue';


const props = defineProps({
  hotelReservation: {
    type: Array,
    default: () => []
  },
  restaurantReservation: {
    type: Array,
    default: () => []
  }
})

console.log('hotels:', props.hotelReservation)
console.log('restaurants:', props.restaurantReservation)


</script>

<template>
  <section class="px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl border-b p-5 border-gray-500 font-bold mb-6 text-center">
        My Reservations
      </h2>
      <h1 v-if="!props.hotelReservation.length && !props.restaurantReservation.length" class="text-3xl font-normal text-center text-gray-500">You have no pending reservations.</h1>
      <div class="flex flex-col gap-4">
        
        <h1 v-if="props.hotelReservation.length" class="text-3xl font-semibold">Hotels reservations:</h1>

        <myReservation
          v-for="room in props.hotelReservation"
          :key='room.id'
          :estaName='room.establishment'
          :checkInDate="new Date(room.check_in_date).toLocaleDateString('en-CA')"
          :checkOutDate="new Date(room.check_out_date).toLocaleDateString('en-CA')"
          :status='room.status'
          :numberOfPeople='room.number_of_people'
          :roomType='room.room_type'
          :id="room.id"
        />
        <h1 v-if="props.restaurantReservation.length" class="text-3xl font-semibold">Restaurants reservations:</h1>
        <myReservationR
          v-for="table in props.restaurantReservation"
          :key="table.id"
          :estaName="table.establishment"
          :date="new Date(table.date).toLocaleDateString('en-CA')"
          :status="table.status"
          :number-of-people="table.numberOfPeople"
          :table_location = "table.table_location"
          :id="table.id"
        />
      </div>
    </div>
  </section>
</template>
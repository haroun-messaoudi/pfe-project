<script setup>
import owneReservation from './owneReservation.vue';   // hotel-reservation card
import owneReservationR from './owneReservationR.vue'; // restaurant-reservation card

const props = defineProps({
  reservations: {
    type: Array,
    default: () => []
  }
});
const emits = defineEmits(['deleted']);
</script>

<template>
  <div class="shadow-lg bg-gray-100 p-5 m-5 rounded-lg">
    <template v-for="res in props.reservations" :key="res.id">
      <owneReservation
        v-if="res.room"
        :reservation-type="'hotels'"
        :id="res.id"
        :estaName="res.establishment_name"
        :checkInDate="res.check_in_date"
        :checkOutDate="res.check_out_date"
        :status="res.status"
        :numberOfPeople="res.numberOfPeople"
        :roomType="res.room_type"
        @deleted="$emit('deleted')"
      />

      <owneReservationR
        v-else-if="res.table"
        :reservation-type="'restaurants'"
        :id="res.id"
        :estaName="res.establishment_name"
        :Date="res.date"
        :status="res.status"
        :numberOfPeople="res.numberOfPeople"
        :tableType="res.table_location"
        @deleted="$emit('deleted')"
      />
    </template>
  </div>
</template>

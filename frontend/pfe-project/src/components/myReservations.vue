<script setup>
import myReservation from '@/components/myReservation.vue'
import myReservationR from './myReservationR.vue';
</script>

<template>
    <section class=" px-4 py-10">
      <div class="container-xl lg:container m-auto">
            <!-- big title -->
            <h2 class="text-3xl border-b p-5 border-gray-500 font-bold  mb-6 text-center">
                My Reservations
            </h2>
            <!-- cards loop -->
            <div class="flex flex-col  gap-4"> 
                <myReservation />
                <myReservation />
                <myReservation />
                <myReservationR />
                <myReservationR />
                <myReservationR />
            </div>
        </div>
    </section>
</template>
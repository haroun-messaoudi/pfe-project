<script setup>
import ownerNav from '@/components/ownerNav.vue';
import owneReserHolder from '@/components/owneReserHolder.vue';
import { ref, onMounted } from 'vue';
import api from '@/axios';

const reservations = ref([]);

// 1️⃣ Extract your load logic into a reusable function
async function loadReservations() {
  try {
    const { data } = await api.get('reservations/owner/list/');
    reservations.value = data;
    console.log(data)
  } catch (err) {
    console.error('failed to load owner reservations', err);
  }
}

// 2️⃣ Call it on mount
onMounted(loadReservations);
</script>

<template>
  <div>
    <ownerNav />

    <h2 class="text-3xl font-bold pb-6 text-center bg-gray-100 pt-5">
      The Reservations
    </h2>

    <!-- 3️⃣ Listen for `deleted` from the holder and reload -->
    <owneReserHolder
      :reservations="reservations"
      @deleted="loadReservations"
    />
  </div>
</template>

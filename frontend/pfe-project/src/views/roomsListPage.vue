<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/axios'

import roomCard from '@/components/roomCard.vue'
import profilenav from '@/components/profilenav.vue'
import HotelReservationDialog from '@/components/HotelReservationDialog.vue'

// grab the establishment id from the URL
const route = useRoute()
const estabId = route.params.id

// state
const rooms = ref([])
const showDialog = ref(false)
const selectedRoom = ref(null)

// fetch once
onMounted(async () => {
  try {
    const { data } = await api.get(`/establishements/${estabId}/rooms/`)
    rooms.value = data
  }
  catch (err) {
    console.error('Failed to fetch rooms:', err)
  }
})

// when a user clicks a room-card
function openReservation(room) {
  selectedRoom.value = room
  showDialog.value = true
}

// after reservation is complete
function onReserved() {
  showDialog.value = false
  // you could re-fetch rooms here if you want
}
</script>

<template>
  <div>
    <profilenav />
    
    <section class="px-1 py-10 bg-gray-100 p-5 m-5 border-0 rounded-lg">
      <div class="container-xl lg:container m-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div
            v-for="room in rooms"
            :key="room.id"
            class="cursor-pointer hover:shadow-lg transition"
            @click="openReservation(room)"
          >
            <roomCard :roomInfo="room" />
          </div>
        </div>
      </div>
    </section>
    
    <!-- the hotel reservation dialog - passing roomInfo instead of roomId -->
    <HotelReservationDialog
      :roomInfo="selectedRoom"
      v-model:visible="showDialog"
      @reserved="onReserved"
    />
  </div>
</template>

<style scoped>
.cursor-pointer { cursor: pointer; }
</style>
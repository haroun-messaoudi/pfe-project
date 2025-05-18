<script setup>
import Card from 'primevue/card'
import restImg from '@/assets/img/rest.webp'

const props = defineProps({
  roomInfo: {
    type: Object,
    required: true
  }
})
console.log(props.roomInfo)
</script>

<template>
  <!-- Card fills its grid column using w-full -->
  <Card class="bg-orange-50 p-4 w-full overflow-hidden">
    <!-- Header: Room Image -->
    <template #header>
      <img
        :src="props.roomInfo.image_url || restImg"
        alt="Room image"
        class="w-full h-48 object-cover mb-4"
      />
    </template>

    <!-- Title: Room Type -->
    <template #title>
      <h3 class="text-xl font-semibold">Type: {{ props.roomInfo.room_type }}</h3>
    </template>

    <!-- Subtitle: Capacity -->
    <template #subtitle>
      <span class="capitalize">Capacity: {{ props.roomInfo.capacity }} guest(s)</span>
    </template>

    <!-- Content: Price and Description -->
    <template #content>
      <p class="text-gray-700 mb-4">
        <strong>Price:</strong> {{ props.roomInfo.price_per_night }} DA
      </p>
      <p class="text-gray-700">
        <strong>Description:</strong>
        {{ props.roomInfo.description || 'No description available.' }}
      </p>
    </template>

    <!-- Footer: Actions slot (e.g., Book button) -->
    <template #footer>
      <div class="flex justify-end">
        <slot name="actions" />
      </div>
    </template>
  </Card>
</template>

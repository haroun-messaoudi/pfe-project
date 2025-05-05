<script setup>
import Card from 'primevue/card';

import restImg from '@/assets/img/rest.webp';
import { warn } from 'vue';

const props = defineProps({
  tableInfo: {
    type: Object,
    required: true
  }
});
</script>

<template>
  <!-- Card fills its grid column using w-full -->
  <Card class="bg-orange-50 p-4 w-full overflow-hidden">
    <!-- Header: Establishment Image -->
    <template #header>
      <img
        :src="props.tableInfo.image_url || restImg"
        alt="Establishment image"
        class="w-full h-48 object-cover mb-4"
      />
    </template>

    <!-- Title: capacity -->
    <template #title>
      <h3 class="text-xl font-semibold">Capacity:{{ props.tableInfo.capacity }}</h3>
    </template>

    <!-- Subtitle: total rooms alike -->
    <template #subtitle>
      <span class="capitalize">Available:{{ props.tableInfo.amount }}</span>
      <span class="mx-1">•</span>
    </template>

    <!-- Content: Description -->
    <template #content>
      <p class="text-gray-700 mb-4">
        Description:{{ props.tableInfo.description || 'No description available.' }}
      </p>
    </template>
    <!-- Content: price per one night -->
    <template #content1>
      <p class="text-gray-700 mb-4">
        Price per night:{{ props.tableInfo.price_per_night }}
      </p>
    </template>
    <!-- Footer: rooms type -->
    <template #footer>
      <div class="flex flex-col">
        <small class="text-sm text-gray-600 mb-2">
          Type: {{ props.tableInfo.room_type }}
        </small>
        
      </div>
    </template>
  </Card>
</template>

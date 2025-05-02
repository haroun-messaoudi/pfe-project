<script setup>
import Card from 'primevue/card';
import Rating from 'primevue/rating';
import restImg from '@/assets/img/rest.webp';
import { RouterLink } from 'vue-router';
import { warn } from 'vue';

const props = defineProps({
  cardInfo: {
    type: Object,
    required: true
  }
});
</script>

<template>
  <RouterLink :to="`/details/${cardInfo.objectID}`">
  <!-- Card fills its grid column using w-full -->
  <Card class="bg-orange-50 p-4 w-full overflow-hidden">
    <!-- Header: Establishment Image -->
    <template #header>
      <img
        :src="props.cardInfo.image || restImg"
        alt="Establishment image"
        class="w-full h-48 object-cover mb-4"
      />
    </template>

    <!-- Title: Name -->
    <template #title>
      <h3 class="text-xl font-semibold">{{ props.cardInfo.name }}</h3>
    </template>

    <!-- Subtitle: Type • City -->
    <template #subtitle>
      <span class="capitalize">{{ props.cardInfo.type }}</span>
      <span class="mx-1">•</span>
      <span>{{ props.cardInfo.city }}</span>
    </template>

    <!-- Content: Description -->
    <template #content>
      <p class="text-gray-700 mb-4">
        {{ props.cardInfo.description || 'No description available.' }}
      </p>
    </template>

    <!-- Footer: Location & Rating (Rating below location) -->
    <template #footer>
      <div class="flex flex-col">
        <small class="text-sm text-gray-600 mb-2">
          📍 {{ props.cardInfo.location }}
        </small>
        <Rating
          :modelValue="Number(props.cardInfo.average_rating)"
          readonly
          :stars="5"
          :cancel="false"
        />
      </div>
    </template>
  </Card>
  </RouterLink>
</template>

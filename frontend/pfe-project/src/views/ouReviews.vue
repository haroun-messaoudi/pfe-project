<script setup>
import ownerNav from '@/components/ownerNav.vue';
import owneReviewsHolder from '@/components/owneReviewsHolder.vue';
import { onMounted } from 'vue';
import { useProfileStore } from '@/stores/profile';
const profileStore = useProfileStore()

onMounted(async() => {
  // Fetch or initialize any data needed for the component
  await profileStore.fetchEstablishementReviews()
  console.log(profileStore.establishement.reviews)
})
</script>


<template>
    <div>
    <ownerNav />
    <h2 class="text-3xl font-bold pb-6 text-center bg-gray-100 pt-5">
        The Reviews
      </h2>
    <owneReviewsHolder :reviews="profileStore.establishementReviews"  />
    </div>
</template>
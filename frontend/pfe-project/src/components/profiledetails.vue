<script setup>
import { useProfileStore } from '@/stores/profile';
import { ref, onMounted } from 'vue';

const profileData = ref({ firstName: '', lastName: '', phoneNumber: '' }); // Reactive ref for profile data
const profileStore = useProfileStore(); // Access the profile store

onMounted(async () => {
  await profileStore.fetchProfileDetails();
  profileData.value.firstName = profileStore.firstName; // Update the ref with store data
  profileData.value.lastName = profileStore.lastName;
  profileData.value.phoneNumber = profileStore.phoneNumber;
  console.log('Profile data:', profileData.value)
});
</script>

<template>
  <div class="p-10 flex space-x-10">
    <!-- Profile Image -->
    <img class="h-40 w-40 rounded-full" src="@/assets/img/rest.webp" />

    <!-- Profile Details -->
    <div>
      <h1 class="text-2xl font-bold">
        {{ profileData.firstName }} - {{ profileData.lastName }}
      </h1>
      <div>{{ profileData.phoneNumber }}</div>
    </div>
  </div>
</template>
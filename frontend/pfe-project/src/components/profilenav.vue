<script setup>
import Button from 'primevue/button';
import { RouterLink} from 'vue-router';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

const logout = async () => {
  try {
    await userStore.logout();

  } catch (error) {
    console.error('Logout failed:', error);
  }
};

</script>

<template>

<div class="h-20 border-b border-gray-800 flex justify-between items-center px-5">
<RouterLink to="/">
<div class="flex space-x-4 items-center  border-2 border-gray-500 p-3 rounded-lg">
    <i class="pi pi-home"></i>
    <p>Home Page</p>
</div>
</RouterLink>
<!-- stay-bite logo -->
<RouterLink to="/">
<img class="h-20 w-auto" src="@/assets/img/logo.png" />
</RouterLink>
<Button label="Logout" severity="warn" rounded @click="logout" v-if="userStore.isAuthenticated"  />
<!-- <RouterLink to="/login">
  <Button label="Login" severity="warn" rounded v-if="!userStore.isAuthenticated"  />
</RouterLink> -->


</div>    
</template>
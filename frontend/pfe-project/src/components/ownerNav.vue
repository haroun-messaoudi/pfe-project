<script setup>
// primeVue
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Toolbar from 'primevue/toolbar';
import Avatar from 'primevue/avatar';

import Select from 'primevue/select';
import { ref } from 'vue';
// routerlink
import { RouterLink } from 'vue-router';
import { useEstablishementStore } from '@/stores/establishement.js';
import { onMounted } from 'vue';
import { useSearchStore } from '@/stores/searchStore.js';
import { MultiSelect } from 'primevue';
import { useUserStore } from '@/stores/user.js';

const searchStore = useSearchStore();

  

const establishementStore = useEstablishementStore();






const userStore = useUserStore();

defineProps({
  page: String
})
</script>

<template>
<div>
    <!-- main navbar -->
    <div class="border-b border-gray-800 flex justify-between items-center px-5">
        <!-- stay-bite logo -->
        <RouterLink to="/">
          <img class="h-20 w-auto" src="@/assets/img/logo.png" />
        </RouterLink>
        <!-- buttons -->
        <div class="flex justify-between gap-10"> 
            <RouterLink to="/ownerPage/ouReservations"> <Button label="Our Reservations" text plain />
            </RouterLink>
            <RouterLink to="/ownerPage/ouReviews"> <Button label="Our Review" text plain />
            </RouterLink>
            <RouterLink to="/contactUs"> <Button label="Contact Us" text plain />
            </RouterLink>
        </div>
        <!-- profile button -->
        <RouterLink v-if="userStore.profileId" to="/profile">
        <Toolbar style="border-radius: 3rem; padding: 1rem 2rem 1rem 1rem">
            <template #end>
                <div class="flex items-center gap-2">
                    <Button label="Profile" severity="warn" rounded />
                    <Avatar image="https://imgs.search.brave.com/MJT-XZW8yyFiiRYQFSPo3uXR3yGVqMiHqBPqduuVYv4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNTA4/NTQwNDE4L3Bob3Rv/L3Byb2ZpbGUtb2Yt/bWlkZGxlLWFnZWQt/YXNpYW4tbWFuLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1Q/d0FFdTU5ZmEta0JX/SmQ0WS1zWV8zMmZm/UHFTdVZrZDJEUmM2/QWNHamxzPQ" style="width: 32px; height: 32px " />
                </div>
            </template>
        </Toolbar>
        </RouterLink>
        <RouterLink v-else to="/login">
          <Button label="Login" severity="warn" rounded />
        </RouterLink>
    </div>

    
    
</div>
</template>
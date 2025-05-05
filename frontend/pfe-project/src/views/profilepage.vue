<script setup>
import profilenav from '@/components/profilenav.vue';
import profiledetails from '@/components/profiledetails.vue';
import myReviews from '@/components/myReviews.vue'
import { useUserStore } from '@/stores/user';


const userStore = useUserStore()
</script>

<template>
    <div>
        <profilenav :buttonText="'log out'"/>
        <profiledetails />
        <myReviews v-if="userStore.profileRole=='client'" />
    </div>
</template>
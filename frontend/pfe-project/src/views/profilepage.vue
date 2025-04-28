<script setup>
import profilenav from '@/components/profilenav.vue';
import profiledetails from '@/components/profiledetails.vue';
import myReviews from '@/components/myReviews.vue'
</script>

<template>
    <div>
        <profilenav :buttonText="'log out'"/>
        <profiledetails />
        <myReviews />
    </div>
</template>
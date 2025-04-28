<script setup>
import myReservations from '@/components/myReservations.vue'
import profilenav from '@/components/profilenav.vue'
 </script>

<template>
    <div>
        <profilenav :buttonText="'Sign Up'" :buttonStatus="false"/>
        <myReservations />
    </div>

</template>
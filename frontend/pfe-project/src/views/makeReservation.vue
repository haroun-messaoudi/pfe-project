<script setup>
import profilenav from '@/components/profilenav.vue';
import tablesHolder from '@/components/tablesHolder.vue';
</script>


<template>
    <profilenav />
    <tablesHolder :title="rooms"/>
</template>
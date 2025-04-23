<script setup>
import { useProfileStore } from '@/stores/profile';
const ProfileStore = useProfileStore();
const { firstName, lastName,  phoneNumber} = ProfileStore;
</script>


<template>
    <div class="p-10 flex  space-x-10">
        <img class="h-40 w-40  rounded-full" src="@/assets/img/rest.webp" />
        <div > 
            <h1 class="text-2xl font-bold "> {{ firstName }} - {{ lastName }}</h1>
            <div> {{ phoneNumber }}</div>
        </div>
    </div>
</template>
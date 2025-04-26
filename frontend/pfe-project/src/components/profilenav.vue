<script setup>
import Button from 'primevue/button';
import { RouterLink } from 'vue-router';
defineProps({
    buttonText:{
        type:String,
    },
    buttonStatus:{
        type:Boolean,
        default:true,
    }
})

</script>

<template>
    <div class="h-20 border-b border-gray-800 flex items-center px-5">
        <RouterLink to="/">
            <div class="flex items-center space-x-4  border-2 border-gray-500 p-3 rounded-lg">
                <i class="pi pi-home"></i>
                <p>Home Page</p>
            </div>
        </RouterLink>
        <!-- stay-bite logo -->
        <div class="flex flex-grow justify-center">
        <RouterLink to="/">
            <img class="h-20 w-auto" src="@/assets/img/logo.png" />
        </RouterLink>
        </div>
        <Button  v-if="buttonStatus" :label="buttonText" severity="warn" rounded />

    </div>    
</template>
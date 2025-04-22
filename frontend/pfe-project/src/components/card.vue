<script setup>
import Card from 'primevue/card';
import Button from 'primevue/button';
import Rating from 'primevue/rating';
import { ref } from 'vue';


defineProps({
    cardInfo:{
        type:Object,
    }
})

</script>

<template>
<Card class="bg-orange-50" style="width: 25rem; overflow: hidden ; padding: 15px;">
    <template #header>
        <img alt="user header" src="@/assets/img/rest.webp" />
    </template>
    <template #name>{{ cardInfo.name }}</template>
    <template #type>{{cardInfo.type}}</template>
    <template #city> {{ cardInfo.city }}</template>
    <template #location> {{ cardInfo.location }}</template>
    <template #description>
        <p class="m-0">
            {{cardInfo.description}}
        </p>
    </template>
    <template #footer>
        <div class="card flex justify-center">
            <Rating class="--p-rating-icon-active-color-red-400" :v-model="cardInfo.average_rating" readonly />
        </div>

    </template>
</Card>

</template>

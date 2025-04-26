<script setup>
// primVue imports
import Card from 'primevue/card';
import Rating from 'primevue/rating';



defineProps({
    cardInfo:{
        type:Object,
    }
})

</script>

<template>
<Card class="bg-orange-50" style="width: 25rem; overflow: hidden ; padding: 15px;">
    <template >
        <img alt="user header" src="@/assets/img/rest.webp" />
    </template>
    <!-- name of estab -->
    <template >{{ cardInfo.name }}</template>
    <!-- restaurant or hatel -->
    <template >{{cardInfo.type}}</template>
    <!-- city of the estab -->
    <template > {{ cardInfo.city }}</template>
    <!-- send location -->
    <template > {{ cardInfo.location }}</template>
    <!-- owner description -->
    <template >
        <p class="m-0">
            {{cardInfo.description}}
        </p>
    </template>
    <template >
        <div class="card flex justify-center">
            <!-- rating of the estab -->
            <Rating class="--p-rating-icon-active-color-red-400" :v-model="cardInfo.average_rating" readonly />
        </div>

    </template>
</Card>
</template>

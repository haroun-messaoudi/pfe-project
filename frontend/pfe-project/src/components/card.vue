<script setup>
import Card from 'primevue/card';
import Button from 'primevue/button';
import Rating from 'primevue/rating';
import { ref } from 'vue';

const value = ref(3);

</script>

<template>
<Card class="bg-orange-50" style="width: 25rem; overflow: hidden ; padding: 15px;">
    <template #header>
        <img alt="user header" src="@/assets/img/rest.webp" />
    </template>
    <template #title>Advanced Card</template>
    <template #subtitle>Card subtitle</template>
    <template #content>
        <p class="m-0">
            waka waka
        </p>
    </template>
    <template #footer>
        <div class="card flex justify-center">
            <Rating class="--p-rating-icon-active-color-red-400" v-model="value" readonly />
        </div>

    </template>
</Card>

</template>

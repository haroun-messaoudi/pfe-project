<script setup>
import { onMounted } from 'vue';
import owneReview from './owneReview.vue';
import { useProfileStore } from '@/stores/profile';


const profileStore = useProfileStore()

const props=defineProps({
    reviews: {
      type: Array,
      required: true
    }
})

</script>




<template>
    
    <div class="shadow-lg bg-gray-100 p-5 m-5 border-0 rounded-lg">
        <owneReview v-for="(item,index) in props.reviews" :key="index" :reviewerName="item.profile" :rating="item.rating" :comment="item.content" :date="item.date_posted" />
    </div>
</template>
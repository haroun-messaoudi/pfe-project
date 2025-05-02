<script setup>
import reviewQst from './reviewQst.vue';
</script>



<template>
    <reviewQst />
    <reviewQst />
    <reviewQst />
    <reviewQst />
    <reviewQst />
    <div class="flex items-start gap-4 mb-4">
      <label for="reviewText" class="font-semibold w-24">Review</label>
      <Textarea id="reviewText" v-model="reviewText" autoResize rows="4" class="flex-auto" />
    </div>
</template>
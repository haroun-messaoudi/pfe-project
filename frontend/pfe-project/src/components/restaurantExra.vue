<template>
    <div class="bg-white rounded-xl shadow p-5 mt-4 w-full max-w-md">
      <h2 class="text-lg font-bold mb-3">Restaurant Details</h2>
  
      <!-- Cuisine Type -->
      <div class="text-sm text-gray-700 mb-3">
        <span class="font-bold ">Cuisine Type:</span> {{ cuisineType }}
      </div>
  
      <!-- View Menu Button -->
      <Button label="View Menu" severity="warn" variant="text"  @click="visible = true" />
  
      <!-- Menu Dialog -->
      <Dialog v-model:visible="visible" modal header="Menu" :style="{ width: '25rem' }">
        <div class="space-y-4">
          <div v-for="(item, index) in menu" :key="index" class="border-b pb-2">
            <div class="font-bold text-base">{{ item.name}}</div>
            <div class="text-sm text-gray-500 mb-1">{{ item.description }}</div>
            <div class="text-sm font-medium text-green-700">{{ item.price }} DA</div>
          </div>
        </div>
        <template #footer>
          <Button label="Close" text severity="warn" @click="visible = false" />
        </template>
      </Dialog>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import Dialog from 'primevue/dialog'
  import Button from 'primevue/button'
  
  const visible = ref(false)

  const props = defineProps({
    menu: {
      type: Array,
      required: true
    },
    cuisineType: {
      type: String,
      required: true
    }
  })
  console.log("menu1", props.menu)
  </script>
  
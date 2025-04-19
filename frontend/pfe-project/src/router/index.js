import Homepage from '@/views/homepage.vue'
import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
   path: '/',
   name: 'home',
   component: Homepage,
    },
  ],
})

export default router

import Homepage from '@/views/homepage.vue'
import { createRouter, createWebHistory } from 'vue-router'
import contactus from '@/views/contactus.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
   path: '/',
   name: 'home',
   component: Homepage,
    },
    {
      path:'/contactUs',
      name:'contactUs',
      component:contactus,
    }
  ],
})

export default router

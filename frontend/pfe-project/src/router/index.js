import Homepage from '@/views/homepage.vue'
import { createRouter, createWebHistory } from 'vue-router'
import contactus from '@/views/contactus.vue'
import profilepage from '@/views/profilepage.vue'

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
    },
    {
      path:'/profile',
      name:'profile',
      component:profilepage,
    },
  ],
})

export default router

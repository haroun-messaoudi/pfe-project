
import EstablishementOwnerDetails from '@/views/establishementOwnerDetails.vue'
import EstablishementCreationPage from '@/views/establishementCreationPage.vue'
import HomePage from '@/views/homepage.vue'
import LoginPage from '@/views/loginPage.vue'
import RegistrationPage from '@/views/registrationPage.vue'
import { createRouter, createWebHistory } from 'vue-router'
import contactus from '@/views/contactus.vue'
import profilepage from '@/views/profilepage.vue'
import reservation from '@/views/reservation.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/register',
      name: 'Registration',
      component: RegistrationPage
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginPage
    }
    ,
    {
      path: '/establishement-create',
      name: 'EstablishementCreate',
      component: EstablishementCreationPage
    }
    ,
    {
      path: '/',
      name: 'Home',
      component: HomePage
    },
    {
      path: '/owner/establishement',
      name: 'OwnerEstablishement',
      component: EstablishementOwnerDetails,
      meta: { requiresAuth: true },
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
    {
      path:'/reservation',
      name:'reservation',
      component:reservation,
    },
  ],
})

export default router

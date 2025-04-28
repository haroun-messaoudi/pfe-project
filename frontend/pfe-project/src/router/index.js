
import EstablishementOwnerDetails from '@/views/establishementOwnerDetails.vue'
import EstablishementCreationPage from '@/views/establishementCreationPage.vue'
import HomePage from '@/views/homePage.vue'
import LoginPage from '@/views/loginPage.vue'
import RegistrationPage from '@/views/registrationPage.vue'
import { createRouter, createWebHistory } from 'vue-router'
import contactus from '@/views/contactus.vue'
import profilepage from '@/views/profilePage.vue'
import SearchResult from '@/views/searchResult.vue'

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
      path:'/searchResult',
      name:'searchResult',
      component:SearchResult
    }
  ],
})

export default router

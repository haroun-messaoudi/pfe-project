
import EstablishementCreationPage from '@/views/establishementCreationPage.vue'
import LoginPage from '@/views/loginPage.vue'
import RegistrationPage from '@/views/registrationPage.vue'
import { createRouter, createWebHistory } from 'vue-router'


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
  ],
})

export default router

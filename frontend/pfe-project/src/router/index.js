import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

import EstablishementOwnerDetails from '@/views/establishementOwnerDetails.vue'
import EstablishementCreationPage from '@/views/establishementCreationPage.vue'
import HomePage from '@/views/homePage.vue'
import LoginPage from '@/views/loginPage.vue'
import RegistrationPage from '@/views/registrationPage.vue'
import contactus from '@/views/contactus.vue'
import reservation from '@/views/reservation.vue'
import detailsPage from '@/views/detailsPage.vue'
import profilepage from '@/views/profilepage.vue'
import SearchResult from '@/views/searchResult.vue'
import makeReservation from '@/views/makeReservation.vue'
import OwnerPage from '@/views/ownerPage.vue'
import OuReservations from '@/views/ouReservations.vue'
import OuReviews from '@/views/ouReviews.vue'
import NotFoundPage from '@/views/notFoundPage.vue'
import HomeWrapper from '@/views/homeWrapper.vue'
import RoomsListPage from '@/views/roomsListPage.vue'
import TablesListPage from '@/views/tablesListPage.vue'

const routes = [
  {
    path: '/register',
    name: 'Registration',
    component: RegistrationPage
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/establishement-create',
    name: 'EstablishementCreate',
    component: EstablishementCreationPage
  },
  {
    path: '/',
    name: 'Home',
    component: HomeWrapper
  },
  {
    path: '/ownerPage/establishement',
    name: 'OwnerEstablishement',
    component: EstablishementOwnerDetails,
    meta: { requiresAuth: true }
  },
  {
    path: '/ownerPage/ouReservations',
    name: 'ouReservations',
    component: OuReservations,
    meta: { requiresAuth: true }
  },
  {
    path: '/ownerPage/ouReviews',
    name: 'ouReviews',
    component: OuReviews,
    meta: { requiresAuth: true }
  },
  {
    path: '/contactUs',
    name: 'contactUs',
    component: contactus
  },
  {
    path: '/profile',
    name: 'profile',
    component: profilepage,
    meta: { requiresAuth: true }
  },
  {
    path: '/myReservation',
    name: 'myReservation',
    component: reservation
  },
  {
    path: '/details/:id',
    name: 'details-page',
    component: detailsPage,
    props: true
  },
  {
    path: '/searchResult',
    name: 'searchResult',
    component: SearchResult
  },
  {
    path: '/makeReservation',
    name: 'makeReservation',
    component: makeReservation
  },
  {
    path: '/:catchAll(.*)',
    name: 'Not-Found-Page',
    component: NotFoundPage
  },
  {
    path:'/rooms/:id',
    name: 'roomsList',
    component : RoomsListPage
  },
  {
    path:'/tables/:id',
    name: 'tablesList',
    component : TablesListPage
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// Global navigation guard to protect routes requiring authentication
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)

  if (requiresAuth && !userStore.isAuthenticated) {
    // User is not authenticated, redirect to login
    return next({ name: 'Login', query: { redirect: to.fullPath } })
  }

  next()
})

export default router

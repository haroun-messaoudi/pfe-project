import './assets/main.css'
import "primeicons/primeicons.css";
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import App from './App.vue'
import router from './router'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { useUserStore } from './stores/user'
import { setupInterceptors } from './axios'
import { ConfirmationService } from 'primevue';
const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
const userStore = useUserStore()
setupInterceptors(userStore)
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
})
app.use(Toastify);
app.use(ConfirmationService)
app.mount('#app')


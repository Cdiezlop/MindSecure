import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from './components/LoginPage.vue'
import PanelPrincipal from './components/PanelPrincipal.vue'
import VerDetalles from './components/VerDetalles.vue'
import AjustesMind from './components/AjustesMind.vue'   // <--- Agregado aquí

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/panel',
    name: 'PanelPrincipal',
    component: PanelPrincipal,
    
  },
  {
    path: '/detalles/:id',
    name: 'VerDetalles',
    component: VerDetalles
  },
  {
    path: '/ajustes',
    name: 'AjustesMind',                // <--- Nueva ruta
    component: AjustesMind,
            // Opcional: proteger acceso si hay login
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


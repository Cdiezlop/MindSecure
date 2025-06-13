import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from './components/LoginPage.vue'
import PanelPrincipal from './components/PanelPrincipal.vue'
import VerDetalles from './components/VerDetalles.vue'
import AjustesDeUsuario from './components/AjustesDeUsuario.vue'

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
    component: PanelPrincipal
  },
  {
    path: '/detalles/:id',
    name: 'VerDetalles',
    component: VerDetalles
  },
  {
    path: '/ajustes',
    name: 'AjustesDeUsuario',
    component: AjustesDeUsuario
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


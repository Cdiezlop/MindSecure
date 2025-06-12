import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from './components/LoginPage.vue'
import PanelPrincipal from './components/PanelPrincipal.vue'
import VerDetalles from './components/VerDetalles.vue'
import AjustesMind from './components/AjustesMind.vue'   

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
    name: 'AjustesMind',               
    component: AjustesMind,
            
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


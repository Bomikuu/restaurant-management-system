import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/admin',
    component: () => import('@/views/dashboard/Index'),
    children: [
      {
        name: 'Dashboard',
        path: 'index',
        component: () => import('@/views/dashboard.vue')
      },
      {
        name: 'User Profile',
        path: 'pages/user',
        component: () => import('@/views/dashboard/pages/UserProfile')
      },
      {
        path: 'products',
        name: 'Products',
        component: () => import('@/views/products.vue')
      },
      {
        path: 'inventory',
        name: 'Inventory',
        component: () => import('@/views/inventory.vue')
      },
      {
        path: 'settings',
        name: 'Setting',
        component: () => import('@/views/settings.vue')
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Login.vue')
  },
  // users_management
  {
    path: '/user/management/',
    component: () => import('@/views/user_management/index.vue'),
    children: [
      // Pages
      /* {
        name: 'users_management',
        path: 'home',
        component: () => import('@/views/user_management/index.vue'),
      }*/
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

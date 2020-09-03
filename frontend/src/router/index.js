import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/dashboard',
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
      },
      {
        path: 'activities',
        name: 'Activity Log',
        component: () => import('@/views/activitylog.vue')
      },
      {
        path: 'users',
        name: 'User',
        component: () => import('@/views/allUsers.vue')
      },
      {
        path: 'roles',
        name: 'Roles',
        component: () => import('@/views/allRoles.vue')
      }
    ]
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/login.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

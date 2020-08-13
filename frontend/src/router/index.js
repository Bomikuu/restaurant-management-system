import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Login.vue"),
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
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import Login from "../components/login.vue"
import SignUp from "../components/signup.vue"
import home from "../components/home.vue"
import course from "../components/course.vue"
import test from "../components/ts.vue"

const routes: Array<RouteRecordRaw> = [
  {
    path:"/home",
    redirect:"/"
  },
  {
    path: '/',
    name: 'home',
    component: home,
    children: [
      {
        path: 'course',
        name: 'course',
        component: course
      },
      {
        path: 'ts',
        name: 'ts',
        component: test
      },
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

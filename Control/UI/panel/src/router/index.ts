import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import Login from "../components/login.vue"
import SignUp from "../components/signup.vue"
import home from "../components/home.vue"
import hmwk from "../components/hmwk.vue"
import hmwk_update from "../components/update/hmwk.vue"
import notice_update from "../components/update/notice.vue"
import res from "../components/res.vue"
import nav from "../components/nav.vue"
import notice from "../components/notice.vue"
import exam from "../components/exam.vue"
import activity from "../components/activity.vue"
import course from "../components/course.vue"
import ts from "../components/ts.vue"

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
        path: 'activity',
        name: 'activity',
        component: activity
      },
      {
        path: 'exam',
        name: 'exam',
        component: exam
      },
      {
        path: 'hmwk',
        name: 'hmwk',
        component: hmwk,
      },
      {
        path: 'notice',
        name: 'notice',
        component: notice,
      },
      {
        path: 'hmwk/update',
        name: 'hmwk_update',
        component: hmwk_update
      },
      {
        path: 'notice/update',
        name: 'notice_update',
        component: notice_update
      },
      {
        path: 'res',
        name: 'res',
        component: res
      },
      {
        path: 'nav',
        name: 'nav',
        component: nav
      },
      {
        path: '/ts',
        name: 'ts',
        component: ts
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

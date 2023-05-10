import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import DogView from '@/views/DogView.vue'

Vue.use(VueRouter)
const isLoggedIn = true


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 함')
        next({ name: 'home' })
      }
      else {
        console.log('로그인 필요함')
        next({ name: 'login' }) // 로그인이 안되어 있다면 로그인 페이지로 이동
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView  
  },
  {
    path: '*', // aesterisk, 순서대로 내려가면서 찾기에 마지막에 나두는 것이 바람직하다.
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router/index.js
// 약간 재귀적으로 작동하는 것으로 생각하면 된다.
// router.beforeEach((to, from, next) => {
//   // 로그인 여부  
//   // const isLoggedIn = true // 로그인 됨
//   const isLoggedIn = false // 로그인 안됨

//   // 로그인이 필요한 페이지 지정  
//   // const authPages = ['hello', 'about', 'home']
//   // 로그인을 하지 않아도 되는 페이지 지정  
//   const allAuthPages = ['login']

  
//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     console.log('Login으로 이동')
//     next({ name: 'login' })
//   } 
//   else {
//     console.log('to로 이동!')
//     next()
//   }
// })


export default router

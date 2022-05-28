import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import MainView from '../views/MainView.vue'
import RecommendView from '../views/RecommendView.vue'
import CommunityView from '../views/CommunityView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ArticleEditView from '../views/ArticleEditView.vue'
import ArticleNewView from '../views/ArticleNewView.vue'
import ProfileView from '../views/ProfileView.vue'
import ProfileImgChange from '../views/ProfileImgChange.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SignUpView from '../views/SignUpView.vue'
import NotFound404 from '../views/NotFound404.vue'

// 임시 영화 상세 페이지 라우터
import MovieDetailView from '../views/MovieDetailView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainpage',
    component: MainView
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/community/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/community/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/upload_img/:username',
    name: 'profileImg',
    component: ProfileImgChange
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/moviedetail/:movie_id',
    name: 'moviedetail',
    component: MovieDetailView,
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
// router.beforeEach((to, from, next) => {
//   // 이전 페이지에서 발생한 에러메시지 삭제
//   store.commit('SET_AUTH_ERROR', null)

//   const { isLoggedIn } = store.getters

//   const noAuthPages = ['login', 'signup', 'community', 'mainpage','recommend','profile','moviedetail','movieactors','similarmovies']

//   const isAuthRequired = !noAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     alert('Require Login. Redirecting..')
//     next({ name: 'login' })
//   } else {
//     next()
//   }

//   if (!isAuthRequired && isLoggedIn) {
//     next({ name: 'articles' })
//   }
// })

export default router

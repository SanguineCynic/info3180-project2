import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomePage from '../views/HomeView.vue';
import RegistrationFormView from '@/views/RegistrationFormView.vue';
import ExploreView from '../views/ExploreView.vue';
// import LoginView from '../views/LoginView.vue';
// import LogoutView from '../views/LogoutView.vue';
// import UserProfileView from '../views/UserProfileView.vue';
// import NewPostView from '../views/NewPostView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: RegistrationFormView
    },
    // {
    //     path: '/login',
    //     name: 'login',
    //     component: LoginView
    // },
    // {
    //     path: '/logout',
    //     name: 'logout',
    //     component: LogoutView
    // },
    {
      path: '/explore',
      name: 'explore',
      component: ExploreView
    },
    // {
    //     path: '/users/:userId',
    //     name: 'userProfile',
    //     component: UserProfileView
    // },
    // {
    //     path: '/posts/new',
    //     name: 'newPost',
    //     component: NewPostView
    // }
  ]
})

export default router

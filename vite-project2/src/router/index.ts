import {createRouter, createWebHistory} from 'vue-router'
import {HomePage} from '../views/Home.vue';

export const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
        // component: () => import('@views/Home.vue')
    },
    {
        path: '/register',
        name: 'register',
        component: () => import('@/views/Register.vue')
    },
    // {
    //     path: '/login',
    //     name: 'login',
    //     component: () => import('@/views/Login.vue')
    // },
    // {
    //     path: '/logout',
    //     name: 'logout',
    //     component: () => import('@/views/Logout.vue')
    // },
    // {
    //     path: '/explore',
    //     name: 'explore',
    //     component: () => import('@/views/Explore.vue')
    // },
    // {
    //     path: '/users/:userId',
    //     name: 'userProfile',
    //     component: () => import('@/views/UserProfile.vue')
    // },
    // {
    //     path: '/posts/new',
    //     name: 'newPost',
    //     component: () => import('@/views/NewPost.vue')
    // },
    // {
    //     path: '/submit',
    //     name: 'submitCode',
    //     component: () => import('@/views/SubmitCode.vue')
    // }
];

export const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});




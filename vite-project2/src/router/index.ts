import {createRouter, createWebHistory} from 'vue-router'
import {HomePage} from '../views/Home.vue';
import {Register} from '../views/Register.vue';
import {Explore} from '../views/Explore.vue';
// import {Login} from '../views/Explore.vue';
// import {Logout} from '../views/Explore.vue';
// import {UserProfile} from '../views/Explore.vue';
// import {NewPost} from '../views/Explore.vue';




export const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    // {
    //     path: '/login',
    //     name: 'login',
    //     component: Login
    // },
    // {
    //     path: '/logout',
    //     name: 'logout',
    //     component: Logout
    // },
    {
        path: '/explore',
        name: 'explore',
        component: Explore
    },
    // {
    //     path: '/users/:userId',
    //     name: 'userProfile',
    //     component: UserProfile
    // },
    // {
    //     path: '/posts/new',
    //     name: 'newPost',
    //     component: NewPost
    // }
];

export const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});




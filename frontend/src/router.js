import Vue from 'vue';

import Router from 'vue-router';

import token from './common/token';
import auth from './storage/modules/auth';


Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Index.vue'),
    },
    {
      path: '/pricing',
      name: 'pricing',
      component: () => import('./views/Pricing.vue'),
    },
    {
      path: '/projects',
      name: 'projects',
      meta: { requiresAuth: true },
      component: () => import('./views/Projects.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('./views/Register.vue'),
    },
    {
      path: '/activate/:uid/:token',
      name: 'activate',
      props: true,
      component: () => import('./views/Activate.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue'),
    },
    {
      path: '/project/create',
      name: 'createProject',
      component: () => import('./views/CreateProject.vue'),
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const accessToken = token.get(token.accessTokenKey);
    const refreshToken = token.get(token.refreshTokenKey);
    if (accessToken === null) {
      next('/register');
    } else {
      Vue.axios
        .post('auth/jwt/verify/', { token: accessToken })
        .then(() => next())
        .catch(() => {
          Vue.axios
            .post('auth/jwt/verify/', { token: refreshToken })
            .then(() => {
              Vue.axios
                .post('auth/jwt/refresh/', { refresh: refreshToken })
                .then((data) => {
                  auth.mutations.setUserAuthentication(data);
                  next();
                })
                .catch(() => next('/register'));
            })
            .catch(() => next('/login'));
        });
    }
  } else {
    next();
  }
});

export default router;

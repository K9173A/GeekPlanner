import Vue from 'vue';

import Router from 'vue-router';

import token from './common/token';
import store from './storage/index';


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
    {
      path: '/project/:id/',
      name: 'project',
      props: true,
      component: () => import('./views/Project.vue'),
    },
    {
      path: '*',
      redirect: '/',
    },
  ],
});

router.beforeEach((to, from, next) => {
  store.commit('clear');
  if (to.meta.requiresAuth) {
    const accessToken = token.get(token.accessTokenKey);
    const refreshToken = token.get(token.refreshTokenKey);
    if (accessToken === null) {
      next({ name: 'register' });
    } else {
      Vue.axios
        .post('auth/jwt/verify/', { token: accessToken })
        .then(() => {
          store.commit('setAuthenticated', true);
          next();
        })
        .catch(() => {
          Vue.axios
            .post('auth/jwt/verify/', { token: refreshToken })
            .then(() => {
              Vue.axios
                .post('auth/jwt/refresh/', { refresh: refreshToken })
                .then((data) => {
                  store.commit('setAuthenticationTokens', data);
                  store.commit('setAuthenticated', true);
                  next();
                })
                .catch(() => {
                  next({ name: 'register' });
                });
            })
            .catch(() => {
              next({ name: 'login' });
            });
        });
    }
  } else {
    next();
  }
});

export default router;

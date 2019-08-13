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
      name: 'create_project',
      component: () => import('./views/CreateProject.vue'),
    },
  ],
});

// Redirects user if he tries to access URLs which requires login and token
router.beforeEach((to, from, next) => {
  // Does the next URL require authentication
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Does user have access token?
    if (token.get(token.accessTokenKey) === null) {
      // Redirects user to the login form to acquire new token
      next('/login');
    } else {
      // Does user have a valid access token?
      Vue.axios.post('auth/jwt/verify/', token.accessTokenKey)
        // User has a valid access token
        .then(() => next())
        // User has expired access token
        .catch(() => {
          // Does user have a valid refresh token?
          Vue.axios.post('auth/jwt/verify/', token.refreshTokenKey)
            // User has a valid refresh token, use it to renew access token
            .then(() => {
              Vue.axios.post('auth/jwt/refresh/', token.refreshTokenKey)
                // Saves renewed tokens
                .then((data) => {
                  token.save(token.accessTokenKey, data.access);
                  token.save(token.refreshTokenKey, data.refresh);
                  auth.state.isAuthenticated = true;
                  next();
                })
                // Can't refresh tokens, redirects to the registration form
                .catch(() => next('/register'));
            })
            // User has expired refresh token
            .catch(() => next('/login'));
        });
    }
  } else {
    next();
  }
});

export default router;

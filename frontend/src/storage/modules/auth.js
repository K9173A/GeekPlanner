import Vue from 'vue';

import token from '@/common/token';


const actions = {
  /**
   * Registers user by sending his credentials to the Django REST backend.
   * @param context - context object.
   * @param userCredentials - user credentials (username, email, password and etc.).
   */
  register(context, userCredentials) {
    Vue.axios.post('auth/users/', userCredentials)
      .then(() => this.$router.push({ name: 'home' }))
      .catch(error => context.commit('setError', error));
  },
  /**
   * Sends POST request to the backend to complete user account activation.
   * @param context - context object.
   * @param userCredentials - user credentials.
   */
  activate(context, userCredentials) {
    Vue.axios.post('auth/users/activation/', userCredentials)
      .catch(error => context.commit('setError', error));
  },
  /**
   * Logs use in by sending his credentials to the Django REST backend.
   * @param context - context object.
   * @param userCredentials - user credentials (username and password).
   */
  login(context, userCredentials) {
    Vue.axios.post('auth/jwt/create/', userCredentials)
      .then((response) => {
        context.commit('setUserAuthentication', response);
        this.$router.push({ name: 'home' });
      })
      .catch(error => context.commit('setError', error));
  },
  /**
   * Logs user out by clearing his auth token.
   * @param context - context object.
   */
  logout(context) {
    context.commit('unsetUserAuthentication');
  },
};

const mutations = {
  /**
   * Sets user authentication data including a token.
   * @param state - Vuex state object.
   * @param data - response data which contains refresh and access tokens.
   */
  setUserAuthentication(state, data) {
    state.isAuthenticated = true;
    state.errorHandler.clear();
    token.save(token.accessTokenKey, data.access);
    token.save(token.refreshTokenKey, data.refresh);
  },
  /**
   * Clears user authentication data.
   * @param state - Vuex state object.
   */
  unsetUserAuthentication(state) {
    state.isAuthenticated = false;
    state.errorHandler.clear();
    token.delete(token.accessTokenKey);
  },
};

const state = {
  isAuthenticated: false,
};

const getters = {};

export default {
  actions,
  mutations,
  state,
  getters,
};

import token from '@/common/token';
import api from '@/common/api';

const actions = {
  /**
   * Registers user by sending his credentials to the Django REST backend.
   * @param context - context object.
   * @param credentials - user credentials (username, email, password and etc.).
   * @returns Promise object.
   */
  register(context, credentials) {
    return new Promise((resolve, reject) => {
      api.register(credentials)
        .then((response) => {
          resolve(response);
        })
        .catch((error) => {
          context.commit('setError', error);
          reject(error);
        });
    });
  },
  /**
   * Logs use in by sending his credentials to the Django REST backend.
   * @param context - context object.
   * @param credentials - user credentials (username and password).
   * @returns Promise object.
   */
  login(context, credentials) {
    return new Promise((resolve, reject) => {
      api.login(credentials)
        .then((response) => {
          context.commit('setUserAuthentication', response);
          resolve(response);
        })
        .catch((error) => {
          context.commit('setError', error);
          reject(error);
        });
    });
  },
  /**
   * Sends POST request to the backend to complete user account activation.
   * @param context - context object.
   * @param credentials - user credentials.
   * @returns Promise object.
   */
  activate(context, credentials) {
    return new Promise((resolve, reject) => {
      api.activate(credentials)
        .then((response) => {
          resolve(response);
        })
        .catch((error) => {
          context.commit('setError', error);
          reject(error);
        });
    });
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
   * Sets new error.
   * @param state - Vuex state object.
   * @param error - response object.
   */
  setError(state, error) {
    Object.entries(error.response.data).forEach((fieldName, messages) => {
      for (let i = 0; i < messages.length; i += 1) {
        state.errors.push(`${fieldName}: ${messages[i]}`);
      }
    });
  },
  /**
   * Sets user authentication data including a token.
   * @param state - Vuex state object.
   * @param data - response data which contains refresh and access tokens.
   */
  setUserAuthentication(state, data) {
    state.isAuthenticated = true;
    state.errors = [];
    token.save(token.accessTokenKey, data.access);
    token.save(token.refreshTokenKey, data.refresh);
  },
  /**
   * Clears user authentication data.
   * @param state - Vuex state object.
   */
  unsetUserAuthentication(state) {
    state.isAuthenticated = false;
    state.errors = [];
    token.delete(token.accessTokenKey);
  },
};

const state = {
  isAuthenticated: !!token.get(token.accessTokenKey),
  errors: [],
};

const getters = {};

export default {
  actions,
  mutations,
  state,
  getters,
};

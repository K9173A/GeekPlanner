import token from '@/common/token';

const actions = {
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
   * @param response - response object.
   */
  setUserAuthentication(state, response) {
    state.isAuthenticated = true;
    token.save(token.accessTokenKey, response.data.access);
    token.save(token.refreshTokenKey, response.data.refresh);
  },
  /**
   * Clears user authentication data.
   * @param state - Vuex state object.
   */
  unsetUserAuthentication(state) {
    state.isAuthenticated = false;
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

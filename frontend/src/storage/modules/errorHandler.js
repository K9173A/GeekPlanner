const actions = {};

const mutations = {
  /**
   * Sets new error.
   * @param state - Vuex state object.
   * @param error - response object.
   */
  setError(state, error) {
    state.errors = [];
    if (error.response) {
      Object.entries(error.response.data).forEach((data) => {
        const [title, messages] = data;
        if (messages instanceof Array) {
          for (let i = 0; i < messages.length; i += 1) {
            state.errors.push(`${title}: ${messages[i]}`);
          }
        } else {
          state.errors.push(`${title}: ${messages}`);
        }
      });
    } else if (error.request) {
      state.errors.push(error.message);
    } else {
      state.errors.push(error.message);
    }
  },

  clear(state) {
    state.errors = [];
  },
};

const state = {
  errors: [],
};

const getters = {};

export default {
  actions,
  mutations,
  state,
  getters,
};

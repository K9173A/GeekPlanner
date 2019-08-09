import token from '@/common/token';
import api from '@/common/api';

const actions = {
  fetchProjects(context, limit=3) {
    return new Promise((resolve, reject) => {
      api.fetchProjects(limit)
        .then(data => {
          context.commit('setProjects', data.projects);
          resolve(data);
        })
        .catch(response => {
          context.commit('setError', response.data.errors);
          reject(response);
        });
    });
  }
};

const mutations = {
  setProjects(state, projects) {
    state.projects = projects
  }
};

const state = {
  projects: {},
  errors: null,
};

const getters = {

};

export default {
  actions,
  mutations,
  state,
  getters,
};

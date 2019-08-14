import Vue from 'vue';

import parsePaginationURL from '@/common/utils';
import token from '@/common/token';


const actions = {
  /**
   * Gets a certain amount of projects defined by pagination classes in the
   * Django REST backend (plannerapp.pagination) and shows them as a list with
   * paginator data.
   * @param context - Vuex context object.
   * @param paginatorData - data needed for ProjectLimitOffPagination (limit & offset).
   */
  fetchProjects(context, paginatorData) {
    Vue.axios
      .get('projects', token.addAuthHeader(paginatorData))
      .then(response => context.commit('setProjects', response.projects))
      .catch(error => context.commit('setError', error));
  },
  /**
   * Creates a new project with data specified by user in the form.
   * @param context - Vuex context object.
   * @param projectData - project data specified by user.
   */
  createProject(context, projectData) {
    Vue.axios
      .post('create_project/', token.addAuthHeader(projectData))
      .then(() => this.$router.push({ name: 'projects' }))
      .catch(error => context.commit('setError', error));
  },
  /**
   * Deletes selected project. Shows modal window (bootbox) for user confirmation.
   * @param context - Vuex context object.
   * @param projectId - selected project Id.
   */
  deleteProject(context, projectId) {
    Vue.axios
      .delete('delete_project/', token.addAuthHeader(projectId))
      .then(response => context.commit('setProjects', response.projects))
      .catch(error => context.commit('setError', error));
  },

  // deleteCard(projectId, cardId) {
  //   Vue.axios.delete('delete_card/',
  //     this.addAuthHeader({'project_pk': projectId, 'card_pk': cardId})
  //   ).catch(error => context.commit('setError', error));
  // },
};

const mutations = {
  setProjects(state, projects) {
    state.projects = projects;
  },
  setPreviousPage(state, pageURL) {
    state.previousPage = parsePaginationURL(pageURL);
  },
  setNextPage(state, pageURL) {
    state.nextPage = parsePaginationURL(pageURL);
  },
};

const state = {
  nextPage: { limit: null, offset: null },
  previousPage: { limit: null, offset: null },
  projects: [],
};

const getters = {
  projectsCount() {
    return state.projects.length;
  },
};

export default {
  actions,
  mutations,
  state,
  getters,
};

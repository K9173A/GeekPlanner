import Vue from 'vue';

import urlParser from '@/common/urlParser';
import token from '@/common/token';

const state = {
  pagination: {
    prevPageNumber: null,
    nextPageNumber: null,
    currPageNumber: 1,
    count: 0,
  },
  project: {
    information: null,
    categories: null,
    cards: null,
  },
  projects: [],
};

const actions = {
  /**
   * Gets a certain amount of projects defined by pagination classes in the
   * Django REST backend (plannerapp.pagination) and shows them as a list with
   * paginator data.
   * @param context - Vuex context object.
   * @param pageNumber - page number where user will be redirected to.
   */
  fetchProjects(context, pageNumber = 1) {
    // console.log(pageNumber);
    Vue.axios
      .get(`planner/projects?page=${pageNumber}`, token.getAuthHeaders())
      .then((response) => {
        const previousPageURL = response.data.previous;
        const nextPageURL = response.data.next;
        let currentPageNumber = 0;

        if (previousPageURL) {
          const p = parseInt(urlParser.parsePageNumberPagination(previousPageURL), 10);
          context.commit('setPageNumber', { pagePosition: 'previous', pageNumber: p });
        }

        if (nextPageURL) {
          const p = parseInt(urlParser.parsePageNumberPagination(nextPageURL), 10);
          context.commit('setPageNumber', { pagePosition: 'next', pageNumber: p });
        }

        if (state.pagination.prevPageNumber && state.pagination.nextPageNumber) {
          currentPageNumber = Math.trunc((response.data.next + response.data.previous) / 2);
        } else if (state.pagination.prevPageNumber && !state.pagination.nextPageNumber) {
          currentPageNumber = state.pagination.prevPageNumber + 1;
        } else if (!state.pagination.prevPageNumber && state.pagination.nextPageNumber) {
          currentPageNumber = 1;
        } else {
          currentPageNumber = -1;
        }

        context.commit(
          'setPageNumber', { pagePosition: 'current', pageNumber: currentPageNumber },
        );
        context.commit('setProjects', response.data.results);
        context.commit('setCount', response.data.count);
        context.commit('setTotalPages', response.data.total_pages);
      })
      .catch(error => context.commit('setError', error));
  },
  /**
   * Deletes selected project. Shows modal window (bootbox) for user confirmation.
   * @param context - Vuex context object.
   * @param id - selected project Id.
   */
  deleteProject(context, id) {
    Vue.axios
      .delete(`planner/delete_project/${id}`, token.getAuthHeaders())
      .then(response => context.commit('setProjects', response.projects))
      .catch(error => context.commit('setError', error));
  },

  loadProject(context, id) {
    Vue.axios
      .get(`planner/project_details/${id}`, token.getAuthHeaders())
      .then(response => context.commit('setProjectData', response.data))
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
  setPageNumber(state, { pagePosition, pageNumber }) {
    switch (pagePosition) {
      case 'previous':
        state.pagination.prevPageNumber = pageNumber;
        break;
      case 'current':
        state.pagination.currPageNumber = pageNumber;
        break;
      case 'next':
        state.pagination.nextPageNumber = pageNumber;
        break;
      default:
        throw Error(`Undefined pagePosition value: ${pagePosition}`);
    }
  },
  setCount(state, count) {
    state.pagination.count = count;
  },
  setTotalPages(state, totalPages) {
    state.pagination.totalPages = totalPages;
  },
  setProject(state, project) {
    state.pagination.project = project;
  },
  setProjectData(state, projectData) {
    state.project = projectData;
  },
};

const getters = {};

export default {
  actions,
  mutations,
  state,
  getters,
};

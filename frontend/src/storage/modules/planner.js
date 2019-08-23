import Vue from 'vue';
import token from '@/common/token';

const data = {
  pagination: {
    prevPageNumber: null,
    nextPageNumber: null,
    currPageNumber: 1,
    totalPages: 0,
    count: 0,
  },
  currentSelection: {
    project: {
      information: {
        title: '',
        description: '',
        thumbnail: null,
        isPublic: null,
      },
      categories: null,
      cards: null,
    },
    category: null,
    card: {
      title: '',
      description: '',
      priority: 2,
    },
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
  fetchProjects({ commit }, pageNumber) {
    Vue.axios
      .get(`planner/projects?page=${pageNumber}`, token.getAuthHeaders())
      .then((response) => {
        commit('setPageNumber', { pagePosition: 'previous', pageNumber: response.data.prev });
        commit('setPageNumber', { pagePosition: 'current', pageNumber: response.data.curr });
        commit('setPageNumber', { pagePosition: 'next', pageNumber: response.data.next });
        commit('setProjects', response.data.results);
        commit('setCount', response.data.count);
        commit('setTotalPages', response.data.total_pages);
      })
      .catch(error => commit('setError', error));
  },
  /**
   * Deletes project (sets it as inactive).
   * @param context - Vuex context object.
   * @param project - project to be deleted.
   */
  deleteProject({ commit, state, dispatch }, project) {
    Vue.axios
      .delete(`planner/delete_project/${project.id}/`, token.getAuthHeaders())
      .then(() => dispatch('fetchProjects', state.pagination.currPageNumber))
      .catch(error => commit('setError', error));
  },

  updateCard({ commit }, id) {
    Vue.axios
      .patch(`planner/update_card/${id}/`, token.getAuthHeaders())
      .catch(error => commit('setError', error));
  },
  /**
   * Show confirmation window. if user confirms, deletes card on the server-side
   * and then deletes from Vue.
   * @param context - Vuex context object.
   * @param id - card id.
   */
  // deleteCard({ commit }, id) {
  //   bootbox.confirm({
  //     message: `Do you really want to delete card #${id}?`,
  //     buttons: {
  //       confirm: {
  //         label: 'Confirm',
  //         className: 'btn-danger',
  //       },
  //       cancel: {
  //         label: 'Cancel',
  //         className: 'btn-success',
  //       },
  //     },
  //     callback: (deleteConfirmed) => {
  //       if (deleteConfirmed) {
  //         Vue.axios
  //           .delete(`planner/delete_card/${id}`, token.getAuthHeaders())
  //           .then(() => commit('deleteCard', id))
  //           .catch(error => commit('setError', error));
  //       }
  //     },
  //   });
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
    state.currentSelection.project = projectData;
  },
  setProjectInformation(state, information) {
    state.currentSelection.project.information = information;
  },
  deleteCard(state, id) {
    Object.entries(state.currentSelection.project.cards).forEach((category, cards) => {
      if (cards.find(card => card.id !== id)) {
        state.currentSelection.project.cards.category =
          cards.filter(card => card.id !== id);
      }
    });
  },
};

const getters = {};

export default {
  actions,
  mutations,
  state: data,
  getters,
};

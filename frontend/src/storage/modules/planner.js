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
      categories: [],
      cards: {},
    },
    category: null,
    card: {
      title: '',
      description: '',
      priority: 2,
    },
  },
  objectTypeToDelete: null,
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
      .delete(`planner/delete_project/${project.information.id}/`, token.getAuthHeaders())
      .then(() => dispatch('fetchProjects', state.pagination.currPageNumber))
      .catch(error => commit('setError', error));
  },
  /**
   * Fetches cards for the specific category.
   * @param commit - function to call mutations.
   * @param state - state object.
   * @param category - Category object.
   */
  fetchCards({ commit, state }, category) {
    return Vue.axios
      .get(`planner/cards/project/${state.currentSelection.project.information.id}` +
        `/category/${category.id}/`, token.getAuthHeaders())
      .then((response) => {
        commit('setProjectCategoryCards', { category, cards: response.data });
        return true;
      })
      .catch((error) => {
        commit('setError', error);
        return false;
      });
  },
  /**
   * Show confirmation window. if user confirms, deletes card on the server-side
   * and then deletes from Vue.
   * @param commit - function to call mutations.
   * @param dispatch - function to call actions.
   * @param card - Card object to be deleted.
   * @param category - Category object which is used to fetch its cards again.
   */
  deleteCard({ commit, dispatch, state }, card) {
    // TODO:
    const category = state.currentSelection.project.categories.find(element => {
      return element.id === state.currentSelection.category;
    });
    Vue.axios
      .delete(`planner/delete_card/${card.id}/`, token.getAuthHeaders())
      .then(() => dispatch('fetchCards', category))
      .catch(error => commit('setError', error));
  },
};

const mutations = {
  setCount(state, count) {
    state.pagination.count = count;
  },
  setTotalPages(state, totalPages) {
    state.pagination.totalPages = totalPages;
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
  setProjects(state, projects) {
    state.projects = projects;
  },
  setCurrentCategory(state, category) {
    state.currentSelection.category = category;
  },
  setCurrentCard(state, card) {
    state.currentSelection.card = card;
  },
  setProjectInformation(state, information) {
    state.currentSelection.project.information = information;
  },
  setProjectCategories(state, categories) {
    state.currentSelection.project.categories = categories;
  },
  setProjectCategoryCards(state, { category, cards }) {
    if (cards) {
      state.currentSelection.project.cards[category.name] = cards;
    }
  },
  setDeleteObjectType(state, objectType) {
    state.objectTypeToDelete = objectType;
  }
};

const getters = {};

export default {
  actions,
  mutations,
  state: data,
  getters,
};

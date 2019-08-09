import Vue from 'vue';
import Vuex from 'vuex';

import auth from '@/storage/modules/auth';
// import projects from '@/storage/modules/projects';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    // projects,
  },
});

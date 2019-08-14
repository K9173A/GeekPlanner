import Vue from 'vue';
import Vuex from 'vuex';

import auth from '@/storage/modules/auth';
import errorHandler from '@/storage/modules/errorHandler';
import planner from '@/storage/modules/planner';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    errorHandler,
    planner,
  },
});

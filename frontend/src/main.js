import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';
import BootstrapVue from 'bootstrap-vue';
import VueFormGenerator from 'vue-form-generator';
import VModal from 'vue-js-modal';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@/assets/css/main/style.css';

import App from './App.vue';
import router from './router';
import store from './storage/index';


Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.use(VModal, { dialog: true });
Vue.use(VueFormGenerator, {
  validators: {
    passwordComparisonValidator: (value, field, model) => {
      if (model.password === value) {
        return [];
      }
      return ['Repeated password does not match!'];
    },
  },
});

Vue.axios.defaults.baseURL = 'http://127.0.0.1:8000/api';
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');

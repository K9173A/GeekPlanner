import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import App from './App.vue';
import router from './router';
import store from './storage/index';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@/assets/css/main/style.css';
import api from '@/common/api';

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

api.initialize();

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');

import Vue from 'vue';
import VueAxios from 'vue-axios';
import axios from 'axios';
import token from './token';

export default {
  /**
   * Initializes axios.
   */
  initialize() {
    Vue.use(VueAxios, axios);
    Vue.axios.defaults.baseURL = 'http://127.0.0.1:8000/api';
  },

  addAuthHeader(data) {
    let newData = data;
    const accessToken = token.get(token.accessTokenKey);
    newData.headers.Authorization = `Bearer ${accessToken}`;
    return newData;
  },

  register: credentials => Vue.axios.post('auth/users/', credentials),

  activate: credentials => Vue.axios.post('auth/users/activation/', credentials),

  login: credentials => Vue.axios.post('auth/jwt/create/', credentials),

  verifyToken: accessToken => Vue.axios.post('auth/jwt/verify/', accessToken),

  renewToken: refreshToken => Vue.axios.post('auth/jwt/refresh/', refreshToken),

  fetchProjects: limit => Vue.axios.get('projects', this.addAuthHeader(limit)),
};

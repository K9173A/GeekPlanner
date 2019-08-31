<template>
<div class="container">
  <div class="row justify-content-center">
    <div class="col-6">
      <ErrorStack/>
      <div class="card my-4 gp-form">
        <div class="card-header text-center text-uppercase font-weigt-bold">
          {{ title }}
        </div>
        <div class="card-body">
          <form v-on:submit.prevent="submit" id="login-form">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
          </form>
          <div class="d-flex justify-content-around px-4 py-4">
            <button @click="$router.go(-1)" class="btn btn-primary col-5">
              Back
            </button>
            <input class="btn btn-primary col-5" type="submit"
                   form="login-form" value="Submit">
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'LoginForm',

  components: { ErrorStack },

  data() {
    return {
      title: 'Sign Up',
      model: {
        username: '',
        password: '',
      },
      schema: {
        groups: [
          {
            fields: [
              {
                type: 'input',
                inputType: 'text',
                label: 'Login',
                model: 'username',
                placeholder: 'John',
                required: true,
              },
              {
                type: 'input',
                inputType: 'password',
                label: 'Password',
                model: 'password',
                min: 8,
                hint: 'Min 8 characters',
                required: true,
              },
            ],
          },
        ],
      },
      formOptions: {
        validateAfterLoad: true,
        validateAfterChanged: true,
        validateAsync: true,
      },
    };
  },

  methods: {
    ...mapMutations(['setAuthenticationTokens', 'setAuthenticated', 'setError']),
    submit() {
      this.axios
        .post('auth/jwt/create/', {
          username: this.model.username,
          password: this.model.password,
        })
        .then((response) => {
          this.setAuthenticationTokens(response);
          this.setAuthenticated(true);
          this.$router.push({ name: 'home' });
        })
        .catch(error => this.setError(error));
    },
  },
};
</script>

<style scoped>

</style>

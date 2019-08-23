<template>
<form v-on:submit.prevent="submit" method="post">
  <vue-form-generator :schema="schema" :model="model" :options="formOptions">
  </vue-form-generator>
  <input class="btn btn-primary col-12" type="submit" value="Submit">
</form>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  name: 'LoginForm',

  data() {
    return {
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

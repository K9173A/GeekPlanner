<template>
<div class="container">
  <div class="row justify-content-center">
    <div class="col-6">
      <ErrorStack/>
      <div class="card my-4 gp-form">
        <div class="card-header text-center text-uppercase font-weigt-bold">
          Sign In
        </div>
        <div class="card-body">
          <form v-on:submit.prevent="submit" method="post">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
            <input class="btn btn-primary col-12" type="submit" value="Submit">
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'Login',

  components: { ErrorStack },

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
    ...mapActions(['login']),
    ...mapMutations(['setUserAuthentication', 'setError']),
    // Logs use in by sending his credentials to the Django REST backend.
    submit() {
      this.axios
        .post('auth/jwt/create/', {
          username: this.model.username,
          password: this.model.password,
        })
        .then((response) => {
          this.setUserAuthentication(response);
          this.$router.push({ name: 'home' });
        })
        .catch(error => this.setError(error));
    },
  },
};
</script>

<style scoped>

</style>

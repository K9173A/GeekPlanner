<template>
<div class="container">
  <div class="row justify-content-md-center">
    <ErrorStack v-if="errors" />
    <div class="card gp-form my-4">
      <div class="card-header text-center text-uppercase font-weigt-bold">
        Registration
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
</template>

<script>
import { mapState, mapActions } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'Register',

  components: { ErrorStack },

  data() {
    return {
      model: {
        username: '',
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        password2: '',
      },
      schema: {
        groups: [
          {
            fields: [
              {
                type: 'input',
                inputType: 'text',
                label: 'Username',
                model: 'username',
                placeholder: 'John123',
                required: true,
                min: 3,
                hint: 'Min 3 characters',
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'First name',
                model: 'firstName',
                placeholder: 'John',
                required: true,
                min: 2,
                hint: 'Min 2 characters',
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'Last name',
                model: 'lastName',
                placeholder: 'Doe',
                required: true,
                min: 2,
                hint: 'Min 2 characters',
              },
              {
                type: 'input',
                inputType: 'email',
                label: 'E-mail',
                model: 'email',
                placeholder: 'johndoe@mail.com',
                required: true,
              },
              {
                type: 'input',
                inputType: 'password',
                label: 'Password',
                model: 'password',
                required: true,
                min: 8,
                hint: 'Min 8 characters',
              },
              {
                type: 'input',
                inputType: 'password',
                label: 'Repeat Password',
                model: 'password2',
                required: true,
                validator: 'passwordComparisonValidator',
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

  computed: {
    ...mapState({ errors: state => state.auth.errors }),
  },

  methods: {
    ...mapActions(['register']),
    submit() {
      this.register({
        username: this.username,
        firstName: this.firstName,
        lastName: this.lastName,
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>

<style scoped>

</style>

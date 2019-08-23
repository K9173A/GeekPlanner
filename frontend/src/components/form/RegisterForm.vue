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
  name: 'RegisterForm',

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

  methods: {
    ...mapMutations(['setError']),
    submit() {
      this.axios
        .post('auth/users/', {
          username: this.username,
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          password: this.password,
        })
        .then(() => this.$router.push({ name: 'home' }))
        .catch(error => this.setError(error));
    },
  },
};
</script>

<style scoped>

</style>

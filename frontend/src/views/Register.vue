<template>
<div class="container">
  <div class="row justify-content-md-center">
    <div class="card my-4 gp-form">
      <div class="card-header text-center text-uppercase font-weight-bold">
        Sign up
      </div>
      <div class="card-body">
        <form v-on:submit.prevent="submit" method="post">
          <div class="form-group">
            <label class="control-label small">
              Username
            </label>
            <input v-model="username" type="text"
                   class="form-control" placeholder="Username" required>
          </div>
          <div class="form-group">
            <label class="control-label small">
              First name
            </label>
            <input v-model="firstName" type="text"
                   class="form-control" placeholder="First name" required>
          </div>
          <div class="form-group">
            <label class="control-label small">
              Last name
            </label>
            <input v-model="lastName" type="text"
                   class="form-control" placeholder="Last name" required>
          </div>
          <div class="form-group">
            <label class="control-label small">
              Email
            </label>
            <input v-model="email" type="text"
                   class="form-control" placeholder="Email" required>
          </div>
          <div class="form-group">
            <label class="control-label small">
              Password
            </label>
            <input v-model="password" type="password"
                   class="form-control" placeholder="Password" required>
          </div>
          <div class="form-group">
            <label class="control-label small">
              Repeat password
            </label>
            <input v-model="password2" type="password"
                   class="form-control" placeholder="Password" required>
          </div>
          <div v-if="errors" class="mt-2">
            <div v-for="error in errors" class="gp-form__error">
              {{ error }}
            </div>
          </div>
          <input class="btn btn-primary col-12" type="submit" value="Submit">
        </form>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Register',

  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      password2: '',
    };
  },

  computed: {
    ...mapState({
      errors: state => state.auth.errors,
    }),
  },

  methods: {
    /*
    validateForm() {
      if (!/[a-zA-Z0-9]{3,}/i.test(this.username)) {
        this.setError('username', 'Username should contain at least 3 characters.');
        return false;
      }
      if (!/\S+@\S+\.\S+/i.test(this.email)) {
        this.setError('email', 'Incorrect email address.');
        return false;
      }
      if (this.password !== this.password2) {
        this.setError('password2', 'Passwords should be the same.');
        return false;
      }
      return true;
    },
    */
    submit() {
      this.$store
        .dispatch('register', {
          username: this.username,
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          password: this.password,
          password2: this.password2,
        })
        .then(
          () => this.$router.push({ name: 'home' }),
        );
    },
  },
};
</script>

<style scoped>

</style>

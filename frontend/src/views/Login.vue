<template>
<div class="container">
  <div class="row justify-content-md-center">
    <div class="card my-4 gp-form">
      <div class="card-header text-center text-uppercase font-weight-bold">
        Sign In
      </div>
      <div class="card-body">
        <form v-on:submit.prevent="submit" method="post">
          <div class="form-group">
            <label class="control-label small">
              Username
            </label>
            <input v-model="username" type="text"
                   class="form-control"  placeholder="Username" required>
          </div>
          <div class="form-group">
            <label class="control-label small">
              Password
            </label>
            <input v-model="password" type="password"
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
  name: 'Login',

  data() {
    return {
      username: '',
      password: '',
    };
  },

  computed: {
    ...mapState({
      errors: state => state.auth.errors,
    }),
  },

  methods: {
    submit() {
      this.$store
        .dispatch('login', {
          username: this.username,
          password: this.password,
        })
        .then(() => this.$router.push({ name: 'home' }))
        .catch(() => this.$router.push({ name: 'login' }));
    },
  },
};
</script>

<style scoped>

</style>

<template>
<div class="container justify-content-center">
  <div class="my-4 jumbotron">
    <h1 class="text-uppercase">
      Activation success
    </h1>
    <p class="lead">
      Now you can create your first project by going to the "Projects" section.
    </p>
    <hr class="my-4">
    <p class="lead">
      <router-link :to="{ name: 'home' }" class="btn btn-primary">
        OK
      </router-link>
    </p>
  </div>
</div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex';

export default {
  name: 'Activate',

  props: ['uid', 'token'],

  mounted() {
    // Sends POST request to the backend to complete user account activation.
    this.axios
      .post('auth/users/activation/', {
        uid: this.$props.uid,
        token: this.$props.token,
      })
      .catch(error => this.setError(error));
  },

  methods: {
    ...mapActions(['activate']),
    ...mapMutations(['setError']),
  },
};
</script>

<style scoped>

</style>

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
export default {
  name: 'Activate',

  props: ['uid', 'token'],

  mounted() {
    this.$store.dispatch('activate', {
      uid: this.$props.uid,
      token: this.$props.token,
    });
  },
};
</script>

<style scoped>

</style>

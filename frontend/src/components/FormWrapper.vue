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
          <component :is="component" v-if="component"></component>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import ErrorStack from './ErrorStack.vue';

export default {
  name: 'FormWrapper',

  props: ['title', 'form'],

  components: { ErrorStack },

  data() {
    return {
      component: null,
    };
  },

  computed: {
    loader() {
      if (!this.form) {
        return null;
      }
      return () => import(`./form/${this.form}`);
    },
  },

  mounted() {
    this.loader()
      .then(() => {
        this.component = () => this.loader();
      })
      .catch(() => {
        this.component = () => import('./form/RegisterForm.vue');
      });
  },
};
</script>

<style scoped>

</style>

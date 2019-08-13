<template>
<div class="my-4 gp-error-stack">
  <div v-if="errors" class="d-flex flex-direction-column">
    <div v-for="error in errors" :key="error" class="gp-error">
      {{ error }}
    </div>
  </div>
</div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'ErrorStack',

  computed: {
    ...mapState({ errors: state => state.errorHandler.errors }),
  },
};
</script>

<style scoped>
.gp-error-stack {
  min-width: 400px;
}
.gp-error {
  width: 100%;
  font-size: 0.75rem;
  font-weight: bold;
  padding: 8px;
  color: #721c24;
  background-color: #f8d7da;
  margin-bottom: 4px;
  border-radius: .25rem;
}
</style>

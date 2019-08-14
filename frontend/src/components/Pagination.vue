<template>
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item">
      <button @click="fetch(previousPage.limit, previousPage.offset)"
              class="page-link">
        Previous
      </button>
    <li class="page-item">
      <button @click="fetch(nextPage.limit, nextPage.offset)"
              class="page-link">
        Next
      </button>
    </li>
  </ul>
</nav>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Pagination',

  props: ['previousPage', 'nextPage'],

  methods: {
    ...mapActions(['fetchProjects']),
    fetch(limit, offset) {
      this.fetchProjects({ limit, offset });
    },
  },
};
</script>

<style scoped>

</style>

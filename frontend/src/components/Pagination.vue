<template>
<nav>
  <ul class="pagination">
    <li v-bind:class="{ disabled: !previousPageNumber }" class="page-item">
      <button @click="fetchProjects(1)" class="page-link" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </button>
    </li>
    <li v-if="previousPageNumber" class="page-item">
      <button @click="fetchProjects(previousPageNumber)" class="page-link" aria-label="Previous">
        {{ previousPageNumber }}
      </button>
    </li>
    <li class="page-item active" aria-current="page">
      <span class="page-link">
        {{ currentPageNumber }}
        <span class="sr-only">(current)</span>
      </span>
    </li>
    <li v-if="nextPageNumber" class="page-item">
      <button @click="fetchProjects(nextPageNumber)" class="page-link" aria-label="Next">
        {{ nextPageNumber }}
      </button>
    </li>
    <li v-bind:class="{ disabled: !nextPageNumber }" class="page-item">
      <button @click="fetchProjects(totalPages)" class="page-link" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </button>
    </li>
  </ul>
</nav>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Pagination',

  computed: {
    ...mapState({
      previousPageNumber: state => state.planner.previousPageNumber,
      currentPageNumber: state => state.planner.currentPageNumber,
      nextPageNumber: state => state.planner.nextPageNumber,
      totalPages: state => state.planner.totalPages,
    }),
  },

  methods: {
    ...mapActions(['fetchProjects']),
  },
};
</script>

<style scoped>

</style>

<template>
<nav>
  <ul class="pagination">
    <li v-bind:class="{ disabled: !prevPageNumber }" class="page-item">
      <router-link :to="{ name: 'projects',  params: { page: 1 }}"
                   class="page-link" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </router-link>
    </li>
    <li v-if="prevPageNumber" class="page-item">
      <router-link :to="{ name: 'projects',  params: { page: prevPageNumber }}"
                   class="page-link" aria-label="Previous">
        {{ prevPageNumber }}
      </router-link>
    </li>
    <li class="page-item active" aria-current="page">
      <span class="page-link">
        {{ currPageNumber }}
        <span class="sr-only">(current)</span>
      </span>
    </li>
    <li v-if="nextPageNumber" class="page-item">
      <router-link :to="{ name: 'projects',  params: { page: nextPageNumber }}"
                   class="page-link" aria-label="Next">
        {{ nextPageNumber }}
      </router-link>
    </li>
    <li v-bind:class="{ disabled: !nextPageNumber }" class="page-item">
      <router-link :to="{ name: 'projects',  params: { page: totalPages }}"
                   class="page-link" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </router-link>
    </li>
  </ul>
</nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Pagination',

  computed: {
    ...mapState({
      prevPageNumber: state => state.planner.pagination.prevPageNumber,
      currPageNumber: state => state.planner.pagination.currPageNumber,
      nextPageNumber: state => state.planner.pagination.nextPageNumber,
      totalPages: state => state.planner.pagination.totalPages,
    }),
  },
};
</script>

<style scoped>

</style>

<template>
<div class="gp-projects d-flex">
  <div class="py-4 gp-projects__left-sidebar">
    Menu
  </div>
  <div class="py-4 gp-projects__main flex-grow-1">
    <div class="px-3 gp-projects__main-menu">
      <h3>
        All projects
      </h3>
      <div class="d-flex justify-content-between align-items-center py-2">
        <span class="text-uppercase">
          {{ projectsCount }} project(s)
        </span>
        <div class="btn-group" role="group">
          <a class="btn btn-primary" href="#">
            <i class="fa fa-plus" aria-hidden="true"></i>
          </a>
          <a class="btn btn-primary" href="#">
            <i class="fa fa-filter" aria-hidden="true"></i>
          </a>
        </div>
      </div>
    </div>
    <div class="px-3 py-2 gp-projects__main-content">
      <Pagination/>
      <ProjectPreview v-for="project in projects" :key="project.id"/>
      <h5 v-if="!projectsCount" class="text-uppercase text-center">
        Empty.
      </h5>
    </div>
  </div>
</div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';
import ProjectPreview from '@/components/ProjectPreview.vue';
import Pagination from '@/components/Pagination.vue';

export default {
  name: 'Projects',

  components: [ProjectPreview, Pagination],

  computed: {
    ...mapState({
      errors: state => state.planner.errors,
      projects: state => state.planner.projects,
    }),
    ...mapGetters(['projectsCount']),
  },
};
</script>

<style scoped>

</style>

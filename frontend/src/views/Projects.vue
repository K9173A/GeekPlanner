<template>
<div class="container">
  <div class="row justify-content-center my-4">
    <div class="col-10">
      <ErrorStack/>
      <div class="card shadow">
        <div class="card-header px-3 py-3">
          <div class="d-flex justify-content-between align-items-center">
            <span class="text-uppercase">
              {{ projectsCount }} project(s)
            </span>
            <div class="btn-group" role="group">
              <router-link :to="{ name: 'createProject' }" class="btn btn-primary">
                New
              </router-link>
              <a class="btn btn-primary" href="#">
                Filter
              </a>
            </div>
          </div>
        </div>
        <div class="card-body px-3 py-2">
          <div v-if="projectsCount">
            <Pagination class="d-flex justify-content-end" />
            <div v-for="(project, index) in projects" :key="index">
              <ProjectPreview :project="project" :index="index"/>
            </div>
          </div>
          <div v-else class="h5 text-uppercase text-center">
            There are no projects.
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import ProjectPreview from '@/components/ProjectPreview.vue';
import Pagination from '@/components/Pagination.vue';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'Projects',

  components: { ProjectPreview, Pagination, ErrorStack },

  computed: {
    ...mapState({
      projects: state => state.planner.projects,
      projectsCount: state => state.planner.pagination.count,
    }),
  },

  mounted() {
    this.fetchProjects();
  },

  methods: {
    ...mapActions(['fetchProjects']),
  },
};
</script>

<style scoped lang="scss">
.card-body {
  min-height: 512px;
}
</style>

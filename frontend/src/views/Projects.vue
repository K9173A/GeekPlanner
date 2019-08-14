<template>
<div class="container">
  <div class="row justify-content-center my-4">
    <div class="col-10">
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
          <h5 v-if="!projectsCount" class="text-uppercase text-center">
            There are no projects.
          </h5>
          <div v-else>
            <ProjectPreview v-for="project in projects" :key="project.id"/>
            <Pagination/>
          </div>
        </div>
      </div>
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

  components: { ProjectPreview, Pagination },

  computed: {
    ...mapState({ projects: state => state.planner.projects }),
    ...mapGetters(['projectsCount']),
  },
};
</script>

<style scoped lang="scss">
.card-body {
  min-height: 512px;
}
</style>

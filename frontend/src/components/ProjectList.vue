<template>
<div class="container">
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
            {{ object_list|length }} project(s)
          </span>
          <div class="btn-group" role="group">
            <a class="btn btn-primary" href="{% url 'planner:create_project' %}">
              <i class="fa fa-plus" aria-hidden="true"></i>
            </a>
            <a class="btn btn-primary" href="#">
              <i class="fa fa-filter" aria-hidden="true"></i>
            </a>
          </div>
        </div>
      </div>
      <div class="px-3 py-2 gp-projects__main-content">
        <ProjectPreview v-for="project in projects" :key="project.id"/>
        <h5 v-if="!projects.length" class="text-uppercase text-center">
          Empty.
        </h5>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import ProjectPreview from "./ProjectPreview";

export default {
  name: 'ProjectList',
  components: [
    ProjectPreview,
  ],
  mounted: {
    fetchProjectList() {
      // Vue.axios.get()
    }
  }
};
</script>

<style scoped>

</style>

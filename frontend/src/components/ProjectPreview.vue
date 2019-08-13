<template>
<div class="my-2 d-flex align-content-stretch gp-projects__main-item rounded-top">
  <div class="gp-projects__main-thumbnail">
    <img class="gp-projects__main-img" :src="project.thumbnail_url" alt="ProjectThumbnail">
    <div class="gp-projects__main-owner text-align-center">
      <div>
        {{ project.date_created }}
      </div>
      <div v-if="project.owner">
        {{ project.owner.first_name }}{{ project.owner.last_name }}
      </div>
      <div v-else>
        Unknown creator
      </div>
    </div>
  </div>
  <div class="gp-projects__main-summary">
    <div class="d-flex justify-content-between">
      <button class="font-weight-bold" href="#">
        {{ project.title }}
      </button>
      <div class="btn-group" role="group">
        <button @click="deleteProject(project.pk)" class="btn btn-outline-primary">
          <i class="fa fa-trash" aria-hidden="true"></i>
        </button>
        <a class="btn btn-outline-primary" href="#">
          <i class="fa fa-cogs" aria-hidden="true"></i>
        </a>
      </div>
    </div>
    <hr class="gp-hr">
    <div class="gp-projects__main-description">
      {{ project.description }}
    </div>
    <hr class="gp-hr">
    <div class="container">
      <div class="row">
        <div class="col-8 gp-projects__main-tags">
          <a class="btn tag" href="#">Python</a>
          <a class="btn tag" href="#">VueJS</a>
          <a class="btn tag" href="#">Django</a>
          <a class="btn tag" href="#">Linux</a>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex';
import bootbox from 'bootbox';

export default {
  name: 'Project',

  props: ['project'],

  methods: {
    ...mapGetters(['deleteProject']),
    deleteProject(projectId) {
      bootbox.confirm({
        message: `Do you really want to delete ${this.project.title}?`,
        buttons: {
          confirm: {
            label: 'Confirm',
            className: 'btn-danger',
          },
          cancel: {
            label: 'Cancel',
            className: 'btn-success',
          },
        },
        callback: (result) => {
          if (result) {
            this.deleteProject({ project_pk: projectId });
          }
        },
      });
    },
  },
};
</script>

<style scoped>

</style>

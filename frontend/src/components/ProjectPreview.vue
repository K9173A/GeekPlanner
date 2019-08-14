<template>
<div class="card">
  <div class="row no-gutters">
    <div class="col">
      <img class="gp-projects__main-img" :src="project.thumbnail_url" alt="ProjectThumbnail">
    </div>
    <div class="col-8">
      <div class="card-header">
        <button class="font-weight-bold" href="#">
          {{ project.title }}
        </button>
      </div>
      <div class="card-body">
        {{ project.description }}
      </div>
      <div class="card-footer">
        <a class="btn tag" href="#">Python</a>
        <a class="btn tag" href="#">VueJS</a>
        <a class="btn tag" href="#">Django</a>
        <a class="btn tag" href="#">Linux</a>
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

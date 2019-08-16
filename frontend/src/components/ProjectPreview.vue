<template>
<div class="card">
  <div class="row no-gutters">
    <div class="col">
      {{ index }}
    </div>
    <div class="col-8">
      <div class="card-header d-flex justify-content-between">
        <router-link :to="{ name: 'projectDetails', params: {id: project.id}}"
                     class="font-weight-bold">
          {{ project.title }}
        </router-link>
        <div class="btn-group" role="group">
          <button @click="edit" class="btn btn-secondary">
            Edit
          </button>
          <button @click="del" class="btn btn-secondary">
            Delete
          </button>
        </div>
      </div>
      <div class="card-body">
        {{ project.description }} ==== {{ project.id }}
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

  props: ['project', 'index'],

  methods: {
    ...mapGetters(['deleteProject']),
    del() {
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
            this.deleteProject(this.project.id);
          }
        },
      });
    },
    edit() {
      console.log(this.project.id);
    },
  },
};
</script>

<style scoped>

</style>

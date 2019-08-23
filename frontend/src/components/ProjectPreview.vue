<template>
<div class="card mb-2">
  <div class="row no-gutters">
    <img src="https://via.placeholder.com/256" alt="">
    <div class="col">
      <div class="card-header d-flex align-items-center justify-content-between">
        <button @click="loadProject" class="btn btn-link font-weight-bold">
          {{ project.title }}
        </button>
        <button @click="participate(true)">
          Join
        </button>
        <button @click="participate(false)">
          Leave
        </button>
        <div class="btn-group" role="group">
          <button @click="updateProject" class="btn btn-sm btn-secondary">
            Edit
          </button>
          <button @click="$modal.show('confirm-delete')" class="btn btn-sm btn-secondary">
            Delete
          </button>
        </div>
      </div>
      <div class="card-body">
        {{ project.description }}
      </div>
      <div class="card-footer">
        <div class="d-flex justify-content-start flex-wrap">
          <span class="badge badge-primary mx-1 my-1">Django</span>
          <span class="badge badge-primary mx-1 my-1">Vue.js</span>
          <span class="badge badge-primary mx-1 my-1">Python</span>
          <span class="badge badge-primary mx-1 my-1">JavaScript</span>
        </div>
      </div>
      <ConfirmDeleteModal :object="project" type="project"/>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations } from 'vuex';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal.vue';
import token from '@/common/token';

export default {
  name: 'Project',

  components: { ConfirmDeleteModal },

  props: ['project', 'index'],

  methods: {
    ...mapMutations(['setProjectInformation', 'setProjectData', 'setError']),

    participate(value) {
      this.axios
        .patch(`planner/participate_project/${this.project.id}`,
          { participate: value }, token.getAuthHeaders())
        .then(() => this.$router.go(-1))
        .catch(error => this.setError(error));
    },

    updateProject() {
      this.setProjectInformation(this.project);
      this.$router.push({ name: 'updateProject', params: { id: this.project.id } });
    },

    loadProject() {
      this.$router.push({ name: 'project', params: { id: this.project.id } });
    },
  },
};
</script>

<style scoped>
.card-header {
  height: 64px;
}
.card-body {
  height: 128px;
}
.card-footer {
  height: 64px;
}
</style>

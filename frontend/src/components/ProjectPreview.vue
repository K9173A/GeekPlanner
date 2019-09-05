<template>
<div class="card mb-2">
  <div class="row no-gutters">
    <img src="https://via.placeholder.com/256" alt="">
    <div class="col">
      <div class="card-header d-flex align-items-center justify-content-between">
        <div v-if="project.is_owner === null" class="font-weight-bold">
          {{ project.title }}
        </div>
        <button v-else @click="loadProject" class="btn btn-link font-weight-bold">
          {{ project.title }}
        </button>
        <div class="btn-group" role="group">
          {{ project.is_owner }}
          <button v-if="project.is_owner === null" @click="participate(true)"
                  class="btn btn-sm btn-secondary">
            Join
          </button>
          <button v-else @click="participate(false)"
                  class="btn btn-sm btn-secondary">
            Leave
          </button>
          <button v-if="project.is_owner !== null" @click="updateProject"
                  class="btn btn-sm btn-secondary">
            Edit
          </button>
          <button v-if="project.is_owner === true" @click="deleteProject"
                  class="btn btn-sm btn-secondary">
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
import { mapActions, mapMutations, mapState } from 'vuex';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal.vue';
import token from '@/common/token';

export default {
  name: 'Project',

  components: { ConfirmDeleteModal },

  props: ['project', 'index'],

  computed: {
    ...mapState({
      currentPage: state => state.planner.pagination.currPageNumber,
    }),
  },

  methods: {
    ...mapActions(['fetchProjects']),
    ...mapMutations(['setProjectInformation', 'setProjectData', 'setError', 'setDeleteObjectType']),

    participate(value) {
      this.axios
        .patch(`planner/participate_project/${this.project.id}/`,
          { participate: value }, token.getAuthHeaders())
        .then(() => this.fetchProjects(this.currentPage))
        .catch(error => this.setError(error));
    },

    updateProject() {
      this.setProjectInformation(this.project);
      this.$router.push({ name: 'updateProject', params: { id: this.project.id } });
    },

    deleteProject() {
      this.setProjectInformation(this.project);
      this.setDeleteObjectType('project');
      this.$modal.show('confirm-delete');
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

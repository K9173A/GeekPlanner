<template>
<div class="container mb-4">
  <div class="row justify-content-center">
    <div class="col-10">
      <ErrorStack/>
      <div class="card shadow">
        <div class="card-header">
          <div class="d-flex justify-content-between">
            <div class="h4 font-weight-bold my-4">
              {{ title }}
            </div>
            <div class="btn-group" role="group">
              <button @click="updateProject" class="btn btn-primary">
                Edit
              </button>
              <button @click="$modal.show('confirm-delete')" class="btn btn-primary">
                Delete
              </button>
              <button @click="$router.go(-1)" class="btn btn-primary">
                Back
              </button>
            </div>
          </div>
        </div>
        <div class="card-body">
          <div class="container">
            <div class="row">
              <div v-for="category in categories" :key="category.id" class="col">
                <Category :name="category.name" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <ConfirmDeleteModal :object="project" type="project"/>
    </div>
  </div>
</div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';
import Category from '@/components/Category.vue';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal.vue';
import token from '@/common/token';

export default {
  name: 'Project',

  components: { ErrorStack, Category, ConfirmDeleteModal },

  props: ['id'],

  computed: {
    ...mapState({
      project: state => state.planner.project,
      title: state => state.planner.project.information.title,
      categories: state => state.planner.project.categories,
      cards: state => state.planner.project.cards,
    }),
  },

  created() {
    this.loadProject();
  },

  methods: {
    ...mapMutations(['setError', 'setProjectData', 'setProjectInformation']),
    loadProject() {
      this.axios
        .get(`planner/project_details/${this.id}/`, token.getAuthHeaders())
        .then(response => this.setProjectData(response.data))
        .catch(error => this.setError(error));
    },

    updateProject() {
      this.setProjectInformation(this.project);
      this.$router.push({ name: 'updateProject', params: { id: this.id } });
    },
  },
};
</script>

<style scoped>
.container {
  min-height: 512px;
}
</style>

<template>
<div class="card">
  <div class="row no-gutters">
    <div class="col">
      {{ index }}
    </div>
    <div class="col-8">
      <div class="card-header d-flex justify-content-between">
        <router-link :to="{ name: 'project', params: {id: project.id}}"
                     class="font-weight-bold">
          {{ project.title }}
        </router-link>
        <div class="btn-group" role="group">
          <button @click="updateProject(project)" class="btn btn-secondary">
            Edit
          </button>
          <button @click="$modal.show('confirm-delete')" class="btn btn-secondary">
            Delete
          </button>
        </div>
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
      <ConfirmDeleteModal :object="project" type="project"/>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal.vue';

export default {
  name: 'Project',

  components: { ConfirmDeleteModal },

  props: ['project', 'index'],

  methods: {
    ...mapActions(['updateProject']),
  },
};
</script>

<style scoped>

</style>

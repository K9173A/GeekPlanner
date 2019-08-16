<template>
<div class="container">
  <div class="row">
    <div class="col-10">
      <ErrorStack/>
      <div class="card shadow">
        <div class="card-header my-4">
          <div class="h3 font-weight-bold">
            {{ project.information.title }}
          </div>
        </div>
        <div class="card-body">
          efefefefefef
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'ProjectDetails',

  components: { ErrorStack },

  props: ['id'],

  computed: {
    ...mapState({
      project: state => state.planner.project,
    }),
  },

  mounted() {
    this.loadProject(this.id);
  },

  methods: {
    ...mapActions(['loadProject']),
  },
};
</script>

<style scoped>

</style>

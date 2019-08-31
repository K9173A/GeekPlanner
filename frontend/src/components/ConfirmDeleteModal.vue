<template>
<modal name="confirm-delete" :classes="['card']" transition="pop-out" :width="400" :height="200">
  <div class="card-header">
    <h5>
      Confirm deleting
    </h5>
  </div>
  <div class="card-body">
    <p>
      Do you really want to delete this object?
    </p>
  </div>
  <div class="card-footer">
    <button @click="deleteObject" type="button" class="btn btn-primary mx-2">
      Delete
    </button>
    <button @click="$modal.hide('confirm-delete')" type="button" class="btn btn-primary mx-2">
      Cancel
    </button>
  </div>
</modal>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'ConfirmDeleteModal',

  computed: {
    ...mapState({
      objectType: state => state.planner.objectTypeToDelete,
      currentSelection: state => state.planner.currentSelection,
    }),
  },

  methods: {
    ...mapActions(['deleteProject', 'deleteCard']),
    deleteObject() {
      this.$modal.hide('confirm-delete');
      switch (this.objectType) {
        case 'project':
          this.deleteProject(this.currentSelection.project);
          break;
        case 'card':
          this.deleteCard(this.currentSelection.card);
          this.$router.go(-1);
          break;
        case 'category':
          // TODO
          break;
        default:
          throw Error('Invalid object type!');
      }
    },
  },
};
</script>

<style scoped>

</style>

<template>
<modal name="confirm-delete" :classes="['card']" transition="pop-out" :width="400" :height="200">
  <div class="card-header">
    <h5>
      Confirm deleting
    </h5>
  </div>
  <div class="card-body">
    <p>
      Do you really want to delete this {{ type }}?
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
import { mapActions } from 'vuex';

export default {
  name: 'ConfirmDeleteModal',

  props: ['object', 'type'],

  methods: {
    ...mapActions(['deleteProject']),
    deleteObject() {
      this.$modal.hide('confirm-delete');
      switch (this.type) {
        case 'project':
          this.deleteProject(this.object);
          break;
        case 'card':
          break;
        case 'category':
          break;
        default:
          throw Error(`Invalid object type: ${this.object}!`);
      }
    },
  },
};
</script>

<style scoped>

</style>

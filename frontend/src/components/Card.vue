<template>
<div class="card shadow-sm">
  <div class="card-header px-2 py-2">
    <div class="h5 font-weight-bold">
      {{ card.title }}
    </div>
    <div class="btn-group" role="group">
      <button @click="updateCard" class="btn btn-secondary">
        Edit
      </button>
      <button @click="deleteCard" class="btn btn-secondary">
        Delete
      </button>
    </div>
  </div>
  <div class="card-body">
    <div class="text-align-justify">
      {{ card.description }}
    </div>
  </div>
  <ConfirmDeleteModal :object="card" type="card"/>
</div>
</template>

<script>
import { mapMutations } from 'vuex';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal.vue';

export default {
  name: 'Card',

  props: ['card'],

  components: { ConfirmDeleteModal },

  computed: {
    id: this.card.id,
  },

  methods: {
  ...mapMutations(['setError', 'setProjectData', 'setProjectInformation']),
    updateCard() {
      this.setProjectInformation(this.project);
      this.$router.push({ name: 'updateCard', params: { id: this.id } });
    },
  },
};
</script>

<style scoped>

</style>

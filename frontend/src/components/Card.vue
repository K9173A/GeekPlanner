<template>
<div class="card shadow-sm">
  <div class="card-header px-2 py-2">
    <div class="h5 font-weight-bold">
      {{ card.title }}
    </div>
    <div class="btn-group" role="group">
      <button @click="updateCard(id)" class="btn btn-secondary">
        Edit
      </button>
      <button @click="deleteCard(id)" class="btn btn-secondary">
        Delete
      </button>
    </div>
  </div>
  <div class="card-body">
    <div class="text-align-justify">
      {{ card.description }}
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Card',

  props: ['card'],

  computed: {
    id: this.card.id,
  },

  methods: {
    ...mapActions(['deleteCard, updateCard']),
  },
};
</script>

<style scoped>

</style>

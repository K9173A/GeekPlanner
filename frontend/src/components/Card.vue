<template>
<div class="card shadow-sm my-3" :class="cardColor">
  <div class="card-header px-2 py-2">
    <div class="font-weight-bold">
      {{ card.title }}
    </div>
  </div>
  <div class="card-body">
    <div class="text-align-justify">
      {{ card.description }}
    </div>
  </div>
  <a href="#" @click.prevent="update" class="stretched-link"></a>
</div>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  name: 'Card',

  props: ['card'],

  computed: {
    cardColor() {
      switch (this.card.priority) {
        case 0:
          return 'text-white bg-dark';
        case 1:
          return 'text-white bg-secondary';
        case 2:
          return 'bg-light';
        case 3:
          return 'text-white bg-primary';
        case 4:
          return 'text-white bg-warning';
        case 5:
          return 'text-white bg-danger';
        default:
          return 'bg-light';
      }
    },
  },

  methods: {
    ...mapMutations(['setCurrentCard', 'setCurrentCategory']),
    update() {
      this.setCurrentCard(this.card);
      this.setCurrentCategory(this.card.category);
      this.$router.push({ name: 'updateCard', params: { id: this.card.id } });
    },
  },
};
</script>

<style scoped>

</style>

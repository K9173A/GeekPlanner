<template>
<div class="card">
  <div class="card-header">
    <div class="d-flex align-items-center justify-content-between">
      <div class="font-weight-bold">
        {{ category.name }}
      </div>
      <button @click="createCard" class="btn btn-secondary btn-sm">
        +
      </button>
    </div>
  </div>
  <div class="card-body">
    <h5 v-if="!cards">
      Empty.
    </h5>
    <div v-for="card in cards" :key="card.id">
      <Card :card="card"/>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations, mapState, mapActions } from 'vuex';
import Card from '@/components/Card.vue';

export default {
  name: 'Category',

  props: ['category'],

  components: { Card },

  data() {
    return { cards: null };
  },

  computed: {
    ...mapState({
      project: state => state.planner.currentSelection.project,
      projectCards: state => state.planner.currentSelection.project.cards,
    }),
  },

  methods: {
    ...mapMutations(['setError', 'setCurrentCategory']),
    ...mapActions(['fetchCards']),
    createCard() {
      this.setCurrentCategory(this.category);
      this.$router.push({
        name: 'createCard',
        params: { id: this.project.information.id },
      });
    },
  },

  created() {
    // arg is from props
    this.fetchCards(this.category)
      .then((fetched) => {
        if (fetched) {
          this.cards = this.projectCards[this.category.name];
        }
      })
      .catch(error => this.setError(error));
  },
};
</script>

<style scoped>

</style>

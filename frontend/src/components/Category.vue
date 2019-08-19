<template>
<div class="card">
  <div class="card-header d-flex justify-content-between">
    <h5>
      {{ category.name }}
    </h5>
  </div>
  <div class="card-body px-2 py-2">
    <h5 v-if="!cards">
      Empty.
    </h5>
    <div v-for="card in cards" :key="card.id" class="row">
      <div class="col-12">
        <Card :card="card"/>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Card from '@/components/card';

export default {
  name: 'Category',

  components: { Card },

  props: ['category'],
};
</script>

<style scoped>

</style>

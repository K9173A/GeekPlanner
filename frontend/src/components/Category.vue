<template>
<div class="card">
  <div class="card-header">
    {{ name }}
    <button @click="createCard" class="btn btn-primary">
      New
    </button>
  </div>
  <div class="card-body">
    Body
  </div>
</div>
</template>

<script>
export default {
  name: 'Category',

  props: ['name'],


};
</script>

<style scoped>

</style>

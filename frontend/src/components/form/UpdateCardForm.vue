<template>
<form v-on:submit.prevent="update" method="post">
  <vue-form-generator :schema="schema" :model="model" :options="formOptions">
  </vue-form-generator>
  <div class="d-flex justify-content-around px-4 py-4">
    <input class="btn btn-primary col-5" type="submit" value="Save">
    <button @click="$router.go(-1)" class="btn btn-primary col-5">
      Back
    </button>
  </div>
</form>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import token from '@/common/token';

export default {
  name: 'UpdateCardForm',

  data() {
    return {
      model: {
        title: '',
        description: '',
        priority: '',
      },
      schema: {
        groups: [
          {
            fields: [
              {
                type: 'input',
                inputType: 'text',
                label: 'Title',
                model: 'title',
                placeholder: 'Awesome card',
                required: true,
                min: 3,
              },
              {
                type: 'textArea',
                inputType: 'text',
                label: 'Description',
                model: 'description',
                placeholder: 'This card is very useful!',
                hint: 'Max 256 characters',
                max: 256,
              },
              {
                type: 'select',
                label: 'Priority',
                model: 'priority',
                values: function() {
                  return [
                    { id: 0, name: 'Lowest' },
                    { id: 1, name: 'Low' },
                    { id: 2, name: 'Normal' },
                    { id: 3, name: 'High' },
                    { id: 4, name: 'Very High' },
                    { id: 5, name: 'Highest' },
                  ]
                },
                default: 'Normal',
              }
            ]
          },
        ],
      }
    }
  },

  methods: {
    ...mapMutations(['setError']),
    update() {
      this.axios
        .patch(`planner/update_card/${this.card.id}`, {
          title: this.model.title,
          description: this.model.description,
          priority: this.model.priority,
        }, token.getAuthHeaders())
        .then(() => this.$router.go(-1))
        .catch(error => this.setError(error));
    },

  }
};
</script>

<style scoped>

</style>

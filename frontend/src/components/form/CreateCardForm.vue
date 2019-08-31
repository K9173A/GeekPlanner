<template>
<div class="container">
  <div class="row justify-content-center">
    <div class="col-6">
      <ErrorStack/>
      <div class="card my-4 gp-form">
        <div class="card-header text-center text-uppercase font-weigt-bold">
          {{ title }}
        </div>
        <div class="card-body">
          <form v-on:submit.prevent="submit" method="post">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
            <div class="d-flex justify-content-around px-4 py-4">
              <button @click="$router.go(-1)" class="btn btn-primary col-5">
                Back
              </button>
              <input class="btn btn-primary col-5" type="submit" value="Submit">
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations, mapState } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';
import token from '@/common/token';

export default {
  name: 'CreateCardForm',

  components: { ErrorStack },

  data() {
    return {
      title: 'New Card',
      model: {
        title: '',
        description: '',
        priority: 2,
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
                values: function fn() {
                  return [
                    { id: 0, name: 'Lowest' },
                    { id: 1, name: 'Low' },
                    { id: 2, name: 'Normal' },
                    { id: 3, name: 'High' },
                    { id: 4, name: 'Very High' },
                    { id: 5, name: 'Highest' },
                  ];
                },
                default: 'Normal',
              },
            ],
          },
        ],
      },
      formOptions: {
        validateAfterLoad: true,
        validateAfterChanged: true,
        validateAsync: true,
      },
    };
  },

  computed: {
    ...mapState({
      project: state => state.planner.currentSelection.project,
      category: state => state.planner.currentSelection.category,
    }),
  },

  methods: {
    ...mapMutations(['setError']),
    submit() {
      this.axios
        .post(`planner/create_card/project/${this.project.information.id}` +
          `/category/${this.category.id}/`, {
          title: this.model.title,
          description: this.model.description,
          priority: this.model.priority,
        }, token.getAuthHeaders())
        .then(() => this.$router.go(-1))
        .catch(error => this.setError(error));
    },
  },
};
</script>

<style scoped>

</style>

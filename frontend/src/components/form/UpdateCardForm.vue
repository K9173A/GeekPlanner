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
          <form v-on:submit.prevent="submit" id="update-card-form">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
          </form>
          <div class="d-flex justify-content-around px-4 py-4">
            <button @click="$router.go(-1)" class="btn btn-primary col-3">
              Back
            </button>
            <button @click="deleteCard" class="btn btn-primary col-3">
              Delete
            </button>
            <input class="btn btn-primary col-3" type="submit"
                   form="update-card-form" value="Save">
          </div>
        </div>
      </div>
      <ConfirmDeleteModal />
    </div>
  </div>
</div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import token from '@/common/token';
import ErrorStack from '@/components/ErrorStack.vue';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal.vue';

export default {
  name: 'UpdateCardForm',

  components: { ErrorStack, ConfirmDeleteModal },

  data() {
    return {
      title: 'Edit Card',
      model: {
        title: '',
        description: '',
        priority: '',
        category: '',
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
              {
                type: 'select',
                label: 'Category',
                model: 'category',
                required: true,
                values: function fn() {
                  return this.$store.state.planner.currentSelection.project.categories;
                },
                default: this.$store.state.planner.currentSelection.category,
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
      card: state => state.planner.currentSelection.card,
      category: state => state.planner.currentSelection.category,
      project: state => state.planner.currentSelection.project,
    }),
  },

  methods: {
    ...mapMutations(['setError', 'setCurrentCard', 'setCurrentCategory', 'setDeleteObjectType']),
    submit() {
      this.axios
        .patch(`planner/update_card/${this.card.id}/`, {
          title: this.model.title,
          description: this.model.description,
          priority: this.model.priority,
          category: this.model.category,
          project: this.project.information.id,
        }, token.getAuthHeaders())
        .then(() => this.$router.go(-1))
        .catch(error => this.setError(error));
    },

    deleteCard() {
      this.setCurrentCard(this.card);
      this.setCurrentCategory(this.category); // ???
      this.setDeleteObjectType('card');
      this.$modal.show('confirm-delete');
    }
  },

  created() {
    this.model = {
      title: this.card.title,
      description: this.card.description,
      priority: this.card.priority,
      category: this.category,
    };
  },
};
</script>

<style scoped>

</style>

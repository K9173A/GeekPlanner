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
          <form v-on:submit.prevent="submit" id="update-project-form">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
          </form>
          <div class="d-flex justify-content-around px-4 py-4">
            <button @click="$router.go(-1)" class="btn btn-primary col-5">
              Back
            </button>
            <input class="btn btn-primary col-5" type="submit"
                   form="update-project-form" value="Save">
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import token from '@/common/token';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'UpdateProjectForm',

  components: { ErrorStack },

  data() {
    return {
      title: 'Edit Project',
      model: {
        title: '',
        description: '',
        thumbnail: '',
        isPublic: '',
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
                placeholder: 'Awesome project',
                required: true,
                min: 3,
              },
              {
                type: 'textArea',
                inputType: 'text',
                label: 'Description',
                model: 'description',
                placeholder: 'This is my favourite project!',
                hint: 'Max 256 characters',
                max: 256,
              },
              {
                type: 'upload',
                label: 'Thumbnail',
                model: 'thumbnail',
              },
              {
                type: 'switch',
                label: 'Make this project public',
                model: 'isPublic',
                textOn: 'Public',
                textOff: 'Private',
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
    ...mapState({ information: state => state.planner.currentSelection.project.information }),
  },

  methods: {
    ...mapMutations(['setError']),
    submit() {
      this.axios
        .patch(`planner/update_project/${this.information.id}/`, {
          title: this.model.title,
          description: this.model.description,
          thumbnail: this.model.thumbnail,
          is_public: this.model.isPublic,
        }, token.getAuthHeaders())
        .then(() => this.$router.go(-1))
        .catch(error => this.setError(error));
    },
  },

  created() {
    this.model = {
      title: this.information.title,
      description: this.information.description,
      thumbnail: this.information.thumbnail,
      isPublic: this.information.is_public,
    };
  },
};
</script>

<style scoped>

</style>

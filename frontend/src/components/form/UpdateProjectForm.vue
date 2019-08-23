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
  name: 'UpdateProjectForm',

  data() {
    return {
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

  created() {
    this.model = {
      title: this.information.title,
      description: this.information.description,
      thumbnail: this.information.thumbnail,
      isPublic: this.information.is_public,
    };
  },

  methods: {
    ...mapMutations(['setError']),
    update() {
      this.axios
        .patch(`planner/update_project/${this.information.id}`, {
          title: this.model.title,
          description: this.model.description,
          thumbnail: this.model.thumbnail,
          is_public: this.model.isPublic,
        }, token.getAuthHeaders())
        .then(() => this.$router.go(-1))
        .catch(error => this.setError(error));
    },
  },
};
</script>

<style scoped>

</style>

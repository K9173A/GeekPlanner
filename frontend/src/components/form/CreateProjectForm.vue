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
          <form v-on:submit.prevent="submit" method="post" enctype="multipart/form-data">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
            <div class="d-flex justify-content-around px-4 py-4">
              <button @click="$router.go(-1)" class="btn btn-primary col-5">
                Cancel
              </button>
              <input class="btn btn-primary col-5" type="submit" value="Create">
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations } from 'vuex';
import token from '@/common/token';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'CreateProject',

  components: { ErrorStack },

  data() {
    return {
      title: 'New Project',
      model: {
        title: '',
        description: '',
        thumbnail: null,
        isPublic: true,
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

  methods: {
    ...mapMutations(['setError']),
    submit() {
      this.axios
        .post('planner/create_project/', {
          title: this.model.title,
          description: this.model.description,
          thumbnail: this.model.thumbnail,
          is_public: this.model.isPublic,
        }, token.getAuthHeaders())
        .then(() => this.$router.push({ name: 'projects' }))
        .catch(error => this.setError(error));
    },
  },
};
</script>

<style scoped>

</style>

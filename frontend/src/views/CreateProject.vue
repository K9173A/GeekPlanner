<template>
<div class="container">
  <div class="row justify-content-center">
    <div class="col-6">
      <ErrorStack/>
      <div class="card gp-form my-4">
        <div class="card-header text-center text-uppercase font-weigt-bold">
          New Project
        </div>
        <div class="card-body">
          <form v-on:submit.prevent="submit" method="post" enctype="multipart/form-data">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
            <div class="d-flex justify-content-around px-4 py-4">
              <input class="btn btn-primary" type="submit" value="Create">
              <router-link :to="{ name: 'projects' }" class="btn btn-primary">
                Cancel
              </router-link>
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

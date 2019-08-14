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
import { mapActions } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'CreateProject',

  components: { ErrorStack },

  data() {
    return {
      model: {
        title: '',
        description: '',
        thumbnail: '',
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
                featured: true,
                hint: 'Max 256 characters',
                max: 256,
              },
              {
                type: 'upload',
                label: 'Thumbnail',
                model: 'thumbnail',
                featured: true,
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
    ...mapActions(['createProject']),
    submit() {
      this.createProject({
        title: this.title,
        description: this.description,
        thumbnail: this.thumbnail,
        is_public: this.isPublic,
      });
    },
  },
};
</script>

<style scoped>

</style>

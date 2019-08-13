<template>
<div class="container">
  <div class="row">
    <div class="col-6">
      <ErrorStack/>
      <form v-on:submit.prevent="submit" method="post" enctype="multipart/form-data">
        <vue-form-generator :schema="schema" :model="model" :options="formOptions">
          <div class="d-flex justify-content-around px-4 py-4">
            <input class="btn btn-primary" type="submit" value="Create">
            <router-link :to="{ name: 'Projects' }" class="btn btn-primary">
              Cancel
            </router-link>
          </div>
        </vue-form-generator>
      </form>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'CreateProject',

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
            legend: 'New Project',
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
                type: 'image',
                label: 'Thumbnail',
                model: 'thumbnail',
                featured: true,
                browse: true,
                preview: true,
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
        isPublic: this.isPublic,
      });
    },
  },
};
</script>

<style scoped>

</style>

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
          <form v-on:submit.prevent="submit" id="update-user-form">
            <vue-form-generator :schema="schema" :model="model" :options="formOptions">
            </vue-form-generator>
          </form>
          <div class="d-flex justify-content-around px-4 py-4">
            <button @click="$router.go(-1)" class="btn btn-primary col-5">
              Back
            </button>
            <input class="btn btn-primary col-5" type="submit"
                   form="update-user-form" value="Save">
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations } from 'vuex';
import ErrorStack from '@/components/ErrorStack.vue';
import token from '@/common/token';

export default {
  name: 'UpdateUserForm',

  components: { ErrorStack },

  props: ['id'],

  data() {
    return {
      title: 'Edit User',
      model: {
        username: '',
        firstName: '',
        lastName: '',
        email: '',
        avatar: '',
        gender: '',
      },
      schema: {
        groups: [
          {
            fields: [
              {
                type: 'input',
                inputType: 'text',
                label: 'Username',
                model: 'username',
                readonly: true,
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'First name',
                model: 'firstName',
                placeholder: 'John',
                min: 2,
                hint: 'Min 2 characters',
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'Last name',
                model: 'lastName',
                placeholder: 'Doe',
                min: 2,
                hint: 'Min 2 characters',
              },
              {
                type: 'input',
                inputType: 'text',
                label: 'E-mail',
                model: 'email',
                readonly: true,
              },
              {
                type: 'upload',
                label: 'Avatar',
                model: 'avatar',
              },
              {
                type: 'select',
                label: 'Gender',
                model: 'gender',
                values: function fn() {
                  return [
                    { id: 0, name: 'Not Set' },
                    { id: 1, name: 'Male' },
                    { id: 2, name: 'Female' },
                  ];
                },
                default: 'Not Set',
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

    loadProfile() {
      this.axios
        .get(`auth/user_profile/${this.id}/`, token.getAuthHeaders())
        .then((response) => {
          this.model = {
            username: response.data.username,
            firstName: response.data.first_name,
            lastName: response.data.last_name,
            email: response.data.email,
            avatar: response.data.avatar,
            gender: response.data.gender,
          };
        })
        .catch(error => this.setError(error));
    },

    submit() {
      this.axios
        .post(`auth/update_profile/${this.id}/`, {
          first_name: this.model.firstName,
          last_name: this.model.lastName,
          avatar: this.model.avatar,
          gender: this.model.gender,
        }, token.getAuthHeaders())
        .then(() => this.$router.go(-1))
        .catch(error => this.setError(error));
    },
  },
};
</script>

<style scoped>

</style>

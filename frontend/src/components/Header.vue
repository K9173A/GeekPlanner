<template>
<nav class="navbar navbar-expand-lg menu p-3">
  <router-link :to="{ name: 'home' }" class="navbar-brand">
    <img src="@/assets/img/logo.png" class="menu__logo" alt="logo">
  </router-link>
  <ul class="nav navbar-nav mx-auto">
    <li>
      <router-link :to="{ name: 'home' }"
         class="nav-link rounded font-weight-bold text-center mx-2 menu__item">
        Main
      </router-link>
    </li>
    <li>
      <router-link :to="{ name: 'pricing' }"
         class="nav-link rounded font-weight-bold text-center mx-2 menu__item">
        Pricing
      </router-link>
    </li>
    <li>
      <router-link :to="{ name: 'home' }"
        class="nav-link rounded font-weight-bold text-center mx-2 menu__item">
        Features
      </router-link>
    </li>
    <li v-if="isAuthenticated">
      <router-link :to="{ name: 'projects' }"
         class="nav-link rounded font-weight-bold text-center mx-2 menu__item">
        Projects
      </router-link>
    </li>
    <li v-if="isSuperuser">
      <router-link :to="{ name: 'home' }"
         class="nav-link rounded font-weight-bold text-center mx-2 menu__item">
        Admin panel
      </router-link>
    </li>
  </ul>
  <div v-if="isAuthenticated" class="btn-group" role="group">
    <button @click="logout" class="btn btn-outline-primary font-weight-bold btn-register">
      Sign out
    </button>
    <router-link :to="{ name: 'home' }"
                 class="btn btn-outline-primary font-weight-bold btn-register">
      Profile
    </router-link>
  </div>
  <div v-else class="btn-group" role="group">
    <router-link :to="{ name: 'login' }"
                 class="btn btn-outline-primary font-weight-bold btn-register">
      Sign in
    </router-link>
    <router-link :to="{ name: 'register' }"
                 class="btn btn-outline-primary font-weight-bold btn-register">
      Sign up
    </router-link>
  </div>
</nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Header',

  computed: {
    ...mapState({
      errors: state => state.auth.errors,
      isAuthenticated: state => state.auth.isAuthenticated,
    }),
    isSuperuser: false,
  },

  methods: {
    logout() {
      this.$store
        .dispatch('logout')
        .then(() => this.$router.push({ name: 'home' }));
    },
  },
};
</script>

<style scoped lang="scss">
.menu {
  background-color: #3b4b8e;
  padding-top: 16px;
  padding-bottom: 16px;
  font-size: 1.2rem;

  @at-root #{&}__item {
    color: #fff;
    min-width: 128px;
    &:hover {
      background-color: #4485d0;
      color: #ffffff;
    }
  }
  @at-root #{&}__item--active {
    background-color: #4368b2;
  }
  @at-root #{&}__logo {
    width: 32px;
    height: 32px;
  }
}

.btn-register {
  min-width: 136px;
  color: #fff;
  border-color: #fff;
  &:hover {
    background-color: #fff;
    color: #4485d0;
    border-color: #fff;
  }
}
</style>

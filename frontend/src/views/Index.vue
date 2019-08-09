<template>
<div class="gp-masthead">
  <div class="container">
    <div class="row align-items-center my-2">
      <div class="col-6 order-md-2 mx-auto">
        <img class="gp-masthead__img" src="@/assets/img/service.png" alt="service">
      </div>
      <div class="col-md-6 order-md-1 text-center">
        <h1 class="gp-masthead__title text-uppercase text-center mb-4">
          GeekPlanner
        </h1>
        <p class="gp-masthead__lead mb-4">
          GeekPlanner was designed to simplify life of our clients when it comes to planning
          and work distribution: business, software development, personal notes - GeekPlanner
          takes care of all of them, increasing productivity and simplifying life.
        </p>
        <a class="btn btn-lg btn-outline-primary gp-masthead__btn px-2 py-2"
           href="#">
          Try now!
        </a>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Index',
};
</script>

<style scoped lang="scss">
.gp-masthead {
  min-height: 600px;
  @at-root #{&}__title {
    color: #4485d0;
    font-size: 3rem;
    letter-spacing: 1.1rem;
  }
  @at-root #{&}__lead {
    text-align: justify;
    font-size: 1.5rem;
    font-weight: 300;
  }
  @at-root #{&}__img {
    height: 512px;
  }
  @at-root #{&}__btn {
    min-width: 256px;
  }
}
</style>

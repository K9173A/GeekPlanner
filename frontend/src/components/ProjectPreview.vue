<template>
<div class="my-2 d-flex align-content-stretch gp-projects__main-item rounded-top">
  <div class="gp-projects__main-thumbnail">
    <img class="gp-projects__main-img" src="{{ project.thumbnail_url }}" alt="ProjectThumbnail">
    <div class="gp-projects__main-owner text-align-center">
      <div>
        {{ project.date_created }}
      </div>
      <div v-if="project.owner">
        {{ project.owner.first_name }}{{ project.owner.last_name }}
        {% else %}
          Unknown creator
        {% endif %}
      </div>
    </div>
  </div>
  <div class="gp-projects__main-summary">
    <div class="d-flex justify-content-between">
      <a class="font-weight-bold" href="{% url 'planner:project_details' project.pk %}">
        {{ project.title }}
      </a>
      <div class="btn-group" role="group">
        <a class="btn btn-outline-primary" href="{% url 'planner:delete_project' project.pk %}">
          <i class="fa fa-trash" aria-hidden="true"></i>
        </a>
        <a class="btn btn-outline-primary" href="{% url 'planner:update_project' project.pk %}">
          <i class="fa fa-cogs" aria-hidden="true"></i>
        </a>
      </div>
    </div>
    <hr class="gp-hr">
    <div class="gp-projects__main-description">
      {{ project.description }}
    </div>
    <hr class="gp-hr">
    <div class="container">
      <div class="row">
        <div class="col-8 gp-projects__main-tags">
          <a class="btn tag" href="#">Python</a>
          <a class="btn tag" href="#">VueJS</a>
          <a class="btn tag" href="#">Django</a>
          <a class="btn tag" href="#">Linux</a>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Project',
  props: [
    'project'
  ],
};
</script>

<style scoped>

</style>

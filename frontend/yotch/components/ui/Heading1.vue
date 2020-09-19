<template>
  <h1>
    <span class="heading1">
      <slot />
    </span>
  </h1>
</template>

<script>
export default {
  name: 'Heading1',
  data () {
    return {}
  }
}
</script>

<style scoped>
.heading1 {
  font-size: 6.0rem;
}

@media screen and (max-width: 480px) {
  .heading1 {
    font-size: 3.0rem;
  }
}
</style>
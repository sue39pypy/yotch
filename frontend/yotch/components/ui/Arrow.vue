<template>
  <div class="arrow-wrap">
    <nuxt-link
      v-scroll-to="'#header'"
      to
    >
      <img src="/assets/img/up-arrow.svg">
    </nuxt-link>
  </div>
</template>

<script>
export default {
  name: 'Arrow',
  props: [
    'color'
  ],
  data () {
    return {}
  }
}
</script>

<style scoped>
.arrow-wrap {
  height: auto;
  width: 100px;
}
</style>
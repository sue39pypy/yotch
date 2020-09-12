<template>
  <h2 class="heading2">
    <span :style="{ color: fontColor ? fontColor: '#000'}">
      <slot />
    </span>
  </h2>
</template>

<script>
export default {
  name: 'Heading2',
  props: {
    fontColor: String
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
.heading2 {
  font-size: 3.0rem;
}

@media screen and (max-width:767px) {
  .heading2 {
    font-size: 2.4rem;
  }
}
</style>
<template>
  <div
    class="kv-wrap"
    :style="{ backgroundImage: 'url(' + image + ')' }"
  >
    <div class="mask"></div>
    <div class="description-wrap">
      <Heading2 :font-color="'#fff'">{{ title }}</Heading2>
      <p
        v-for="(line, index) in description"
        :key="'kv-description-' + index"
      >
        {{ line }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Kv',
  props: {
    title: String,
    image: String,
    description: Array
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
.description-wrap {
  display: inline-block;
  line-height: 1.2;
  margin: 0 auto;
  max-width: 768px;
  position: relative;
  vertical-align: middle;
  width: auto;
  z-index: 20;
}

.description-wrap > h2 {
  margin-bottom: 10px;
}

.kv-wrap {
  background-position: center;
  background-size: cover;
  height: 400px;
  line-height: 400px;
  position: relative;
  text-align: center;
  vertical-align: middle;
  width: 100vw;
  z-index: 0;
}

.kv-wrap * {
  color: #fff;
}

.mask {
  background-color: #000;
  height: 100%;
  left: 0;
  opacity: 0.4;
  position: absolute;
  top: 0;
  width: 100%;
  z-index: 10;
}

@media screen and (max-width: 767px) {
  .description-wrap {
    margin: 0 20px;
  }

  .kv-wrap {
    height: 300px;
    line-height: 300px;
  }
}

</style>
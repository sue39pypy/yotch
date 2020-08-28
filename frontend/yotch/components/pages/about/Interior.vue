<template>
  <div class="content-container">
    <Heading2>{{ content.title }}</Heading2>
    <div class="detail-wrap">

      <div class="description-wrap">
        <p v-for="(line, index) in content.description_converted"
          :key="'content-description-' + index"
        >
          {{ line }}
        </p>
      </div>

      <ul class="images-wrap">
        <li
          v-for="(interior, index) in contentProps"
          :key="'interior-' + index"
          class="interior"
        >
          <img class="interior-image" :src="interior.image_path">
          <!-- <dev class="mask"></dev> -->
          <!-- <dev class="title">{{ interior.title }}</dev> -->
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutInterior',
  props: [
    'content',
    'contentProps'
  ],
  data () {
    return {
      interiors: null
    }
  }
}
</script>

<style scoped>
* {
  color: #333333;
}

.content-container {
  margin: 0 auto;
  width: 100%;
}

.description-wrap {
  margin-top: 40px;
}

.interior {
  background-position: center;
  background-size: cover;
}

.images-wrap {
  column-count: 2;
  column-gap: 0;
  height: auto;
  margin: 40px auto 0;
  width: 100%;
}

.images-wrap .interior {
  -webkit-column-break-inside: avoid;
  padding: 2px;
  page-break-inside: avoid;
  position: relative;
  break-inside: avoid;
}

.images-wrap .interior img {
  height: auto;
  vertical-align: top;
  width: 100%;
  z-index: 1;
}

.images-wrap .interior .mask {
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, .3));
  background-position: 100% 50%;
  background-repeat: no-repeat;
  background-size: 100%;
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
  z-index: 10;
}

.images-wrap .interior .title {
  bottom: 0;
  color: #FFF;
  font-size: 1.2rem;
  left: 0;
  opacity: .8;
  padding: 10px;
  position: absolute;
  z-index: 20;
}

@media screen and (max-width: 767px) {
  .content-container {
    width: 90%;
  }

  .description-wrap p {
    font-size: .9rem;
  }

  .images-wrap .interior .title {
    font-size: 0.8rem;
    padding: 5px;
  }
}
</style>
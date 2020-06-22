<template>
  <div class="container">
    <div class="slide-wrap">
      <agile
        :as-nav-for="asNavFor1"
        class="main"
        :options="options1"
        ref="main"
      >
        <div
          :class="['slide', `slide--${index}`]"
          :key="`main-slide-${index}`"
          v-for="(slide, index) in slides"
        >
          <img :src="slide.image_path">
        </div>
      </agile>
      <agile
        :as-nav-for="asNavFor2"
        class="thumbnails"
        :options="options2"
        ref="thumbnails"
      >
        <div
          :class="['slide', 'slide--thumbnails', `slide--${index}`]"
          @click="$refs.thumbnails.goTo(index)"
          :key="`thumbnail-${index}`"
          v-for="(slide, index) in slides"
        >
          <div class="slide-mask"></div>
          <div class="slide-title"><p>{{ slide.title }}</p></div>
          <img :src="slide.image_path">
        </div>
      </agile>
    </div>
  </div>
</template>

<script>
import { VueAgile } from 'vue-agile'

export default {
  name: 'About',
  components: {
    agile: VueAgile
  },
  data () {
    return {
      asNavFor1: [],
      asNavFor2: [],
      options1: {
        dots: false,
        fade: true,
        navButtons: false,
        slidesToShow: 1
      },
      options2: {
        autoplay: false,
        centerMode: true,
        dots: false,
        navButtons: false,
        slidesToShow: 3,
        responsive: [
          {
            breakpoint: 767,
            settings: {
              slidesToShow: 5
            }
          }
        ]
      },
      slides: null
    }
  },
  async asyncData({ $axios }) {
    // カルーセルの要素をAPIで取得
    const url = "/api/slides"
    const response = await $axios.get(url)
    return { slides: response.data.slides }
  },
  mounted () {
    this.asNavFor1.push(this.$refs.thumbnails)
    this.asNavFor2.push(this.$refs.main)
  }
}
</script>

<style scoped>
.agile .thumbnails {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}

.container {
  margin: 0 auto;
  max-width: 1024px;
  position: relative;
  width: 90%;
}

.main {
  margin-bottom: 2px;
}

.slide {
  align-items: center;
  box-sizing: border-box;
  color: #fff;
  display: flex;
  display: -ms-flexbox;
  height: 40vh;
  justify-content: center;
  position: relative;
}

.slide img {
  height: 100%;
  left: 0;
  object-fit: cover;
  object-position: center;
  position: absolute;
  top: 0;
  width: 100%;
  z-index: 0;
}

.slide-mask {
  background-color: #000;
  height: 100%;
  left: 0;
  opacity: .5;
  position: absolute;
  top: 0;
  vertical-align: middle;
  width: 100%;
  z-index: 10;
}

.slide--thumbnails {
  cursor: pointer;
  height: 10vh;
  padding: 0 1px;
  transition: opacity .3s;
}

.slide--thumbnails:hover {
  opacity: .75;
}

.slide-title {
  z-index: 100;
}

.slide-title p {
  color: #FFF;
  font-size: 1.6rem;
}

.slide-wrap {
  position: absolute;
  top: 80px;
  width: 75vh;
}

.thumbnails {
  margin: 0 -1px;
  width: calc(100% + 2px);
}

@media screen and (max-width: 480px) {
  .container {
    width: 100%;
  }

  .slide-wrap {
    margin: 0;
    top: 0;
    width: 100%;
  }
}
</style>
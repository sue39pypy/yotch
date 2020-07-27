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
          @click="$refs.thumbnails.goTo(index); adjustContentWrapHeight(index);"
          :key="`thumbnail-${index}`"
          v-for="(slide, index) in slides"
        >
          <div class="slide-mask"></div>
          <div class="slide-title"><p>{{ slide.title }}</p></div>
          <img :src="slide.image_path">
        </div>
      </agile>
    </div>
    <div class="contents-wrap">
      <agile
        :as-nav-for="asNavFor3"
        class="contents"
        :options="options3"
        ref="contents"
      >
        <div
          :class="['slide', 'slide--contents', `slide--${index}`]"
          :key="'content-' + index"
          v-for="(content, index) in contents"
        >
          <component :is="content" />
        </div>
      </agile>
    </div>
  </div>
</template>

<script>
import { VueAgile } from 'vue-agile'

import AboutSkills from '~/components/pages/about/Skills.vue'
import AboutYotch from '~/components/pages/about/Yotch.vue'

export default {
  name: 'About',
  components: {
    agile: VueAgile,
    AboutSkills,
    AboutYotch
  },
  data () {
    return {
      asNavFor1: [],
      asNavFor2: [],
      asNavFor3: [],
      contents: [
        'about-yotch',
        'about-skills'
      ],
      heights: [],
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
          },
          {
            breakpoint: 1025,
            settings: {
              slidesToShow: 3
            }
          }
        ]
      },
      options3: {
        autoplay: false,
        centerMode: false,
        dots: false,
        navButtons: false,
        slidesToShow: 1,
        swipeDistance: 1000000
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
  methods: {
    // ページコンテンツの高さを子要素の高さに調節
    adjustContentWrapHeight (index) {
      let agileList = document.querySelector('.contents .agile__list')
      let agileSlidesRegular = document.querySelector('.contents .agile__list .agile__track .agile__slides--regular')
      agileList.style.height = this.heights[index] + 'px'
      agileSlidesRegular.style.height = this.heights[index] + 'px'
    }
  },
  mounted () {
    this.asNavFor1.push(this.$refs.thumbnails)
    this.asNavFor1.push(this.$refs.contents)
    this.asNavFor2.push(this.$refs.main)
    this.asNavFor2.push(this.$refs.contents)

    this.$nextTick(() => {
      // vue-agile表示部分ラッパー要素
      let agileSlidesRegular = document.querySelector('.contents .agile__list .agile__track .agile__slides--regular')
      // ページコンテンツラッパー要素
      let contentsContainers = agileSlidesRegular.children

      let tmp = []
      let height = 0
      for (let i = 0; i < contentsContainers.length; i++) {
        height = contentsContainers[i].firstElementChild.clientHeight
        tmp.push(height)
      }
      this.heights = tmp

      // ページコンテンツラッパー要素の高さを初期化
      this.adjustContentWrapHeight(0)
    })
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
  min-height: 100vh;
  width: 90%;
}

.contents {
  height: auto;
}

.contents-wrap {
  padding: 50px 0 50px;
  width: 100%;
}

.slide {
  align-items: center;
  box-sizing: border-box;
  color: #fff;
  display: block;
  height: 36vh;
  position: relative;
}

.slide img {
  height: 100%;
  object-fit: cover;
  object-position: center;
  overflow: hidden;
  position: relative;
  width: 100%;
  z-index: 0;
}

.slide--contents {
  height: 100%;
}

.slide-mask {
  background-color: #000;
  height: 100%;
  left: 0;
  opacity: .5;
  overflow: hidden;
  position: absolute;
  top: 0;
  vertical-align: middle;
  width: 100%;
  z-index: 10;
}

.slide--thumbnails {
  cursor: pointer;
  height: 10vh;
  position: relative;
  transition: opacity .3s;
}

.slide--thumbnails:hover {
  opacity: .75;
}

.slide-title {
  font-weight: bold;
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 100;
}

.slide-title p {
  color: #FFF;
  font-size: 1.4rem;
}

.slide-wrap {
  margin: 100px auto 0;
  width: 100%;
}

.thumbnails {
  margin: 0 auto;
  width: 100%;
}

@media screen and (max-width: 480px) {
  .container {
    width: 100%;
  }

  .slide-wrap {
    margin: 0;
    top: 0;
  }
}

@media screen and (min-width: 1025px) {
  .contents-wrap {
    padding: 0 0 100px;
  }

  .slide-wrap {
    margin: 100px 0 0 auto;
    width: 50%;
  }
}
</style>
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
          @click="slidesContent(index)"
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
        :swipe-distance="100000"
      >
        <div
          :class="['slide', 'slide--contents', `slide--${index}`]"
          :key="'content-' + index"
          v-for="(content, index) in contents"
        >
          <component
            :is="content"
            :content="slides[index]"
            :content-props="contentsProps[index]"
          />
        </div>
      </agile>
    </div>
  </div>
</template>

<script>
import { VueAgile } from 'vue-agile'

import AboutContact from '~/components/pages/about/Contact.vue'
import AboutSkills from '~/components/pages/about/Skills.vue'
import AboutYotch from '~/components/pages/about/Yotch.vue'

export default {
  components: {
    agile: VueAgile,
    AboutContact,
    AboutSkills,
    AboutYotch,
  },
  data () {
    return {
      asNavFor1: [],
      asNavFor2: [],
      asNavFor3: [],
      contentsProps: null,
      contents: [
        'about-yotch',
        'about-skills',
        'about-contact'
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
        slidesToShow: 3
      },
      options3: {
        autoplay: false,
        centerMode: false,
        dots: false,
        navButtons: false,
        slidesToShow: 1
      },
      slides: null
    }
  },
  async asyncData({ $axios }) {
    // コンテンツ子コンポーネントに渡すpropsの配列を作成
    let contentsProps = []

    // カルーセルの要素をAPIで取得
    let url = "/api/slides"
    let response = await $axios.get(url)
    let slides = response.data.slides

    // スライドに応じたpropsを生成
    let key = ''
    let title = ''

    for (let i = 0; i < slides.length; i++) {
      title = slides[i]['title']

      switch (title) {
        case 'Yotch':
          // Yotchコンテンツ用の管理情報を取得
          let yotchContents = {}
          url = '/api/informations/?type=account'
          key = 'informations'
          response = await $axios.get(url)
          yotchContents['yotch'] = response.data[key]

          // Cookingのデータを取得
          url = '/api/dishes'
          key = 'dishes'
          response = await $axios.get(url)
          yotchContents['cooking'] = response.data[key]

          // Interiorのデータを取得
          url = '/api/interiors'
          key = 'interiors'
          response = await $axios.get(url)
          yotchContents['interior'] = response.data[key]

          contentsProps.push(yotchContents)
          break
        case 'Skills':
          // Skillsコンテンツ用の管理情報を取得
          url = '/api/skills'
          key = 'skills'

          response = await $axios.get(url)
          contentsProps.push(response.data[key])
          break
        case '':
          // 連絡先等情報を取得
          url = '/api/informations'
          key = 'informations'

          response = await $axios.get(url)
          contentsProps.push(response.data[key])
          break
        default:
          url = ''
          key = ''
          contentsProps.push('')
      }
    }

    return {
      contentsProps: contentsProps,
      slides: slides
    }
  },
  methods: {
    // ページコンテンツの高さを子要素の高さに調節
    adjustContentWrapHeight (index) {
      let agileList = document.querySelector('.contents .agile__list')
      let agileSlidesRegular = document.querySelector('.contents .agile__list .agile__track .agile__slides--regular')
      agileList.style.height = this.heights[index] + 'px'
      agileSlidesRegular.style.height = this.heights[index] + 'px'
    },
    // Vue-Agileスライドの切り替え
    slidesContent (index) {
      // スライドの切り替え
      this.$refs.thumbnails.goTo(index);
      // ページコンテンツ領域の高さを子要素の高さに調整
      this.adjustContentWrapHeight(index)
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
        console.log('height iterate index is ' + i)
        height = contentsContainers[i].firstElementChild.clientHeight
        console.log(height)
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
  width: 100%;
}

.contents {
  height: auto;
}

.contents-wrap {
  padding: 50px 0 50px;
  width: 100%;
}

.fixed-width {
  margin: 0 auto;
  max-width: 1030px;
  width: 90%;
}

.slide {
  align-items: center;
  box-sizing: border-box;
  color: #fff;
  display: block;
  height: 70vh;
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
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

.slide--thumbnails:hover {
  opacity: .75;
}

.slide-title {
  font-weight: bold;
  left: 50%;
  opacity: .8;
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
  margin: 0 auto;
  width: 100%;
}

.thumbnails {
  margin: 0 auto;
  width: 100%;
}

@media screen and (max-width: 767px) {
  .main .agile__slides--regular .slide {
    height: 40vh;
  }

  .agile__slides--regular .slide--thumbnails {
    height: 10vh;
  }

  .slide-wrap {
    margin: 0;
    top: 0;
  }
}

@media screen and (min-width: 1025px) {
  .contents-wrap {
    margin-top: 50px;
    padding: 0 0 100px;
  }

  .slide-wrap {
    margin: 0 auto;
    width: 100%;
  }
}
</style>
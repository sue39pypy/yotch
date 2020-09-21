<template>
  <div class="container">
    <Heading2>Works</Heading2>

    <div class="detail-wrap">
      <ul class="work-wrap">
        <li
          v-for="(work, index) in works"
          :key="'work-' + index"
          class="work"
        >
          <a class="thumbnail" :href="work.url" target="_blank" rel="noopener noreferrer">
            <div :style="{ backgroundImage: 'url(' + work.image_path + ')' }">
            </div>
          </a>
          <div class="name-wrap">
            <h2>{{ work.name }}</h2>
          </div>
          <div class="description-wrap">
            <p
              v-for="(description, index) in work.description_converted"
              :key="'work-description-' + index">
              {{ description }}
            </p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      works: []
    }
  },
  async asyncData({ $axios }) {
    // 製作物取得API呼び出し
    let url = 'api/works'
    let response = await $axios.get(url)
    let works = response.data.works

    console.log(works)

    return {
      works: works,
    }
  },
}
</script>

<style scoped>
.container {
  margin: 0 auto;
  margin-top: 80px;
  max-width: 1030px;
  min-height: 100vh;
  width: 90%;
}

.description-wrap {
  padding: 10px;
}

.detail-wrap {
  margin: 100px auto 0;
  width: 100%;
}

.name-wrap {
  margin-top: 20px;
  text-align: center;
}

.thumbnail div {
  background-position: center;
  background-size: cover;
  height: 300px;
  width: 100%;
}

.work-wrap {
  align-content: center;
  display: flex;
  display: -ms-flexbox;
  flex-wrap: wrap;
  width: 100%;
}

.work-wrap .work {
  padding: 10px;
  width: 45%;
}

@media screen and (max-width: 767px) {
  .detail-wrap {
    margin: 60px auto 0;
  }

  .thumbnail div {
    height: 240px;
  }

  .work-wrap .work {
    width: 100%;
  }
}
</style>
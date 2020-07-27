<template>
  <div class="container">
    <ul class="wallpaper-wrap">
      <li v-for="(wallpaper, index) in wallpapers"
        class="wallpaper"
        :key="`wallpaper-${index}`"
        :style="{ backgroundImage: `url(${wallpaper.image_path})` }">
      </li>
    </ul>
    <div class="title-wrap">
      <Heading1>Y Room</Heading1>
      <p class="title-description">料理、PG、日々のあれこれ</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      wallpapers: null
    }
  },
  async asyncData ({ $axios }) {
    const url = "/api/wallpapers"
    const response = await $axios.get(url)
    return { wallpapers: response.data.wallpapers }
  }
}
</script>

<style scoped>
.container {
  align-items: center;
  display: flex;
  justify-content: center;
  margin: 0 auto;
  min-height: 100vh;
  position: relative;
  text-align: center;
}

.title-wrap {
  font-family: 'Lato', sans-serif;
  font-weight: bold;
  position: fixed;
  left: 50%;
  text-align: left;
  top: 65%;
}

.title-wrap .title-description {
  font-size: 1.6rem;
  font-weight: normal;
  margin-top: 10px;
}

.wallpaper {
  background-position: center;
  background-size: cover;
  height: 100%;
  position: absolute;
  width: 100vw;
}

.wallpaper-wrap {
  height: 100vh;
  position: relative;
  width: 100%;
}

@media screen and (max-width: 480px) {
  .title-wrap .title-description {
    font-size: 0.8rem;
    margin-top: 6px;
  }
}

@media screen and (min-width: 768px) {
  .title-wrap {
    position: absolute;
  }
}

@media screen and (max-width: 1024px) {
  .title-wrap {
    left: 5%;
  }
}

@media screen and (min-width: 1025px) {
  .title-wrap .title-description {
    font-size: 0.9rem;
  }

  .wallpaper {
    background-size: 100%;
    height: 80vh;
    left: 0;
    position: absolute;
    top: 70px;
    width: 60vh;
  }

  .wallpaper-wrap {
    margin: 0 auto;
    width: 80vw;
  }
}
</style>

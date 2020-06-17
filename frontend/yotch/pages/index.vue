<template>
  <div class="container">
    <ul class="wallpaper-wrap">
      <li v-for="(wallpaper, index) in wallpapers"
        class="wallpaper"
        :key="'wallpaper-' + index"
        :style="{ backgroundImage: 'url(' + wallpaper.image_path + ')' }">
      </li>
    </ul>
    <div class="title-wrapper">
      <p>Yotch</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  components: {
  },
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

<style>
.container {
  align-items: center;
  display: flex;
  justify-content: center;
  margin: 0 auto;
  min-height: 100vh;
  position: relative;
  text-align: center;
}

.title-wrapper {
  font-family: Century;
  font-size: 4.0rem;
  font-weight: bold;
  position: absolute;
  left: 50%;
  text-align: left;
  top: 50%;
}

.wallpaper {
  background-position: center;
  background-size: cover;
  height: 100%;
  width: 100vw;
}

.wallpaper-wrap {
  height: 100vh;
  position: relative;
  width: 100%;
}

@media screen and (min-width: 1025px) {
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

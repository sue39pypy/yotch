<template>
  <div class="container">
    <div>
      <ul>
        <li v-for="(wallpaper, index) in wallpapers"
          class="wallpaper"
          :key="'wallpaper-' + index"
          :style="{ backgroundImage: 'url(' + wallpaper.image_path + ')' }">
        </li>
      </ul>
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
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.wallpaper {
  background-position: center;
  background-size: cover;
  height: 100vh;
  width: 100vw;
}
</style>

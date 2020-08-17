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

      <div class="images-wrap">
        <div
          v-for="(interior, index) in contentProps"
          :key="'interior-' + index"
          :class="['image', 'image' + index]"
          :style="{ backgroundImage: 'url(' + interior.image_path + ')' }"
        >
          <div class="image-mask">
            {{ interior.title }}
          </div>
        </div>
      </div>
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

.image {
  background-position: center;
  background-size: cover;
}

.image0, .image1, .image2 {
  height: 450px;
  width: 33%;
}

.image3, .image4 {
  height: 300px;
  width: 50%;
}

.images-wrap {
  display: flex;
  display: -ms-flexbox;
  display: -webkit-box;
  flex-wrap: wrap;
  height: auto;
  align-content: space-between;
  width: 100%;
}

@media screen and (max-width: 767px) {
  .content-container {
    width: 90%;
  }
}
</style>
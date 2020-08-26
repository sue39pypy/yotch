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

      <ul class="dish-wrap">
        <li
          v-for="(dish, index) in contentProps"
          :key="'dish-' + index"
          :class="['dish', 'dish' + index]"
        >
          <div
            class="dish-content"
            :style="{ backgroundImage: 'url(' + dish.image_path + ')' }"
          >
            <a
              :href="dish.image_path"
              rel="noopener noreferrer"
              target="_blank"
            >
            </a>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutCooking',
  props: [
    'content',
    'contentProps'
  ],
  data () {
    return {}
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

.dish-wrap {
  display: flex;
  display: -ms-flexbox;
  display: -webkit-box;
  flex-wrap: wrap;
  margin-top: 40px;
  width: 100%;
}

.dish-wrap li {
  padding: 1px;
  width: 33%;
}

.dish-wrap li .dish-content {
  background-position: center;
  background-size: cover;
  padding-top: 100%;
  position: relative;
  width: 100%;
}

.dish-wrap li .dish-content a {
  bottom: 0;
  display: block;
  height: 100%;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  width: 100%;
}

@media screen and (max-width: 767px) {
  .content-container {
    width: 90%;
  }

  .dish-wrap li {
    padding: 1px;
  }
}
</style>
<template>
  <div class="content-container">
    <div class="detail-wrap">
      <section id="yotch-sec" class="fixed-width">
        <Heading2>{{ content.title }}</Heading2>
        <div class="description-wrap">
          <p v-for="(line, index) in content.description_converted"
            :key="'content-description-' + index"
          >
            {{ line }}
          </p>
        </div>
      </section>

      <section id="cooking-sec">
        <kv
          title="Cooking"
          :description="[
            '大学生の頃から料理をしています',
            'レパートリーの一部を見てってください'
          ]"
          image="/assets/img/cooking.jpg"
        ></kv>

        <ul class="dish-wrap fixed-width">
          <li
            v-for="(dish, index) in contentProps['cooking']"
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
      </section>

    </div>
  </div>
</template>

<script>
import Kv from '~/components/ui/Kv.vue'

export default {
  name: 'AboutYotch',
  components: {
    Kv
  },
  props: [
    'content',
    'contentProps'
  ],
  data () {
    return {
      accounts: []
    }
  }
}
</script>

<style scoped>
* {
  color: #333333;
  font-size: 0.9rem;
}

section {
  margin: 60px 0 0;
}

section:first-child {
  margin-top: 0;
}

.fixed-width {
  margin: 0 auto;
  max-width: 1030px;
  width: 90%;
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
  margin-top: 100px;
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
}

.info-row {
  display: flex;
  display: -ms-flexbox;
  margin-top: 20px;
  width: 100%;
}

.info-header {
  width: 20%;
}

.info-data {
  width: 80%;
  word-break: break-all;
}

.info-header {
  font-weight: bold;
}

.info-wrap {
  margin-top: 40px;
}

.social-wrap {
  display: flex;
  display: -ms-flexbox;
  flex-wrap: wrap;
  max-width: 300px;
  min-width: 210px;
}

.social-wrap li {
  margin-bottom: 20px;
  width: 30%;
}

.social-wrap li a i {
  font-size: 1.4rem;
}

@media screen and (max-width: 767px) {
  * {
    font-size: .9rem;
  }
  .dish-wrap {
    margin-top: 50px;
  }

  .dish-wrap li {
    padding: 1px;
  }

  .info-data {
    width: 75%;
  }

  .info-header {
    width: 25%;
  }

  .info-row {
    font-size: 1.0rem;
  }

  .social-wrap li a i {
    font-size: 1.4rem;
  }
}
</style>
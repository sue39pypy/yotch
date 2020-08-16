<template>
  <div class="content-container">
    <Heading2>{{ content.title }}</Heading2>
    <div class="detail-wrap">
      <div
        class="skill"
        v-for="(skill, index) in contentProps"
        :key="'skill-' + index"
      >
        <p class="skill-icon"><i :class="skill.icon"></i></p>
        <p class="skill-name">{{ skill.name }}</p>
        <div class="skill-level-wrap">
          <span
            class="skill-level-black"
            v-for="n of skill.level"
            :key="'level-mark-' + n"
          >
            ★
          </span>
          <span
            class="skill-level-blank"
            v-for="n of 3 - skill.level"
            :key="'skill-blank-' + n"
          >☆</span>
        </div>
        <div class="skill-caption-wrap">
          <p
            v-for="(caption, index) in skill.caption_converted"
            :key="'skill-caption-' + index"
          >
            {{ caption }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutSkills',
  props: [
    'content',
    'contentProps'
  ],
  data () {
    return {
      skills: []
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

.skill {
  padding: 12px;
  text-align: center;
  width: 33%;
}

.skill-caption-wrap {
  padding: 0 16px;
  text-align: left;
}

.skill-icon {
  font-size: 4.0rem;
}

.skill-level-wrap {
  padding: 10px;
}

.skill-name {
  font-size: 1.0rem;
}

.detail-wrap {
  align-content: center;
  display: flex;
  display: -ms-flexbox;
  flex-wrap: wrap;
  margin: 50px auto 0;
  width: 100%;
}

@media screen and (max-width: 767px) {
  .content-container {
    width: 90%;
  }
  .skill {
    width: 100%;
  }
}
</style>
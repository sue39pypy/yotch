<template>
  <div class="content-container fixed-width">
    <Heading2>{{ content.title }}</Heading2>

    <ul class="info-wrap">
      <li v-for="(information, index) in contentProps"
        :key="'information-' + index"
      >
        <a
          v-if="information.url"
          :href="information.url"
          target="_blank"
          rel="noopener noreferrer"
        >
          <i
            :class="`icon ${information.icon}`"
            :data-color="information.name.toLowerCase()"
          ></i>
        </a>
        <span v-else>
          <i
            :class="`icon ${information.icon}`"
            content="Copied!"
            :data-color="information.name.toLowerCase()"
            :data-info="information.value"
            :data-name-ja="information.name_ja"
            v-tippy="{ placement: 'top', arrow: true, trigger: 'click'}"
            @click="copyToClipboard(information.value)"
          ></i>
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'AboutContact',
  props: {
    'content': Object,
    'contentProps': Array
  },
  data () {
    return {
      interiors: null
    }
  },
  methods: {
    copyToClipboard (text) {
      this.$copyText(text)
    }
  }
}
</script>

<style scoped>
.content-container {
  margin: 0 auto;
  width: 100%;
}

.fixed-width {
  margin: 0 auto;
  max-width: 1030px;
  width: 90%;
}

a:visited {
  color: #333333;
}

ul.info-wrap {
  display: flex;
  display: -ms-flexbox;
  display: -webkit-box;
  flex-wrap: wrap;
  margin: 100px auto 0;
  width: 100%;
}

ul.info-wrap li {
  color: #333333;
  margin-bottom: 20px;
  padding: 20px;
  text-align: center;
  width: 33%;
}

ul.info-wrap li span {
  cursor: pointer;
}

ul.info-wrap li * {
  font-size: 2.8rem;
  transition: all .5s;
}

ul.info-wrap li *:hover {
  transform: translateY(-10px);
  background-color: attr(color);
}

ul.info-wrap li * i {
  transition: all .5s;
}

ul.info-wrap li *:hover i[data-color="twitter"] {
  color: #1DA1F2;
}

ul.info-wrap li *:hover i[data-color="instagram"] {
  color: #f00075;
}

ul.info-wrap li *:hover i[data-color="facebook"] {
  color: #1877f2;
}

ul.info-wrap li *:hover i[data-color="email"],
ul.info-wrap li *:hover i[data-color="github"] {
  color: #000;
}

ul.info-wrap li *:hover i[data-color="linkedin"] {
  color: #0e76a8;
}

@media screen and (max-width: 767px) {
  .content-container {
    width: 90%;
  }

  ul.info-wrap li * {
    font-size: 2.4rem;
  }
}
</style>
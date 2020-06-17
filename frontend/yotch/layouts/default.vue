<template>
  <div>
    <common-header id="header" />
    <nuxt id="nuxt-body" />
    <common-footer id="footer" />
  </div>
</template>

<script>
import CommonFooter from '~/components/layouts/Footer.vue'
import CommonHeader from '~/components/layouts/Header.vue'

export default {
  components: {
    CommonFooter,
    CommonHeader
  }
}
</script>

<style>
common-header {
  z-index: 100;
}

#header {
  z-index: 10;
}

#nuxt-body, #footer {
  z-index: 0;
}

* {
  color: #000;
}

a {
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

ul {
  list-style: none;
  padding-left: 0;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}
</style>

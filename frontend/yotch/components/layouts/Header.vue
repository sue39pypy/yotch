<template>
  <header>
    <ul class="menu-wrap">
      <li
        v-for="(menu, index) in menus"
        :key="`menu-${index}`"
        :style="{ textDecoration: menu.path === $route.path ? 'underline' : 'none' }"
      >
        <nuxt-link :to="menu.path" class="menu-link">{{ menu.title }}</nuxt-link>
      </li>
    </ul>
  </header>
</template>

<script>
export default {
  name: 'CommonHeader',
  data () {
    return {
      menus: [
        { title: 'Home', path: '/' },
        { title: 'About', path: '/about' },
        { title: 'Blog', path: '/blogs' },
        { title: 'Works', path: '/works' },
      ]
    }
  }
}
</script>

<style scoped>
* {
  color: #333;
  font-size: 1.6rem;
}

header {
  left: 0;
  padding: 28px 5% 12px;;
  position: fixed;
  top: 0;
  width: 100vw;
}

.menu-wrap {
  display: flex;
  display: -ms-flexbox;
  justify-content: flex-end;
  margin-left: auto;
}

.menu-wrap > * {
  margin-left: 60px;
  font-weight: bold;
}

@media screen and (max-width: 1024px) {
  * {
    font-size: 2.0rem;
  }

  .menu-wrap > * {
    margin-left: 40px;
  }
}

@media screen and (max-width: 768px) {
  * {
    font-size: 2.0rem;
  }

  .menu-wrap > * {
    margin-left: 40px;
  }
}

@media screen and (min-width: 768px) {
  header {
    background-color: #FFF;
  }
}

@media screen and (max-width: 480px) {
  * {
    font-size: 1.4rem;
  }

  header {
    padding: 20px 5% 5px 5%;
  }

  .menu-wrap > * {
    margin-left: 16px;
  }
}

@media screen and (max-width: 360px) {
  * {
    font-size: 1.2rem;
  }
}

@media screen and (max-width: 320px) {
  * {
    font-size: 1.0rem;
  }
}
</style>
<template>
  <header>
    <ul class="menus-wrap">
      <li v-for="(menu, index) in menus" :key="'menu-' + index">
        <a :href="menu.path" class="menu-link">{{ menu.title }}</a>
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
  font-size: 1.6rem;
}

header {
  left: 0;
  padding: 28px 5% 0;
  position: fixed;
  top: 0;
  width: 100vw;
}

.menus-wrap {
  display: flex;
  display: -ms-flexbox;
  justify-content: flex-end;
  margin-left: auto;
}

.menus-wrap > * {
  margin-left: 60px;
  font-weight: bold;
}

@media screen and (max-width: 1024px) {
  * {
    font-size: 2.0rem;
  }

  .menus-wrap > * {
    margin-left: 40px;
  }
}

@media screen and (max-width: 768px) {
  * {
    font-size: 2.0rem;
  }

  .menus-wrap > * {
    margin-left: 40px;
  }
}

@media screen and (max-width: 480px) {
  * {
    font-size: 1.4rem;
  }

  header {
    padding: 20px 5% 5px 5%;
  }

  .menus-wrap > * {
    margin-left: 16px;
  }
}
</style>
<template>
  <footer>
    <div class="footer-mask"></div>

    <div class="footer-content-wrap">
      <ul class="menu-wrap">
        <li
          v-for="(menu, index) in menus"
          :key="'footer-menu-' + index"
          :style="{ textDecoration: menu.path === $route.path ? 'underline' : 'none' }"
        >
          <nuxt-link :to="menu.path">{{ menu.title }}</nuxt-link>
        </li>
      </ul>
      <div class="address-wrap">
        <p>mail:&nbsp;{{ address }}</p>
      </div>

      <ul class="social-wrap">
        <li v-for="(social, index) in socials" :key="'social-' + index">
          <a :href="social.path" target="_blank" rel="noopener noreferrer"><i :class="'social-icon ' + social.class"></i></a>
        </li>
      </ul>

      <div class="copyright-wrap">
        <p class="copyright"><i class="far fa-copyright"></i>&nbsp;2020 Youki Yoshioka</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'CommonFooter',
  data () {
    return {
      address: 'yotch.youki.you@gmail.com',
      menus: [
        { title: 'Home', path: '/' },
        { title: 'About', path: '/about' },
        { title: 'Blog', path: '/blogs' },
        { title: 'Works', path: '/works' },
      ],
      socials: [
        { name: 'Twitter', path: 'https://twitter.com/dwde10wy', class: 'fab fa-twitter' },
        { name: 'Instagram', path: 'https://www.instagram.com/youki_pv/', class: 'fab fa-instagram' },
        { name: 'facebook', path: 'https://www.facebook.com/profile.php?id=100003161367890', class: 'fab fa-facebook-f' },
        { name: 'Github', path: 'https://github.com/sue39pypy', class: 'fab fa-github' }
      ]
    }
  }
}
</script>

<style scoped>
* {
  color: #FFF;
  font-size: 1.2rem;
}

footer {
  background-image: url("/assets/img/footer_background_image.jpg");
  background-position: 50% calc(50% - 50px);
  background-size: cover;
  height: auto;
  min-height: 280px;
  position: relative;
  width: 100vw;
  z-index: 0;
}

.footer-content-wrap {
  align-items: center;
  display: flex;
  display: -ms-flexbox;
  flex-direction: column;
  justify-content: flex-start;
  height: auto;
  left: 0;
  position: absolute;
  padding: 40px;
  top: 0;
  width: 100%;
  z-index: 10;
}

.footer-content-wrap > * {
  margin-top: 30px;
}

.footer-content-wrap > *:first-child {
  margin-top: 0;
}

.footer-mask {
  background-color: #000;
  height: 100%;
  left: 0;
  opacity: 0.5;
  position: absolute;
  top: 0;
  width: 100%;
  z-index: 1;
}

.menu-wrap {
  display: flex;
  display: -ms-flexbox;
}

.menu-wrap > * {
  border-right: solid 1px #FFF;
  padding: 0 20px;
}

.menu-wrap > *:last-child {
  border-right: none;
}

.social-icon {
  font-size: 1.6rem;
  padding: 0 20px;
}

.social-wrap {
  display: flex;
  display: -ms-flexbox;
}

@media screen and (max-width: 480px) {
  * {
    font-size: 1.0rem;
  }

  .social-icon {
    font-size: 1.4rem;
  }
}

@media screen and (max-width: 1024px) {
  footer {
    background-position: center;
  }
}
</style>
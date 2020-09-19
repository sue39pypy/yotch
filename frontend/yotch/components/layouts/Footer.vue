<template>
  <footer>
    <div class="footer-mask"></div>

    <div class="footer-content-wrap">
      <arrow />
      <ul class="menu-wrap">
        <li
          v-for="(menu, index) in menus"
          :key="`footer-menu-${index}`"
          :style="{ textDecoration: menu.path === $route.path ? 'underline' : 'none' }"
        >
          <nuxt-link :to="menu.path">{{ menu.title }}</nuxt-link>
        </li>
      </ul>
      <div class="address-wrap">
        <p><i class="fas fa-envelope"></i>&nbsp;{{ address }}</p>
      </div>

      <ul class="social-wrap">
        <li v-for="(account, index) in accounts" :key="`social-${index}`">
          <a :href="account.url" target="_blank" rel="noopener noreferrer"><i :class="`social-icon ${account.icon}`"></i></a>
        </li>
      </ul>

      <div class="copyright-wrap">
        <p class="copyright"><i class="far fa-copyright"></i>&nbsp;2020 Youki Yoshioka</p>
      </div>
    </div>
  </footer>
</template>

<script>
import { mapGetters } from 'vuex'

import Arrow from '~/components/ui/Arrow.vue'

export default {
  name: 'CommonFooter',
  components: {
    Arrow
  },
  data () {
    return {
      address: 'yotch.youki.you@gmail.com',
      menus: [
        { title: 'Home', path: '/' },
        { title: 'About', path: '/about' },
        { title: 'Blog', path: '/blogs' },
        { title: 'Works', path: '/works' },
      ],
      accounts: []
    }
  },
  computed: {
    ...mapGetters('information', [
      'getAccounts',
      'getProfile'
    ])
  },
  created () {
    // storeからアカウント情報を取得
    this.accounts = this.getAccounts
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
  min-height: 305px;
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
  padding: 10px 40px 40px;
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

  .menu-wrap > * {
    padding: 0 10px;
  }

  .social-icon {
    font-size: 1.4rem;
    padding: 0 10px;
  }
}

@media screen and (max-width: 1024px) {
  footer {
    background-position: center;
  }
}
</style>
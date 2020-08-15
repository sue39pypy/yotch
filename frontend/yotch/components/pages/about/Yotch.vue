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
      <div class="info-wrap">
        <div class="info-row">
          <div class="info-header">生年月日：</div>
          <div class="info-data">
            1991/5/23
          </div>
        </div>

        <div class="info-row">
          <div class="info-header">主な職歴：</div>
          <div class="info-data">
            <p>B2G SE</p>
            <p>シンクタンク系コンサルタント</p>
            <p>B2B SE</p>
          </div>
        </div>

        <div class="info-row">
          <div class="info-header">趣味：</div>
          <div class="info-data">
            プログラミング、料理、ジョギング、カラオケ、ギター、アニメ、漫画、コーヒーetc
          </div>
        </div>

        <div class="info-row">
          <div class="info-header">各種SNS：</div>
          <div class="info-data">
            <ul class="social-wrap">
              <li v-for="(account, index) in accounts" :key="`account-${index}`">
                <a :href="account.url" target="_blank" rel="noopener noreferrer"><i :class="`social-icon ${account.icon}`"></i></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutYotch',
  props: [
    'content'
  ],
  data () {
    return {
      accounts: [
        { service_name: 'Twitter', url: 'https://twitter.com/dwde10wy', icon: 'fab fa-twitter' },
        { service_name: 'Instagram', url: 'https://www.instagram.com/youki_pv/', icon: 'fab fa-instagram' },
        { service_name: 'facebook', url: 'https://www.facebook.com/profile.php?id=100003161367890', icon: 'fab fa-facebook-f' },
        { service_name: 'Github', url: 'https://github.com/sue39pypy', icon: 'fab fa-github' },
        { service_name: 'Spotify', url: 'https://open.spotify.com/user/1onk9oj4f2zdl1ol45yitessp', icon: 'fab fa-spotify' },
        { service_name: 'LinkedIn', url: 'https://www.linkedin.com/in/%E6%B9%A7%E7%94%9F-%E5%90%89%E5%B2%A1-4616051a9/', icon: 'fab fa-linkedin' }
      ]
    }
  }
}
</script>

<style scoped>
* {
  color: #333333;
  font-size: 0.9rem;
}

.content-container {
  margin: 0 auto;
  width: 100%;
}

.description-wrap {
  margin-top: 40px;
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

.info-wrap {
  font-weight: bold;
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
  .content-container {
    width: 90%;
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
<template>
  <div class="contents-container">
    <Heading2>Yotch</Heading2>
    <div class="content-wrap">
      <div class="description-wrap">
        <p>広島でPGをしています。</p>
        <p>これまでの業務の中で、行政システムの保守・改修やコンサルタント、webサイト製作を担当してきました。</p>
        <p>現在は主にwebアプリケーションの開発業務に従事しています。</p>
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
              <li v-for="(social, index) in socials" :key="`social-${index}`">
                <a :href="social.path" target="_blank" rel="noopener noreferrer"><i :class="`social-icon ${social.class}`"></i></a>
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
  data () {
    return {
      socials: [
        { name: 'Twitter', path: 'https://twitter.com/dwde10wy', class: 'fab fa-twitter' },
        { name: 'Instagram', path: 'https://www.instagram.com/youki_pv/', class: 'fab fa-instagram' },
        { name: 'facebook', path: 'https://www.facebook.com/profile.php?id=100003161367890', class: 'fab fa-facebook-f' },
        { name: 'Github', path: 'https://github.com/sue39pypy', class: 'fab fa-github' },
        { name: 'Spotify', path: 'https://open.spotify.com/user/1onk9oj4f2zdl1ol45yitessp', class: 'fab fa-spotify' },
        { name: 'LinkedIn', path: 'https://www.linkedin.com/in/%E6%B9%A7%E7%94%9F-%E5%90%89%E5%B2%A1-4616051a9/', class: 'fab fa-linkedin' }
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

.contents-container {
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
  .contents-container {
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
    font-size: 1.6rem;
  }
}
</style>
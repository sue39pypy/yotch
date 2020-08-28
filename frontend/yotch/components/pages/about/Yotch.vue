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
              <li v-for="(account, index) in contentProps" :key="`account-${index}`">
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
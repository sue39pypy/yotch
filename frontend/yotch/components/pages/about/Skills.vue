<template>
  <div class="contents-container">
    <Heading2>Skills</Heading2>
    <div class="skills-wrap">
      <div
        class="skill"
        v-for="(skill, index) in skills"
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
          <p>{{ skill.caption }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutSkills',
  data () {
    return {
      skills: [
        { name: 'Javascript', icon: 'fab fa-js', level: 2, caption: 'Vue.js、Nuxt.js、jQueryによる開発案件にアサインしてきました。当サイトはNuxt.jsでフロントエンドを構築しています。' },
        { name: 'PHP', icon: 'fab fa-php', level: 2, caption: '現職にてFuelPHPによる開発を日常的に行っていて、たまにWordpressで独自テーマを作ったりしています。Laravelを学習中。' },
        { name: 'Python', icon: 'fab fa-python', level: 2, caption: '個人開発では専らDjangoを用いています。当サイトのバックエンドもDjangoにより構築しています。機械学習の勉強中。' },
        { name: 'HTML5&CSS3', icon: 'fab fa-html5', level: 2, caption: '一つ前の会社ではフロントエンドを書くことが多かったので一通り書けます。' },
        { name: 'SQL', icon: 'fas fa-database', level: 2, caption: '業務および個人開発では主にMySQL（5.6、5.7、8系）を使用しています。現在は生のSQLを書く機会は減りましたが、前職まではストアドプロシージャの実装やチューニング等行っていました。' },
        { name: 'Git', icon: 'fab fa-git', level: 2, caption: '現職にてソース管理にGitを用いているため、基本的なことは抑えています。' },
        { name: 'Docker', icon: 'fab fa-docker', level: 1, caption: '現職にて環境構築に利用しています。当サイトもDockerを用いています。基本的なことに関しては理解しています。' },
        { name: 'VBA', icon: 'fas fa-file-excel', level: 3, caption: 'GUIの作成やマクロの実装等、割と何でもできます。コンサル時代は社内SEもしていて、自動化による業務の効率化を行ったりしていました。' }
      ]
    }
  }
}
</script>

<style scoped>
* {
  color: #333333;
}

.contents-container {
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

.skills-wrap {
  align-content: center;
  display: flex;
  display: -ms-flexbox;
  flex-wrap: wrap;
  margin: 50px auto 0;
  width: 100%;
}

@media screen and (max-width: 767px) {
  .contents-container {
    width: 90%;
  }
  .skill {
    width: 100%;
  }
}
</style>
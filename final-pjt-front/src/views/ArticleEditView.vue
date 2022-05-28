<template>
  <div id="main">
    <div id="title">게시글 수정</div>
    <article-form v-if="isArticle" :article="article" action="수정하기">
    </article-form>
  </div>

</template>

<script>
import ArticleForm from '@/components/community/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'AritcleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle',])
    },
    methods: {
      ...mapActions(['fetchArticle'])
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    },
  }
</script>

<style scoped>

  #title {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 50px;
    margin: 80px 30px 80px 150px;
  }

  #main {
    margin-bottom: 100px;
  }

</style>

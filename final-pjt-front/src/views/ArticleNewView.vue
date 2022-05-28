<template>
  <div id="main">
    <div id="title">게시글 작성</div>
    <!-- <h1>New Article</h1> -->
    <article-form :article="article" action="작성하기"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/community/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>
  
<style scoped>

  #main {
    margin-bottom: 100px;
  }

  #title {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 50px;
    margin: 80px 30px 80px 150px;
  }
</style>

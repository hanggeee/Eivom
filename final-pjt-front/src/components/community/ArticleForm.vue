<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <div class="input">
        <input class="title_input" v-model="newArticle.title" type="text" id="title" placeholder="제목을 입력하세요."/>
      </div>
      <div id="content">
        <textarea class="content_input" v-model="newArticle.content" type="text" placeholder="내용을 입력하세요."></textarea>
        <div class="text-end"><button class="yp-btn yp-btn-white">{{ action }}</button></div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === '작성하기') {
          this.createArticle(this.newArticle)
        } else if (this.action === '수정하기') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style scoped>
  .container {
    background-color: #fff6ea;
    margin-top: 1rem;
    border-radius: 10px;
    height: 800px;
  }
  .input{
    display:flex;
    justify-content: space-between;
    align-items: center;
  }

  .title_input {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 18px;
  font-weight: 500;

  width: 100%;
  border: 2px solid #d5d5d5;
  background-color: white;
  border-radius: 5px;
  padding: 0.6rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
  padding-left: 1.5rem;
  outline: none;
  }

  #content {
    background-color: white;
    border: 2px solid #d5d5d5;
    height: 700px;
    border-radius: 5px;
  }

  textarea {
    font-family: 'Noto Sans KR', sans-serif;
    width: 100%;
    border: none;
    border-radius: 4px;
    font-size: 18px;
    font-weight: 500;
    height: 610px;
    padding: 0.6rem;
    margin-top: 10px;
    margin-right: 0.5rem;
    margin-bottom: 1rem;
    padding-right: 2rem;
    padding-left: 1.6rem;
    outline: none;
    resize: none;
  }

  button {
    margin-right: 60px;
    background-color: rgba(0, 0, 0, 0);
    border: 0px;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 18px;
    font-weight: 500;
    color: rgb(124, 124, 124);

  }

</style>

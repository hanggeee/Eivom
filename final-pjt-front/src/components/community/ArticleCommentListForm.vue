<template>
  <div>


    <div id="form">
      <div class="in_form_margin">
        <div>
          {{ currentUser.username }}
        </div>
        <form @submit.prevent="onSubmit">
          <div class="d-flex">
            <textarea name="" id="comment" v-model="content" placeholder="댓글을 달아주세요" required></textarea>
              <!-- <input type="text" id="comment" v-model="content" placeholder="댓글을 달아주세요" required> -->
            <button id="sub" style="margin-top: 70px">등록</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ArticleCommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article', 'currentUser']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style scoped>

  #form {
    border: 2px solid rgb(216, 216, 216);
    height: 150px;
    border-radius: 6px;
  }

  textarea {
    height: 70px;
    width: 200%;
    outline: none;
    border: none;
    resize: none;
  }

  #sub {
    width: 100px;
    border: none;
    background-color: rgba(255, 255, 255, 0);
    color: rgb(157, 157, 157);
    font-size: 0.8em;
  }

  .in_form_margin {
    margin: 15px 10px 10px 20px;
  }
</style>
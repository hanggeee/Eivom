<template>
  <div id="comment-list-item">
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <a :href="`http://localhost:8080/profile/${ comment.user.username }`">
          <img v-if="comment.user.profile_img" :src="comment.user.profile_img" alt="profile_img" class="profile_img">
          <img v-else class="profile_img" src="@/assets/default_profile.jpg">
        </a>
        <div id="comment_info">
          <div class="d-flex">
            <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
              <div>{{ comment.user.username }}</div>
            </router-link> 

            <div id="comment_edit" v-if="currentUser.username === comment.user.username && !isEditing">
              <button @click="switchIsEditing">수정</button>
              <button @click="deleteComment(payload)">삭제</button>
            </div>
          </div>
          <div class="divfont" v-if="!isEditing">{{ payload.content }} </div>
          <div id="editing" v-if="isEditing">
            <div class="d-flex">
              <input type="text" v-model="payload.content">
              <div>
                <button @click="onUpdate">수정</button>
                <button @click="switchIsEditing">취소</button>
              </div>
            </div>
          </div>
        </div>


      </div>
      <p>{{ comment.updated_at }}</p>
    </div>
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'article_comment_item',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }

  #comment-list-item {
    margin: 10px 10px 10px 10px;
  }

  hr {
    margin: 7px 0px 7px 0px;
    color: rgb(212, 212, 212);
  }

  .divfont {
    font-weight: 400;
    font-size: 15px;
  }

  img {
    width: 50px;
    height: 50px;
    border-radius: 100%;
  }

  a {
    text-decoration: none;
    color: black;
  }

  #comment_info {
    margin: 0px 10px 0px 10px;
  }

  #comment_edit {
    display: flex;
    align-items: center;
    margin-left: 15px;
  }

  #comment_edit > button {
    padding: 0 0 0 0;
    border: none;
    background-color: rgba(0, 0, 0, 0);
    font-size: 10px;
    color: rgb(194, 194, 194);
    margin: 0 0 0 10px;
  }

  #editing > div > input {
    border: none;
    background-color: rgba(0, 0, 0, 0);
    font-size: 15px;
    font-weight: 400;
    /* height: 25px; */
    width: 300px;
  }
  #editing > div > input:focus {
    border: none;
    background-color: rgba(0, 0, 0, 0);
    font-size: 15px;
    font-weight: 400;
    /* height: 25px; */
    width: 300px;
    outline: none;
  }

  #editing > div {
    border: 1px solid rgb(165, 165, 165);
    border-radius: 3px;
    font-size: 15px;
    font-weight: 400;
    height: 30px;
    width: 375px;
  }

  #editing > div > div > button {
    border: none;
    background-color: rgba(0, 0, 0, 0);
    border-radius: 3px;
    margin-top: 0px;
    font-size: 12px;
    font-weight: 500;
    color: rgb(136, 136, 136);
  }

    /* 버튼 css */
    /* Buttons */
  
  #sub,
  #sub:hover,
  #sub:focus,
  #sub:active {
    color: rgb(0, 0, 0);
    text-decoration: none;
    outline: none;
    background-color: rgb(255, 255, 255);
    border-radius: 5px;
  }

  #sub {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
    position: relative;
    height: 40px;
    width: 90px;
    z-index: 1;
  }

  #sub:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    /* border: 2px solid #fff; */
    border-radius: 5px;
    z-index: -1;
    /* transform: skew(-6deg); */
    background: none;
    transition: 0.3s background ease, 0.3s border ease;
  }

  .yp-btn,
  .yp-btn:hover,
  .yp-btn:focus,
  .yp-btn:active {
    color: rgb(0, 0, 0);
    text-decoration: none;
    outline: none;
    background-color: rgb(255, 255, 255);
    border-radius: 5px;
    border: 1.5px solid rgb(9, 9, 56);
  }

  .yp-btn {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
    position: relative;
    height: 30px;
    width: 80px;
    z-index: 1;
  }
  .yp-btn.yp-btn-xs {
    padding: 4px 15px;
  }
  .yp-btn.yp-btn-sm {
    padding: 8px 20px;
  }
  .yp-btn.yp-btn-md {
    padding: 15px 40px;
  }
  .yp-btn.yp-btn-lg {
    padding: 15px 50px;
  }
  .yp-btn.yp-btn-full {
    margin-left: 0;
    margin-right: 0;
    width: 100%;
  }
  .yp-btn:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    /* border: 2px solid #fff; */
    border-radius: 5px;
    z-index: -1;
    /* transform: skew(-6deg); */
    background: none;
    transition: 0.3s background ease, 0.3s border ease;
  }


  .yp-btn-white:hover,
  .yp-btn-white:focus,
  .yp-btn-white.focus,
  .yp-btn-white:active,
  .yp-btn-white.active {
    color: rgb(0, 0, 0);
    border: 1px solid #fff;
  }
  .yp-btn-white:hover:before,
  .yp-btn-white:focus:before,
  .yp-btn-white.focus:before,
  .yp-btn-white:active:before,
  .yp-btn-white.active:before {
    /* border: 1px solid #fff; */
    border-radius: 5px;
    background: #FFD2E2;
  }

  input:checked + label {
    background: #FFD2E2;
    border-radius: 5px;
    color: black;
  }

  label {
    display: flex;
    justify-content: center;
    align-items: center;
    -webkit-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
    user-select:none;
    cursor: pointer;
  }
</style>
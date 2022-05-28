<template>
  <div>
    <div id="comment">
      <!-- <div class="d-flex">
        <img src="@/assets/director1.jpg" alt="">
        <div>영화 댓글</div>
      </div> -->
      <div class="d-flex justify-content-between">
        <div class="d-flex">
          <a id="a_img" :href="`http://localhost:8080/profile/${comment.user.username}`">
            <div class="box" style="background: #BDBDBD;">
              <img v-if="comment.user.profile_img" :src="comment.user.profile_img" alt="profile_img" class="profile_img">
              <img v-else class="profile_img" src="@/assets/default_profile.jpg">
            </div>
          </a>
          <div class="ms-3">
            <div class="d-flex">
              <a :href="`http://localhost:8080/profile/${comment.user.username}`"><div>{{ comment.user.username }}</div></a>
              <div v-if="currentUser.username == comment.user.username" class="d-flex" style="margin-left:10px;">
                <button v-if="!isEditing" @click="switchIsEditing">수정</button>
                <button v-if="isEditing" @click="onUpdate; add()">업데이트</button>
                <button @click="delete_movie_Comment(payload); add()">삭제</button>
                <button v-if="isEditing" @click="switchIsEditing">취소</button>
              </div>
            </div>
            <div v-if="!isEditing">{{ payload.content }}</div>
            <span v-if="isEditing">
              <input type="text" v-model="payload.content">
            </span>
          </div>
        </div>
        <div class="d-flex">
          <div>
            <div id="star" class="text-end">{{ counting_star }}</div>
            <div>{{ comment.updated_at }}</div>
          </div>
        </div>
      </div>
    </div>


  </div>
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'movie_comment_item',
  props:{
    comment: Object,
  },
  data: function(){
    return {
      isEditing: false,
      payload: {
        moviePk: this.comment.movie,
        commentPk: this.comment.id,
        content: this.comment.content
      },
      num: 0,
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    counting_star() {
      return `★`.repeat(this.comment.rate)
    },
    profile_img() {
      return this.comment.profile_img
    }
  },
  methods: {
    ...mapActions(['delete_movie_Comment', 'update_movie_Comment' ]),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.update_movie_Comment(this.payload)
      this.isEditing = false
    },
    add(){
      this.num = this.num + 1
    }
  },
  watch: {
    "num" () {
      location.reload()
      
    },
  }
}
</script>

<style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

  #comment {
    margin: 10px 10px 10px 10px;
    padding: 10px 20px 10px 10px;
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 1.5rem;
    font-weight: 500;
    border-radius: 5px;
    background-color:	#ffffff;
    /* border-bottom: 1.5px solid #bcbcbc; */
  }

  .box {
      width: 65px;
      height: 65px; 
      margin: 5px;
      border-radius: 70%;
      overflow: hidden;
  }
  .profile {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }

  img {
    width: 65px;
    height: 65px;
    border-radius: 70%;
  }
  #star {
    color: rgb(250, 187, 0);
  }

  button {
    border: none;
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 0.9rem;
    font-weight: 300;
    background-color: rgba(255, 255, 255, 0);
    color: #acacac;
    margin-right: 5px
  }

  a {
    text-decoration: none;
    color: rgb(0, 0, 0);
  }
  
  #a_img {
    border-radius: 70%;
    overflow: hidden;
  }
</style>
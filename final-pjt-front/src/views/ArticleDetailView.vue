<template>
  <div id="b_color">
    <div style="height: 50px;"></div>
    <div class="container appdetail">
      <div class="margin">
      <div class="article_logo display-5">
        게시글
      </div>
        <div class="d-flex justify-content-between align-items-end">
          <div id="title">{{ article.title }}</div>
          <div>
            <div v-if="isAuthor">
              <div id="dropstart" class="dropstart">
                <button type="button" data-bs-toggle="dropdown"><i class="fa-solid fa-ellipsis-vertical"></i></button>
                <ul class="dropdown-menu">
                  <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
                    <div class="dropdown-item">
                      <button class="drop_in_button">게시글 수정</button>
                    </div>
                  </router-link>
                  <div class="dropdown-item" @click="deleteArticle(articlePk)" style="cursor: pointer;">
                    <button class="drop_in_button">게시글 삭제</button>
                  </div>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <hr>
          <div class="d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center">
              <div>
                <a :href="`http://localhost:8080/profile/${article.user.username}`">
                  <img v-if="article.user.profile_img" :src="article.user.profile_img" alt="profile_img" class="profile_img">
                  <img v-else class="profile_img" src="@/assets/default_profile.jpg">
                </a>
              </div>
              <div>
                <a :href="`http://localhost:8080/profile/${article.user.username}`"><div id="article_writer">{{ article.user.username }}</div></a>
                <div class="d-flex" id="create_update_at">
                  <div>작성일 {{ article.created_at }}</div>
                  <div style="font-size:10px">|</div>
                  <div>수정일 {{ article.updated_at }}</div>
                </div>
              </div>
            </div>
            <div>
              <div id="side_like" class="likecomment">
                <div><i class="fa-regular fa-heart" style="color:red;"></i>&nbsp;</div>
                <span>좋아요 {{ likeCount }}</span><div>&nbsp;&nbsp;&nbsp;</div>
                <div>
                  <i class="fa-regular fa-comment"></i>
                  댓글 {{ article.comments.length }}
                </div>
              </div>
            </div>
          </div>
        <hr>
        <div id="article_content">{{ article.content }}</div>

        <!-- Article Like UI -->
        <div class="d-flex align-items-center">
          <button v-if="articleLiking" class="btn btn-link shadow-none" style="color:crimson; font-size:25px;"
            @click="likeArticle(articlePk)"
          ><i class="fa-solid fa-heart" style="font-size: 23px"></i></button>
          <button v-else class="btn btn-link shadow-none" style="color:crimson; font-size:25px;"
            @click="likeArticle(articlePk)"
          ><i class="fa-regular fa-heart" style="font-size: 23px"></i></button>
          <!-- {{ article.article_like }} -->
          <div class="likecomment">
            <span>좋아요 {{ likeCount }}</span><div>&nbsp;&nbsp;&nbsp;</div>
            <div>
              <i class="fa-regular fa-comment"></i>
              댓글 {{ article.comments.length }}
            </div>
          </div>
        </div>
        <hr>
        <div id="comment_entry">댓글</div>
        <!-- Comment UI -->
        <div id="article_comment_list">
          <article-comment-list :comments="article.comments"></article-comment-list>
        </div>
        <div class="text-end" style="margin-right: 20px;">
          <router-link :to="{ name: 'community' }">
            <button class="yp-btn yp-btn-white">목록</button>
          </router-link>
        </div>
        <div style="height: 100px"></div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ArticleCommentList from '@/components/community/ArticleCommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { ArticleCommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'articleLiking', 'currentUser']),
      likeCount() {
        return this.article.article_like?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';

  #b_color {
    background-color: RGB(242, 240, 240); 
  }

  .article_logo {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    color: #1d1d1f;
    /* padding-left: 4%; */
    padding-top: 5%;
    padding-bottom: 50px;
    /* left: 20%;
    top: 10%; */
  }

  hr {
    margin: 5px 0px 5px 0px;
  }

  #title {
    font-size: 30px;
    font-weight: 500;
    letter-spacing: 1px;
  }
  
  a {
    text-decoration: none;
    color: black;
  }

  #article_writer {
    font-size: 23px;
  }

  #create_update_at > div {
    font-size: 12px;
    font-weight: 400;
    margin-right: 10px;
    color: #aeaeae;
  }

  #article_content {
    font-size: 20px;
    font-weight: 400;
    margin: 20px 20px 20px 20px;
  }

  #side_like {
    font-size: 15px;
  }

  #comment_entry {
    font-size: 25px;
    font-weight: 600;
    margin: 10px 10px 10px 10px;
  }

  #article_comment_list {
    margin: 10px 20px 10px 20px;
  }

  #dropstart > button {
    border: none;
    background-color: rgba(255, 255, 255, 0);
    color: rgb(133, 133, 133)
  }

  .drop_in_button {
    border: none;
    background-color: rgba(255, 255, 255, 0);
    font-size: 15px;
  }

  .dropdown-item:active {
    background-color: #d0d0d0 !important;
  }
  

  * {
      font-family: 'Noto Sans KR',  sans-serif;
      font-weight: 500;
  }

  .appdetail{
    background-color: #ffffff;
  }

  .margin {
    margin: 25px;
  }

  .profile_img {
    margin: 10px 10px 10px 10px;
    width: 50px;
    height: 50px;
    border-radius: 70%;
  }

  .userinfo {
    display: flex;
    flex-direction: column;
  }

  .likecomment {
    display: flex;
    /* width: 150px; */
    justify-content: space-between;
  }

  img {
    margin-right: 5px;
  }

  .button {
    margin:10px;
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
    border: 2px solid rgb(192, 192, 192);
  }

  .yp-btn {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
    font-size: 15px;
    position: relative;
    height: 35px;
    width: 45px;
    z-index: 1;
  }

  .yp-btn:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    /* border: 2px solid #fff; */
    border-radius: 3px;
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
    background: #b2b2b2;
  }

</style>

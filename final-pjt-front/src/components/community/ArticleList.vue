<template>
  <div class="haha">
    <div class="community d-flex justify-content-between">
      <h1>커뮤니티</h1>
      <router-link :to="{ name: 'articleNew' }">
        <button class="yp-btn yp-btn-white">게시글 작성</button>
      </router-link>
    </div>
    <div class="board">
      <table>
          <thead class="board__header">
            <tr>
              <th class="board__header__row" style="width: 4rem">번호</th>
              <th class="board__header__row">제목</th>
              <th class="board__header__row" style="width: 10rem">글쓴이</th>
              <th class="board__header__row" style="width: 8rem">작성일</th>
              <!-- <th class="board__header__row" style="width: 4rem">조회수</th> -->
            </tr>
          </thead>

          <tbody
          v-for="article in articles"
          :key="article.pk"
          class="board__body"
          >
            <tr>
              <td class="board__body__row">{{ article.pk }}</td>
              <router-link :to="{ name: 'article', params : { articlePk: article.pk} }">
                <td class="board__body__row hover">
                  {{ article.title }} <span style="color: #EE3B3B">[{{ article.comments.length }}]</span>
                  <!-- <span class="board__comment"
                    >[{{ article.comments_count }}]</span -->
                  
                </td>
              </router-link>
              <td class="board__body__row">
                <router-link :to="{ name: 'profile', params: { username: article.user.username } }">
                  {{ article.user.username }}
                </router-link> 
              </td>
              <td class="board__body__row">
                {{ article.created_at }}
              </td>
              <!-- <td class="board__body__row">{{ article.post_hit }}</td> -->
            </tr>
          </tbody>
      </table>
    </div>



    <!-- <div class="d-flex justify-content-center">
      <pagination></pagination>
    </div> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
// import Pagination from '@/components/community/Pagination.vue'
export default { 
  name: "article_list",
  components: {
    // Pagination
  },
  methods: {
    ...mapActions(['fetchArticles']),
  },
  computed: {
    ...mapGetters(['articles'])
  },
  created() {
    this.fetchArticles()
  },
  
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  
  table {
    font-family: 'Noto Sans KR',  sans-serif !important;
    width: 900px;
  }
  .haha{
    width: 50vw;
  }
  a {
    text-decoration: none;
    color: black;
    margin: 0 0 0 0;
    padding: 0 0 0 0;
  }
  .community {
    min-width: 400px;
    margin: 70px 30px 50px 30px;

  }

  .community > h1 {
    font-size: 55px;
    font-weight: 700;
  }

  #commu {
    height: 100%;
    width: 60rem;
  }


  table {
    min-width: 420px;
    box-shadow: 1px 2px 3px 2px rgba(0, 0, 0, 0.275);
    border-radius: 6px;
    overflow: hidden;
    width: 50vw;
    /* height: 100%; */

  }

  .board__header {
    background-color: #fff6ea;
    color: var(--board-header-text);
  }

  .board__header__row {
    padding: 0.5rem;
    text-align: center;
    font-size: 16px;
    font-weight: 700;
  }
  .board__body {
    background-color: var(--board-body);
    /* color: gray; */
    border-top: 2px solid #f2f2f2;
  }
  .board__body__row {
    padding: 0.5rem;
    font-size: 16px;
    text-align: center;
    font-weight: 400;
    /* border-left: 1px solid #f2f2f2; */
  }
  /* th:nth-child(2) {
    width: 100%;
  } */
  /* --------버튼-------- */
  /*---------------------------------------------------- */
  /* 버튼 css */
    /* Buttons */

  .yp-btn,
  .yp-btn:hover,
  .yp-btn:focus,
  .yp-btn:active {
    color: rgb(0, 0, 0);
    text-decoration: none;
    outline: none;
    background-color: rgb(255, 255, 255);
    border-radius: 50px;
    border: 2px solid rgb(150, 150, 150);
  }

  .yp-btn {
    top: 15px;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: 20px;
    position: relative;
    height: 50px;
    width: 170px;
    z-index: 1;
    box-shadow: 1px 3px 6px 1px rgba(0, 0, 0, 0.198);
    
  }

  .yp-btn:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 50px;
    z-index: -1;
    background: none;
    transition: 0.7s background ease, 0.7s border ease;
  }

  .yp-btn-white:hover,
  .yp-btn-white:focus,
  .yp-btn-white.focus,
  .yp-btn-white:active,
  .yp-btn-white.active {
    color: rgb(0, 0, 0);
    border: 1px solid rgb(150, 150, 150);
  }
  .yp-btn-white:hover:before,
  .yp-btn-white:focus:before,
  .yp-btn-white.focus:before,
  .yp-btn-white:active:before,
  .yp-btn-white.active:before {
    border: 1px solid rgb(150, 150, 150);
    border-radius: 50px;
    background: rgb(255, 241, 212);
  }

</style>
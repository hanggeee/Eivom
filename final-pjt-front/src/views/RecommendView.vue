<template>
  <div class="app6">

    <section class="timeline">
      <ul>
        <li>
          <div>
            <time>인사</time>
            <p class="question">어서오세요!</p>
            <p class="question">Eivom에 오신걸 환영합니다</p>
            <p class="question">간단한 질문 후에 영화를 추천해 드리겠습니다.</p>
          </div>
        </li>
        <li>
          <div>
            <time>장르</time>
            <p class="question">어떤 장르가 있었으면 좋겠나요?</p>
            <buttons id="genres" class="d-flex" style="height:100px;">
              <com class="row">
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="action1" value=28 v-model="with_genres">
                  <label for="action1" class="yp-btn yp-btn-white">액션</label>
                  <input type="checkbox" id="animation1" value=16 v-model="with_genres">
                  <label for="animation1" class="yp-btn yp-btn-white">애니메이션</label>
                  <input type="checkbox" id="comedy1" value=35 v-model="with_genres">
                  <label for="comedy1" class="yp-btn yp-btn-white">코미디</label>
                  <input type="checkbox" id="drama1" value=18 v-model="with_genres">
                  <label for="drama1" class="yp-btn yp-btn-white">드라마</label>
                </com>
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="fantasy1" value=14 v-model="with_genres">
                  <label for="fantasy1" class="yp-btn yp-btn-white">판타지</label>
                  <input type="checkbox" id="romance1" value=10749 v-model="with_genres">
                  <label for="romance1" class="yp-btn yp-btn-white">로맨스</label>
                  <input type="checkbox" id="SF1" value=878 v-model="with_genres">
                  <label for="SF1" class="yp-btn yp-btn-white">SF</label>
                  <input type="checkbox" id="thriller1" value=53 v-model="with_genres">
                  <label for="thriller1" class="yp-btn yp-btn-white">스릴러</label>
                </com>
              </com>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <time>장르</time>
            <p class="question">싫어하는 장르가 있나요?</p>
            <buttons id="genres" class="d-flex" style="height:100px;">
              <com class="row">
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="action2" value=28 v-model="without_genres">
                  <label for="action2" class="yp-btn yp-btn-white">액션</label>
                  <input type="checkbox" id="animation2" value=16 v-model="without_genres">
                  <label for="animation2" class="yp-btn yp-btn-white">애니메이션</label>
                  <input type="checkbox" id="comedy2" value=35 v-model="without_genres">
                  <label for="comedy2" class="yp-btn yp-btn-white">코미디</label>
                  <input type="checkbox" id="drama2" value=18 v-model="without_genres">
                  <label for="drama2" class="yp-btn yp-btn-white">드라마</label>
                </com>
                <com class="d-flex justify-content-around align-items-center">
                  <input type="checkbox" id="fantasy2" value=14 v-model="without_genres">
                  <label for="fantasy2" class="yp-btn yp-btn-white">판타지</label>
                  <input type="checkbox" id="romance2" value=10749 v-model="without_genres">
                  <label for="romance2" class="yp-btn yp-btn-white">로맨스</label>
                  <input type="checkbox" id="SF2" value=878 v-model="without_genres">
                  <label for="SF2" class="yp-btn yp-btn-white">SF</label>
                  <input type="checkbox" id="thriller2" value=53 v-model="without_genres">
                  <label for="thriller2" class="yp-btn yp-btn-white">스릴러</label>
                </com>
              </com>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <time>옛 영화</time>
            <p class="question">옛날 영화도 좋아하시나요?</p>
            <buttons id="genres" class="d-flex" style="height:50px;">
              <input name="rel" type="radio" id="yes_rel" v-model="primary_release_date_gte" value="2000" />
              <label for="yes_rel" class="yp-btn yp-btn-white">네</label>
              <input name="rel" type="radio" id="no_rel" v-model="primary_release_date_gte" value="2010" />
              <label for="no_rel" class="yp-btn yp-btn-white">아니요</label>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <time>유명도</time>
            <p class="question">유명한 영화 위주로 찾을까요?</p>
            <buttons id="genres" class="d-flex" style="height:50px;">
              <input name="pop" type="radio" id="yes_pop" v-model="sort_by" value="popularity_asc" />
              <label for="yes_pop" class="yp-btn yp-btn-white">네</label>
              <input name="pop" type="radio" id="no_pop" v-model="sort_by" value="popularity_desc" />
              <label for="no_pop" class="yp-btn yp-btn-white">아니요</label>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <time>연령</time>
            <p class="question">성인 영화도 포함할까요?</p>
            <buttons id="genres" class="d-flex" style="height:50px;">
              <input name="age" type="radio" id="yes_age" v-model="include_adult" value="true" />
              <label for="yes_age" class="yp-btn yp-btn-white">네..!</label>
              <input name="age" type="radio" id="no_age" v-model="include_adult" value="false" />
              <label for="no_age" class="yp-btn yp-btn-white">아니요</label>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <time>평점</time>
            <p class="question">평점이 좋은 영화 위주로 찾을까요?</p>
            <buttons id="genres" class="d-flex" style="height:50px;">
              <input name="vote" type="radio" id="yes_vote" v-model="vote_average_gte" value="7" />
              <label for="yes_vote" class="yp-btn yp-btn-white">네</label>
              <input name="vote" type="radio" id="no_vote" v-model="vote_average_gte" value="4" />
              <label for="no_vote" class="yp-btn yp-btn-white">아니요</label>
            </buttons>
          </div>
        </li>
        <li>
          <div>
            <p class="question">제출할까요?</p>
            <buttons>
              <button @click="submission" class="last_btn">영화 추천받기!</button>
            </buttons>
          </div>
        </li>
      </ul>
    </section>

    <div v-if="title" class="container justify-content-center">
      <div class="movie-card">
          <div class="poster-wrapper">
            <div class="poster">
              <img v-if="poster_path" :src="`https://image.tmdb.org/t/p/original/${ poster_path }`" alt="poster" />
              <img v-else src="@/assets/Eivom_poster.jpg" alt="poster" />
            </div>
          </div>
          <!-- end poster-wrapper -->
          <div class="movie-info">
            <div class="header-section">
              <h2>{{ title }}</h2>
              <p>{{ original_title }}</p>
              <div class="extra">
                <div class="ratings"><p>	&#9733; {{ vote_average }}</p></div>
              </div>
            </div>

            <div class="synopsis-section">
              <h3>SYNOPSIS</h3>
              <p>
                {{ overview }}
              </p>
            </div>
            <div class="gallery-section">
              <h3>VIDEO / PICTURE</h3>
              <div class="gallery">
                <div class="small" v-if="backdrop1"><img :src="`https://image.tmdb.org/t/p/original/${ backdrop1 }`" alt="media" /></div>
                <div class="small" v-else><img src="@/assets/back1.jpg" alt="media" /></div>
                <div class="medium" v-if="backdrop2"><img :src="`https://image.tmdb.org/t/p/original/${ backdrop2 }`" alt="media" /></div>
                <div class="small" v-else><img src="@/assets/back1.jpg" alt="media" /></div>
                <div class="small" v-if="backdrop3"><img :src="`https://image.tmdb.org/t/p/original/${ backdrop3 }`" alt="media" /></div>
                <div class="small" v-else><img src="@/assets/back1.jpg" alt="media" /></div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from "lodash"

const URL = "https://api.themoviedb.org/3/discover/movie"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'RecommendView',
  components: {
  },
  data: function() {
    return {
      with_genres: [],
      without_genres: [],
      primary_release_date_gte: "",
      sort_by: "",
      include_adult: null,
      vote_average_gte: 5,

      title: "",
      original_title: "",
      poster_path: "",
      vote_average: "",
      overview: "",

      movie_id: "",
      backdrop1: "",
      backdrop2: "",
      backdrop3: "",

    }
  },
  methods: {
    submission() {
      let with_genre = ""
      for (let i = 0; i < this.with_genres.length - 1; i++){
        with_genre += this.with_genres[i] + ", " 
      }

      let without_genre = ""
      for (let i = 0; i < this.without_genres.length - 1; i++){
        without_genre += this.without_genres[i] + ", " 
      }

      const random_num = _.random(1, 20)

      axios.get(URL, {
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
          with_genres: with_genre + this.with_genres[this.with_genres.length],
          without_genres: without_genre + this.without_genres[this.without_genres.length],
          "primary_release_date.gte": this.primary_release_date_gte,
          sort_by: this.sort_by,
          include_adult: this.include_adult,
          "vote_averagte.gte": this.vote_average_gte
        }
      })
        .then(res => {
          const movie = res.data.results[random_num]
          if (movie.poster_path === "") {
            this.submission()
          } else {
            this.title = movie.title
            this.original_title = movie.original_title
            this.poster_path = movie.poster_path
            this.vote_average = movie.vote_average
            this.overview = movie.overview
            this.movie_id = movie.id

            axios.get("https://api.themoviedb.org/3/movie/" + this.movie_id + "/images", {
            params: {
              api_key: API_KEY,
            }
          })
            .then(res => {
              this.backdrop1 = res.data.backdrops[0].file_path
              this.backdrop2 = res.data.backdrops[1].file_path
              this.backdrop3 = res.data.backdrops[2].file_path
            })
            .catch(err => {
              console.error(err)
            })
          }
        })
        .catch(err => {
          console.error(err)
        })
      

    },
  },
  mounted() {
    var items = document.querySelectorAll(".timeline li");

    function isElementInViewport(el) {
      var rect = el.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <=
          (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    }

    function callbackFunc() {
      for (var i = 0; i < items.length; i++) {
        if (isElementInViewport(items[i])) {
          items[i].classList.add("in-view");
        }
      }
    }

    // listen for events
    window.addEventListener("load", callbackFunc);
    window.addEventListener("resize", callbackFunc);
    window.addEventListener("scroll", callbackFunc);

  }
}
</script>

<style scoped>

  #genres > com > com > button {
    height: 30px;
    width: 65px;
    font-size: 10px;
  }


  /* TIMELINE
  –––––––––––––––––––––––––––––––––––––––––––––––––– */


  .app6 {
    background-image: linear-gradient(to bottom, #d2eeff, #d3ecfd, #d4ebfa, #d4e9f8, #d5e8f5, #d8e9f5, #daebf4, #ddecf4, #e3f0f6, #eaf4f8, #f0f7fa, #f7fbfc);
    padding: 50px 0;
  }

  .timeline ul li {
    list-style-type: none;
    position: relative;
    width: 6px;
    margin: 0 auto;
    padding-top: 50px;
    background: #DBDBDB;
  }

  .timeline ul li::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: inherit;
    z-index: 1;
  }
  
  .timeline ul li div {
    position: relative;
    bottom: 0;
    width: 500px;
    padding: 15px;
    background: #E6F4F1;
    border-radius: 7px;
    box-shadow: 5px 5px 5px rgb(195, 195, 195);
  }

  .timeline ul li div::before {
    content: "";
    position: absolute;
    bottom: 3px;
    width: 0;
    height: 0;
    border-style: solid;
  }

  /* 오른쪽 박스 위치 */
  .timeline ul li:nth-child(odd) div {
    left: 45px;
  }

  /* 오른쪽 꼬리표 */
  .timeline ul li:nth-child(odd) div::before {
    left: -12px;
    border-width: 8px 16px 8px 0;
    border-color: transparent #E6F4F1 transparent transparent;
  }

  /* 왼쪽 박스 위치 */
  .timeline ul li:nth-child(even) div {
    left: -540px;
  }

  /* 왼쪽 꼬리표 */
  .timeline ul li:nth-child(even) div::before {
    right: -12px;
    border-width: 8px 0 8px 16px;
    border-color: transparent transparent transparent #E6F4F1;
  }


  time {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    display: block;
    font-size: 1.4rem;
    margin-bottom: 8px;
  }

  .question {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: 1.2rem !important;
  }

  .last_btn{
    border-radius: 4px;
    border: 0px;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    background-color: white;
    height: 40px;
    width: 150px;
  }

  /* EFFECTS
  –––––––––––––––––––––––––––––––––––––––––––––––––– */

  .timeline ul li::after {
    transition: background 0.5s ease-in-out;
  }

  .timeline ul li.in-view::after {
    background: #FFD2E2;
  }

  .timeline ul li div {
    visibility: hidden;
    opacity: 0;
    transition: all 1s ease-in-out;
  }

  .timeline ul li:nth-child(odd) div {
    transform: translate3d(200px, 0, 0);
  }

  .timeline ul li:nth-child(even) div {
    transform: translate3d(-200px, 0, 0);
  }

  .timeline ul li.in-view div {
    transform: none;
    visibility: visible;
    opacity: 1;
  }


  /* GENERAL MEDIA QUERIES
  –––––––––––––––––––––––––––––––––––––––––––––––––– */

  @media screen and (max-width: 900px) {
    .timeline ul li div {
      width: 250px;
    }
    .timeline ul li:nth-child(even) div {
      left: -289px;
      /*250+45-6*/
    }
  }

  @media screen and (max-width: 600px) {
    .timeline ul li {
      margin-left: 20px;
    }
    .timeline ul li div {
      width: calc(100vw - 91px);
    }
    .timeline ul li:nth-child(even) div {
      left: 45px;
    }
    .timeline ul li:nth-child(even) div::before {
      left: -15px;
      border-width: 8px 16px 8px 0;
      border-color: transparent #c7c9cc transparent transparent;
    }
  }


  /* EXTRA/CLIP PATH STYLES
  –––––––––––––––––––––––––––––––––––––––––––––––––– */
  .timeline-clippy ul li::after {
    width: 40px;
    height: 40px;
    border-radius: 0;
  }

  .timeline-rhombus ul li::after {
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
  }

  .timeline-rhombus ul li div::before {
    bottom: 12px;
  }

  .timeline-star ul li::after {
    clip-path: polygon(
      50% 0%,
      61% 35%,
      98% 35%,
      68% 57%,
      79% 91%,
      50% 70%,
      21% 91%,
      32% 57%,
      2% 35%,
      39% 35%
    );
  }

  .timeline-heptagon ul li::after {
    clip-path: polygon(
      50% 0%,
      90% 20%,
      100% 60%,
      75% 100%,
      25% 100%,
      0% 60%,
      10% 20%
    );
  }

  .timeline-infinite ul li::after {
    animation: scaleAnimation 2s infinite;
  }

  @keyframes scaleAnimation {
    0% {
      transform: translateX(-50%) scale(1);
    }
    50% {
      transform: translateX(-50%) scale(1.25);
    }
    100% {
      transform: translateX(-50%) scale(1);
    }
  }


/* --------------------------------------------------------- */
/* movie card */

  @import url("https://fonts.googleapis.com/css?family=Lato");
  /*-- Variables --*/
  /*---- Global ----*/
  .movie-card {
    background-color: rgb(245, 245, 245);
    margin: 20px;
    padding: 100px;
    border: 0;
    border-radius: 20px;
    outline: 0;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
    font-size: 100%;
    vertical-align: bottom;
    text-decoration: none;
    box-sizing: border-box;
    box-shadow: 5px 5px 5px rgb(209, 209, 209);

  }
  p {
    font-size: 14px;
    line-height: 20px;
  }

  img {
    width: 100%;
  }

  h1 {
    color: #020518;
  }

  h2 {
    color: #020518;
  }

  h3 {
    color: #020518;
  }

  h4 {
    color: #020518;
  }

  h5 {
    color: #020518;
  }

  h6 {
    color: #020518;
  }

  h2 {
    font-size: 30px;
  }

  h3 {
    font-size: 14px;
    margin-bottom: 15px;
  }

  /*movie-card*/
  .movie-card {
    display: grid;
    grid-template-columns: 2fr 400px 0.5fr 400px 2fr;
    grid-template-areas: ". p . m .";
  }
  @media screen and (max-width: 1024px) {
    .movie-card {
      grid-template-columns: 1fr 4fr 1fr 4fr 1fr;
    }
  }
  @media screen and (max-width: 780px) {
    .movie-card {
      grid-template-columns: 1fr 4fr 1fr;
      grid-template-areas: ". p ." ". m .";
    }
  }
  @media screen and (max-width: 500px) {
    .movie-card {
      grid-template-columns: 0.5fr 4fr 0.5fr;
      grid-template-areas: ". p ." ". m .";
    }
  }
  .movie-card .poster-wrapper {
    grid-area: p;
  }
  .movie-card .poster-wrapper .poster {
    position: relative;
    color: #fff;
  }
  @media screen and (max-width: 500px) {
    .movie-card .poster-wrapper .poster {
      margin-bottom: 30px;
    }
  }
  .movie-card .poster-wrapper .poster .release-date {
    position: absolute;
    top: 30px;
    left: -30px;
    background-color: #3686ff;
    padding: 10px;
    text-align: center;
  }
  .movie-card .poster-wrapper .poster .release-date h2 {
    font-size: 42px;
    color: #fff;
  }
  .movie-card .poster-wrapper .poster .release-date .divider {
    background-color: #fff;
    height: 2px;
    width: 20px;
    margin: 10px auto;
  }
  .movie-card .poster-wrapper .poster .btn-play {
    position: absolute;
    bottom: 30px;
    right: -30px;
    background-color: #3686ff;
    padding: 15px;
    font-size: 24px;
    cursor: pointer;
    transition: all 0.4s;
  }
  .movie-card .poster-wrapper .poster .btn-play:hover {
    background-color: #fdba2e;
  }
  .movie-card .movie-info {
    grid-area: m;
  }
  .movie-card .movie-info > div {
    margin-bottom: 30px;
  }
  .movie-card .movie-info .header-section p {
    margin: 5px 0;
  }
  .movie-card .movie-info .header-section .extra {
    display: flex;
    align-items: center;
  }
  @media screen and (max-width: 500px) {
    .movie-card .movie-info .header-section .extra {
      display: block;
    }
  }
  .movie-card .movie-info .header-section .extra .ratings {
    margin-right: 50px;
    color: #fdba2e;
  }
  .movie-card .movie-info .header-section .extra .ratings p {
    font-size: 18px;
  }
  .movie-card .movie-info .header-section .extra .channels > span {
    margin-right: 5px;
  }
  .movie-card .movie-info .cast-section .casts {
    display: flex;
  }
  .movie-card .movie-info .cast-section .casts img {
    width: 40px;
    height: 40px;
    object-fit: cover;
    border-radius: 50%;
    margin-right: 15px;
  }
  .movie-card .movie-info .gallery-section .gallery {
    display: grid;
    grid-template-columns: repeat(autofit, minmax(50px, 1fr));
    grid-auto-rows: 75px;
    grid-row-gap: 10px;
    grid-column-gap: 10px;
    grid-auto-flow: dense;
  }
  .movie-card .movie-info .gallery-section .gallery .small {
    grid-column: span 1;
  }
  .movie-card .movie-info .gallery-section .gallery .medium {
    grid-column: span 3;
  }
  .movie-card .movie-info .gallery-section .gallery img {
    object-fit: cover;
    width: 100%;
    height: 100%;
  }


  /*---------------------------------------------------- */
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
  }

  .yp-btn {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
    position: relative;
    height: 40px;
    width: 90px;
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

  input {
    visibility: hidden;
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

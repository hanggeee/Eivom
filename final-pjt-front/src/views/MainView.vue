<template>
  <div>

    <!-- 첫 메인화면 -->
    <div class="main d-flex justify-content-center align-items-center">
      <div>
        <div class="byline">
          <h1 class="display-1">영화,</h1>
          <div class="text-end">
            <h1 class="display-1">그 이상의 즐거움.</h1>
            <h3 class="fw-bold">Movie, Pleasure beyond</h3>
          </div>
        </div>
      </div>
    </div>

    <!-- 움직이는 영상 + 영화 이름 -->
    
    <div class="" style="position: relative;">
      <video class="main_video" muted="" autoplay="" loop="" data-inline-media=""  preload="none" width="100%" height="100%" :src="video"></video>
      <div class="center">
        <div class="title">
          <h3 class="display-1">{{ title }}</h3>
          <h3 class="fs-5">{{ release_date }}</h3>
        </div>
      </div>
    </div>

    <!-- 중간 파트 -->
    <div class="container">
      <div id="middle" class="d-flex justify-content-center">
        <div>
          <!-- 크기 가로 900 세로 1000으로 자른 뒤, css 이용해 height 600px로 조절 -->
          <div class="d-flex highlight" style="position: relative;">
            <img :src="highlight" alt="highlight" class="img1">
            <div id="main_sentense" class="ms-5" style="position: absolute; left: 520px; right: -500px; ">
              <h3 class="display-1">{{ sentense1 }}</h3>
              <h3 class="display-1">{{ sentense2 }}</h3>
              <h3 class="display-1">{{ sentense3 }}</h3>
            </div>
          </div>
          <div class="director">
            <div class="d-flex align-items-center">
              <p id="highlight_sen" class="me-5">{{ overview }}</p>
              <img id="director" :src="director" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- back image + 제작노트 or 평론 부분 -->
    <div class="" style="position: relative;">
      <img class="main_video" :src="back" alt="">
      <div class="center">
        <div class="title d-flex justify-content-center">
          <div id="review">
            <div>
              <p class="">{{ review }}</p>
              <p class="text-end">{{ reviewer }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 영화 카드 리스트 -->
    <div class="page">
      <main-card-list></main-card-list>
    </div>
    <div style="height:500px">

    </div>
  </div>
</template>


<script>

  import MainCardList from '../components/main/MainCardList.vue'
  import movie from '../assets/main_movies/movies.json'
  import _ from 'lodash'

  let num = _.random(1, 9)
  // console.log(movie)
  // console.log(movie.movies[num].title)

  export default {
    name: 'MainView',
    components: {
      MainCardList,
    },
    data: function() {
      return {
        movie_data: movie,
        title: "",
        release_date: "",
        sentense1: "",
        sentense2: "",
        sentense3: "",
        overview: "",
        review: "",
        reviewer: "",
        video:require("../assets/main_movies/movie" + num + ".mp4"),
        highlight:require("../assets/main_movies/highlight" + num + ".jpg"),
        director:require("../assets/main_movies/director" + num + ".jpg"),
        back:require("../assets/main_movies/back" + num + ".jpg"),
      }
    },
    created() {
      this.title = movie.movies[num].title
      this.release_date = movie.movies[num].release_date
      this.sentense1 = movie.movies[num].sentense1
      this.sentense2 = movie.movies[num].sentense2
      this.sentense3 = movie.movies[num].sentense3
      this.overview = movie.movies[num].overview
      this.review = movie.movies[num].review
      this.reviewer = movie.movies[num].reviewer
      },
  }

  window.addEventListener('scroll', function(){
      scrollMotion()
  });

  function scrollMotion(){
      const ele = document.querySelectorAll('.title');
      let eleOffsetArr = [];

      ele.forEach(e => {
          let eleOffset = e.getBoundingClientRect().top + window.pageYOffset - 800;
          eleOffsetArr.push(eleOffset)
          // console.log(eleOffset)
      });
      
      eleOffsetArr.forEach((offset, idx) => {
              ele[idx].style.cssText = ( window.scrollY > offset 
              ? 'opacity:1; transform: translateY(0);'
              : 'opacity:0; transform: translateY(50px);' )
      });
  }

</script>


<style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

  #detail {
    height: 100vh;
  }

  .img1 {
    height: 600px;
  }

  #middle {
    margin-top: 13rem;
    margin-bottom: 13rem;
  }

  .highlight {
    z-index: 10;
  }

  #main_sentense {
    padding-top: 100px;
  }

  #highlight_sen {
    color: #6e6e73;
    width:400px;
    padding-top: 100px;
  }

  .director {
    position: relative;
    top: -70px;
    left: 40px;
    z-index: -10;
  }

  #director {
    width: 22rem;
  }

  #review > div > p {
    width: 50vw;
    font-size: 2vw;
    color: #ffffffd1;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }

  h1 {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
  }

  h3 {
    font-family: 'Open Sans', sans-serif;
    font-weight: 700;
  }

  p {
    font-family: 'Noto Sans KR','Open Sans',  sans-serif;
    font-weight: 500;
  }

  .main {
    height: 100vh;
  }
  
  .main_video {
    width: 100%;
    filter: brightness(0.7);
  }

  .center {
    position: absolute;
    top: 40%;
    width: 100%;
    text-align: center;
    z-index: 10;
  }

  .page {
    position: relative;
    /* height: 100vh; */
    margin: 0;
  }

  .byline {
      color: #000000;
      opacity: 0;
      transform: translateY(-15px);
      animation: subtext .8s ease-out both;
  }

  .byline {
    animation-delay: 0.5s;
  }

  @keyframes subtext {
      100% {
          opacity: 1;
          transform: translateX(0);
      }
  }

  .title {
    opacity: 0;
    transform: translatey(50px);
    transition: all 0.5s;
    font-size: 20px;
    /* text-align: center; */
    color: #ffffff;
  }

</style>
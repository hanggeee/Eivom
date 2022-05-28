<template>
  <div>
    <div class="container-lg">
      <div class="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <div class="container text-end">
          <h2 class="text-uppercase">{{title}}</h2>
          <div>
            <h3>{{original_title}}</h3>
          </div>
        </div>
      </div>
    </div>
      <div class="container-fluid parallax bg-img1"
      :style="`background: linear-gradient(rgba(0,0,0,.15), rgba(0,0,0,.15)), url('https://image.tmdb.org/t/p/original/${ backdrop_path }');`">
        <div class="heading text-center">
          <!-- <h2>{{restAPI.release_date}}</h2> -->
          <!-- <h2 class="text-uppercase poster_title">{{title}}</h2> -->
        </div>
      </div>
    <div class="container-lg">
      <div class="container-fluid py-5 bg-faded" id="info">
        <div class="container-xxl d-flex justify-content-end">
          <div>
            <div class="d-flex justify-content-end">
              <div>
                <div class="d-flex">
                  <div v-for=" genre in genres" :key="genre.id">{{ genre.name }}&nbsp;&nbsp;</div>
                  <div>{{ runtime }}</div>
                </div>
                <div class="text-end">
                  개봉일 {{ release_date }}
                </div>
                <div class="text-end">
                  평점 {{ vote_average }}
                  <p></p>
                </div>
              </div>
            </div>
            <div class="text-end" style="width: 550px">
              {{ overview }}
            </div>
          </div>
        </div>
      </div> 

      <hr>
      <div>
        

        <div id="menu" class="d-flex justify-content-between" >
          <div class="d-flex">
            <div id="actors" class="long_menu ms-5 me-5 actived" @click="click_actor" >배우들 목록</div>
            <div id="s_movie" class="long_menu ms-5 me-5" @click="click_s_movie" >비슷한 영화</div>
          </div>
          <div>
            <!-- <button @click="likeMovie(moviePk)" v-if="isLiking">이 영화 찜 취소</button>
            <button @click="likeMovie(moviePk)" v-else>이 영화 찜하기</button> -->
            <!-- <button @click="likeMovie(moviePk)">이 영화 찜하기</button> -->

            <button id="follow" @click="likeMovie(moviePk)" class="heart-button" :class="{active : isLiking}">
              <div class="heart-flip"></div>
              <span>Like<span>d</span></span>
            </button>
            
          </div>
        </div>
        <movie-actors-list :movie="movie" v-if="menubar"></movie-actors-list>
        <similar-movie-item v-if="menubar === false" :movie="movie"></similar-movie-item>
      </div>
      <hr>
      <movie-comment-list :movie_id="movie"></movie-comment-list>


    </div>
  </div>
</template>

<script>
import MovieCommentList from '../components/moviedetail/MovieCommentList.vue'
import MovieActorsList from '../components/moviedetail/MovieActorsList.vue'
import SimilarMovieItem from '../components/moviedetail/SimilarMovieItem.vue'
import { mapActions, mapGetters } from "vuex"

import axios from "axios"
// import _ from "lodash"

const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default {
  name: 'MovieDetailView',
  data: function(){
    return {
      // get_movieID: "",
      movie: this.$route.params.movie_id,
      moviePk: this.$route.params.movie_id,
      // movie: this.get_movie,
      title: '',
      original_title: '',
      backdrop_path: '',
      genres: [],
      release_date: '',
      runtime: '',
      vote_average: '',
      overview: '',
      menubar: true,
    }
  },
  computed: {
    ...mapGetters(['get_movie', 'isLiking', 'currentUser', 'get_movie_data']),
  },
  methods: {
    ...mapActions(['likeMovie', 'fetchCurrentUser', 'search']),
    click_actor: function() {
      if (this.menubar === false) {
        this.menubar = true
        const actors = document.querySelector("#actors")
        const s_movie = document.querySelector("#s_movie")
        actors.classList.add('class', 'actived')
        s_movie.classList.remove('class', 'actived')
      }
    },
    click_s_movie: function() {
      if (this.menubar === true) {
        this.menubar = false
        const actors = document.querySelector("#actors")
        const s_movie = document.querySelector("#s_movie")
        actors.classList.remove('class', 'actived')
        s_movie.classList.add('class', 'actived')
      }
    }
  },
  components: {
    MovieCommentList, MovieActorsList, SimilarMovieItem
  },
  created() {
    // console.log(this.get_movie)
    axios.get(URL + this.movie, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    })
      .then(res => {
      this.title = res.data.title
      this.original_title = res.data.original_title
      this.backdrop_path = res.data.backdrop_path
      this.genres = res.data.genres
      this.release_date = res.data.release_date

      const hour = parseInt(res.data.runtime / 60)
      const min = parseInt(res.data.runtime % 60)
      this.runtime = hour + "h " + min + "m"

      this.vote_average = res.data.vote_average
      this.overview = res.data.overview
      // console.log(res.data)
      })
      .catch(err => console.log(err))
      this.fetchCurrentUser()
      this.search(this.movie)
  },
  mounted() {
    document.querySelectorAll('.heart, .heart-button').forEach(button => button.addEventListener('click', () => button.classList.toggle('active')));
  },
  watch: {
      '$route' (to, from) {
        location.reload()
        console.log(to)
        console.log(from)
      }
  }
}
</script>

<style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

  #menu {
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 20px;
    font-weight: 500;
    padding-bottom: 8px;
    border-bottom: 1.5px solid #bcbcbc;
  }

  .actived:after {
    padding-right: 15px;
    content: "";
    display: block;
    border-bottom: 2px solid #000000;
    width: 100px;
    position: absolute;
    margin: 12px auto;
  }

  #actors {
    cursor: pointer;
    line-height: 1.9;
  }

  #s_movie {
    cursor: pointer;
    line-height: 1.9;
  }

  #info {
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 22vm;
    font-weight: 500;
    color: #6c757d;
  }
/* 
  .long_menu:hover:after {
    content: "";
    display: block;
    width: 40px;
    border-bottom: 2px solid #bcbcbc;
    margin: 3px auto;
    position: absolute;
    margin-left: 20px;
    } */


  .loading {
    margin-top: 3.5rem;
    width:100%;
    height:100%;
    position:fixed;
    left:0px;
    top:0px;
    background:#fff;
    z-index:1000;
    transition: opacity 1s;
  }

  body, html {
    height: 100%;
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 14px;
  }

  h1 {
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 4.5rem;
    letter-spacing: 0.5rem;
  }

  h2 {
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 5rem;
    font-weight: 900;
    letter-spacing: 0.5rem;
    color: black;
  }

  h3 {
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    /* letter-spacing: 0.2rem; */
    color: #d6d6d6;
  }

  .poster_title {
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 3rem;
    font-weight: 700;
    /* letter-spacing: 0.2rem; */
    color: #d6d6d6;
  }

  p {
    margin-top: 1rem;
  }

  a {
    color:#5bc0de;
  }

  a:hover {
    color: #31b0d5;
    text-decoration: none;
  }

  #hm {
    min-height: 100%;
    height: 300px;
  }

  .heading {
    color: #FFF;
    left: 0;
    position: absolute;
    text-align: center;
    top: 40%;
    width: 100%;
  }

  .middle {
    color: #FFF;
    left: 0;
    position: absolute;
    text-align: center;
    top: 30%;
    width: 100%;
  }

  .bg-img1 {
    background-repeat: no-repeat;
    background-size: cover !important;
    /* background: linear-gradient(rgba(0,0,0,.3), rgba(0,0,0,.3)), url('https://wallpapercave.com/wp/wp1906348.png'); */
    height: 900px;
  }

  .bg-img2 {
    background-repeat: no-repeat;
    background-size: cover !important;
    /* background: linear-gradient(rgba(0,0,0,.3), rgba(0,0,0,.3)), url('https://i.pinimg.com/originals/96/18/6b/96186b308addc3c4700a26adb3aac278.gif'); */
    height: 1000px;
}

  .parallax {
    background-attachment: fixed !important;;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    min-height: 100%;
    position: relative;
  }

  .container {
    margin-right: auto;
    margin-left: auto;
    max-width: 850px;
  }

  .card {
    margin-bottom: 1rem;
    margin-top: 1rem;
  }

  .card-text {
    font-size: 1rem;
    font-weight: 300;
  }

  @media only screen and (max-device-width: 1024px) {
    .parallax {background-attachment: scroll;}
    .heading {top: 30%;} 
    .middle {top: 15%;}
  }

  #follow {
    margin-bottom: 5px;
  }

  #follow span {
    font-size: 0.9rem;
  }


  .heart,
  .heart-button {
    cursor: pointer;
    outline: none;
    -webkit-appearance: none;
    -webkit-tap-highlight-color: transparent;
  }
  .heart .heart-flip,
  .heart-button .heart-flip {
    --base: 32px;
    --duration: .6s;
    --active: #ea4673;
    --inactive: #d1d6ee;
    width: var(--base);
    height: calc(var(--base) + var(--base) / 2);
    border-radius: calc(var(--base) / 2) calc(var(--base) / 2) 0 0;
    position: relative;
    transform-origin: 50% 66.66%;
    transform-style: preserve-3d;
    transform: rotate(var(--rotate, -45deg));
    transition: background var(--duration), transform var(--duration) ease;
    background: var(--heart-background, var(--inactive));
  }
  .heart .heart-flip:before, .heart .heart-flip:after,
  .heart-button .heart-flip:before,
  .heart-button .heart-flip:after {
    content: "";
    width: calc(var(--base) / 2);
    height: var(--base);
    border-radius: var(--pseudo-border-radius, calc(var(--base) / 2) 0 0 calc(var(--base) / 2));
    position: absolute;
    left: var(--pseudo-left, -50%);
    transform-origin: var(--pseudo-origin, 100%) 50%;
    bottom: 0;
    background: var(--heart-background, var(--inactive));
    filter: brightness(var(--pseudo-filter, 50%));
    transform: translateX(1%) rotateY(var(--pseudo-rotate, 90deg)) translateZ(0);
    transition: background var(--duration), transform var(--duration) ease, filter var(--duration);
  }
  .heart .heart-flip:after,
  .heart-button .heart-flip:after {
    --pseudo-border-radius: 0 calc(var(--base) / 2) calc(var(--base) / 2) 0;
    --pseudo-left: 100%;
    --pseudo-origin: 0;
    filter: brightness(var(--pseudo-filter-second, 100%));
    transform: translateX(-1%) rotateY(var(--pseudo-rotate-second, 0deg)) translateZ(0);
  }
  .heart.active .heart-flip,
  .heart-button.active .heart-flip {
    --rotate: 45deg;
    --pseudo-filter: 100%;
    --pseudo-filter-second: 50%;
    --pseudo-rotate: 0deg;
    --pseudo-rotate-second: 90deg;
    --heart-background: var(--active);
  }

  .heart {
    background: none;
    border: none;
    padding: 0;
    transform: scale(var(--button-scale, 1)) translateZ(0);
    transition: transform 0.2s;
  }
  .heart:active {
    --button-scale: .95;
  }

  .heart-button {
    --duration: .4s;
    --color: #404660;
    --color-hover: #2b3044;
    --color-active: #fff;
    --border: #d1d6ee;
    --border-hover: #bbc1e1;
    --border-active: #ea4673;
    --background: #fff;
    --background-active: #ea4673;
    font-family: inherit;
    font-size: 14px;
    line-height: 1.6;
    font-weight: 600;
    padding: 6px 16px;
    border-radius: 7px;
    color: var(--button-color, var(--color));
    border: 1px solid var(--button-border, var(--border));
    background: var(--button-background, var(--background));
    transform: scale(var(--button-scale, 1)) translateZ(0);
    transition: background var(--duration), border-color var(--duration), color var(--duration), transform 0.2s;
  }
  .heart-button .heart-flip {
    --base: 8px;
    --active: #fff;
    --inactive: #bbc1e1;
    display: inline-block;
    vertical-align: top;
    margin: 4px 6px 0 0;
  }
  .heart-button span {
    display: inline-block;
    vertical-align: top;
  }
  .heart-button > span {
    transform: translateX(var(--text-x, 4px));
    transition: transform var(--duration);
  }
  .heart-button > span span {
    display: inline-block;
    vertical-align: top;
    opacity: var(--span-opacity, 0);
    transform: translateX(var(--span-x, 4px));
    transition: opacity var(--duration), transform var(--duration);
  }
  .heart-button:active {
    --button-scale: .95;
  }
  .heart-button:hover {
    --button-color: var(--color-hover);
    --button-border: var(--border-hover);
  }
  .heart-button.active {
    --text-x: 0;
    --button-color: var(--color-active);
    --button-border: var(--border-active);
    --button-background: var(--background-active);
    --span-opacity: 1;
    --span-x: 0;
  }








</style>
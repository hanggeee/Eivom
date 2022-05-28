<template>
  <div>
    <div class="movie-card" :style="`background: url('https://image.tmdb.org/t/p/w500/${backdrop_path}');`">
      <div class="title_part">
        <h1>{{ title }}</h1>
        <span>{{ original_title }}</span>
          <span>
            {{ vote_average }}
            <i class="fas fa-star"></i>
          </span>
      </div>
      <p>{{ overview }}</p>
      <div class="d-flex justify-content-between">
        <button class="watch m-1" @click="reload">다른 영화 보기</button>
        <button class="watch m-1">상세보기</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import _ from "lodash"

const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default {
  name: "similar_movie_item",
  props: {
    movie: Number,
  },
  data: function() {
    return {
      title: "",
      original_title: "",
      vote_average: "",
      backdrop_path: "",
      overview: "",
      release_data: "",
    }
  },
  methods: {
    reload() {
      const random_num = _.random(0, 15)
      console.log(random_num)
      axios.get(URL + this.movie + "/similar", {
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
        }
      })
        .then(res => {
          const movie = res.data.results[random_num]
          this.title = movie.title
          this.original_title = movie.original_title
          this.overview = movie.overview.slice(0, 120) + "...."
          this.release_data = movie.release_data
          this.backdrop_path = movie.backdrop_path
          this.vote_average = movie.vote_average.slice(0, 3)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  mounted() {
    const random_num = _.random(0, 10)
    console.log(random_num)
    axios.get(URL + this.movie + "/similar", {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    })
      .then(res => {
        const movie = res.data.results[random_num]
        this.title = movie.title
        this.original_title = movie.original_title
        this.overview = movie.overview.slice(0, 120) + "...."
        this.release_data = movie.release_data
        this.backdrop_path = movie.backdrop_path
        this.vote_average = movie.vote_average
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

  /* body {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    background: black;
  } */

  /* 영화 카드 */
  .movie-card {
    position: relative;
    box-sizing: border-box;
    width: 50%;
    max-width: 800px;
    height: 300px;
    background-position: center;
    background-size: cover !important;
    margin: 4vh auto;
    border-radius: 4px;
    box-shadow: 2px 3px 12px rgba(0, 0, 0, .4);
    color: white;
    padding: 2vh 3%;
    z-index: 10;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 300;
  }

  /* 영화 카드 어둡게 */
  .movie-card:after{
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 4px;
    background: linear-gradient(to right, rgba(40,40,60,1) 0%,rgba(40,0,60,0) 90%);
    background-blend-mode: multiply;
    will-change: transform;
    z-index: 0 ;
  }


  /* 제목, 소제목 부분  */
  .title_part {
    margin-top: 10px;
    margin-bottom: 30px;
  }

  /* 평점 별모양 아이콘 */
  i {
    font-size: .7em;
    color: #ff5b84;
  }

  /* 제목 / title */
  h1 {
    font-size: 170%;
    position: relative;
    z-index: 10;
    margin-bottom: 0px;
  }

  /* 영어 title */
  span {
    display: inline-block;
    position: relative;
    font-size: 80%;
    z-index: 10;
    margin-right: 80px;
    margin-left: 5px;
    color: rgb(210, 210, 210);
  }

  .watch {
    display: block;
    border: 1px solid white;
    border-radius: 4px;
    position: relative;
    z-index: 30;
    color: white;
    padding: 10px;
    text-align: center;
    background: rgba(0, 0, 0, .3);
    margin: 20px 0px;
    outline: none;
    box-shadow: 0 0 10px rgba(0,0,0,.5);
    transition: all .2s;
  }

  button {
    position: relative;
    z-index: 30;
    cursor: pointer;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    background: rgba(255, 255, 255, .8);
  }

  button:hover {
    background: rgba(191, 191, 191, 0.8);
    color: black;
    box-shadow: 0 0 10px rgba(255,255,255,.5);
    mix-blend-mode: screen;
    cursor: pointer;
  }
  button:active {
    transform: translateY(2px);
  }

  p {
    position: relative;
    z-index: 10;
    font-size: .8em;
    width: 60%;
    height: 35%;
  }

  @media (max-width: 768px) {
    body {
      background: none;
    }
    .movie-card {
      width: 75%;
      height: 200px;
    }
    h1 {
    font-size: 120%;
    }
    p {
      display: none;
      overflow: hidden;
      width: 100%;
      height: 30%;
    }
    .watch {
      margin: 5% auto;
    }
  }
  @media (max-width: 500px) {
    .movie-card {
      width: 100%;
    }
  }
</style>
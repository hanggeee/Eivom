<template>
    <div class="app3" v-if="overview != '' && backdrop_path != '' ">
      <!-- <h3>이 영화 어때요</h3>
      <community-card-item></community-card-item> -->
      <div class="container">
        <div id="tag">이런 영화는 어때요?</div>
        <div class="poster">    
          <div class="poster__img" 
          :style="`
            background: url('https://image.tmdb.org/t/p/w500/${ backdrop_path }');
            height: 200px;
            background-position: center;
            background-size: cover;
            width: 100%;
          `"></div>
          <div class="poster__info">
            <h1 class="poster__title">{{ title }}</h1>
            <p class="poster__text">{{ custom_overview }}</p>
          </div>
        </div>
        <a :href="`http://localhost:8080/moviedetail/${ movie_id }`">자세히 보기</a>
      </div>
    </div>
</template>

<script>
// import CommunityCardItem from './CommunityCardItem.vue'

import _ from 'lodash'
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/top_rated"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
let page = _.random(1, 480)
let num = _.random(0,19)


export default {

  name: 'community_card',
  components: {
    // CommunityCardItem,
  },
  data: function(){
    return {
      movie_id: '',
      title: '',
      original_title: '',
      backdrop_path: '',
      genres: [],
      release_date: '',
      vote_average: '',
      overview: '',
      poster_path: '',
    }
  },
  created() {
    axios.get(URL, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
        page: page
      }
    })
      .then(res => {
      console.log(res.data.results[num])
      this.movie_id = res.data.results[num].id
      this.title = res.data.results[num].title
      this.poster_path = res.data.results[num].poster_path
      this.original_title = res.data.results[num].original_title
      this.backdrop_path = res.data.results[num].backdrop_path
      this.genres = res.data.results[num].genres_ids
      this.release_date = res.data.results[num].release_date
      this.vote_average = res.data.results[num].vote_average
      this.overview = res.data.results[num].overview
      })
      .catch(err => console.log(err))
  },
  computed: {
    custom_overview() {
      return this.overview.slice(0, 180) + '...'
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
  .app3 {
    margin-top: 190px;
    margin-left: 30px;
    margin-right: 30px;
    /* background-color: lightgrey; */
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-radius: 15px;
  }

  .card__left__img {
    width: 150px;
  }

  .cards {
  width: 30rem;
  display: flex;
  justify-content: space-evenly;
  border-radius: 4px;
  padding: 1rem 0rem;
  border-bottom: 1px solid var(--recommend-border);
  margin-left: 35px;
  margin-right: 35px;
  }

  .card__right{
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .card__right__header {
    display: flex;
    justify-content: space-between;
    align-items: space-between;
  }

  .card__right__header__score{
    display: flex;
  }

  #tag {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 23px;
    margin: 0 0 0 0;
    position: absolute;
    top: 3%;
  }




  html {
    font-size: 18px;
  }

  body {
    font-family: "Roboto", sans-serif;
    font-size: 1em;
    line-height: 1.6;
    background: #eee;
  }

  .container {
    min-width: 350px;
    display: block;
    /* width: 375px; */
    width: 17vw;
    /* height: 677px; */
    background: #ffffff;
    box-shadow: 0 0 30px 0 rgba(0, 0, 0, 0.1);
    padding: 70px 30px 0;
    position: relative;
    border-radius: 30px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  .container:before {
    content: "";
    display: block;
    position: absolute;
    width: 100%;
    height: 200px;
    background: red;
    top: 0;
    left: 0;
    z-index: -1;
    border-radius: 30px 30px 0px 0px;
    background: linear-gradient(130deg, #fff9a0 10%, #fbd073 100%);
  }

  .poster {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 1px 0 10px 0 rgba(0, 0, 0, 0.2);
  }
  .poster__img {
    height: 200px;
    background-position: center !important;
    background-size: cover !important;
    width: 100%;
  }
  .poster__info {
    background: #fff;
    padding: 25px 25px 40px;
  }
  .poster__title {
    font-size: 1.2em;
    font-weight: 300;
    margin-bottom: 0.4em;
  }
  .poster__text {
    font-size: 0.9em;
    color: #999;
    font-weight: 300;
  }

  a {
    display: block;
    /* width: 250px; */
    background: #27ae60;
    text-align: center;
    margin: 30px auto;
    height: 50px;
    line-height: 50px;
    border-radius: 25px;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-family: 'Noto Sans KR', sans-serif;
    text-decoration: none;
    font-size: 0.9em;
    font-weight: 500;
    background: linear-gradient(90deg, #2ecc71, #27ae60);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.18);
    transition: 0.3s;
  }
  a:hover {
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.1), 0 8px 8px rgba(0, 0, 0, 0.18);
  }
</style>
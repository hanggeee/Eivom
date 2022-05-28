<template>
  <div>
    <div id="now" class="text-center">
      현재 상영중인 영화.
    </div>
    <div id="owl">
      <carousel v-if="movies.length > 0"
      :items="5.5"
      :center="true"
      :loop="true"
      :margin="0"
      :nav="false"
      :dots="false"
      :autoplay="true"
      :autoplayTimeout="6000"
      :autoplaySpeed="6000"
      :autoplayHoverPause="true"
      :responsive="{
        0:{
          items: 1,
        },
        576:{
          items: 2,
        },
        769:{
          items: 3,
        },
        992:{
          items: 4,
        }
      }">
        <main-card-item v-for="movie in movies" :key="movie.id" :movie="movie"></main-card-item>
      </carousel>
    </div>
  </div>
</template>

<script>
import MainCardItem from './MainCardItem.vue'
import carousel from "vue-owl-carousel2";

import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/now_playing"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default {
  name: 'MainCardList',
  components: {
    MainCardItem, 
    carousel
  },
  data: function() {
    return {
      movies: {},
    }
  },
  created() {
    axios.get(URL, {
      params: {
        api_key: API_KEY,
        language: "ko-KR",
        region: "KR"
      }
    })
      .then(res => {
        this.movies = res.data.results.slice(0, 10)
        })
      .catch(err => {
        console.log(err)
      })
  }
  
}
</script>

<style scoped>

#now {
  margin-top: 500px;
  margin-bottom: 100px;
  font-family: 'Noto Sans KR', 'Open Sans',  sans-serif;
  font-weight: 700;
  font-size: 4rem;
}
</style>
<template>
  <div>
    <div id="owl">
      <carousel v-if="actors.length > 0"
      :items="5.5"
      :loop="true"
      :margin="30"
      :nav="false"
      :dot="true"
      :responsive="{
        0: {
          items: 10
        },
        768: {
          items: 6
        }
      }">
        <movie-actors-item v-for="actor in actors" :key="actor.id" :actor="actor"></movie-actors-item>
      </carousel>
    </div>
  </div>
</template>

<script>
import MovieActorsItem from './MovieActorsItem.vue'
import carousel from "vue-owl-carousel2";

import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

  export default {
    name: 'movie_actor_list',
    components: {
      MovieActorsItem,
      carousel
    },
    props: {
      movie: String,
    },
    data: function() {
      return {
        actors: {},
      }
    },
    computed: {

    },
    created() {
      axios.get(URL + this.movie + "/credits", {
        params: {
          api_key: API_KEY,
        }
      })
        .then(res => {
          // console.log(res.data.cast.slice(0, 15))
          this.actors = res.data.cast.slice(0, 15)
          })
        .catch(err => {
          console.log(err)
        })
    }
  }



</script>

<style scoped>

  #owl {
      margin: 30px;
      margin-top: 40px;
  }

</style>
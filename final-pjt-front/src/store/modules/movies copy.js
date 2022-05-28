import router from '@/router';
import axios from 'axios'
import drf from '@/api/drf'

const URL = "https://api.themoviedb.org/3/search/movie"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default{
  // state는 절대 직접 접근하지 않음.

  state: {
    // token: "",
    movieID: "",
  },
  getters: {
    get_movieID: state => state.movieID,

  },
  mutations:{
    SET_MOVIE_ID: (state, movieID) => state.movieID = movieID,
  },
  actions:{
    search: function({ commit }, movie_id ) {
      axios({
        url: drf.movies.movie(movie_id),
        method: 'get',
      })
        .then(res => {
          console.log(res.data)
          const movie_id = res.data.movie_id
          commit("SET_MOVIE_ID", movie_id)
          router.push({ name: 'moviedetail', params: { movie_id: movie_id }}).catch(err => err)
        })
        .catch(err => {
          console.log(err)
          router.push({ name: 'mainpage'}).catch(err => err)
        })
    },
    
    test1(){
      console.log("TEst")
    },
    
    search_movie_ID: function ({ dispatch }, search_movie) {
      console.log(search_movie)
      axios.get(URL, {
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
          query: search_movie,
        }
      })
        .then(res => {
          console.log(res.data.results[0].id)
          const movie_id = res.data.results[0].id
          console.log(movie_id)
          dispatch("search", movie_id)
          // dispatch("test1")
        })
        .catch(err => {
          console.log(err)
        })
        .catch(err => {
          console.log(err)
          router.push({ name: 'mainpage' }).catch(err => err)
        })
    },
  },
}
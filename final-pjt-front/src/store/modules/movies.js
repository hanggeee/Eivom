import router from '@/router';
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'
const URL = "https://api.themoviedb.org/3/search/movie"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default{
  // state는 절대 직접 접근하지 않음.

  state: {
    // token: "",
    movie_data: {},
    movie: localStorage.getItem('movie') || {},
    // movie: {},
    comments: {},
    currentUser: {},
  },
  getters: {
    currentUser: state => state.currentUser,
    get_movie_data: state => state.movie_data,
    get_movie: state => state.movie,
    get_comments: state => state.comments,
    // isLiking: state => _.includes(state.movie_data.like_user, state.currentUser.pk),
    isLiking: state => _.some(state.movie_data.like_user, {"pk":state.currentUser.pk}),
  },
  mutations:{
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_MOVIE_DATA: (state, movie) => state.movie_data = movie,
    SET_MOVIE_ID: (state, movie) => state.movie = movie,
    SET_COMMENT: (state, comments) => state.comments = comments,
    SET_MOVIES_COMMENT: (state, comments) => (state.movie.comment = comments),
  },
  actions:{
    search: function({ commit }, movie_id ) {
      // console.log("서치")
      axios({
        url: drf.movies.movie(movie_id),
        method: 'get',
      })
        .then(res => {
          console.log(res.data.movie_id)
          localStorage.setItem('movie', res.data.movie_id)
          commit("SET_MOVIE_ID", movie_id)
          commit('SET_MOVIE_DATA', res.data)
            axios({ 
              url: "http://localhost:8000/movies/" + res.data.movie_id + '/comments/',
              method: 'get',
            })
              .then(res => {
                console.log(res.data)
                commit("SET_COMMENT", res.data)
                
              })
              .catch(err => {
                // console.log("ehck")
                if (err.response.status === 404) {
                  commit("SET_MOVIES_COMMENT", {})
                  router.push({ name: 'moviedetail', params: { movie_id: movie_id }})
                }
              })

          router.push({ name: 'moviedetail', params: { movie_id: movie_id }}).catch(err => err)
          // router.go()
        })
        .catch(err => {
          console.log(err)
          router.push({ name: 'mainpage'}).catch(err => err)
        })
    },
    
    search_movie_ID: function ({ commit, dispatch }, search_movie) {
      // console.log(search_movie)
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
          dispatch("search", movie_id)
          commit("SET_MOVIE_DATA", res.data.results[0])
        })
        .catch(err => {
          console.log(err)
        })
        .catch(err => {
          console.log(err)
          router.push({ name: 'mainpage' }).catch(err => err)
        })
    },
		create_movie_Comment({ commit, getters }, { movie_id, content, rate }) {
      console.log(movie_id)
      console.log(content)
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
          */
      const comment = { content, rate }
      console.log(comment)
      axios({
        url: drf.movies.movie_comment(movie_id),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIES_COMMENT', res.data)
        })
        .catch(err => console.error(err.response))
    },

    delete_movie_Comment({ commit, getters }, { moviePk, commentPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.movie_comment_delete(moviePk, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIES_COMMENT', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
      update_movie_Comment({ commit, getters }, { moviePk, commentPk, content }) {
        /* 댓글 수정
        PUT: comment URL(댓글 입력 정보, token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
        */
        const comment = { content }
  
        axios({
          url: drf.movies.movie_comment_delete(moviePk, commentPk),
          method: 'put',
          data: comment,
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIES_COMMENT', res.data)
          })
          .catch(err => console.error(err.response))
      },
      likeMovie({ commit, getters }, moviePk) {
        /* 좋아요
        POST: likeMovie URL(token)
          성공하면
            state.article 갱신
          실패하면
            에러 메시지 표시
        */
        axios({
          url: drf.movies.likeMovie(moviePk),
          method: 'post',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_MOVIE_DATA', res.data))
          .catch(err => console.error(err.response))
      },
  },
}
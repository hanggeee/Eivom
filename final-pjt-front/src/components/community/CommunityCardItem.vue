<template>
  <div>
    <div class="containers" :style="`background: url('https://image.tmdb.org/t/p/original${poster_path}')`">
        <!-- <img :src="`https://image.tmdb.org/t/p/original${poster_path}`" alt=""> -->
        <div class="overlay">
          <div class = "items"></div>
          <div class = "items head">
            <p>{{ title }}</p>
            <hr>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const REC = 'recommendations'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

let num1 = _.random(100, 957)
export default {
data: function(){
    return {
      movieID: 453395,
      title: '',
      original_title: '',
      backdrop_path: '',
      genres: [],
      release_date: '',
      runtime: '',
      vote_average: '',
      overview: '',
      poster_path: '',
      menubar: true,
    }
  },
  created() {
    console.log(num1)
    axios.get(URL + num1 + REC, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    })
      .then(res => {
      console.log(res.data)
      this.title = res.data.title
      this.poster_path = res.data.poster_path
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

  }
}
</script>

<style scoped>

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

/* 영화추천 card */
  img {
    width: 300px;
    height: 450px;
    position: absolute;
    border-radius: 9px;
  }
.containers {
  background-repeat: no-repeat;
  background-size: cover !important;
  width: 300px;
  height: 450px;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  margin: auto;
  background-color: black;
  background-size: cover;
  cursor: pointer;
  -webkit-box-shadow: 0 0 5px #000;
  box-shadow: 0 0 5px #000;
  border-radius: 9px;
}
.overlay {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr 2fr 2fr 1fr;
  background: rgba(53, 53, 53, 0.505);
  color: #ffffff;
  opacity: 0;
  transition: all 1.0s;
  font-family: 'Noto Sans KR',  sans-serif;
  font-weight: 500;
  border-radius: 9px;
}

.items {
  padding-left: 20px;
  letter-spacing: 3px;
}

.head {
  font-size: 30px;
  line-height: 40px;
  transform: translateY(40px);
  transition: all 0.7s;
}

.head hr {
  display: block;
  width: 0;
  border: none;
  border-bottom: solid 2px #FEF5DF;
  position: absolute;
  left: 20px;
  transition: all 0.5s;
}

.price {
  font-size: 22px;
  line-height: 10px;
  font-weight: bold;
  opacity: 0;
  transform: translateY(40px);
  transition: all 0.7s;
}
.price .old {
  text-decoration: line-through;
  color: #b3b3b3;
}

.cart {
  font-size: 12px;
  opacity: 0;
  letter-spacing: 1px;
  font-family: "Lato", sans-serif;
  transform: translateY(40px);
  transition: all 0.7s;
}
.cart i {
  font-size: 16px;
}
.cart span {
  margin-left: 10px;
}

.containers:hover .overlay {
  opacity: 1;
}
.containers:hover .overlay .head {
  transform: translateY(0px);
}
.containers:hover .overlay hr {
  width: 75px;
  transition-delay: 0.4s;
}
.containers:hover .overlay .price {
  transform: translateY(0px);
  transition-delay: 0.3s;
  opacity: 1;
}
.containers:hover .overlay .cart {
  transform: translateY(0px);
  transition-delay: 0.6s;
  opacity: 1;
}
</style>
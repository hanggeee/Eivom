<template>
  <div id="app">
    <nav>
      <ul class="nav align-items-center justify-content-between">
        <div class="d-flex align-items-center justify-content-between">
          <div class="">
            <router-link to="/" class="nav-link text-secondary">
              <img src="./assets/Eivom_uppercase.png" alt="" class="nav-link">
          </router-link>
          </div>

          <li class="nav-item short_menu">
            <router-link to="/" class="nav-link text-secondary"
            active-class="active">메인</router-link>
          </li>

          <li class="nav-item long_menu">
            <router-link to="/recommend" class="nav-link text-secondary"
            active-class="active">추천</router-link>
          </li>

          <li class="nav-item long_menu">
            <router-link to="/community" class="nav-link text-secondary"
            active-class="active">광장</router-link>
          </li>
          
        </div>

        <div class="d-flex me-3">
          <!-- <router-link to="/" class="nav-link fw-bold text-secondary"
            active-class="active">Search icon</router-link> -->
          <div>
            <div class="search-form">
              <div class="search-box">
                <input type="text" @keydown.enter="search_movie_ID(search_movie)" v-model="search_movie"/>
                <span></span>
              </div>
            </div>
          </div>
          <router-link :to="{ name : 'profile', params: { username: currentUser.username} }" class="nav-link text-secondary"
            active-class="active" v-if="isLoggedIn" style="font-size:22px; color: gray !important;"><i class="fa-solid fa-circle-user"></i></router-link>
          <router-link to="/logout" class="nav-link text-secondary"
            active-class="active" v-if="isLoggedIn" style="font-size:22px; color: gray !important;"><i class="fa-solid fa-arrow-right-from-bracket"></i></router-link>
          <router-link to="/login" class="nav-link text-secondary"
            active-class="active" v-else style="font-size:22px; color: gray !important;"><i class="fa-solid fa-arrow-right-to-bracket"></i></router-link>
        </div>
      </ul>
    </nav>
    <router-view/>

    <footer class="fs-3 text-center">
      <div class="foot d-flex justify-content-center align-items-center" style="height: 100px">
        <div class="">
          <div><a href="https://github.com/DasisCore/last-project"><i class="fa-brands fa-github"></i></a></div>
          <div style="font-size: 10px;">MADE BY</div>
          <div class="d-flex">
            <div style="font-size: 15px; margin-right: 10px;">Hyeoungjun Yoon</div>
            <div style="font-size: 15px; margin-left: 10px;">Jaeyoung Heo</div>
          </div>
        </div>
      </div>
    </footer>

    <div style="position:fixed; top: 92%; left: 96%; color: rgba(115, 115, 115, 0.709); z-index: 1000">
      <div class="posit" style="cursor:pointer;" onclick="window.scrollTo(0,0);"><i class="fa-solid fa-circle-chevron-up fa-3x"></i></div>
    </div>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'App',
  components: {

    },
  data: function() {
    return {
      search_movie: "",
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'search_movie_ID']),
  },
  created() {
    this.fetchCurrentUser()
  }
  
}
</script>

<style scoped>
  @import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css";
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

  a {
    text-decoration: none;
    color: rgb(255, 255, 255);
  }

  posit {
    display: none;
    position: absolute;
    bottom: 100px;
    right: 100px;
  }

  footer {
    background-color: #24292f;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 300;
    color: white;
    height: 100px;
  }


  nav {
  height: 100%;
  font-family: 'Noto Sans KR',  sans-serif;
  font-weight: 500 !important;
  font-size: 14px;
  background-color: #f5f5f7;
  }
  
  .short_menu:hover:after {
  content: "";
  display: block;
  width: 30px;
  border-bottom: 2px solid #bcbcbc;
  margin: 3px auto;
  }

  .long_menu:hover:after {
  content: "";
  display: block;
  width: 30px;
  border-bottom: 2px solid #bcbcbc;
  margin: 3px auto;
  }


  img {
    height: 3.5rem;
  }

  .active {
    color: black !important;
  }


  @import url(https://fonts.googleapis.com/css?family=Open+Sans:300);

  h1{ 
    text-align:center; 
    font-family: 'Noto Sans KR',  sans-serif;
    font-size:24px; 
    margin-top:10%; 
    color:#33739A;
  }
  
  /* 서치 아이콘 위치 설정 */
  .search-form {
    /* position: absolute; */
    /* right: 20%;
    left: 90%; */
    /* top: 100px; */
    margin-right: 10px;
    margin-top: 16px;
    transform: translate(-0%);
  }

  .search-box input[type="text"] {
    border: none;
    background: none;
    z-index: 1;
    width: 25px;
    height: 20px;
    transition: all .25s ease-in .25s;
    color: transparent;
    font-size: .75rem;
    line-height: 25px;
  }
  .search-box input[type="text"]:hover {
    cursor: pointer;
  }
  .search-box input[type="text"]:hover:focus {
    cursor: text;
  }
  .search-box input[type="text"]:hover + span {
    background: rgba(255, 255, 255, 0.2);
  }
  .search-box input[type="text"]:focus {
    width: 250px;
    padding: 0px 15px;
    outline: none;
    color: black;
    background: none;

  }
  .search-box input[type="text"]:focus + span {
    top: -6px;
    width: 250px;
    height: 30px;
    border: none;
    background: #c5c5c5e5;
  }
  .search-box input[type="text"]:focus + span::before {
    width: 2px;
    opacity: 0;
    transition: all .25s ease-in;
  }
  .search-box input[type="text"] + span {
    z-index: -1;
    position: absolute;
    border: 2px solid #948C8C;
    top: 0;
    width: 15px;
    height: 15px;
    transition: all .25s ease-in .25s;
    border-radius: 25px;
    left: 0px;
  }
  .search-box input[type="text"] + span::before {
    transition: all .25s ease-in .5s;
    transform-origin: left top;
    content: '';
    position: absolute;
    width: 8px;
    height: 4px;
    border-radius: 5px;
    background:#948C8C;
    transform: rotate(45deg) translate(26px, -2px);
    top: -9px;
    left: -9px;
  }
</style>

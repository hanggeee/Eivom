<template>
  <div id="main" class="d-flex">
      <div class="login_logo display-4">
        로그인
      </div>
    <div class="container d-flex align-items-center justify-content-center">
      <div class="d-flex justify-content-center align-items-center mb-5">
          <div>
            <account-error-list v-if="authError"></account-error-list>
            <div>
              <form @submit.prevent="login(credentials)" id="userInfo" name="userInfo">
                <div class="login-form">
                  <div class="backbtn" id="backbtn" @click="back">
                    <i class="fa-solid fa-reply"></i>
                  </div>
                  <div class="phases" id="phase-form">
                    <div class="phase-1">
                      <input id="username" v-model="credentials.username" autocomplete="off" type="text" placeholder="User ID">
                      <button @click.prevent="next"><i class="fa-solid fa-circle-arrow-right"></i></button>
                    </div>
                    <div class="phase-2">
                      <input type="password" v-model="credentials.password" id="password" @keydown.esc="back" @keydown.enter="submitForm" placeholder="Enter password">
                      <button @click="submitForm"><i class="fa-solid fa-circle-arrow-right"></i></button>      
                    </div>
                  </div>
                  <div class="loading"></div>
                </div>
              </form>
            </div>

            <div>
              <div class="separator" style="width:100%; max-width: 328px; margin:auto; height: 1px; background-image: url(https://appleid.cdn-apple.com/appleauth/static/bin/cb1633718600/dist/assets/HR_gradient_dark.png); background-size: cover;"></div>
              <div class="text-center sign_up">
                <div class="mt-4">계정이 없으신가요?</div>
                <router-link to="/signup" class="nav-link" active-class="active">지금 바로 만들러 가기</router-link>
              </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/account/AccountErrorList.vue'
export default {
  name: 'LoginView',
  components: {
      AccountErrorList,
    },
  data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
        state: false,
      }
    },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login']),

    // 로그인 폼 관련 js
    trim: function(str) {
      str = str.replace(/^\s+/, "");
      for (var i = str.length - 1; i >= 0; i--) {
        if (/\S/.test(str.charAt(i))) {
          str = str.substring(0, i + 1);
          break;
        }
      }
      return str;
    },
    next() {
      // var username = this.trim(document.getElementById("username").value);
      let username = document.getElementById("username").value
      if (username) {
        document.getElementById("backbtn").classList.add("active");
        // document.getElementById("backbtn").classList.add("next");
        document.getElementById("phase-form").classList.add("next");
        setTimeout(function() {document.getElementById("password").focus()}, 250)
        
        try {
          document.getElementById("username").classList.remove("error");
        } catch {
          console.log("remove")
        }
        this.state = true;
      } else {
        document.getElementById("username").classList.add("error");
      }
    },
    submitForm() {
      var password = this.trim(document.getElementById("password").value);
      if (password) {
        //Submit form ...
        document.getElementsByClassName("loading")[0].classList.add("show-it");
        setTimeout(() => { this.login(this.credentials) }, 1300)
        // setTimeout(this.login(this.credentials), 3000)
        // this.login(this.credentials)
      } else {
        document.getElementById("password").classList.add("error");
      }
    },
    back() {
      if (this.state) {
        document.getElementById("backbtn").classList.remove("active");
        document.getElementById("phase-form").classList.remove("next");
        this.credentials.username = ""
        this.credentials.password = ""
        setTimeout(function() {document.getElementById("username").focus()}, 250)
        this.state = false;
      }
    },
  },
}




</script>

<style scoped>

  @import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  @import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css";
  

  .login_logo {
    position: absolute;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    color: #1d1d1f;
    padding-left: 20%;
    padding-top: 5%;
    /* left: 20%;
    top: 10%; */
  }

  #main {
    height: 1150px;

  }

  .separator {
    width:100%;
    max-width: 328px; 
    margin:auto; 
    height: 1px; 
    background-image: url(https://appleid.cdn-apple.com/appleauth/static/bin/cb1633718600/dist/assets/HR_gradient_dark.png); 
    background-size: cover;
  }

  .sign_up {
    color: #494949;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 400;
  }

  .sign_up > a {
    text-decoration-line: none;
    color: #0070c9;
  }


  .login-form {
    margin:0px;
    padding:0px;
    box-sizing:border-box;
    font-family: 'Noto Sans KR',  sans-serif;

    position:relative;
    /* top:50%;
    left:50%; */
    /* transform:translate(-50%,-50%); */
    transform:translate(0%,0%);
    width: 350px;
    height: 100px;
    background: rgba(144, 61, 61, 0);
    box-shadow: 0px 5px 80px 0px #e4e8f000;
    overflow:hidden;
  }
  
  .login-form .backbtn {
    position:relative;
    top: 10px;
    left: 10px;
    background:#d0d0d0;
    width: 25px;
    height: 25px;
    text-align: center;
    line-height: 25px;
    border-radius: 50%;
    color:#fff;
    cursor:not-allowed;
    transition:all 200ms ease;
    visibility: hidden;
  }
  .login-form .backbtn.active {
    background:#647ace;
    cursor:pointer;
  }
  .login-form .backbtn.disabled {
    background:#eee;
  }
  .phases {
    position:relative;
    top: 10px;
    /* height:200px; */
    width: 200%;
    left: 0%;
    transition:all 300ms ease;
  }
  .phases  div {
    width: 50%;
    float: left;
    display: flex;
    flex-direction:column;
    padding: 0px 20px;
  }
  .phases div * {
    margin: -4px -10px;
  }
  .phases div input {
    height: 40px;
    border: 1px solid #d6d6d6;
    padding-left: 10px;
    border-radius: 7px;
  }
  #username:focus {
    height: 40px;
    /* border: 4px solid #0070c9 !important; */
    border-width: 1px;
    border-color: #0070c9;
    box-shadow: 0 0 0 1px #0070c9;
    z-index: -10000;
    padding-left: 10px;
    border-radius:7px;
    outline: none;
  }

  #password:focus {
    height:40px;
    /* border: 4px solid #0070c9 !important; */
    border-width: 1px;
    border-color: #0070c9;
    box-shadow: 0 0 0 1px #0070c9;
    z-index: -10000;
    padding-left: 10px;
    border-radius: 7px;
    outline: none;
  }

  .phases div input.error {
    border-color:tomato;
  }

  .phases div button {

    position: relative;
    top: -24px;
    left: 300px;
    background:#d0d0d0;
    width:23px;
    height:23px;
    text-align:center;
    line-height:0px;
    border-radius:50%;
    border: none;
    font-size: 25px;
    color:#ffffff;
    transition:all 200ms ease;
    z-index: 99999px !important;
  }
  .phases.next {
    left:-100%;
  }
  .loading {
    position:absolute;
    top:0px;
    left:0px;
    width:100%;
    height:100%;
    background:#ffffff;
    display:none;
    z-index:2;
  }
  .loading.show-it {
    display:inline-block;
  }
  .loading:before {
    content:"";
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%) rotate(0deg);
    width:50px;
    height:50px;
    border:5px solid #eee;
    border-top-color:#b3b3b3;
    border-radius:50%;
    animation:loading 900ms ease infinite;
  }
  @keyframes loading {
    to {
      transform:translate(-50%,-50%) rotate(360deg);
    }
  }



</style>
<template>
  <div id="main" class="d-flex">
    <div class="login_logo display-4">
      회원가입
    </div>
    <div class="container d-flex align-items-center justify-content-center">
      <div class="d-flex justify-content-center align-items-center mb-5">
        <div>
          <account-error-list v-if="authError"></account-error-list>
          <div>
            <form @submit.prevent="signup(credentials)">
              <div class="login-form">
                <div class="phases" id="phase-form">
                  <div class="phase-1">
                    <input id="username" v-model="credentials.username" autocomplete="off" type="text" placeholder="아이디를 입력하세요." required>
                    <input type="password" v-model="credentials.password1" id="password1" autocomplete="off"  placeholder="비밀번호를 입력하세요." required>
                    <input type="password" v-model="credentials.password2" id="password2" autocomplete="off"  @keydown.enter="submitForm" placeholder="비밀번호 확인" required>
                  </div>
                  <div>
                    <div class="separator mt-4" style="width:100%; max-width: 328px; margin:auto; height: 1px; background-image: url(https://appleid.cdn-apple.com/appleauth/static/bin/cb1633718600/dist/assets/HR_gradient_dark.png); background-size: cover;"></div>
                    <div class="text-center sign_up">
                      <div class="mt-4 mb-4">Eivom의 가족이 될 준비가 되었나요?</div>
                      <button class="btn btn-primary ms-4 me-4">회원가입</button>
                    </div>
                  </div>                  
                </div>
              </div>
            </form>
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
  name: 'SignUpView',
  components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
}
</script>

<style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
  @import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css";

  .login_logo {
    position: absolute;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    color: #1d1d1f;
    padding-left: 20%;
    padding-top: 5%;
  }

  #main {
    height: 1150px;
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

  button {
    font-family: 'Noto Sans KR',  sans-serif;
  }


  .login-form {
    margin:0px;
    padding:0px;
    box-sizing:border-box;
    font-family: 'Noto Sans KR',  sans-serif;
    position:relative;
    width: 400px;
    background: rgba(144, 61, 61, 0);
    box-shadow: 0px 5px 80px 0px #e4e8f000;
    overflow:hidden;
  }
  
  .phases {
    top: 10px;
    left: 0%;
  }
  .phases  div {
    display: flex;
    flex-direction:column;
    padding: 0px 20px;
  }
  .phases div * {
    margin: 5px;
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

  #password1:focus {
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

  #password2:focus {
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

  .separator {
    width:100%;
    max-width: 328px; 
    margin:auto; 
    height: 1px; 
    background-image: url(https://appleid.cdn-apple.com/appleauth/static/bin/cb1633718600/dist/assets/HR_gradient_dark.png); 
    background-size: cover;
  }

</style>
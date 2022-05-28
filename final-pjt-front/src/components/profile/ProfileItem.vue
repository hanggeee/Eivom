<template>
  <div class="app9" >
    <div id="back_profile" :style="`background-color:${colors[random_num]}`">
      <div id="movie_logo"> 계정 </div>
      <div class="d-flex justify-content-center">
        <div id="main_profile"  class="d-flex justify-content-between">
          <div class="d-flex flex-column">
            <router-link :profile_img="profile.profile_img" v-if="currentUser.username == profile.username" :to="{ name: 'profileImg', params : { username: profile.username } } ">
              <div class="changeText">프로필 사진 변경</div>
              <img v-if="profile.profile_img" :src="profile.profile_img">
              <img v-else class="profile" src="@/assets/default_profile.jpg">
            </router-link>
            <div v-else>
              <img v-if="profile.profile_img" :src="profile.profile_img">
              <img v-else class="profile" src="@/assets/default_profile.jpg">
            </div>
          </div>
          <div class="d-flex flex-column" style="margin-top: 80px">
            <div class="d-flex justify-content-between">
              <div style="font-size: 50px">
                <div v-if="currentUser.username == profile.username" style="margin:0;">어서와요!</div>
                <div>{{ profile.username }}<span v-if="currentUser.username == profile.username" style="margin:0; font-size:50px">.</span><span v-else style="margin:0; font-size:50px">의</span></div>
                <div class="d-flex align-items-center">
                  <div v-if="currentUser.username != profile.username" style="margin:0; font-size:50px; font-weight: 500">프로필</div>
                    <button v-if="currentUser.username != profile.username" id="follow" @click="followProfile(username)" class="heart-button" :class="{active : isFollowing}">
                      <div class="heart-flip"></div>
                      <span>follow<span>ed</span></span>
                    </button>
                </div>
              </div>

              <!-- 본인 프로필이면 팔로우 버튼 x
              팔로우 상태면 언팔로우버튼
              언팔로우 상태면 팔로우버튼 -->
            </div>
            <div>
              <span>{{ likeCount }} movie &nbsp;</span>
              <span>{{ followersCount }} followers &nbsp;</span>
              <span>{{ followingsCount }} followings</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from "lodash"

import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'profile_item',
  computed: {
      ...mapGetters(['profile', 'notMyAccount', 'isFollowing', 'currentUser']),
      likeCount() {
        return this.profile.like_movies?.length
      },
      followersCount() {
        return this.profile.followers?.length
      },
      followingsCount() {
        return this.profile.followings?.length
      },
    },
    
  data() {
    return {
      username: this.$route.params.username,
      colors : ["#F4BFBF", "#CCF3EE" ,"#E3FCBF", "#FFE69A", "#FFF6EA", "#B3E8E5", ],
      // 빨: F4BFBF 파:CCF3EE  초: E3FCBF 노:FFE69A 보:F0D9FF 베이지:FFF6EA 민트:B3E8E5 흰:FFFFFF
      random_num: 0,
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'followProfile', 'updateImg']),

  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    this.random_num = _.random(0, 5)

  },
  mounted() {
    document.querySelectorAll('.heart, .heart-button').forEach(button => button.addEventListener('click', () => button.classList.toggle('active')));
  }
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
  * {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
  }

  img {
    border-radius: 70%;
    margin-right: 15px;
    width: 300px;
    height: 300px;
  }

  a {
    border-radius: 70%;
    margin-right: 15px;
  }
  a:hover img {
    transition: all 0.3s;
    filter: brightness(65%);
  }
  a:hover .changeText {
    
    opacity: 1;
  }
  .changeText {
    font-weight: 700;
    transition: all 0.1s;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    width: 300px;
    height: 300px;
    opacity: 0;
    color: white;
    -webkit-text-stroke: 0.6px black;
    font-size: 27px;
    z-index: 10;
  }
  #back_profile {
    height: 37rem;
  }

  #movie_logo {
    padding: 50px 50px 50px 200px;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 2.0rem
  }

  #movie_logo:after {
  content: "";
  display: block;
  width: 56px;
  border-bottom: 2px solid #bcbcbc;
  margin: 3px auto;
  position: absolute;
  margin-left: 3px;
  }

  #main_profile {
    width: 800px
  }

  span {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 1.31rem;
  }
  #follow {
    height: 40px;
  }

  #follow span {
    font-size: 0.9rem;
  }

  .heart,
  .heart-button {
    cursor: pointer;
    outline: none;
    -webkit-appearance: none;
    -webkit-tap-highlight-color: transparent;
  }
  .heart .heart-flip,
  .heart-button .heart-flip {
    --base: 32px;
    --duration: .6s;
    --active: #ea4673;
    --inactive: #d1d6ee;
    width: var(--base);
    height: calc(var(--base) + var(--base) / 2);
    border-radius: calc(var(--base) / 2) calc(var(--base) / 2) 0 0;
    position: relative;
    transform-origin: 50% 66.66%;
    transform-style: preserve-3d;
    transform: rotate(var(--rotate, -45deg));
    transition: background var(--duration), transform var(--duration) ease;
    background: var(--heart-background, var(--inactive));
  }
  .heart .heart-flip:before, .heart .heart-flip:after,
  .heart-button .heart-flip:before,
  .heart-button .heart-flip:after {
    content: "";
    width: calc(var(--base) / 2);
    height: var(--base);
    border-radius: var(--pseudo-border-radius, calc(var(--base) / 2) 0 0 calc(var(--base) / 2));
    position: absolute;
    left: var(--pseudo-left, -50%);
    transform-origin: var(--pseudo-origin, 100%) 50%;
    bottom: 0;
    background: var(--heart-background, var(--inactive));
    filter: brightness(var(--pseudo-filter, 50%));
    transform: translateX(1%) rotateY(var(--pseudo-rotate, 90deg)) translateZ(0);
    transition: background var(--duration), transform var(--duration) ease, filter var(--duration);
  }
  .heart .heart-flip:after,
  .heart-button .heart-flip:after {
    --pseudo-border-radius: 0 calc(var(--base) / 2) calc(var(--base) / 2) 0;
    --pseudo-left: 100%;
    --pseudo-origin: 0;
    filter: brightness(var(--pseudo-filter-second, 100%));
    transform: translateX(-1%) rotateY(var(--pseudo-rotate-second, 0deg)) translateZ(0);
  }
  .heart.active .heart-flip,
  .heart-button.active .heart-flip {
    --rotate: 45deg;
    --pseudo-filter: 100%;
    --pseudo-filter-second: 50%;
    --pseudo-rotate: 0deg;
    --pseudo-rotate-second: 90deg;
    --heart-background: var(--active);
  }

  .heart {
    background: none;
    border: none;
    padding: 0;
    transform: scale(var(--button-scale, 1)) translateZ(0);
    transition: transform 0.2s;
  }
  .heart:active {
    --button-scale: .95;
  }

  .heart-button {
    --duration: .4s;
    --color: #404660;
    --color-hover: #2b3044;
    --color-active: #fff;
    --border: #d1d6ee;
    --border-hover: #bbc1e1;
    --border-active: #ea4673;
    --background: #fff;
    --background-active: #ea4673;
    font-family: inherit;
    font-size: 14px;
    line-height: 1.6;
    font-weight: 600;
    padding: 6px 16px;
    border-radius: 7px;
    color: var(--button-color, var(--color));
    border: 1px solid var(--button-border, var(--border));
    background: var(--button-background, var(--background));
    transform: scale(var(--button-scale, 1)) translateZ(0);
    transition: background var(--duration), border-color var(--duration), color var(--duration), transform 0.2s;
  }
  .heart-button .heart-flip {
    --base: 8px;
    --active: #fff;
    --inactive: #bbc1e1;
    display: inline-block;
    vertical-align: top;
    margin: 4px 6px 0 0;
  }
  .heart-button span {
    display: inline-block;
    vertical-align: top;
  }
  .heart-button > span {
    transform: translateX(var(--text-x, 4px));
    transition: transform var(--duration);
  }
  .heart-button > span span {
    display: inline-block;
    vertical-align: top;
    opacity: var(--span-opacity, 0);
    transform: translateX(var(--span-x, 4px));
    transition: opacity var(--duration), transform var(--duration);
  }
  .heart-button:active {
    --button-scale: .95;
  }
  .heart-button:hover {
    --button-color: var(--color-hover);
    --button-border: var(--border-hover);
  }
  .heart-button.active {
    --text-x: 0;
    --button-color: var(--color-active);
    --button-border: var(--border-active);
    --button-background: var(--background-active);
    --span-opacity: 1;
    --span-x: 0;
  }

  html {
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
  }

  * {
    box-sizing: inherit;
  }
  *:before, *:after {
    box-sizing: inherit;
  }

  body {
    font-family: "Inter", Arial;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background: #F6F8FF;
  }
  body .heart-button {
    margin-left: 20px;
    margin-top: 15px;
  }
</style>
<template>
  <div class="m-3 carousel card">
    <a :href="search_naver" target="_blank">
      <p class="carousel-text">{{actor.name}}</p>
      <div class="carousel-bg"></div>
      <img v-if="actor.profile_path == null" src="@/assets/annonymous.jpg" alt="actor">
      <img v-else :src="actorImg" alt="actor">

    </a>
  </div>
</template>

<script>

export default {
  name: 'movie_actors_item',
  props: {
    actor: Object
  },
  computed: {
    actorImg() {
      // console.log("https://image.tmdb.org/t/p/original/" + this.actor.profile_path)
      return "https://image.tmdb.org/t/p/w500/" + this.actor.profile_path
    },
    search_naver() {
      return "https://search.naver.com/search.naver?query=" + this.actor.name
    }
  }

}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');


  .carousel {
    position: relative;
    border-radius: 7px;
    overflow: hidden;
  }
  .carousel-text {
    position: absolute;
    bottom: 10px;
    margin-left: 7px;
    z-index: 551;
    color: #ffffff;
    font-size: 1.5rem;
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    width: 160px;
  }
  .carousel-bg {
    width: 100%;
    position: absolute;
    bottom: 0px;
    height: 100%;
    background: linear-gradient(transparent, #000000);
    opacity: 0.6;
    z-index: 550;
  }

  .card {
    transition: all .4s cubic-bezier(0.175, 0.885, 0, 1);
    position: relative;
    overflow: hidden;
  }
  .card:hover {
    transform: scale(1.10, 1.10);
  }
</style>
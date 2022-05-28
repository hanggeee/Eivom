<template>
  <div>
    <div class="youplay-carousel">
      <a class="angled-img" :href="`http://localhost:8080/moviedetail/${ movie.id }`">
        <div class="img">
          <img :src="poster_img" alt="poster">
        </div>
      </a>
    </div>
  </div> 
</template>

<script>
export default {
  name: "MovieCardItme",
  props: {
    movie: Object,
  },
  computed: {
    poster_img() {
      return "https://image.tmdb.org/t/p/original/" + this.movie.poster_path
    }
  }
}
</script>

<style scoped>

  .angled-img {
    position: relative;
    display: block;
    shape-outside: polygon(9% 0, 0 100%, 91% 100%, 100% 0%);
  }
  .angled-img, .angled-img:hover, .angled-img:focus {
    color: inherit;
    text-decoration: none;
    outline: none;
  }
  .angled-img .img {
    position: relative;
    overflow: hidden;
    transform: skew(-8deg);
    transform-origin: 50% 50%;
    background: #131313;
    -webkit-backface-visibility: hidden;
  }
  .angled-img .img > img {
    width: 120%;
    transform: skew(8deg) scale(1.15);
    transition: 0.3s opacity ease;
    -webkit-backface-visibility: hidden;
    opacity: 0.6;
    height: 600px;
  }
  .angled-img:hover .img > img {
    opacity: 0.9;
  }


  .youplay-carousel .angled-img {
    margin-left: -1px;
  }
  .youplay-carousel .owl-nav {
    margin: 0;
  }
  .youplay-carousel .owl-nav .owl-prev,
  .youplay-carousel .owl-nav .owl-next {
    position: absolute;
    cursor: pointer;
    font-size: 2rem;
    top: 0;
    height: 100%;
    width: 70px;
    transition: 0.3s opacity ease;
    opacity: 1;
    margin: 0;
    padding: 0;
  }
  .youplay-carousel .owl-nav .owl-prev:hover,
  .youplay-carousel .owl-nav .owl-next:hover {
    opacity: 0.8;
  }
  .youplay-carousel .owl-nav .owl-prev,
  .youplay-carousel .owl-nav .owl-prev:hover {
    left: 0;
    background: linear-gradient(to right, #131313, rgba(19, 19, 19, 0));
  }
  .youplay-carousel .owl-nav .owl-next,
  .youplay-carousel .owl-nav .owl-next:hover {
    right: -0.1px;
    background: linear-gradient(to left, #131313, rgba(19, 19, 19, 0));
  }
</style>
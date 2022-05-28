<template>
  <div >
    <div id="comment_list" class="container">
      <div id="comment">댓글</div>
      <div>
        <movie-comment-item v-for="comment in get_comments" :key="comment.id" :comment="comment"></movie-comment-item>
      </div>
      
      <div v-if="isLoggedIn" id="comment_writer">
        <form @submit.prevent="create_movie_Comment(commentform); add();">
          <div class="d-flex row" style="margin: 10px 10px 10px 10px;">
            <div>
              <div class="d-flex justify-content-between">
                <div>
                  <div>
                    <label for="comment_w" id="user">{{ currentUser.username }}</label>
                  </div>
                </div>
                <div class="stars">
                  <input type="radio" name="star" class="star-1" id="star-1" v-model="commentform.rate" value="1" />
                  <label class="star-1" for="star-1">1</label>
                  <input type="radio" name="star" class="star-2" id="star-2" v-model="commentform.rate" value="2" />
                  <label class="star-2" for="star-2">2</label>
                  <input type="radio" name="star" class="star-3" id="star-3" v-model="commentform.rate" value="3" />
                  <label class="star-3" for="star-3">3</label>
                  <input type="radio" name="star" class="star-4" id="star-4" v-model="commentform.rate" value="4" />
                  <label class="star-4" for="star-4">4</label>
                  <input type="radio" name="star" class="star-5" id="star-5" v-model="commentform.rate" value="5" />
                  <label class="star-5" for="star-5">5</label>
                  <span></span>
                </div>
              </div>
              <textarea name="" id="comment_w" cols="30" rows="10" autocomplete="off" autocorrect="off" maxlength="200" v-model="commentform.content"></textarea>
            </div>
            <div class=" d-flex justify-content-end">
              <button>등록</button>
            </div>
          </div>
        </form>
      </div>
      <br>
    </div>
  </div>
</template>

<script>
import MovieCommentItem from './MovieCommentItem.vue'
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'movie_comment_list',
  components: {
    MovieCommentItem,
  },
  props:{
    movie_id:Object,
  },
  data: function() {
    return {
      commentform: {
        movie_id: this.$route.params.movie_id,
        content: "",
        rate: 0,
      },
      get_comments: {},
      num: 0,
    }
  },
  methods: {
    ...mapActions(['create_movie_Comment', 'fetchCurrentUser']),
    add(){
      this.num++
    },
  },
  computed: {
    ...mapGetters(['isLoggedIn', "get_comments", 'get_movie', 'currentUser', ]),
  },
  created() {
    axios.get("http://localhost:8000/movies/" + this.$route.params.movie_id + "/comments/", {})
      .then(res => {
        console.log(res.data)
        this.get_comments = res.data
      }),
    this.fetchCurrentUser()
  },
  watch: {
    "num"() {
      location.reload()
    }
  }

}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');


  #comment_list {
    min-width: 500px;
    background-color: #f2f2f2;
    border-radius: 20px;
    /* height: 1000px; */
    margin-bottom: 200px;
  }

  #comment {
    padding: 20px 20px 20px 20px;
    font-family: 'Noto Sans KR',  sans-serif;
    font-size: 3rem;
    font-weight: 700;
    /* border-bottom: 1.5px solid #bcbcbc; */
  }

  #comment_writer {
    margin: 10px 10px 10px 10px;
    background-color: #ffffff;
    border: 2px solid rgba(0, 0, 0, 0.1);
    border-radius: 6px;
    padding: 16px 10px 10px 18px;
  }

  #user {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 900;
    font-size: 17px;
  }

  textarea {
    height: 5.2rem;
    border: none;
    color: black;
    width: 99%;
    font-family: 'Noto Sans KR',  sans-serif;
    padding: 5px 10px 5px 5px;
    outline-color: rgba(255, 255, 255, 0);
    resize: none;
  }

  textarea:focus {
    border: none;
  }

  button {
    border: none;
    background-color: rgba(255, 255, 255, 0);  
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    color: #9a9a9a;
    margin-bottom: 10px;
    margin-right: 10px;
  }

  /* 
  
  */

  body {
    padding: 50px;
  }

  form .stars {
    background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAABaCAYAAACv+ebYAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNXG14zYAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDcvMDMvMTNJ3Rb7AAACnklEQVRoge2XwW3bMBSGPxa9NxtIGzTAW8DdRL7o3A0qb+BrdNIm9QAm0G7gbJBMwB5MoVJNUSRFIXGqHwhkmXr68hOPNH9ljOEt9OlNqBs4RlrrSmtdpdZ/Ti0EGnvtUoqTHFunBVCkuk6d6mbi83rggdteSa5THDeB3+UDO9z2inatXFum1roESuAReAB29vp15n2/gRfgZK+/gIuIXLxgrfUO+Bnzn0fom4ic+pvRVNuB/QrQ/RB6A7bwLjN8b985krO5MsKd0ElwJvgk1AteCPdCYWI5/SutddQxRUTU3DOzG4hd01EKqQnZuaLBITUh4F0CeLYm5CDw6PjuFTjaz9+BLwE1I8VO9StwAEoRaUSkseMHO+aqcWq2qwcdfQCOIvIy8dwDV/c/YL6zvWDbnQ3QuH5hltQEreM1dH/n6g28gT8eWLVUqqVKrb+vtGidFkCR6vp+0uLAba8k1/eRFh1ue0W7dv4sqpaSjGnR1Fy8YNWyY8W0aGpO/c1oqu3AKmlxCL0BW3iXGb637xzJ2VwZ4U7oJDgTfBLqBS+Ee6EQeMpULVFHUVOzPC3aNR2lkJotLbr0vtKiqWlMTcNaaXHQ0QfgaGqcaVG1jNLibGcbYyb/eDIlT6bjyZS+51JqtrS4gTfw/wzWqkKrKrU8fQPR6gKAmDKlPM3x1WkBFKmu0xxf3fZR5jnFdbzjv257JbmOdzx22yvadZzjW7e9ol27HWtVkjEtIubiB2u1Y8W0iJhTfzOe6uvAKmlxCL0FX+FdZvjevnMkd3Plgzuh0+A88EmoH7wM7oVC6AaiVdwuI2Z5WrRrOk4BNVtadOl9pUXENIhpWCstDjr6ABwR40yLaDVKi7Od7U1/Z0pzpjNngtNiaM2WFj8++A+motm0NTqjmwAAAABJRU5ErkJggg==') repeat-x 0 0;
    width: 150px;
    margin: 0 10;
  }
  .ie7 form .stars {
    *zoom: 1;
  }
  form .stars:before, form .stars:after {
    display: table;
    content: "";
  }
  form .stars:after {
    clear: both;
  }
  form .stars input[type="radio"] {
    position: absolute;
    opacity: 0;
    filter: alpha(opacity=0);
  }
  form .stars input[type="radio"].star-5:checked ~ span {
    width: 100%;
  }
  form .stars input[type="radio"].star-4:checked ~ span {
    width: 80%;
  }
  form .stars input[type="radio"].star-3:checked ~ span {
    width: 60%;
  }
  form .stars input[type="radio"].star-2:checked ~ span {
    width: 40%;
  }
  form .stars input[type="radio"].star-1:checked ~ span {
    width: 20%;
  }
  form .stars label {
    display: block;
    width: 30px;
    height: 30px;
    margin: 0 !important;
    padding: 0 !important;
    text-indent: -999em;
    float: left;
    position: relative;
    z-index: 10;
    background: transparent !important;
    cursor: pointer;
  }
  form .stars label:hover ~ span {
    background-position: 0 -30px;
  }
  form .stars label.star-5:hover ~ span {
    width: 100% !important;
  }
  form .stars label.star-4:hover ~ span {
    width: 80% !important;
  }
  form .stars label.star-3:hover ~ span {
    width: 60% !important;
  }
  form .stars label.star-2:hover ~ span {
    width: 40% !important;
  }
  form .stars label.star-1:hover ~ span {
    width: 20% !important;
  }
  form .stars span {
    display: block;
    height: 30px;
    width: 0;
    position: relative;
    top: 0;
    left: 0;
    background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAABaCAYAAACv+ebYAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNXG14zYAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDcvMDMvMTNJ3Rb7AAACnklEQVRoge2XwW3bMBSGPxa9NxtIGzTAW8DdRL7o3A0qb+BrdNIm9QAm0G7gbJBMwB5MoVJNUSRFIXGqHwhkmXr68hOPNH9ljOEt9OlNqBs4RlrrSmtdpdZ/Ti0EGnvtUoqTHFunBVCkuk6d6mbi83rggdteSa5THDeB3+UDO9z2inatXFum1roESuAReAB29vp15n2/gRfgZK+/gIuIXLxgrfUO+Bnzn0fom4ic+pvRVNuB/QrQ/RB6A7bwLjN8b985krO5MsKd0ElwJvgk1AteCPdCYWI5/SutddQxRUTU3DOzG4hd01EKqQnZuaLBITUh4F0CeLYm5CDw6PjuFTjaz9+BLwE1I8VO9StwAEoRaUSkseMHO+aqcWq2qwcdfQCOIvIy8dwDV/c/YL6zvWDbnQ3QuH5hltQEreM1dH/n6g28gT8eWLVUqqVKrb+vtGidFkCR6vp+0uLAba8k1/eRFh1ue0W7dv4sqpaSjGnR1Fy8YNWyY8W0aGpO/c1oqu3AKmlxCL0BW3iXGb637xzJ2VwZ4U7oJDgTfBLqBS+Ee6EQeMpULVFHUVOzPC3aNR2lkJotLbr0vtKiqWlMTcNaaXHQ0QfgaGqcaVG1jNLibGcbYyb/eDIlT6bjyZS+51JqtrS4gTfw/wzWqkKrKrU8fQPR6gKAmDKlPM3x1WkBFKmu0xxf3fZR5jnFdbzjv257JbmOdzx22yvadZzjW7e9ol27HWtVkjEtIubiB2u1Y8W0iJhTfzOe6uvAKmlxCL0FX+FdZvjevnMkd3Plgzuh0+A88EmoH7wM7oVC6AaiVdwuI2Z5WrRrOk4BNVtadOl9pUXENIhpWCstDjr6ABwR40yLaDVKi7Od7U1/Z0pzpjNngtNiaM2WFj8++A+motm0NTqjmwAAAABJRU5ErkJggg==') repeat-x 0 -60px;
    -webkit-transition: -webkit-width 0.5s;
    -moz-transition: -moz-width 0.5s;
    -ms-transition: -ms-width 0.5s;
    -o-transition: -o-width 0.5s;
    transition: width 0.5s;
  }
 
</style>
<template>
  <div class="app">
    <div>
      <div class="d-flex justify-content-around">
        <article-list></article-list>
        <community-card></community-card>  
      </div>
      
    </div>
    
  </div>
</template>

<script>
import ArticleList from '../components/community/ArticleList.vue'
import CommunityCard from '../components/community/CommunityCard.vue'
// import Pagination from '../components/community/Pagination.vue'



export default {
  name: 'CommunityView',
  components: {
    ArticleList, CommunityCard
    // , Pagination
  }
}
</script>

<style scoped>

  .app {
    margin-left: 15rem;
    margin-right: 15rem;
    margin-bottom: 100px;
  }

</style>
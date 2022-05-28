<template>
  <div class="article-comment-list">
    <article-comment-list-item 
      v-for="comment in comments" 
      :comment="comment" 
      :key="comment.pk">
    </article-comment-list-item>        
    <article-comment-list-form></article-comment-list-form>
  </div>
</template>

<script>
import ArticleCommentListItem from '@/components/community/ArticleCommentListItem.vue'
import ArticleCommentListForm from '@/components/community/ArticleCommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { ArticleCommentListForm, ArticleCommentListItem },
  props: { comments: Array },
}
</script>

<style>

</style>
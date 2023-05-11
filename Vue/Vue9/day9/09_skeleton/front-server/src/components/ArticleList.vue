<template>
  <div class="article-list">
    <h3>Article List</h3>
    <ArticleListItem v-for="article in aritcles" :key="article.id"
    :article="article"/>
  </div>
</template>

<script>
import ArticleListItem from './ArticleListItem.vue'
import { mapState } from 'vuex'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    ...mapState({
      aritcles: 'articles'
    })
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>

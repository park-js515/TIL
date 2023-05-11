<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
  </div>
</template>

<script>
const API_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
      })
      .then((response) => {
        console.log(response)
        this.article = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

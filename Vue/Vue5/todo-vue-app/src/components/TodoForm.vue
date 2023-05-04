<template>
  <div>
    <!-- 중요! -->
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
  </div>
</template>

<script>
export default {
  name: "TodoForm",
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      if (this.todoTitle){
        this.$store.dispatch('createTodo', this.todoTitle)
        this.todoTitle = null
      }
      else {
        alert("할 일을 입력하세요!")
      }
    }
  }
}
</script>

<style>

</style>
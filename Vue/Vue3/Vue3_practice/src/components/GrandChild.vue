<template>
  <div> 
    <h2>GrandChild</h2>
    <p>myName: {{ myName }}</p>
    <button @click="changeMyName">부모 함수 실행</button>
  </div>
</template>

<script>
export default ({
    props: {
        myName: String,
    },
    methods: {
        changeMyName() {
            this.$emit("changeMyName", "싸피")
        }
    }
})
</script>

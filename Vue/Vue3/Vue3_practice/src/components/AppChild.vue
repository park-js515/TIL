<template>
  <div>    
    <h2>AppChild</h2>
    <div>myName: {{ myName }}</div>
    <div>myAge: {{ myAge }}</div>
    <button @click="changeMyAge"> 나이 변경</button>
    <GrandChild :myName="myName" @changeMyName="changeMyName"/>
  </div>
</template>

<script>
import GrandChild from '@/components/GrandChild.vue'

export default ({
  components: {
    GrandChild
  },
  props: {
    myName: String,
    myAge: Number,  
  },
  methods: {
    changeMyName(myName) {
      this.$emit("changeMyName", myName)
    },
    changeMyAge() {
      this.$emit("changeMyAge", 20)
    }
  }
    
})
</script>

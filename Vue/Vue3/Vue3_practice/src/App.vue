<template>
  <div>
    <h1>App</h1>
    <div>myName: {{ myName }}</div>
    <div>myAge: {{ myAge }}</div>
    <AppChild 
    :myName="myName" 
    :myAge="myAge" 
    @changeMyName="changeMyName" 
    @changeMyAge="changeMyAge"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild.vue'

export default ({
  components: {
    AppChild
  },
  data() {
    return {
      myName: "ssafy",
      myAge: 40
    }
  },
  methods: {
    changeMyName(myName) {
      this.myName = myName
    },
    changeMyAge(myAge) {
      this.myAge = myAge
    }
  }
})
</script>


<template>
  <div>
    <h1>App</h1>
    <!-- <div>myName: {{ myName }}</div>
    <div>myAge: {{ myAge }}</div> -->
    <button @click="getData">데이터를 가져오자!</button>
    <ul>
      <li v-for="data in datas" :key="data.id">{{ data.title }}</li>
    </ul>
    <AppChild />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild.vue'


export default {
  name: 'App',
  components: {
    AppChild
  },
  data() {
    return {

    }
  },
  computed: {
    // myName() {
    //   return this.$store.state.myName
    // },
    // myAge() {
    //   return this.$store.state.myAge
    // },
    datas() {
      return this.$store.state.datas
    }
  },
  methods: {
    getData() {
      this.$store.dispatch("getDataFromServer")
    }
  },
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

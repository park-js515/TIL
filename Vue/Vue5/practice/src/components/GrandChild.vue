<template>
  <div>
    <h3>GrandChild</h3>
    <!-- <div>myName: {{ myName }}</div>
    <button @click="becomingYoung">젊어지는 버튼</button> -->
  </div>
</template>

<script>
export default {
    name: "GrandChild",
    data() {
        return {

        }
    },
    computed: {
      // myName() {
      //   return this.$store.getters.getMyName
      // },
      // myAge() {
      //   return this.$store.state.myAge
      // }
    },
    methods: {
      // becomingYoung() {
      //   this.$store.dispatch("changeMyAge", 20)
      // }
    },

}
</script>

<style>

</style>
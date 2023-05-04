<template>
  <div>
    <h2>AppChild</h2>
    <!-- <div>myName: {{ myName }}</div>
    <div>myAge: {{ myAge }}</div> -->
    <GrandChild />
  </div>
</template>

<script>
import GrandChild from '@/components/GrandChild.vue'

export default {
  name: "AppChild",
  components: {
    GrandChild
  },
  data () {
    return {

    }
  },
  computed: {
    // myName() {
    //   return this.$store.state.myName
    // },
    // myAge() {
    //   return this.$store.state.myAge
    // }
  },
  methods: {

  },
}
</script>

<style>

</style>
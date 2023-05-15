<template>
  <div>
    <h1>Sign Up Page</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: "",
      password1: "",
      password2: ""
    }    
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch("signUp", payload)
    }
  }
}
</script>

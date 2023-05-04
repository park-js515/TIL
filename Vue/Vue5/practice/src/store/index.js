import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // myName: "ssafy",
    // myAge: 40,
    datas: [],
  },
  getters: {
    // getMyName(state) {
    //   return `제 이름은 ${state.myName}입니다.`
    // }
  },
  mutations: {
    // CHANGE_MY_NAME(state, myName) {
    //   state.myName = myName
    // },
    // CHANGE_MY_AGE(state, myAge) {
    //   state.myAge = myAge
    // },
    CHANGE_DATAS(state, datas) {
      state.datas = datas
    }
  },
  actions: {
    // changeMyName(context, myName) {
    //   context.commit("CHANGE_MY_NAME", myName)
    // },
    // changeMyAge(context, myAge) {
    //   context.commit("CHANGE_MY_AGE", myAge)
    // },
    getDataFromServer(context) {
      axios({
        method: 'GET',
        url: "https://jsonplaceholder.typicode.com/todos",
      })
      .then((response) => {
        context.commit("CHANGE_DATAS", response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  modules: {
  }
})

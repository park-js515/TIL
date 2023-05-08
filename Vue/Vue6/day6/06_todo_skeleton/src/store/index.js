
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
    ]
  },
  getters: {
    alltodosCount(state) {
      return state.todos.length
    },
    // 구현 상 좋지 않다.
    // 실제로는 클릭 또는 제거 시에 반영하는 것이 올바르다.
    // 시간적 복잡도가 좋지 않다.
    completedtodosCount(state) {
      let num = 0
      const todos = state.todos

      todos.forEach((todo) => {
        if (todo.isCompleted) {
          num += 1
        }
      })

      return num
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      // console.log(todoItem) // 삭제 버튼을 누른 todo 찾아서 state.todos에서 제거
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO(state, todoItem) {
      // click한 todo item을 찾고 해당 todo의 todo.islCompleted를 toggle
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) { // 찾아서
          todo.isCompleted = !todo.isCompleted // 뒤집는다.
        }
        return todo
      })
    },
    LOAD_TODOS(state) {
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)

      state.todos = parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // console.log(context)
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    updateTodo(context, todoItem) {
      context.commit('UPDATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    saveTodosToLocalStorage(context) {
      const jsonTodos = JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    },
    loadTodos(context) {
      context.commit('LOAD_TODOS')
    }
  },
  modules: {
  }
})

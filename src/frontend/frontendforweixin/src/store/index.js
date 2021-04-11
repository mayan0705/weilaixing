import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    hasLogin: false,
    userName: '',
    userId: '',
  },
  mutations: {
    setId(state, userId) {
      state.userId = userId
      localStorage.setItem('userId', userId)
    },
    login(state, userName) {
      state.userName = userName || '新用户';
      state.hasLogin = true;
    },
    logout(state) {
      state.userName = '';
      state.hasLogin = false;
    }
  },
});

export default store;

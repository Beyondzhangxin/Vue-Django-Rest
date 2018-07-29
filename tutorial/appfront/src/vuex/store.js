import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  // 定义状态
  state: {
    isShowAside: 0,
  },
  mutations: {
    showIt() {
      this.state.isShowAside = 1;
    },
    hideIt() {
      this.state.isShowAside = 0;
    }
  }
})

export default store

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  // 定义状态
  state: {
    isShowAside: 0,
    chooseTree: [],
  },
  mutations: {
    updateTree(state, element) {
      console.log(element);
      state.chooseTree.push(element);
    },
    cleanTree() {
      this.state.chooseTree = [];
    },
    showIt() {
      this.state.isShowAside = 1;
    },
    hideIt() {
      this.state.isShowAside = 0;
    }
  }
})

export default store

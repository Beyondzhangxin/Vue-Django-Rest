import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  // 定义状态
  state: {
    isShowAside: 0,
    chooseTree: [],
    choosefilter: '系统',
  },
  mutations: {
    updateTree(state, element) {
      //信号量
      var flag = 0;
      for (var i = 0; i < state.chooseTree.length; i++) {
        if (state.chooseTree[i].system == element.system) {
          state.chooseTree[i].devices.push(element.device);
          flag = 1;
        }
      }
      if (flag == 0) {
        state.chooseTree.push({system: element.system, devices: [element.device]});
      }
    },
    cleanTree() {
      this.state.chooseTree = [];
    },
    filter(state, str) {
      state.choosefilter = str;
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

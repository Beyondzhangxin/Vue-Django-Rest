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
      //信号量
      var flag = 0;
      for (var i = 0; i < this.state.chooseTree.length; i++) {
        if (this.state.chooseTree[i].system == element.system) {
          this.state.chooseTree[i].devices.push(element.device);
          flag = 1;
        }
      }
      if (flag == 0) {
        this.state.chooseTree.push({system: element.system, devices: [element.device]});
      }
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

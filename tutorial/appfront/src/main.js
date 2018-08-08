// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App'
import router from './router'
/* 导入项目需要的js*/
import axios from 'axios'
import VueResource from 'vue-resource'
import Vuex from 'vuex'
import store from './vuex/store'


//引入jquery
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
//import echarts from 'echarts'

// 修改全局变量的名称
Vue.use(ElementUI)
Vue.use(Vuex)
Vue.use(VueResource)
Vue.prototype.$ajax = axios
//echarts的全局配置由于过于庞大改由局部配置。
//Vue.prototype.$echarts = echarts
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})

import Vue from 'vue'
import Router from 'vue-router'
import FaultDetection from '@/components/FaultDetection'
import HomeContainer from '@/components/HomeContainer'
import PvdataList from '@/components/el-simple-com/PvdataList'
Vue.use(Router)

/*
  Home 为根目录
  pv 为pvdata的数据实验
  detection 关多的修改
  echarts_elements 为 echarts的元素
  el-simple-com 为 element的元素
*/

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      redrect: '/Home',
      component: HomeContainer
    },
    {
      path: '/pv',
      name: 'pv',
      component: PvdataList
    },
    {
      path: '/detection',
      name: 'detection',
      component: FaultDetection
    }
  ]
})

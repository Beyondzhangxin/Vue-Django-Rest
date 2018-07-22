import Vue from 'vue'
import Router from 'vue-router'
import FaultDetection from '@/components/detection/FaultDetection'
import HomeContainer from '@/pages/HomeContainer'
import PvdataList from '@/components/el-simple-com/PvdataList'
import First from '@/components/First'
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
      redirect: '/Home',

    },
    {
      path: '/Home',
      name: 'Home',
      component: HomeContainer,
      children: [
        {
          path: 'detection',
          component : FaultDetection,
        },
        {
          path: 'first',
          component: First,
        }
      ]
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

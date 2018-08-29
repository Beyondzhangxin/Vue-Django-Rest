import Vue from 'vue'
import Router from 'vue-router'
import FaultDetection from '@/components/detection/FaultDetection'
import HomeContainer from '@/pages/HomeContainer'
import PvdataList from '@/components/el-simple-com/PvdataList'
import First from '@/components/first/First'
import Gauge from '@/components/echarts_elements/Gauge1'
import Power from '@/components/power/Power'
import Device from '@/components/device/Device'
import Analysis from '@/components/analysis/Analysis'
import VueResource from 'vue-resource'
import Gmm from '@/components/gmm/gmm'
import Calculation from '@/components/gmm/calculation'
import Demo from '@/components/gmm/demo01'
import Effect from '@/Effect'




Vue.use(VueResource)
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
      redirect: '/effect',
    },
    {
      path: '/Gauge',
      name: 'Gauge',
      component: Gauge,
    },
    {
      path:'/effect',
      component: Effect,
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
        },{
          path: 'power',
          component: Power,
        },{
          path: 'device',
          component: Device,
        },
        {
          path:'analysis',
          component: Analysis,
        },
        // {
        //   path: '/gmm',
        //   name: 'gmm',
        //   component: Gmm
        // },
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
    },
    {
      path: '/gmm',
      name: 'gmm',
      component: Gmm
    },
    {
      path: '/calculation',
      name: 'calculatiopn',
      component: Calculation
    },
    {
      path: '/demo',
      name: 'demo',
      component: Demo
    }
  ]
})

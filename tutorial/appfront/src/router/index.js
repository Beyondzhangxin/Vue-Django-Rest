import Vue from 'vue'
import Router from 'vue-router'
import NewContact from '@/components/NewContact'
import FaultDetection from '@/components/FaultDetection'
import SimpleList from '@/components/el-simple-com/SimpleList'
import HomeContainer from '@/components/HomeContainer'
import t1 from '@/components/t1'
import input from '@/components/el-simple-com/com-input'
import PvdataList from '@/components/el-simple-com/PvdataList'
import hello from '@/components/hello'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      redrect: '/Home',
      component: HomeContainer
    },
    {
      path: '/home',
      name: 'home1',
      component: SimpleList
    },
    {
      path: '/newcontact',
      name: 'newcontact',
      component: NewContact
    },
    {
      path: '/add',
      name: 'add',
      component: input
    },
    {
      path: '/pv',
      name: 'pv',
      component: PvdataList
    },
    {
      path: '/hello',
      name: 'hello',
      component: hello
    },
    {
      path: '/detection',
      name: 'detection',
      component: FaultDetection
    }
  ]
})

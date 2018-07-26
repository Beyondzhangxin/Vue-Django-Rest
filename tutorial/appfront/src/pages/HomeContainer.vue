<template>
  <el-container>
    <!-- 导入header-->
    <el-header><HomeHeader/></el-header>
    <el-container>
      <el-aside  v-if="isShowAside()"  width="200px"><HomeAside/></el-aside>
      <el-container>
        <el-main><router-view/></el-main>
        <el-footer>Powered by 清华四川能源互联网研究院</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>
<script>
  import HomeHeader from '@/components/Home/header'
  import HomeAside  from '@/components/Home/aside'

  export default {
    name: 'home',
    components: {
      HomeHeader,
      HomeAside,
    },
    data () {
      return {
        active: 'detection',
      }
    },
    methods: {
      isShowAside(){
        return this.$router.history.current.fullPath == '/home/power'
      },
    },
    // watch: {
    //   active (newVal) {
    //     this.$router.push({
    //       path: '${this.active}'
    //     })
    //   }
    // }
  }
</script>
<style>
.el-header{
  background-color: #B3C0D1;
  color: #333;
  height: 20%;
}

.el-footer {
  background-color: #B3C0D1;
  color: #333;
  height: 20%;
  padding-top:20px;
}

.el-aside {
    background-color: #D3DCE6;
    color: #333;
}

 .el-main {
    background-color: #E9EEF3;
    color: #333;
    height: 100%;
}

 #app > .el-container {
    height: 100%;
  }

  .HomePage {
    width: 100%;
    height: 100%;
  }
</style>

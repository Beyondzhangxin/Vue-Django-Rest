<template>
  <el-container>
    <!-- 导入header-->
    <el-header><HomeHeader/></el-header>
    <el-main>
        <el-container>
            <el-aside  v-if="this.$store.state.isShowAside"  width="18%"><HomeAside/></el-aside>
            <el-main class="m1"><router-view/></el-main>
        </el-container>
    </el-main>
    <el-footer>Powered by 清华四川能源互联网研究院</el-footer>
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
  padding-left: 0px;
  padding-right: 0px;
}

.el-footer {
  background-color:#6fc7f7;
  color: #333;
  height: 20%;
  padding-top:20px;
}

.el-aside {

}

 .el-main {
    background-color: #E9EEF3;
    color: #333;
    height: 100%;
    padding-left: 0px;
    padding-right: 0px;
    padding-top: 0px;
    padding-bottom: 0px;
}

.el-main .el-container {
  height: 100%;
}

 #app > .el-container {
    height: 100%;
  }

  .HomePage {
    width: 100%;
    height: 100%;
  }
  .m1 {
    padding-top: 12px;
    padding-left: 12px;
    display: block;
    z-index: auto;
    line-height: 20px;
  }
</style>

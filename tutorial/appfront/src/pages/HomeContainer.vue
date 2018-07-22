<template>
  <el-container>
    <!-- 导入header-->
    <el-header><HomeHeader :active.sync='active'/></el-header>
    <el-main><router-view/></el-main>
    <el-footer>Footer</el-footer>
  </el-container>
</template>
<script>
  import HomeHeader from '@/components/Home/header'

  export default {
    name: 'home',
    components: {
      HomeHeader
    },
    data () {
      return {
        active: 'detection'
      }
    },
    watch: {
      active (newVal) {
        this.$router.push({
          path: '${this.active}'
        })
      }
    }
  }
</script>
<style>
.el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

.el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

 .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

 #app > .el-container {
    height: 100%;
  }
</style>

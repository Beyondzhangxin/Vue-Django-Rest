<template>
  <el-container>
    <!-- 导入header-->
    <el-header><HomeHeader/></el-header>
    <el-main>
        <el-container>
            <el-aside v-if="this.$store.state.isShowAside" width="260px"><HomeAside/></el-aside>
            <el-main class="m1"><router-view/>
            </el-main>
        </el-container>
    </el-main>
    <!-- <el-footer class="HomeFooter"><div>Powered by 清华四川能源互联网研究院</div></el-footer> -->
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
.HomeFooter {
  background-color: #12AFE3;
  background: -webkit-linear-gradient(30deg, #12AFE3, #0d7feb); /* Safari 5.1 - 6.0 */
  background: -o-linear-gradient(30deg, #12AFE3, #0d7feb); /* Opera 11.1 - 12.0 */
  background: -moz-linear-gradient(30deg, #12AFE3, #0d7feb); /* Firefox 3.6 - 15 */
  background: linear-gradient(30deg, #12AFE3,  #0d7feb); /* 标准的语法（必须放在最后） */
}

.HomeFooter div {
  color: #fff;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}

.el-header{
  height: 20%;
  padding-left: 0px;
  padding-right: 0px;
  background-color: rgb(84, 92, 100);
}

.el-footer {

  height: 20%;
  padding-top:20px;
}

.el-aside {
  width: 260px;
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

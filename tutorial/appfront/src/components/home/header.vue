<template>
  <div class="header">
    <div class="head-left">
  		<span class="logo">光伏智能运维系统</span>
    </div>

    <div class="head-right">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal"
     @select="handleSelect" text-color="#fff" background-color="#12AFE3">
      <el-menu-item index="0">首页</el-menu-item>
      <el-submenu index="1">
        <template slot="title">运行监测</template>
          <el-menu-item index="1-1">电站监测</el-menu-item>
          <el-menu-item index="1-2">设备监测</el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">数据分析</template>
          <el-menu-item index="2-1">对比分析</el-menu-item>
          <el-menu-item index="2-2">发电量分析</el-menu-item>
          <el-menu-item index="2-3">发电效率分析</el-menu-item>
          <el-menu-item index="2-4">损耗分析</el-menu-item>
          <el-menu-item index="2-5">故障报表</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">故障告警</template>
          <el-menu-item index="4-1">故障监测</el-menu-item>
          <el-menu-item index="4-2">报警分析</el-menu-item>
      </el-submenu>
      <el-menu-item index="4">系统设置</el-menu-item>
    </el-menu>
    </div>
  </div>
</template>


<script>
   export default {

    data() {
      return {
        activeIndex: '1',
        routerTable: [
          {router: "/home/first"},
          {router: "/home/power"},
          {router: "/home/first"},
          {router: "/home/detection"},
          {router: "/home/first"},
        ],
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key);
        console.log(key);
        console.log(this.routerTable);
        this.$router.push(this.routerTable[Number(keyPath[0])].router)
      }
    }
  }
</script>

<style scoped>
.header {
  background-color: #12AFE3;
  color: #fff;
}

  .head-left{
    float:left;
    height: 100%;
    text-align: center;
    display: inline-block;
    padding-top: 10px;
    margin-left: 40px;
  }

  .head-right{
    float:right;
    display: inline-block;
  }

  .header {
    height: 100%;
    text-align: center;
  }

  .logo {
    font-size: 30px;
    text-align: center;
    font-style: Hiragino Sans GB;
  }
</style>

<template>
  <div class="header">
    <div class="head-left">
  		 <a>光伏云运维</a>
    </div>

    <div class="head-right">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal"
     @select="handleSelect"
     background-color="#545c64"
     active-text-color="#ffd04b"
     text-color="#fff">
      <el-menu-item index="0"><i class="el-icon-location"></i>首页</el-menu-item>
      <el-submenu index="1">
        <template slot="title">运行监测</template>
          <el-menu-item index="1-0">电站监测</el-menu-item>
          <el-menu-item index="1-1">设备监测</el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title" >数据分析</template>
          <el-menu-item index="2-0">对比分析</el-menu-item>
          <el-menu-item index="2-1">发电量分析</el-menu-item>
          <el-menu-item index="2-2">发电效率分析</el-menu-item>
          <el-menu-item index="2-3">损耗分析</el-menu-item>
          <el-menu-item index="2-4">故障报表</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">故障告警</template>
          <el-menu-item index="3-0">故障监测</el-menu-item>
          <el-menu-item index="3-1">报警分析</el-menu-item>
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
          {router: ["/home/first"]},
          {router: ["/home/power", "/home/device"]},
          {router: ["/home/analysis"]},
          {router: ["/home/detection"]},
          {router: ["/home/first"]},
        ],
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(keyPath);
        if (keyPath[1]) {
          this.$router.push(this.routerTable[Number(keyPath[0])].router[keyPath[1].split("-")[1]])
        }else {
          this.$router.push(this.routerTable[Number(key)].router[0])
        }
      }
    }
  }
</script>

<style scoped>
  .el-menu-demo {
    font-family: Helvetica Neue,Helvetica,PingFang SC,Hiragino Sans GB,
    Microsoft YaHei,SimSun,sans-serif;
    font-weight: 400;
  }

  .header {
    background-color: rgb(84, 92, 100);
  }

  .head-left{
    float:left;
    height: 100%;
    display: block;
  }

  .head-left a {
    color: #fff;
    position: absolute;
    top: 0px;
    background: rgb(31, 40, 55);
    width: 260px;
    padding: 15px;

    text-align: left;
    font-size: 24px;
    font-weight: 700;
    /* text-transform: uppercase; */
    line-height: 30px;
  }

 .head-left a:hover{
   color:#c0c0c0;
 }

  .head-right{
    float:right;
    display: inline-block;
  }

  .header {
    height: 100%;
    text-align: center;
    background-color: rgb(31, 40, 55);
  }
</style>

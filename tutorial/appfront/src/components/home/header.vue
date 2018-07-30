<template>
  <div class="header">
    <div class="head-left">
  		<span class="logo">光伏智能运维系统</span>
    </div>

    <div class="head-right">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal"
     @select="handleSelect" text-color="#fff" background-color="#12AFE319">
      <el-menu-item index="0">首页</el-menu-item>
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
          {router: ["/home/first"]},
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
.header {
  background-color: #12AFE3;
  background: -webkit-linear-gradient(-60deg, #12AFE3, #0d7feb); /* Safari 5.1 - 6.0 */
  background: -o-linear-gradient(-60deg, #12AFE3, #0d7feb); /* Opera 11.1 - 12.0 */
  background: -moz-linear-gradient(-60deg, #12AFE3, #0d7feb); /* Firefox 3.6 - 15 */
  filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#12AFE3,endColorstr=#0d7feb,grandientType=1);/*IE 9.0以上*/
  background: linear-gradient(-60deg, #12AFE3,  #0d7feb); /* 标准的语法（必须放在最后） */
  color: #fff;
}

  .head-left{
    float:left;
    height: 100%;
    text-align: center;
    display: inline-block;
    position: relative;
    top: 9px;
    left: 8px;
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

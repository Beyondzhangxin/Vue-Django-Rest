<template>
  <div>
    <div class="head-left">
  		<span class="logo">光伏智能运维系统</span>
    </div>

    <div class="head-right">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">首页</el-menu-item>
      <el-submenu index="2">
        <template slot="title">运行监测</template>
          <el-menu-item index="2-1">电站监测</el-menu-item>
          <el-menu-item index="2-2">设备监测</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">数据分析</template>
          <el-menu-item index="3-1">对比分析</el-menu-item>
          <el-menu-item index="3-2">发电量分析</el-menu-item>
          <el-menu-item index="3-3">发电效率分析</el-menu-item>
          <el-menu-item index="3-4">损耗分析</el-menu-item>
          <el-menu-item index="3-5">故障报表</el-menu-item>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title">故障告警</template>
          <el-menu-item index="4-1">故障监测</el-menu-item>
          <el-menu-item index="4-2">报警分析</el-menu-item>
      </el-submenu>
      <el-menu-item index="5">系统设置</el-menu-item>
    </el-menu>
    </div>
  </div>
</template>


<script>
   export default {
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        activeIndex3: '1',
        activeIndex4: '1',
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>


<style>
.head-left{
  float:left;
  margin-top:20px;
}

.head-right{
  float:right;
}

</style>

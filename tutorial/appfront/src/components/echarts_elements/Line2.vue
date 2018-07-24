<template>
  <div class="line" :style="{width: '100%', height: '100%'}">
    <div v-bind:id="id" :style="{width: '100%', height: '100%'}"></div>
  </div>
</template>
<script>
  let echarts = require('echarts/lib/echarts')

  require('echarts/lib/chart/bar')
  // 引入提示框和title组件
  require('echarts/lib/component/tooltip')
  require('echarts/lib/component/title')
  require('echarts/lib/component/toolbox')
  require('echarts/lib/component/dataZoom')


export default {
  name: 'line2',
  props: ['id', 'option'],
  data () {
    return {
    }
  },
  watch: {
    option: function () {
      this.drawLine();
    }
  },
  mounted: function() {
    this.drawLine();
    this.setInterval();
  },
  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      let line1 = echarts.init(document.getElementById(this.id))
      //初始化变量
      // 绘制图表
      console.log(this.option);
      line1.setOption(this.option);
    },
    setInterval () {

    }
  }
}
</script>
<style>
</style>

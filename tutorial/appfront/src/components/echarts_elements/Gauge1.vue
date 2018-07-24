<template>
  <div class="gauge" :style="{width: '100%', height: '100%'}">
    <div v-bind:id="id" :style="{width: '100%', height: '100%'}"></div>
  </div>
</template>
<script>
  let echarts = require('echarts/lib/echarts')

  require('echarts/lib/chart/gauge')
  // 引入提示框和title组件
  require('echarts/lib/component/tooltip')
  require('echarts/lib/component/title')
  require('echarts/lib/component/toolbox')


export default {
  name: 'Gauge1',
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
    setInterval(this.setValues, 2000);
  },
  methods: {
    drawLine () {
      console.log(this.id);
      console.log(this.gauge);
      // 基于准备好的dom，初始化echarts实例
      let gauge1 = echarts.init(document.getElementById(this.id))
      //初始化变量
      // 绘制图表
      console.log(this.option);
      gauge1.setOption(this.option);
    },
    setValues () {
      //赋值
      let gauge1 = echarts.init(document.getElementById(this.id))
      this.option.series[0].data[0].value = this.value||0;
      gauge1.setOption(this.option, true);
    },
  }
}
</script>
<style>
</style>

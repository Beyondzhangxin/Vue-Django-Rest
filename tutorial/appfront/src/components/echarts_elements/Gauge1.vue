<template>
  <div class="gauge" :style="{width: '100%', height: '100%'}">
    <div v-bind:id='id' :style="{width: '100%', height: '100%'}"></div>
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
    props: {
      id: String,
      value: Number,
      dataName: String,
    },
    data () {
      return {
        msg: 'Welcome to Your Vue.js App',
        option: {
          tooltip : {
            formatter: "{a} <br/>{b} : {c}%"
          },
          toolbox: {
            feature: {
              restore: {},
              saveAsImage: {}
            }
          },
          series: [
            {
              name:  this.data? this.data.name:'未命名1',
              type: 'gauge',
              detail: {formatter:'{value}kW'},
              data: [{value: this.value||50, name: this.dataName||'未命名2'}]
            }
          ]
        },
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
        console.log(this.gauge);
        // 基于准备好的dom，初始化echarts实例
        let gauge1 = echarts.init(document.getElementById(this.id))
        //初始化变量
        // 绘制图表
        gauge1.setOption(this.option);
      },
      setInterval () {
      },
    }
  }
</script>
<style>
</style>

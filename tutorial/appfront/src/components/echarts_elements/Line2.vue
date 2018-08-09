<template>
    <div class="Line2" v-bind:id="id"></div>
</template>
<script>
  let echarts = require('echarts/lib/echarts')

  require('echarts/lib/chart/bar')
  require('echarts/lib/chart/line')
  // 引入提示框和title组件
  require('echarts/lib/component/tooltip')
  require('echarts/lib/component/title')
  require('echarts/lib/component/toolbox')
  require('echarts/lib/component/dataZoom')
  require('echarts/lib/component/legend')

var interval = 0
var line1 = 0

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
    interval = setInterval(this.updateData, 2000);
  },

  destroyed: function() {
    clearInterval(interval)
  },

  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      line1 = echarts.init(document.getElementById(this.id))
      //初始化变量
      // 绘制图表
      console.log(this.option);
      line1.setOption(this.option);
      setTimeout(function (){
        window.onresize = function () {
          line1.resize();
        }
      },200);
    },
    updateData () {
      line1.setOption(this.option)
    }
  }
}
</script>
<style scoped>
  .Line2 {
    height: 100%;
    width: 100%;
  }
</style>

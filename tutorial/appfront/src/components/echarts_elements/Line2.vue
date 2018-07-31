<template>
    <div v-bind:id="id"></div>
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
 

  },
  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      let line1 = echarts.init(document.getElementById(this.id))
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
  }
}
</script>
<style scoped>

</style>

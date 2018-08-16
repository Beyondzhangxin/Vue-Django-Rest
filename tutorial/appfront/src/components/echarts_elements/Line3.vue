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



export default {
  name: 'line2',
  props: ['id', 'option'],
  line1: 0,
  interval: 0,


  data () {
    return {
      changeOption: this.option
    }
  },
  watch: {
    option:{
      handler:function(val,oldval){
        this.updateData();
      },
      deep:true//对象内部的属性监听，也叫深度监听
    }
  },

  mounted: function() {
    this.drawLine();
    var interval = setInterval(this.drawLine, 2000);
  },

  destroyed: function() {
    clearInterval(this.interval);
  },

  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      var line1 = echarts.init(document.getElementById(this.id))
      //初始化变量
      // 绘制图表
      line1.setOption(this.option);
      setTimeout(function (){
        window.onresize = function () {
          line1.resize();
        }
      },200);
    },
    updateData () {
      this.drawLine()
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

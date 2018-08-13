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
  props: ['id', 'option', 'request'],
  line1: 0,
  interval: 0,


  data () {
    return {
      changeOption: this.option
    }
  },

  mounted: function() {
    this.drawLine();
    this.loadData();
    this.interval = setInterval(this.updateData, 2000);
  },

  destroyed: function() {
    clearInterval(this.interval)
  },

  methods: {
    loadData() {
      if (this.request.length == 2) {
        this.$ajax.get(this.request[1])
        .then(function (response) {
          //处理数据
          var list1 = [];
          var list2 = [];
          console.log(response);
          for (var j = 0; j < response.data.data.series.length; j++) {
            list1.push(response.data.data.series[j][0]);
            list2.push(response.data.data.xAxix[j][0]);
          }
          this.changeOption.series[1].data = list1;
          this.changeOption.xAxis[0].data = list2;
          console.log(asdasd);
        }.bind(this))
        .catch(function (error) {
          return 0;
        });
      }
      this.$ajax.get(this.request[0])
      .then(function (response) {
        //处理数据
        var list1 = [];
        var list2 = [];
        console.log(response.data);
        for (var j = 0; j < response.data.data.series.length; j++) {
          list1.push(response.data.data.series[j][0]);
          list2.push(response.data.data.xAxix[j][0]);
        }
        console.log(list1);
        console.log(list2);
        this.changeOption.series[0].data = list1;
        this.changeOption.xAxis[0].data = list2;
        console.log(asdafafa);
      }.bind(this))
      .catch(function (error) {
        return 0;
      });

    },
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      this.line1 = echarts.init(document.getElementById(this.id))
      //初始化变量
      // 绘制图表
      console.log(this.option);
      this.line1.setOption(this.option);
      setTimeout(function (){
        window.onresize = function () {
          this.line1.resize();
        }
      },200);
    },
    updateData () {
      this.line1.setOption(this.option)
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

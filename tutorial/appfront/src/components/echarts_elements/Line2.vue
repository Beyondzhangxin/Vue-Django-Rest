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

    mounted: function () {
      this.drawLine();
    },

    destroyed: function () {
      clearInterval(this.interval)
    },

    methods: {
      loadData() {
        if (this.request.length == 2) {
          this.$ajax.get(this.request[1])
            .then(function (response) {
              this.changeOption.series[1].data = response.data.data.series;
              this.changeOption.xAxis[0].data = response.data.data.xAxix;
              console.log("I am doing things")
            }.bind(this))
            .catch(function (error) {
              return 0;
            });
        }
        this.$ajax.get(this.request[0])
          .then(function (response) {
            this.changeOption.series[0].data = response.data.data.series;
            this.changeOption.xAxis[0].data = response.data.data.xAxix;
            console.log(this.changeOption)
          }.bind(this))
          .catch(function (error) {
            return 0;
          });


      },
      drawLine () {
        // 基于准备好的dom，初始化echarts实例
        var line1 = echarts.init(document.getElementById(this.id))
        //初始化变量
        // 绘制图表
        this.interval = setInterval( () =>{
          this.loadData();
          line1.setOption(this.changeOption);
        }, 5000)
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

<template>
      
        <!-- header -->
        <!-- <el-container class="container"> -->
        <el-card class="card0"> 

        <el-header id="header" style="height:80px;">
            <el-row>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/station.png" id="image">
                        <span id="text"><strong>电站对比</strong></span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/self.png" id="image">
                        <span id="text"><strong>设备对比</strong></span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/equipment.png" id="image">
                        <span id="text"><strong>自身对比</strong></span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content"></div></el-col>
            </el-row>
        </el-header>

        <hr width=100% size=1 color=#bbbcbc style="FILTER: alpha(opacity=100,finishopacity=0)"> 

        <!-- main1 -->
        <div id="main1">
            <el-header id="header" style="height:80px;">
            <el-row>
                <el-col :span="12" id="span1">
                        <el-col :span="4" id="span0">对比内容:</el-col>
                        <el-col :span="4">
                            <el-button id="button1">功率</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button1">效率</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button2">等效时数</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button1">符合率</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button1">发电量</el-button>
                        </el-col>
                </el-col>
                <el-col :span="12" id="span2">
                    <span id="text1">查询日期</span>
                  <!-- 日期选择器 -->
                        <span class="demonstration"></span>
                        <el-date-picker
                            v-model="value2"
                            align="right"
                            type="date"
                            placeholder="选择日期"
                            :picker-options="pickerOptions1">
                        </el-date-picker>
               </el-col>
            </el-row>
            </el-header>
        </div>

        <!-- main2 -->
        <el-main id="main2">
            <el-row>
                <el-col :span="24">
                    <div class="text2">已选电站：</div>
                </el-col>
            </el-row>
            <div class="sel">
                <el-button type="primary" plain>北京光伏电站</el-button>
                <el-button type="primary" plain>上海光伏电站</el-button>
            </div>

        </el-main>

    <hr width=100% size=1 color=#bbbcbc style="FILTER: alpha(opacity=100,finishopacity=0)"> 
    
        <!-- main3 -->
        <el-main id="main3">
          <div class="m3">
            <Line2 v-bind="l2"></Line2>
          </div>
        </el-main>
        <!-- </el-container> -->
        </el-card>
</template>



<script>
import Line2 from '../echarts_elements/Line2'

export default {
    name: 'analysis',
    components: {
      Line2: Line2
    },
    data(){
        return{
        pickerOptions1: {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        },
        l2:{
          id: 'line1',
          option:{
            title: {
              text: '功率图表(单位:kW)',
            },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                backgroundColor: '#283b56'
              }
            }
          },
          legend: {
            data:['北京光伏电站', '上海光伏电站','理论发电量']
          },
          toolbox: {
            show: true,
            feature: {
              dataView: {readOnly: false},
              restore: {},
              saveAsImage: {}
            }
          },
          dataZoom: {
            show: false,
            start: 0,
            end: 100
          },
          xAxis: [
            {
              type: 'category',
              boundaryGap: true,
              data: (function (){
                var now = new Date();
                var res = [];
                var len = 10;
                while (len--) {
                    res.unshift(now.toLocaleTimeString().replace(/^\D*/,''));
                    now = new Date(now - 2000);
                }
                return res;
              })()
          },
          {
            type: 'category',
            boundaryGap: true,
            data: (function (){
                var res = [];
                var len = 10;
                while (len--) {
                    res.push(10 - len - 1);
                }
                return res;
            })()
          }
        ],
        yAxis: [
          {
            type: 'value',
            scale: true,
            name: 'kW',
            max: 500,
            min: 0,
            boundaryGap: [0.2, 0.2]
          },
        ],
        series: [
          {
            name:'北京光伏电站',
            type:'line',
            xAxisIndex: 1,
            yAxisIndex: 0,
            data:(function (){
                var res = [];
                var len = 10;
                while (len--) {
                    res.push(Math.round(Math.random() * 1000));
                }
                return res;
            })()
          },
          {
            name:'上海光伏电站',
            type:'line',
            xAxisIndex: 1,
            yAxisIndex: 0,
            data:(function (){
                var res = [];
                var len = 10;
                while (len--) {
                    res.push(Math.round(Math.random() * 1000));
                }
                return res;
            })()
          },
        ]
      },
      },
        value1: '',
        value2: '',
      };
    },
    mounted: function() {
      this.$store.commit('showIt');
    },
    destroyed: function() {
      this.$store.commit('hideIt')
    },
}


</script>


<style scoped>
.container {
  margin-top: 20px;
  /* padding-left: 15px;
  padding-right: 15px; */
  overflow-y: hidden;
}

.m3 {
  height: 550px;
  background-color: #fff;
}

#header{
    background:white;
    padding-top:10px;
}

#button1{
    margin-top:10px;
    font-size:14px;
    margin-bottom:10px;
}

#button2{
    margin-top:10px;
    font-size:14px;
    margin-bottom:10px;
    padding-right:10px;
    padding-left:10px;
}

#text{
   padding-bottom:2px;
   padding-top:2px;
   display: block;
   font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
   font-size:16px;
}

#span0{
    padding-top:10px;
    padding-left:2px;
    font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size:16px;
    margin-left:-20px;
}

#span1{
    background:white;
}

#span2{
    background:white;
    padding-left:250px;
    padding-top:10px;
   
}

#span0{
    margin-top:8px;
    padding-left:20px;
}

#main1{
    margin-top:20px;
    height:100px;
}

#main2{
    background:white;
}

#main3{
    margin-top:50px;
}

#text1{
    padding-right:20px;
    margin-bottom:10px;
}

.text2{
    float: left;
    margin-top:20px;
    margin-left:20px;
}

.sel{
    float:left;
    margin-top:20px;
    margin-left:30px;
    margin-bottom: 10px;
}

.card0{
    margin-top:20px;
    margin-left:15px;
    margin-right:20px;
}


</style>

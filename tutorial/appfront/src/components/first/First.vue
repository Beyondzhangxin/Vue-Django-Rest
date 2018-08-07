<template>
    <el-container>
      <el-main>

        <el-card>
            <!-- <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="全部电站信息" name="first">北京，上海，深圳电站统计</el-tab-pane>
             </el-tabs> -->
             <div class="inf">北京，上海，深圳电站统计</div>
              <hr width=100% size=1 color=#bbbcbc style="FILTER: alpha(opacity=100,finishopacity=0)"> 
          <div class="row0">
            <el-row>
              <el-col :span="8">
                <div class="ca1">
                  <el-card class="card2"><Gauge2/></el-card>
                    <el-card class="card1">
                    <div class="card1m c1m">
                      <span>当前发电功率</span>
                    </div>
                    <div class="card1m">
                      <div class="row1">总容量：<strong>{{(c1.total||"~")}}</strong> kWh</div>
                      <div  class="row1">当日累计发电量：<strong>{{(c1.total||"~")}}</strong>  kWh</div>
                      <div  class="row1">当月累计发电量：<strong>{{(c1.total||"~")}}</strong> 万kWh</div>
                      <div class="row1">累计总发电量：<strong>{{(c1.total||"~")}}</strong> 万kWh</div>
                    </div>
                  </el-card>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="ca2">
                  <el-card class="card2"><Gauge2/></el-card>
                  <el-card class="card1">
                    <div class="card1m c1m">
                      <span>综合效率</span>
                    </div>
                    <div class="card1m">
                      <div class="row1">理论电量：<strong>{{(c2.the||"~")}}</strong> kWh</div>
                      <div  class="row1">发电量：<strong>{{(c2.act||"~")}}</strong> kWh</div>
                      <div  class="row1">理论实际差值：<strong>{{( (c2.the - c2.act)||"~")}}</strong> kWh</div>
                    </div>
                  </el-card>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="ca3">
                  <el-card class="card2"><Gauge2/></el-card>
                  <el-card class="card1">
                    <div class="card1m c1m">
                      <span>逆变器转换效率</span>
                    </div>
                    <div class="card1m">
                      <div class="row1">逆变器转换效率：<strong>{{(c3.eff||"~") +"" }}</strong> %</div>
                    </div>
                  </el-card>
                </div>
              </el-col>
            </el-row>
          </div>


          <div class="row0">
            <el-row>
              <el-col :span="12">
                <el-card class="card3">
                  <div class="card3Li">
                    <Line2 v-bind="settings.l1"></Line2>
                  </div>
                </el-card>
              </el-col>
              <el-col :span="12">
                <el-card class="card3">
                  <div class="card3Li">
                    <Line2 v-bind="settings.l2"></Line2>
                  </div>
                </el-card>
              </el-col>
            </el-row>
          </div>


          <!-- 环保数据 -->
          <div class="box">
          <el-card class="box-card1">
            <div slot="header" class="clearfix">
              <span id="htop"><strong>环保数据</strong></span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>

            <div class="data">
              <el-row :gutter="60">
                <el-col :span="4"><div class="grid-content">
                  <el-card>
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/coal.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计节约标准煤</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg1}}吨</div>
                </el-card>
                </div>
                </el-col>

                <el-col :span="4"><div class="grid-content">
                  <el-card>
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/co2.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计减排</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg2}}吨</div>
                  </el-card>
                </div></el-col>

                <el-col :span="4"><div class="grid-content">
                  <el-card>
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/so2.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计减排</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg3}}吨</div>
                  </el-card>
                </div></el-col>

                <el-col :span="4"><div class="grid-content">
                  <el-card>
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/no2.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计减排</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg4}}kg</div>
                  </el-card>
                </div></el-col>

                <el-col :span="4"><div class="grid-content">
                  <el-card>
                   <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/tree.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计植树</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg5}}棵</div>
                  </el-card>
                </div></el-col>
              </el-row>
            </div>
          </el-card>
          </div>

        </el-card>

      </el-main>
  </el-container>
</template>

<script>
import Gauge1 from '../echarts_elements/Gauge1'
import Line2 from '../echarts_elements/Line2'
import Gauge2 from '../echarts_elements/Gauge2'


export default {
  name : 'First',
  components: {
    Gauge1: Gauge1,
    Gauge2: Gauge2,
    Line2: Line2,
  },
  data () {
    return {

       activeName: 'first',
      //配置最下面的list


      msg1:146.23,
      msg2:393.09,
      msg3:10.86,
      msg4:5429.41,
      msg5:988.97,

      c1: {
        total: 1,
        day: 1,
        mouth: 1,
        sumAll: 1,
      },
      c2: {
        the: 1,
        act: 1,
      },
      c3: {
        eff: 1,
      },
      tabs: [
        {text: '累计节约标准煤'},
        {text: '累计减排'},
        {text: '累计减排'},
        {text: '累计减排'},
        {text: '累计植树'},
      ],
      //配置组件option
      settings: {
        g1:{
          id: 'gauge1',
          //需要输入的值-
          value: 0,
          option:{
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
                name: '当前发电功率',
                type: 'gauge',
                detail: {formatter:'{value}kW'},
                data: [{value: 50, name: '当前发电功率'}]
              }
            ]
          },
        },
        g2:{
          id: 'gauge2',
          option:{
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
                name: '业务指标',
                type: 'gauge',
                detail: {formatter:'{value}%'},
                data: [{value: 50, name: '综合发电效率'}]
              }
            ]
          },
        },
        g3:{
          id: 'gauge3',
          option:{
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
                name: '业务指标',
                type: 'gauge',
                detail: {formatter:'{value}%'},
                data: [{value: 50, name: '逆变器转换效率'}]
              }
            ]
          },
        },
        l1:{
          id: 'line1',
          option:{
            title: {
              text: '当日发电量',
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
            data:['逆变器发电量', '电能表发电量', '理论发电量']
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
            name: 'kWh',
            max: 500,
            min: 0,
            boundaryGap: [0.2, 0.2]
          }
        ],
        series: [
          {
            name:'逆变器发电量',
            type:'bar',
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
            name:'电能表发电量',
            type:'bar',
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
            name:'理论发电量',
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
        l2:{
          id: 'line2',
          option: {
            title: {
              text: '当日发电功率',
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
            data:['逆变器发电功率', '电能表发电功率', '总辐照度']
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
          }
        ],
        series: [
          {
            name:'逆变器发电功率',
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
            name:'电能表发电功率',
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
            name:'总辐照度',
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

        }
      }
    }
  }
}
</script>
<style scoped>


  .c1m {
    border-bottom: 1px solid #eeeeee;
  }

  .card3Li {
    height: 400px;
    width: 100%;
  }

  .card3 {
    height: 400px;
    margin: 30px;

    width: 900px;

    margin-bottom: 10%;
  }


  .card1m span {
    padding: 5%;
    float: right;
    font-size: 25px;
  }

  .card1m {
    text-align: left;
    width: 100% large;
    height: 85px;
    font-size: 14px;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }

  .row1 {
    color: #909399;
    padding-top: 13px;
    padding-bottom: 13px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
  }

  .row1 strong {
    font-size: 15px;
    font-weight: 300;
    color: #974e45;
  }

  .card1 {
    position: relative;
    left: 100px;
    margin-left: -15px;
    width: 500px;
    height: 300px;
  }

  .card2 {
    width: 120px;
    height: 120px;
    position: relative;
    top: 100px;
    left: 120px;
    z-index: 1;
    background-color: #974e45;
  }

  .mainBody {
    height: 1000px;
  }

  .button {
    float: right;
  }

  .fm2 {
    height: 50%;
  }

  .fml{
    height: 33%;
    margin: 30px;
  }

  .fm {
    width: 50%;
    height: 1000px;
    background-color: #fff;
    float: left;
  }

  .ln1 {
    height: 500px;
  }

  .g1 {
    height: 400px;
    width: 100%;
  }

  .e1-row0 {
    background-color: #12AFE3;
    background: -webkit-linear-gradient(-60deg, #12AFE3, #0d7feb); /* Safari 5.1 - 6.0 */
    background: -o-linear-gradient(-60deg, #12AFE3, #0d7feb); /* Opera 11.1 - 12.0 */
    background: -moz-linear-gradient(-60deg, #12AFE3, #0d7feb); /* Firefox 3.6 - 15 */
    background: linear-gradient(-60deg, #12AFE3,  #0d7feb); /* 标准的语法（必须放在最后） */
    color: #fff;
  }
  .e1-row0 span {
    float: left;
    margin-left: 2%;
  }

  .col1 {
    border:5px dotted #12AFE3;
    background: #55d5e0;
  }

  .col2 {
    color: #fff;
  }

  .col2 ul li {
    position: relative;
    top: -7px;
    width: 200px;
    height: 30px;
    background-color: #e5e5e5;

    border-radius: 5px;
    text-align: center;
    line-height:30px;
    font-size: 14px;
    color: gray;
  }

  .First {
    height: 100%;
  }

  .el-container {
    height: 100%;
    overflow-y: hidden;
  }

  .el-row {
    height: 60%;
    margin-bottom: 20px;
  }

.el-col {
  border-radius: 4px;
  height: 100%;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.envData {
  background-color: rgb(255, 255, 255);
  height: 230px;
  height: 80%;

}

.envData li{
  float: left;
  width: 20%;
  list-style: none;
}

.icon {
  width: 50%;
}

.li1 {
  list-style-type: none;
  font-family: Helvetica Neue,Helvetica,PingFang SC,Hiragino Sans GB,Microsoft YaHei,SimSun,sans-serif;
  font-size: 14px;
  float: left;
  position: relative;
  top: 50px;
}

.text0{
  margin-top:5px;
  margin-right:10px;
}

.box-card1{
  /* margin-top:20px; */
}

.box{
  margin-right:20px;
  margin-left:30px;
  margin-top:-20px;
  margin-bottom:20px;
}

.data{
  padding-left:150px;
}

.inf{
  font-size:20px;
  font-family: 'STHeiti Light [STXihei]' ;
}

.row0{
  margin-top:-40px;
}
</style>

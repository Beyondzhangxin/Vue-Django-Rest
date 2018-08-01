<template>
  <div class="First">
    <el-container>
      <el-main>
        <!-- <el-row class="mainRow" :gutter="20">
          <el-col class="col2" :span="12">
            <el-card :body-style="{ padding: '0px' }">
              <el-row class="e1-row0">
                <span>当前发电功率</span>
              </el-row>
              <el-row>

                <el-col class="col1" :span="12"><Gauge2/></el-col>
                <el-col class="col2" :span="12">
                  <ul>
                    <li class="li1">{{ "总容量：" + (c1.total||"~") +" kWh"}}</li>
                    <li class="li1">{{ "当日累计发电量：" + (c1.total||"~") +" kWh" }}</li>
                    <li class="li1">{{ "当月累计发电量：" + (c1.total||"~") +" 万kWh" }}</li>
                    <li class="li1">{{ "累计总发电量：" + (c1.total||"~") +" 万kWh" }}</li>
                  </ul>
                </el-col>
              </el-row>
              <div style="padding: 14px;">
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                  <el-button type="text" class="button">操作按钮</el-button>
                </div>
              </div>
            </el-card>

            <el-card :body-style="{ padding: '0px' }">
              <el-row class="e1-row0">
                <span>综合效率</span>
              </el-row>
              <el-row>
                <el-col class="col1" :span="12"><Gauge2/></el-col>
                <el-col class="col2" :span="12">
                  <ul>
                    <li class="li1">{{ "理论电量：" + (c2.the||"~") +" kWh"}}</li>
                    <li class="li1">{{ "发电量：" + (c2.act||"~") +" kWh" }}</li>
                    <li class="li1">{{ "理论实际差值" + ( (c2.the - c2.act)||"~") +" kWh" }}</li>
                    <li class="li1">{{ "" }}</li>
                  </ul>
                </el-col>
              </el-row>
              <div style="padding: 14px;">
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                  <el-button type="text" class="button">操作按钮</el-button>
                </div>
              </div>
            </el-card>

            <el-card :body-style="{ padding: '0px' }">
              <el-row class="e1-row0">
                <span>逆变器转换效率</span>
              </el-row>
              <el-row>
                <el-col class="col1" :span="12"><Gauge2/></el-col>
                <el-col class="col2" :span="12">
                  <ul>
                    <li class="li1">{{ "逆变器转换效率" + (c3.eff||"~") +"%" }}</li>
                  </ul>
                </el-col>
              </el-row>
              <div style="padding: 14px;">
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                  <el-button type="text" class="button">操作按钮</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col class="col2" :span="12">


          </el-col> -->
          <!-- <el-col :span="24">
            <div>
              环保数据
            </div>
            <div class="envData">
              <ul>
                <li v-for="tab in tabs">
                  <div>{{ tab.text }}</div>
                </li>
              </ul>
            </div>
          </el-col> -->
          <div class="fm">
            <div class="fml">
              <el-card :body-style="{ padding: '0px' }">
                <el-row class="e1-row0">
                  <span>当前发电功率</span>
                </el-row>
                <el-row>

                  <el-col class="col1" :span="12"><Gauge2/></el-col>
                  <el-col class="col2" :span="12">
                    <ul>
                      <li class="li1">{{ "总容量：" + (c1.total||"~") +" kWh"}}</li>
                      <li class="li1">{{ "当日累计发电量：" + (c1.total||"~") +" kWh" }}</li>
                      <li class="li1">{{ "当月累计发电量：" + (c1.total||"~") +" 万kWh" }}</li>
                      <li class="li1">{{ "累计总发电量：" + (c1.total||"~") +" 万kWh" }}</li>
                    </ul>
                  </el-col>
                </el-row>
                <div style="padding: 14px;">
                  <div class="bottom clearfix">
                    <time class="time">{{ currentDate }}</time>
                    <el-button type="text" class="button">操作按钮</el-button>
                  </div>
                </div>
              </el-card>
            </div>
            <div class="fml">
              <el-card :body-style="{ padding: '0px' }">
                <el-row class="e1-row0">
                  <span>综合效率</span>
                </el-row>
                <el-row>
                  <el-col class="col1" :span="12"><Gauge2/></el-col>
                  <el-col class="col2" :span="12">
                    <ul>
                      <li class="li1">{{ "理论电量：" + (c2.the||"~") +" kWh"}}</li>
                      <li class="li1">{{ "发电量：" + (c2.act||"~") +" kWh" }}</li>
                      <li class="li1">{{ "理论实际差值" + ( (c2.the - c2.act)||"~") +" kWh" }}</li>
                      <li class="li1">{{ "" }}</li>
                    </ul>
                  </el-col>
                </el-row>
                <div style="padding: 14px;">
                  <div class="bottom clearfix">
                    <time class="time">{{ currentDate }}</time>
                    <el-button type="text" class="button">操作按钮</el-button>
                  </div>
                </div>
              </el-card>
            </div>
            <div class="fml">
              <el-card :body-style="{ padding: '0px' }">
                <el-row class="e1-row0">
                  <span>逆变器转换效率</span>
                </el-row>
                <el-row>
                  <el-col class="col1" :span="12"><Gauge2/></el-col>
                  <el-col class="col2" :span="12">
                    <ul>
                      <li class="li1">{{ "逆变器转换效率" + (c3.eff||"~") +"%" }}</li>
                    </ul>
                  </el-col>
                </el-row>
                <div style="padding: 14px;">
                  <div class="bottom clearfix">
                    <time class="time">{{ currentDate }}</time>
                    <el-button type="text" class="button">操作按钮</el-button>
                  </div>
                </div>
              </el-card>
            </div>
          </div>
          <div class="fm">
            <div class="fm2">
              <Line2 v-bind="settings.l1"></Line2>
            </div>
            <div class="fm2">
              <Line2 v-bind="settings.l2"></Line2>
            </div>
          </div>
          <!-- 环保数据 -->
          <div class="box">
          <el-card class="box-card1">
            <div slot="header" class="clearfix">
              <span>环保数据</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <div class="data">
              <el-row :gutter="20">
                <el-col :span="4"><div class="grid-content">
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/coal.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计节约标准煤</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg1}}吨</div>
                </div></el-col>
                <el-col :span="4"><div class="grid-content">
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/co2.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计减排</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg2}}吨</div>
                </div></el-col>
                <el-col :span="4"><div class="grid-content">
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/so2.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计减排</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg3}}吨</div>
                </div></el-col>
                <el-col :span="4"><div class="grid-content">
                  <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/no2.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计减排</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg4}}kg</div>
                </div></el-col>
                <el-col :span="4"><div class="grid-content">
                   <el-row>
                    <el-col :span="12"><div class="grid-content">
                      <img src="../../assets/tree.png" id="image">
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content">
                    <div class="text0">累计减排</div>
                    </div></el-col>
                  </el-row>
                <div>{{msg5}}棵</div>
                </div></el-col>
              </el-row>
            </div>
          </el-card>
          </div>
        
      </el-main>
  </el-container>
  </div>
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
          },
          {
            type: 'value',
            scale: true,
            name: '预购量',
            max: 1200,
            min: 0,
            boundaryGap: [0.2, 0.2]
          }
        ],
        series: [
          {
            name:'逆变器发电量',
            type:'bar',
            xAxisIndex: 1,
            yAxisIndex: 1,
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
            yAxisIndex: 1,
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
            yAxisIndex: 1,
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
            name: 'kWh',
            max: 500,
            min: 0,
            boundaryGap: [0.2, 0.2]
          },
          {
            type: 'value',
            scale: true,
            name: '预购量',
            max: 1200,
            min: 0,
            boundaryGap: [0.2, 0.2]
          }
        ],
        series: [
          {
            name:'逆变器发电功率',
            type:'line',
            xAxisIndex: 1,
            yAxisIndex: 1,
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
            yAxisIndex: 1,
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
            yAxisIndex: 1,
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
  .fm2{
    height: 50%;
  }

  .fml{
    height: 33%;
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

  .el-card {
    background: #fff;
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
  margin-top: 20px;
  margin-bottom: 20px;
  font-family: Helvetica Neue,Helvetica,PingFang SC,Hiragino Sans GB,Microsoft YaHei,SimSun,sans-serif;
  font-size: 14px;
  text-align: left;
}

.text0{
  margin-top:5px;
  
}
</style>

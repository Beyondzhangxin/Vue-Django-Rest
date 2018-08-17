<template>
  <el-container>
    <!-- 调用canvas -->
    <!-- <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas> -->
    <el-main>

      <!-- <el-card class="maincard"> -->

      <!-- <el-card class="card"> -->
      <div class="inf"><strong>多功能光伏电站系统,图书馆微电网系统电站统计</strong></div>
      <hr width=100%                                     size=1                                     color=#bbbcbc
      style="FILTER: alpha(opacity=100, finishopacity=0)">
      <div class="row0">
        <el-row>
          <el-col :span="8">
            <div class="ca1">
              <el-card class="card2">
                <Gauge2 :percent="c1.day*100/95+'%'"/>
              </el-card>
              <el-card class="card1">
                <div class="card1m c1m">
                  <span>当前发电功率</span>
                </div>
                <div class="card1m">
                  <div class="row1">总容量：<strong>{{(c1.total || "0.00")}}</strong> kWh</div>
                  <div class="row1">当日累计发电量：<strong>{{(c1.day || "0.00")}}</strong> kWh</div>
                  <div class="row1">当月累计发电量：<strong>{{(c1.month || "0.00")}}</strong> 万kWh</div>
                  <div class="row1">累计总发电量：<strong>{{(c1.sumAll.toFixed(2) || "0.00")}}</strong> 万kWh</div>
                </div>
              </el-card>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="ca2">
              <el-card class="card2">
                <Gauge2 :percent="((c2.act)*100/(c2.the)).toFixed(2)+'%'"/>
              </el-card>
              <el-card class="card1">
                <div class="card1m c1m">
                  <span>综合效率</span>
                </div>
                <div class="card1m">
                  <div class="row1">理论电量：<strong>{{(c2.the || "~")}}</strong> kWh</div>
                  <div class="row1">发电量：<strong>{{(c2.act || "~")}}</strong> kWh</div>
                  <div class="row1">理论实际差值：<strong>{{( (c2.the - c2.act) || "~")}}</strong> kWh</div>
                </div>
              </el-card>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="ca3">
              <el-card class="card2">
                <Gauge2 :percent="c3.eff+'%'"/>
              </el-card>
              <el-card class="card1">
                <div class="card1m c1m">
                  <span>逆变器转换效率</span>
                </div>
                <div class="card1m">
                  <div class="row1">逆变器转换效率：<strong>{{(c3.eff || "~") + "" }}</strong> %</div>
                </div>
              </el-card>
            </div>
          </el-col>
        </el-row>
      </div>


      <div class="row2">
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
            <el-button style="float: right; padding: 3px 0" type="text"></el-button>
          </div>

          <div class="data">
            <el-row :gutter="60">
              <el-col :span="4">
                <div class="grid-content">
                  <el-card class="elcard0">
                    <el-row>
                      <el-col :span="12">
                        <div class="grid-content">
                          <img src="../../assets/coal.png" id="image">
                        </div>
                      </el-col>
                      <el-col :span="12">
                        <div class="grid-content">
                          <div class="text0">累计节约标准煤</div>
                        </div>
                      </el-col>
                    </el-row>
                    <div>{{msg1}}吨</div>
                  </el-card>
                </div>
              </el-col>

              <el-col :span="4">
                <div class="grid-content">
                  <el-card class="elcard0">
                    <el-row>
                      <el-col :span="12">
                        <div class="grid-content">
                          <img src="../../assets/co2.png" id="image">
                        </div>
                      </el-col>
                      <el-col :span="12">
                        <div class="grid-content">
                          <div class="text0">累计减排</div>
                        </div>
                      </el-col>
                    </el-row>
                    <div>{{msg2}}吨</div>
                  </el-card>
                </div>
              </el-col>

              <el-col :span="4">
                <div class="grid-content">
                  <el-card class="elcard0">
                    <el-row>
                      <el-col :span="12">
                        <div class="grid-content">
                          <img src="../../assets/so2.png" id="image">
                        </div>
                      </el-col>
                      <el-col :span="12">
                        <div class="grid-content">
                          <div class="text0">累计减排</div>
                        </div>
                      </el-col>
                    </el-row>
                    <div>{{msg3}}吨</div>
                  </el-card>
                </div>
              </el-col>

              <el-col :span="4">
                <div class="grid-content">
                  <el-card class="elcard0">
                    <el-row>
                      <el-col :span="12">
                        <div class="grid-content">
                          <img src="../../assets/no2.png" id="image">
                        </div>
                      </el-col>
                      <el-col :span="12">
                        <div class="grid-content">
                          <div class="text0">累计减排</div>
                        </div>
                      </el-col>
                    </el-row>
                    <div>{{msg4}}kg</div>
                  </el-card>
                </div>
              </el-col>

              <el-col :span="4">
                <div class="grid-content">
                  <el-card class="elcard0">
                    <el-row>
                      <el-col :span="12">
                        <div class="grid-content">
                          <img src="../../assets/tree.png" id="image">
                        </div>
                      </el-col>
                      <el-col :span="12">
                        <div class="grid-content">
                          <div class="text0">累计植树</div>
                        </div>
                      </el-col>
                    </el-row>
                    <div>{{msg5}}棵</div>
                  </el-card>
                </div>
              </el-col>
            </el-row>
          </div>
        </el-card>
      </div>

      <!-- </el-card> -->

    </el-main>
  </el-container>
</template>

<script>
  import Gauge1 from '../echarts_elements/Gauge1'
  import Line2 from '../echarts_elements/Line2'
  import Gauge2 from '../echarts_elements/Gauge2'
  // import myCanvas from 'vue-atom-canvas'


  export default {
    name: 'First',
    components: {
      Gauge1: Gauge1,
      Gauge2: Gauge2,
      Line2: Line2,
      // myCanvas
    },

    mounted: function () {
      this.loadData();
      this.envProtectData();
      // this.interval = setInterval(function(){
      //   this.envProtectData();
      //   this.loadData();
      // }.bind(this), 5000);
    },
    // destroyed: function() {
    //   clearInterval(this.interval)
    // },

    methods: {
      envProtectData(){
        this.$ajax.get('http://localhost:8000/system/getHBSJ')
          .then(function (response) {
            //处理数据
            var hb_data = response.data.data;
            this.msg1 = hb_data.msg1;
            this.msg2 = hb_data.msg2;
            this.msg3 = hb_data.msg3;
            this.msg4 = hb_data.msg4;
            this.msg5 = hb_data.msg5;

          }.bind(this))
          .catch(function (error) {
            return 0;
          });
      },
      loadData(){
        this.$ajax.get('http://localhost:8000/system/getDQFDGL')
          .then(function (response) {
            //处理数据
            this.c1 = response.data.data.c1

          }.bind(this))
          .catch(function (error) {
            return 0;
          });
      }
    },
    data () {
      return {
        interval: 0,
        dotsNum: 60,
        activeName: 'first',
        //配置最下面的list
        percentage: {
          c1: (50 + Math.round(Math.random() * 50)) / 100,
          c2: (50 + Math.round(Math.random() * 50)) / 100,
          c3: (50 + Math.round(Math.random() * 50)) / 100

        },

        msg1: 77,
        msg2: 393.09,
        msg3: 10.86,
        msg4: 5429.41,
        msg5: 988.97,

        c1: {
          id: 'c1',
        },
        c2: {
          the: Math.round(500 + Math.random() * 500),
          act: Math.round(Math.random() * 500),
        },
        c3: {
          eff: Math.round(Math.random() * 100),
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
          g1: {
            id: 'gauge1',
            //需要输入的值-

            value: 0,
            option: {
              tooltip: {
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
                  detail: {formatter: '{value}kW'},
                  data: [{value: 50, name: '当前发电功率'}]
                }
              ]
            },
          },
          g2: {
            id: 'gauge2',
            option: {
              tooltip: {
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
                  detail: {formatter: '{value}%'},
                  data: [{value: 50, name: '综合发电效率'}]
                }
              ]
            },
          },
          g3: {
            id: 'gauge3',
            option: {
              tooltip: {
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
                  detail: {formatter: '{value}%'},
                  data: [{value: 50, name: '逆变器转换效率'}]
                }
              ]
            },
          },
          l1: {
            id: 'line1',
            request: ['http://localhost:8000/system/echartsDataForInverterFDL'],
            option: {
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
                data: ['逆变器发电量']
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
                  data:[]
                }
              ],
              yAxis: [
                {
                  type: 'value',
                  scale: true,
                  name: 'kWh',
                }
              ],
              series: [
                {
                  name: '逆变器发电量',
                  type: 'bar',
                  xAxisIndex: 0,
                  yAxisIndex: 0,
                  data: []
                }
              ]
            },
          },
          l2: {
            id: 'line2',
            request: ['http://localhost:8000/system/echartsDataForInverterFDGL', 'http://localhost:8000/system/echartsDataForFZD'],
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
                data: ['逆变器发电功率', '总辐照度']
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
                  data: (function () {
                    var now = new Date();
                    var res = [];
                    var len = 10;
                    while (len--) {
                      res.unshift(now.toLocaleTimeString().replace(/^\D*/, ''));
                      now = new Date(now - 2000);
                    }
                    return res;
                  })()
                },
              ],
              yAxis: [
                {
                  type: 'value',

                  name: 'kW',

                }
              ],
              series: [
                {
                  name: '逆变器发电功率',
                  type: 'line',
                  xAxisIndex: 0,
                  yAxisIndex: 0,
                  data: (function () {
                    var res = [];
                    var len = 10;
                    while (len--) {
                      res.push(Math.round(Math.random() * 1000));
                    }
                    return res;
                  })()
                },
                {
                  name: '总辐照度',
                  type: 'line',
                  xAxisIndex: 0,
                  yAxisIndex: 0,
                  data: (function () {
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
    width: 700px;
    margin-bottom: 20px;
    /* background-color:rgba(255, 255, 255, 0.3) */
    background: -webkit-linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);
    background: -o-linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);
    background: -moz-linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);
    background: linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);
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
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }

  .row1 {
    /* color: #909399; */
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

  .row2 {
    padding-left: 100px;
    padding-right: -40px;
    margin-top: -20px;
  }

  .card1 {
    position: relative;
    left: 100px;
    margin-left: -15px;
    width: 500px;
    height: 300px;
    /* background-color:rgba(255, 255, 255, 0.2) */
    background: -webkit-linear-gradient(30deg, rgb(55, 59, 68, 0.3), #355C7D);
    background: -o-linear-gradient(30deg, rgb(55, 59, 68, 0.3), #355C7D);
    background: -moz-linear-gradient(30deg, rgb(55, 59, 68, 0.3), #355C7D);
    background: linear-gradient(30deg, rgb(55, 59, 68, 0.3), #355C7D);
  }

  .card2 {
    width: 120px;
    height: 120px;
    position: relative;
    top: 100px;
    left: 120px;
    z-index: 1;
    background-color: rgba(190, 30, 30, 0.4)
  }

  /* .mainBody {
    height: 1000px;
  } */

  .button {
    float: right;
  }

  .fm2 {
    height: 50%;
  }

  .fml {
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

  .col1 {
    border: 5px dotted #12AFE3;
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
    line-height: 30px;
    font-size: 14px;
    color: gray;
  }

  .First {
    height: 100%;
  }

  .el-container {
    height: 100%;
    overflow-y: hidden;
    background: -webkit-linear-gradient(30deg, rgb(180, 180, 180, 0.1), #355C7D);
    background: -o-linear-gradient(30deg, rgb(180, 180, 180, 0.1), #355C7D);
    background: -moz-linear-gradient(30deg, rgb(180, 180, 180, 0.1), #355C7D);
    background: linear-gradient(30deg, rgb(180, 180, 180, 0.1), #355C7D);
    margin-left: -12px;
    margin-top: -12px;
  }

  .el-row {
    height: 60%;
    margin-bottom: 20px;
  }

  .el-col {
    border-radius: 4px;
    height: 100%;
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

  .envData li {
    float: left;
    width: 20%;
    list-style: none;
  }

  .icon {
    width: 50%;
  }

  .li1 {
    list-style-type: none;
    font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, SimSun, sans-serif;
    font-size: 14px;
    float: left;
    position: relative;
    top: 50px;
  }

  .text0 {
    margin-top: 5px;
    margin-right: 10px;
  }

  .box-card1 {

    background: -webkit-linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);
    background: -o-linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);
    background: -moz-linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);
    background: linear-gradient(30deg, rgb(55, 59, 68, 0.2), #355C7D);

  }

  .box {
    margin-right: 20px;
    margin-left: 30px;
    margin-top: -20px;
    margin-bottom: 20px;

  }

  .data {
    padding-left: 150px;
  }

  .inf {
    font-size: 20px;
    font-family: 'STHeiti Light [STXihei]';
    padding-top: 10px;
  }

  .row0 {
    margin-top: -80px;
  }

  .elcard0 {
    background-color: rgba(255, 255, 255, 0.3)
  }

</style>

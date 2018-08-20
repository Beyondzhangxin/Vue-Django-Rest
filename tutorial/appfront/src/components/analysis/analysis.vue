<template>

  <el-card class="card0">

    <el-header id="header" style="height:80px;">

      <el-row>
        <el-col :span="3">
          <div class="grid-content">
            <el-button id="button"  ref="button1" @click=" changeColor(1); carryModel.model='dzdb'; $store.commit('filter', '系统')">
              <img src="../../assets/station.png" id="image">
              <span id="text"><strong>电站对比</strong></span>
            </el-button>
          </div>
        </el-col>
        <el-col :span="3">
          <div class="grid-content">
            <el-button id="button"  ref="button2" @click=" changeColor(2); carryModel.model='sbdb'; $store.commit('filter', '逆变器')">
              <img src="../../assets/self.png" id="image">
              <span id="text"><strong>设备对比</strong></span>
            </el-button>
          </div>
        </el-col>
        <el-col :span="3">
          <div class="grid-content">
            <el-button id="button" disabled>
              <img src="../../assets/equipment.png" id="image">
              <span id="text"><strong>自身对比</strong></span>
            </el-button>
          </div>
        </el-col>
        <el-col :span="3">
          <div class="grid-content"></div>
        </el-col>
      </el-row>



    </el-header>

    <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">

    <!-- main1 -->
    <div id="main1">

      <card class="card1">
        <el-row>

        <div class="block">
          <span id="text0">查询内容</span>
          <el-select v-model="carryModel.compareParam" clearable placeholder="请选择" >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled">
          </el-option>
        </el-select>
        </div>


            <div class="block1">
            <span id="text1">查询日期</span>
            <!-- 日期选择器 -->
            <span class="demonstration"></span>
            <el-date-picker
              v-model="carryModel.searchDate"
              align="right"
              type="date"
              placeholder="选择日期"
              value-format="yyyy-MM-dd"
              :picker-options="pickerOptions1">
            </el-date-picker>
            </div>


        </el-row>
      </card>
    </div>

 <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">

    <!-- main2 -->
    <el-main id="main2">
      <el-row>
        <el-col :span="24">
          <div class="text2">已选电站：</div>
        </el-col>
      </el-row>
      <div class="sel">
        <el-button type="primary"  @click="" plain v-for="sel in selList"  :key="sel1" v-show="carryModel.model=='dzdb'">{{ sel.system }}</el-button>
        <span v-for="sel in selList" :key="sel2" v-show="carryModel.model=='sbdb'">
          <el-button type="primary"  @click="" plain v-for=" dev in sel.devices" :key="dev">{{ dev }}</el-button>
        </span>
      </div>

    </el-main>

    <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">

    <!-- main3 -->
    <el-main id="main3">
      <div class="m3">
        <Line3 v-bind="l2"></Line3>
      </div>
    </el-main>
    <!-- </el-container> -->
  </el-card>
</template>


<script>
  import Line3 from '../echarts_elements/Line3'


  export default {
    name: 'analysis',
    components: {
      Line3: Line3,

    },
    methods: {
      changeColor(num) {
        if(num == 1) {
          this.$refs.button1.type = "primary";
          this.$refs.button2.type = "";
        }
        if(num == 2) {
          this.$refs.button2.type = "primary"
          this.$refs.button1.type = "";
        }
      },
      loadData(){
        var url = ""
        var fromData = ""
        if (this.carryModel.model == 'dzdb') {
           url = 'http://localhost:8000/system/getStationCompareInfo';
           fromData = "stationList=" + JSON.stringify(this.carryModel.stationList) + "&compareParam=" + this.carryModel.compareParam + "&searchDate=" + this.carryModel.searchDate;
        }

        if (this.carryModel.model == 'sbdb') {
          url = 'http://localhost:8000/system/getDeviceCompareInfo';
          fromData = 'deviceList=' + JSON.stringify(this.carryModel.deviceList) + "&compareParam=" + this.carryModel.compareParam + "&searchDate=" + this.carryModel.searchDate;
        }

        var instance = this.$ajax.create({
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });

        instance.post(url,
          fromData
        )
          .then(function (response) {

            //处理数据
            this.l2.option.series= [];
            var dataList = [];
            if (this.carryModel.compareParam == 'DXSS') {
              for (var i = 0; i < response.data.data.series.length; i++) {
                var list = [];
                for (var j = 0; j < response.data.data.xAxis[0].data.length; j++) {
                  list.push(response.data.data.series[i].data);
                }
                dataList.push(list);
              }
              for (var i = 0; i < response.data.data.series.length; i++) {
                this.l2.option.series.push({
                  data: dataList[i],
                  name: response.data.data.series[i].name + " - " + this.carryModel.compareParam,
                  type: 'line',
                  xAxisIndex: 0,
                  yAxisIndex: 0,
                })
              }

            }else {
              for (var i = 0; i < response.data.data.series.length; i++) {
                this.l2.option.series.push({
                  data: response.data.data.series[i].data,
                  name: response.data.data.series[i].name + " - " + this.carryModel.compareParam,
                  type: 'line',
                  xAxisIndex: 0,
                  yAxisIndex: 0,
                })
              }
            }
            this.l2.option.xAxis[0].data = response.data.data.xAxis[0].data
            //{"bwrq": "2018-03-21", "ljfd": "5346.532596464663", "zjrl": 50.0, "dqgl": null, "jrdx": 0, "jrfd": 0.0}
          }.bind(this))
          .catch(function (error) {
            return 0;
          });
      },
    },

    data(){
      return {

          options: [{
          value: 'GL',
          label: '功率'
        }, {
          value: 'XL',
          label: '效率',
          disabled:true,
        }, {
          value: 'DXSS',
          label: '等效时数'
        }, {
          value: 'FHL',
          label: '符合率',
          disabled:true,
        }, {
          value: 'FDL',
          label: '发电量'
        }],
        selList: [],
        carryModel: {
          model: "dzdb",
          stationList: ['SPGS', 'PVMG'],
          deviceList: [],
          compareParam: "GL",
          searchDate: "2017-04-27",
        },
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
        l2: {
          id: 'line1',
          option: {
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
              data: ['多功能光伏电站系统', '图书馆微电网系统']
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
                data: []
              },
              {
                type: 'category',
                boundaryGap: true,
                data: []
              }
            ],
            yAxis: [
              {
                type: 'value',
                scale: true,
                name: 'kW',
              },
            ],
            series: []
          },
        },
        value1: '',
        value2: '',
      };
    },
    computed: {
      listenChooseTree() {
        return this.$store.state.chooseTree;
      }
    },
    watch: {
      listenChooseTree: function(val, oldval) {
        this.selList = val;
        this.carryModel.deviceList = [];
        this.carryModel.stationList = []
        for (var i = 0; i < val.length; i++) {
          //对station进行对比
          // for (var j = 0; j < this.carryModel.stationList.length; j++) {
          //   if (this.carryModel.stationList[j] == val[j].system) {
          //   }else {
          //     this.carryModel.stationList.push(val[j].system)
          //   }
          // }
          this.carryModel.stationList.push(val[i].system);
          if (val[i].system == "PVMG") {
            this.carryModel.deviceList.push({'PVMG':val[i].devices});
          }
          if (val[i].system == "SPGS") {
            this.carryModel.deviceList.push({'SPGS':val[i].devices});
          }
        }
      },
      carryModel:{
        handler:function(val,oldval){
          this.loadData();
        },
        deep:true//对象内部的属性监听，也叫深度监听
      }
    },
    mounted: function () {
      this.$store.commit('showIt');
      this.loadData();
      // this.interval = setInterval(function(){
      //   this.loadData();
      // }.bind(this), 5000);
    },
    destroyed: function () {
      this.$store.commit('hideIt');
      // clearInterval(this.interval);
    },
  }


</script>


<style scoped>

  .m3 {
    height: 550px;
    /* background-color: #fff; */
    /* background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
     background: -o-linear-gradient(30deg, #373B44, #355C7D);
     background: -moz-linear-gradient(30deg, #373B44, #355C7D);
     background: linear-gradient(30deg, rgb(55,59,68,0.4),#355C7D); */
    background-color: rgba(255, 255, 255, 0.3);
  }

  #header {
    background: white;
    padding-top: 10px;
    background-color: rgba(180, 180, 180, 0.1);
  }

  #button {
    background-color: rgba(255, 255, 255, 0.1)

  }

  #text {
    color: whitesmoke;
  }

  #button1 {
    margin-top: 10px;
    font-size: 14px;
    margin-bottom: 10px;
    background-color: rgba(255, 255, 255, 0.1)
  }

  #button2 {
    margin-top: 10px;
    font-size: 14px;
    margin-bottom: 10px;
    padding-right: 10px;
    padding-left: 10px;
  }

  #text {
    padding-bottom: 2px;
    padding-top: 2px;
    display: block;
    font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    font-size: 16px;
  }

  #span0 {
    padding-top: 10px;
    padding-left: 2px;
    font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    font-size: 16px;
    margin-left: -20px;
  }

  #span1 {
    /* background:white; */
  }

  #span2 {
    /* background:white; */
    padding-left: 250px;
    padding-top: 10px;

  }

  #span0 {
    margin-top: 8px;
    padding-left: 20px;
  }

  #main1 {
    margin-top: 20px;
    height: 80px;

  }

  #main2 {
    background-color: rgba(180, 180, 180, 0.1);
  }

  #main3 {
    margin-top: 50px;

  }

#text0{
  color: aliceblue;
  padding-right: 20px;
}


  #text1 {
    padding-right: 20px;
    /* margin-bottom: 10px; */
    color: aliceblue;
  }

  .text2 {
    float: left;
    margin-top: 20px;
    margin-left: 20px;
    color: aliceblue;
  }

  .sel {
    float: left;
    margin-top: 20px;
    margin-left: 100px;
    margin-bottom: 10px;
    padding-right: 20px;
  }

.card0{
    margin-top:-13px;
    background: -webkit-linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    background: -o-linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    background: -moz-linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    margin-left:-13px;
}

  .card1 {
    background-color: rgba(180, 180, 180, 0.1);
  }

.block{
  float: left;
  position:relative;
  left:20px;
  top:15px;
}

.block1{
  float:right;
  position:relative;
  right:700px;
  top:15px;
}
</style>

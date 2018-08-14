<template>
      <el-container class="c1">
        <!-- 调用canvas -->
        <!-- <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas> -->

        <el-main class="m1" style="height: 100%">

          <div class="mov">
            <el-card class="card1">
              <el-row>
                <span id="line" v-for="item in items" :key="item.id">{{ item.key }} <strong>{{ item.value +' '+ item.unit }}</strong></span>
              </el-row>
              <el-row>
              <el-col :span="24">
                <div class="spanList">
                  <span class="span1">
                    电站状态：
                  </span>
                  <span  class="span1">
                    <strong>正常 </strong><i class="el-icon-success"></i>
                  </span>
                  <span  class="span1">
                    <strong>异常 </strong><i class="el-icon-warning"></i>
                  </span>
                  <span  class="span1">
                    <strong>离线 </strong><i class="el-icon-loading"></i>
                  </span>
                  <span  class="span1">
                    <strong>停机 </strong><i class="el-icon-circle-close"></i>
                  </span>
                </div>
              </el-col>
            </el-row>
            </el-card>
          </div>

          <el-card class="card2">
              <el-row>
                <el-col>
                  <div class="col1">
                  当日有效时数:
                  <el-input class="row1input" v-model="input1" :value="number" placeholder="起始时间"></el-input>
                    ~
                  <el-input class="row1input" v-model="input2" :value="number" placeholder="结束时间"></el-input>
                </div>
                </el-col>

                <el-col>
                  <div class="col2">
                  电站所在地区:
                  <el-select class="select"
                  style="margin-left: 0px;"
                    v-model="value10"
                    multiple
                    filterable
                    allow-create
                    default-first-option
                    placeholder="请选择地区">
                    <el-option
                      v-for="item in options5"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
                  </div>
                </el-col>
              </el-row>
            </el-card>


          <div class="mm">
            <el-col :span="24"><div class="grid-content"></div></el-col>
            <elPower style="margin-top: 20px;" v-for="card in cardLists" v-bind="card"  :key="card"/>
          </div>

        </el-main>
        </el-container>

</template>


<script>
import Gauge from '../echarts_elements/Gauge1'
import Line2 from '../echarts_elements/Line2'
import elPower from './elPower'
// import myCanvas from 'vue-atom-canvas'


export default {
  name : 'Power',
  components: {
    elPower:elPower,
    // myCanvas
  },
  data () {
    return {
      input1: '',
      input2: '',
      showLists: [],
      //对应elpower中属性
      //依次是总装机容量 当前运行功率 当日有效时数 当月有效时数
      cardLists: [

        // {
        //   id: 'SH',
        //   msg1: 1,
        //   msg2: 1,
        //   msg3: 1,
        //   msg4: 1,
        //   msg5: 1,
        //   msg6: '',
        //   msg7: '上海光伏电站',
        // },

      ],
      items: [
          {
            key: "电站总数:",
            index: "dzzs",
            value: 2,
            unit: "座",
          },
          {
            key: "总装机容量:",
            index: "zjrl",
            value: 660.66,
            unit: "kWp",
          },
          {
            key: "今日总发电量:",
            index: "jrfdl",
            value: 3038.26,
            unit: "kWh",
          },
          {
            key: "累计总发电量:",
            index: "ljzjdl",
            value: 36.22,
            unit: "万kWh",
          }
      ],
      options5: [
        {
          value: 'ALL',
          label: '全部'
        },{
          value: 'BJ',
          label: '北京'
        },{
          value: 'SH',
          label: '上海',
        },{
          value: 'SZ',
          label: '深圳'
        },
      ],
        //和el-select选中程序同步
        value10: [],
    }
  },
  mounted: function() {
    this.loadData();
    this.$store.commit('showIt');
    //this.show();
  },

  destroyed: function() {
    this.$store.commit('hideIt')
  },

  methods: {
    loadData(){
      this.$ajax.get('http://localhost:8000/system/getStationMonitorInfo')
      .then(function (response) {
        console.log(737252537);
        console.log(response.data);
        //处理数据\
        for (var i = 0; i < this.items.length; i++) {
          if (this.items[i].index) {
            this.items[i].value = response.data.data.items[this.items[i].index]
          }
        }
        console.log(this.items);

        console.log(response.data.data.cardLists);
        for (var i = 0; i < response.data.data.cardLists.length; i++) {
          this.cardLists.push(response.data.data.cardLists[i])
        }
        console.log(this.cardLists);
      }.bind(this))
      .catch(function (error) {
        return 0;
      });
    },
    // show(){
    //   for (var i = 0; i < this.cardLists.length; i++) {
    //     this.showLists.push(this.cardLists[i]);
    //   }
    // },
    checkLists(card){
        //aside的过滤写在这里

        //有效时间的过滤
        try {
          if (this.input1&&card.msg3 <this.input1) {
            return false;
          }
          if (this.input2&&card.msg3 >this.input2) {
            return false;
          }
        } catch (e) {
          console.log(e);
        }
        //地区的过滤
        if (this.value10.length == 0) {
          return true;
        }
        for (var j = 0; j < this.value10.length; j++) {
          if ((this.value10[j]=='ALL')||(card.id == this.value10[j])) {
            return true;
          }
        }
        return false;
    },
  }
}
</script>


<style scoped>
  .spanList {
    margin-top: 15px;
  }

   .span1 {
     float:left;
   }

  .col1 {
    float: left;
    padding-bottom: 1%;
    padding-left: 0px;
  }

  .col2 {
    float: left;
  }

  .row1input {
    width: 200px;
  }

  .areaRow {
    position: relative;
    right: 3%;
    width: 30%;
  }

  .row1 {
    width: 524px;
    margin-bottom: 22px;
  }

  .c1 {
    margin-top:-12px;
    width:100%;
    height:100%;
  }

  .m1 {
    width: 100%;
    height:100%;
    margin-left:-12px;
    /* overflow: hidden; */
  }

  .cardList {
    padding-top: 3%;
    height: 1200px;
  }

  .el-container {
    height: 100%;
    width:100%
  }


  .Power {
    height: 100%;
    width: 1500px;
    box-shadow: 1px 1px 10px 5px #c0c0c0;
    /* margin: 60px; */
  }

  .el-main {
    height: 80%;
    background:white
  }

  .el-header{
    background:white;
    margin-bottom:35px;
  }

  .mm {
    margin-top: 14px;
    height: 00px;
  }

  #main1 {
    height: 1400px;
  }

  #input {
    /* width: 80px; */
    margin-top:5px;
    border-radius:10px;
  }

  #label{
    margin-top:5px;
    margin-left:80px;
  }

  #li {
    float: left;
    display: inline-block;
  }

.num1{
  margin-left:30px;
  margin-top:20px;
  font-size:15px;
  font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}

#num{
  margin-top:20px;
  margin-left:-65px;
  font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;

}

 .hour{
   margin-left:75px;

 }

#time{
  margin-left: -105px;
  margin-top:0px;
  font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size:16px;
}

#area{
  margin-left: 10px;
  padding-top:10px;
  font-size:16px;
  font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}

#line{
  margin-right: 38px;
  float:left;
  font-size:16px;
  font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}

.mov span{
  margin-right: 55px;
}

.el-select{
  margin-top:0px;
  margin-left:30px;
}

.mov{
  height:100px;
  /* margin-left:-65px; */
  margin-bottom:20px;

}

/* .row{
  padding: 10px;
  height: 70px;
  padding-top: 20px;
} */

.card1{
     /* background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D); */
    background-color:rgba(180, 180, 180, 0.1);
    margin-top:20px;
    margin-right:30px;
    margin-left:10px;
}

.card2{
     /* background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D); */
    background-color:rgba(180, 180, 180, 0.1);
    margin-right:30px;
    margin-left:10px;
}

.el-main{
   background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
}
</style>

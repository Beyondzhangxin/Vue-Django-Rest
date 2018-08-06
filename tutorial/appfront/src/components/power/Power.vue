<template>
      <el-container class="c1">
        <el-main class="m1" style="height: 100%">
          <div class="mov">
            <el-card>
              <el-row>
                <span id="line" v-for="item in items[0]" :key="item.id">{{ item.key }} <strong>{{ item.value }}</strong></span>
              </el-row>
              <el-row class="row1">
              <el-col :span="2">电站状态：</el-col>
              <el-col :span="2">
                <div><strong>正常 </strong><i class="el-icon-success"></i> </div>
              </el-col>
              <el-col :span="2">
                <div><strong>异常 </strong><i class="el-icon-warning"></i> </div>
              </el-col>
              <el-col :span="2">
                <div><strong>离线 </strong><i class="el-icon-loading"></i> </div>
              </el-col>
              <el-col :span="2">
                <div><strong>停机 </strong><i class="el-icon-circle-close"></i></div>
              </el-col>
            </el-row>
            </el-card>
          </div>

          <el-card>
          <div class="row1">
              <el-row :gutter=20>
                <el-col :span="6" id ="time">当日有效时数:</el-col>
                <el-col :span="4">
                  <el-input v-model="input1" :value="number" placeholder="起始时间"></el-input>
                </el-col>
                <el-col :span="1" class="span0">
                  ~
                </el-col>
                <el-col :span="4">
                  <el-input v-model="input2" :value="number" placeholder="结束时间"></el-input>
                </el-col>
                <el-col :span="4">
                  <div class="hour"></div>
                </el-col>
              </el-row>
            </div>

            <div class="row2">
              <el-row :gutter=20>
                <el-col :span="8" id="area">电站所在地区</el-col>
                <el-col :span="5">
                  <el-select class="select"
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
                </el-col>
              </el-row>
            </div>
          </el-card>

          <div class="mm">
            <el-col :span="24"><div class="grid-content"></div></el-col>
            <elPower style="margin-top: 20px;" v-for="card in showLists" v-show="checkLists(card)" v-bind="card" :key="card"/>
          </div>
        </el-main>
        </el-container>

</template>


<script>
import Gauge from '../echarts_elements/Gauge1'
import Line2 from '../echarts_elements/Line2'
import elPower from './elPower'


export default {
  name : 'Power',
  components: {
    elPower:elPower,
  },
  data () {
    return {
      input1: '',
      input2: '',
      showLists: [],
      //对应elpower中属性
      //依次是总装机容量 当前运行功率 当日有效时数 当月有效时数
      cardLists: [
        {
          id: 'BJ',
          msg1: 1,
          msg2: 1,
          msg3: 2,
          msg4: 1,
          msg5: 1,
          msg6: '',
        },
        {
          id: 'SH',
          msg1: 1,
          msg2: 1,
          msg3: 1,
          msg4: 1,
          msg5: 1,
          msg6: '',
        },
      ],
      items: [
        [
          {
            key: "电站总数:",
            value: 2+"座",
          },
          {
            key: "总装机容量:",
            value: 660.66+"kWp",
          },
          {
            key: "今日总发电量:",
            value: 3038.26+"kWh",
          },
          {
            key: "累计总发电量:",
            value: 36.22+"万kWh",
          },
        ],
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
    this.$store.commit('showIt');
    this.show();
  },

  destroyed: function() {
    this.$store.commit('hideIt')
  },

  methods: {
    show(){
      for (var i = 0; i < this.cardLists.length; i++) {
        this.showLists.push(this.cardLists[i]);
      }
    },
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


  .row1 {
    position: relative;
    margin-top: 10px;
    padding: 5px;
    padding-left: 0px;
    padding-right: 0px;
    left: -3px;
    height:100px;
  }

  .c1 {
    margin-top: 40px;
    margin-left: 50px;
    margin-right: 50px;
  }

  .span0 {
    padding: 10px;
    margin-top:-10px;
  }

  .m1 {
    width: 100%;
  }

  .cardList {
    padding-top: 3%;
    height: 1200px;
  }

  .el-container {
    height: 100%;

  }
  .el-row {
    /* display: block; */
    height: 60%;
    margin-bottom: 0;
  }

  .Power {
    height: 100%;
    width: 1500px;
    box-shadow: 1px 1px 10px 5px #c0c0c0;
    margin: 60px;
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
  padding: 2px;
  float:left;
  font-size:16px;
  font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}

.mov span{
  margin:0 15px;
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


.row2{
  margin-left:-220px;
}

.el-input{
  margin-top:-10px;
  margin-bottom:20px;

}
</style>

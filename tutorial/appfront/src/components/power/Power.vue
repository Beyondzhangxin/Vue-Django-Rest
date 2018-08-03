<template>
  <div class="Power">
    <el-container class="c1">
        <el-main class="m1" style="height: 100%">
          <div class="mov">
            <el-card>
          <el-row>
          <el-col :span="4" id="line" v-for="item in items[0]" :key="item.id">{{ item.key+item.value }}</el-col>
        </el-row>
        <el-row>
          <el-col :span="4" id="num">电站状态：</el-col>
          <el-col :span="2">
            <div class="num1">正常 <i class="el-icon-success"></i> </div>
          </el-col>
          <el-col :span="2">
            <div class="num1">异常 <i class="el-icon-warning"></i> </div>
          </el-col>
          <el-col :span="2">
            <div class="num1">离线 <i class="el-icon-loading"></i> </div>
          </el-col>
          <el-col :span="2">
            <div class="num1">停机 <i class="el-icon-circle-close"></i> </div>
          </el-col>
        </el-row>
            </el-card>
          </div>

          <el-card>
          <div class="row">
              <el-row :gutter=20>
                <el-col :span="6" id ="time">当日有效时数:</el-col>
                <el-col :span="4">
                  <input id="input" type="text" placeholder="请输入数字"></input>
                </el-col>
                <el-col :span="2" id="label">
                  ~
                </el-col>
                <el-col :span="4">
                  <input id="input" type="text" placeholder="请输入数字"></input>
                </el-col>
                <el-col :span="4">
                  <div class="hour">小时</div>
                </el-col>
              </el-row>
            </div>

            <div class="row">
              <el-row :gutter=20>
                <el-col :span="8" id="area">电站所在地区</el-col>
                <el-col :span="14">
                  <el-select
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
            <div class="cardList">
                <elPower v-for="card in showLists" v-show="checkLists(card)" v-bind="card" :key="card"/>
            </div>
          </div>
        </el-main>
        </el-container>
  </div>
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
      showLists: [],
      //对应elpower中属性
      cardLists: [
        {
          id: 'BJ',
          msg1: 1,
          msg2: 1,
          msg3: 1,
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


  .m1 {
    width: 100%;
  }

  .cardList {
    padding-top: 3%;
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
  margin-left:50px;
  margin-top:20px;
}

#num{
  margin-top:20px;
  margin-left:-7px;
}

 .hour{
   margin-left:75px;
   margin-top:7px;
 }

#time{
  margin-left:-10px;
  margin-top:5px;
}

#area{
  margin-left:18px;
  padding-top:10px;
}

#line{
  margin-left:0px;
  margin-top:5px;
  padding-left:-10px;
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

.row{
  margin-bottom:10px;
  height:50px;
}



</style>

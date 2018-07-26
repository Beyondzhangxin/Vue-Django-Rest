<template>
  <div class="Power">
    <el-container>
    
      <!-- head部分 -->
      <el-header>
        <el-row>
          <el-col :span="4" v-for="item in items[0]" :key="item.id">{{ item.key+item.value }}</el-col>
        </el-row>
        <el-row>
          <el-col :span="2"><div class="num">电站状态：</div></el-col>
          <el-col :span="2">
            <div class="num">正常</div>
          </el-col>
          <el-col :span="2">
            <div class="num">异常</div>
          </el-col>
          <el-col :span="2">
            <div class="num">离线</div>
          </el-col>
          <el-col :span="2">
            <div class="num">停机</div>
          </el-col>
        </el-row>
      </el-header>

      <!-- main mh部分 -->
      <el-main>
        <el-container>
          <el-header class="mh">
            <div class="row">
              <el-row>
                <el-col :span="3">当日有效时数:</el-col>
                <el-col :span="3">
                  <input id="input" type="text" style="margin-top:2px"></input>
                </el-col>
                <el-col :span="1">
                  ~
                </el-col>
                <el-col :span="3">
                  <input id="input" type="text" style="margin-top:2px"></input>
                </el-col>
                <el-col :span="3">
                  <div class="hour">小时</div>
                </el-col>
              </el-row>
            </div>
            <div class="row">
              <el-row>
                <el-col :span="3" style="padding-top:10px" >电站所在地区</el-col>
                <el-col :span="7">
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
          </el-header>

          <!-- main mm部分 -->
          <el-main class="mm">
            

          </el-main>
          
        </el-container>
      </el-main>
    </el-container>
  </div>
</template>


<script>
import Gauge from '../echarts_elements/Gauge1'
import Line2 from '../echarts_elements/Line2'


export default {
  name : 'Power',
  components: {
  },
  data () {
    return {
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
          value: '全部',
          label: '全部'
        },{
          value: '北京',
          label: '北京'
        },{
          value: '上海',
          label: '上海'
        },{
          value: '深圳',
          label: '深圳'
        },
      ],
        value10: []
    }
  }
}
</script>


<style scoped>
  .el-container {
    height: 100%;
  }
  .el-row {
    /* display: block; */
    height: 60%;
    margin-bottom: 0;
  }
  .el-col {
    /* display: inline-block; */
    /* border: 1px solid black; */
    
  }

  .Power {
    height: 100%;
  }

  .el-main {
    height: 80%;
  }

  .mh {
    /* border: 1px solid black; */
  }

  .mm {
    border: 1px solid black;
    border-top: 0px;
  }

  #input {
    width: 80px
  }

  #li {
    float: left;
    display: inline-block;
  }

.num{
  margin-left:70px;
}
 
 .hour{
   margin-left:-100px;
 }


</style>

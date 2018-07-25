<template>
  <div class="Power">
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="4" v-for="item in items[0]">{{ item.key+item.value }}</el-col>
        </el-row>
        <el-row>
          <el-col :span="2">电站状态</el-col>
          <el-col :span="2">
            <div>全部</div>
          </el-col>
          <el-col :span="2">
            <div>正常</div>
          </el-col>
          <el-col :span="2">
            <div>异常</div>
          </el-col>
          <el-col :span="2">
            <div>离线</div>
          </el-col>
          <el-col :span="2">
            <div>停机</div>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
        <el-container>
          <el-header class="mh">
            <div class="row">
              <el-row>
                <el-col :span="3">当日有效使数:</el-col>
                <el-col :span="4">
                  <div>小时</div>
                </el-col>
                <el-col :span="3">
                  <input>

                  </input>
                </el-col>
                <el-col :span="1">
                  ~
                </el-col>
                <el-col :span="3">
                  <input>

                  </input>
                </el-col>
                <el-col :span="3">
                  <div>小时</div>
                </el-col>
              </el-row>
            </div>
            <div class="row">
              <el-row>
                <el-col :span="3">电站所在地区</el-col>
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
      msg: "Hello world",
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
    display: block;
    height: 50%;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    display: inline-block;
    border: 1px solid black;
  }

  .Power {
    height: 100%;
  }

  .el-main {
    height: 80%;
  }

  .el-select {

  }

  .mh {
    border: 2px solid black;
  }

  .mm {
    border: 2px solid black;
    border-top: 0px;
  }

  .row .el-row{

  }

  input {
    width: 50px

  }


  #plist {

  }
  #li {
    float: left;
    display: inline-block;
  }
</style>

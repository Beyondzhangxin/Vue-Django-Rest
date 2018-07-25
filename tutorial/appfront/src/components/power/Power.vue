<template>
  <div class="Power">
    <div id="pheader">
      <div id="">123</div>
      <div id="">213</div>
    </div>
    <div id="pmain">
      <el-row>
        <el-col :span="12"><div class="grid-content1 bg-purple">北京光伏电站</div></el-col>
        <el-col :span="12"><div class="grid-content1 bg-purple-light">上海光伏电站</div></el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="6"><div class="grid-content2 bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content2 bg-purple">
          <div id="text">
          <div class="text1">总装机容量：</div><br>
          <div class="text2">当前运行功率：</div><br>
          <div class="text3">当日有效时数：</div><br>
          <div class="text4">当月有效时数：</div><br>
          </div>
        </div></el-col>
        <el-col :span="6"><div class="grid-content2 bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content2 bg-purple">
          <div id="text">
          <div class="text1">总装机容量：</div><br>
          <div class="text2">当前运行功率：</div><br>
          <div class="text3">当日有效时数：</div><br>
          <div class="text4">当月有效时数：</div><br>
          </div>
        </div></el-col>
      </el-row>
      <el-row>
        <el-col :span="12"><div class="grid-content3 bg-purple">正常</div></el-col>
        <el-col :span="12"><div class="grid-content3 bg-purple-light">正常</div></el-col>
      </el-row>
    </div>
    </div>
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
     
    }
  }
}
</script>
<style scoped>
  .Power {
    height: 100%;
    width: 100%;
  }
  #pheader {
    height: 100px;
  }
  #pheader div{
    margin: 0 auto;
    padding: 6px 0 8px;
    float: left;
  }
  #pmain{
    height: 400px;
    background-color: white;
  }

 .el-row {
    margin-bottom: 20px;
  }

  .el-col {
    border-radius: 4px;
  }

.bg-purple {
    background: #d3dce6;
  }

  .bg-purple-light {
    background: #e5e9f2;
  }

  .grid-content1 {
    border-radius: 4px;
    min-height: 40px;
    padding-top:10px;
  }

 .grid-content2 {
    border-radius: 4px;
    min-height: 200px;
    margin-top:20px;
  }

.grid-content3{
    border-radius: 4px;
    min-height: 50px;
    margin-top:20px;
    padding-top:10px;
}

#text{
  float:left;margin-top:20px;margin-left:10px;
}
</style>

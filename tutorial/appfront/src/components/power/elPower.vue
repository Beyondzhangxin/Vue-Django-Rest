<template>
  <el-card class="box-card" >
    <div slot="header" class="clearfix">
      <span>{{ id }}</span>
      <el-button style="float: right; padding: 3px 0" type="text"></el-button>
    </div>
    <div class="text item">
      <img class="image1" ref="image" src="..\..\assets\SHGF.jpg">
      <el-row>
        <el-col :span="12"><div class="grid-content1">
          <div class="tem1">总装机容量：<strong>{{(zjrl||"0")}}</strong>kwp</div>
          <div class="tem2">当前运行功率：<strong>{{(yxgl||"0")}}</strong>kw</div>
          <div class="tem3">当日有效时数：<strong>{{(dayHours||"0")}}</strong>h</div>
          <div class="tem4">当月有效时数：<strong>{{(monthHours||"0")}}</strong>h</div>
        </div></el-col>
        <el-col :span="12"><div class="grid-content2">
          <div class="con">电站状态：&nbsp正常&nbsp</div>
          <div class="mes">异常消息：&nbsp<strong>{{messageNum}}</strong>条</div>
        </div></el-col>
        </el-row>
    </div>
  </el-card>
</template>

<script>
export default {
  name : 'powerCard',
  props: ['status','messageNum','dayHours','id','monthHours','yxgl','zjrl'],
  data () {
    return {
        c1: {
        total: 1,
        day: 1,
        mounth: 1,
        sumAll: 1,
      },
    }
  },
  mounted: function() {
    this.$refs.image.src = "/static/img/SHGF.c4b0247.jpg";
  }
}

</script>

<style scoped>

.el-row {
    margin-bottom: 20px;
    margin-bottom: 0;
 }

.el-col {
    border-radius: 4px;
}


 .text {
    font-size: 15px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    height: 600px;
    margin-bottom: 20px;
    width: 49%;
    float: left;
    background: -webkit-linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
    background: -o-linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
    background: -moz-linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
  }

.image1{
  height:300px;
  width:50%;
  float:left;
}

.tem1{
  color: #909399;
    padding-top: 25px;
    padding-bottom: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
    padding-left:12px;
}

.grid-content1 strong {
    font-size: 15px;
    font-weight: 300;
    color: #974e45;
}

.con{
    color: #909399;
    padding-top: 13px;
    padding-bottom: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
    padding-left:10px;
}

.mes{
    color: #909399;
    padding-top: 13px;
    padding-bottom: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
    padding-left:0px;
}
.grid-content2 strong {
    font-size: 15px;
    font-weight: 300;
    color: #974e45;
}

.tem2{
    padding-left:17px;
    color: #909399;
    padding-top: 13px;
    padding-bottom: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
}

.tem3{
    padding-left:10px;
    color: #909399;
    padding-top: 13px;
    padding-bottom: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
}

.tem4{
    padding-left:10px;
    color: #909399;
    padding-top: 13px;
    padding-bottom: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
}

</style>

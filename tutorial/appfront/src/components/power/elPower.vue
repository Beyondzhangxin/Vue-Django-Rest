<template>
  <el-card class="box-card" >
    <div slot="header" class="clearfix">
      <span>北京光伏电站</span>
      <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
    </div>
    <div class="text item">
      <img class="image1" ref="image" src="..\..\assets\SHGF.jpg">
      <el-row>
        <el-col :span="12"><div class="grid-content1">
          <div class="tem1">总装机容量：<strong>{{(c1.total||"~")}}</strong>kwp</div>
          <div class="tem2">当前运行功率：<strong>{{(c1.total||"~")}}</strong>kw</div>
          <div class="tem3">当日有效时数：<strong>{{(c1.total||"~")}}</strong>h</div>
          <div class="tem4">当月有效时数：<strong>{{(c1.total||"~")}}</strong>h</div>
        </div></el-col>
        <el-col :span="12"><div class="grid-content2">
          <div class="con">正常&nbsp&nbsp&nbsp&nbsp<i class="el-icon-circle-check"></i></div>
          <div class="mes">消息：<strong>{{msg5}}</strong>条</div>
        </div></el-col>
        </el-row>
    </div>
  </el-card>
</template>

<script>
export default {
  name : 'powerCard',
  props: ['msg1','msg2','msg3','msg4','msg5','msg6'],
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
    console.log(this.msg6);
    console.log(this.$refs.image.src)
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
  }

.image1{
  height:300px;
  width:100%;
}

.tem1{
  color: #909399;
    padding-top: 13px;
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
}

.mes{
    color: #909399;
    padding-top: 13px;
    padding-bottom: 10px;
    box-sizing: border-box;
    border-bottom: 1px solid #eeeeee;
    padding-left:5px;
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

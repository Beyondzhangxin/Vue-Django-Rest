<template>
  <el-card class="box-card" shadow="always">
    <div slot="header" class="clearfix">
      <span>北京光伏电站</span>
      <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
    </div>
    <div class="text item">
      <img v-bind:src="msg6" class="image1">
      <el-row>
        <el-col :span="12"><div class="grid-content1">
          <div class="tem1">总装机容量：{{msg1}}kwp</div>
          <div class="tem2">当前运行功率：{{msg2}}kw</div>
          <div class="tem3">当日有效时数：{{msg3}}h</div>
          <div class="tem4">当月有效时数：{{msg4}}h</div>
        </div></el-col>
        <el-col :span="12"><div class="grid-content1">
          <div class="con">正常&nbsp&nbsp&nbsp&nbsp<i class="el-icon-circle-check"></i></div>
          <div class="mes">消息：{{msg5}}条</div>
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

    }
  },
  mounted: function() {
    console.log(this.msg6);
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
    width: 50%;
  }

.image1{
  height:300px;
  width:100%;
}

</style>

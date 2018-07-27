<template>
<div class=text>
    <p v-html="msg1"></p>


  <el-row>
      <el-col id="obj1">
      <el-card :body-style="{ padding: '0px' }">
      <img src="" class="image">
      <div style="padding: 14px;">
        <span>停机设备</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">操作按钮</el-button>
        </div>
      </div>
    </el-card>
    </el-col>

    <el-col id="obj2">
     <el-card :body-style="{ padding: '0px' }">
      <img src="" class="image">
      <div style="padding: 14px;">
        <span>告警设备</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">操作按钮</el-button>
        </div>
      </div>
    </el-card>
    </el-col>

    <el-col id="obj3">
     <el-card :body-style="{ padding: '0px' }">
      <img src="" class="image">
      <div style="padding: 14px;">
        <span>离线设备</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">操作按钮</el-button>
        </div>
      </div>
    </el-card>
    </el-col>

</el-row>

</div>
</template>


<script>
export default {
  name: 'text',
  data: function (){
    return {
        msg1:'异常检测共3项',
    }
  },
}


</script>


<style scoped>
.text{
float:left;margin-top:-10px;
}

 .el-row {
    margin-bottom: 20px;
      margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
    
  }


  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }


#obj1{
  margin-left:20px;
}

#obj2{
  float:right
}

#obj3{
   float:right
}

</style>

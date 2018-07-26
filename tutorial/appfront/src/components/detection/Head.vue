<template>
<div class=text>
    <p v-html="msg1"></p>

  <el-row>
      <el-col ：span="6">
      <el-card id="lef" :body-style="{ padding: '0px' }">
      <img src="" class="image">
      <div style="padding: 14px;">
        <span>停机设备</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">操作按钮</el-button>
        </div>
      </div>
    </el-card>
    

     <el-card id="mid" :body-style="{ padding: '0px' }">
      <img src="" class="image">
      <div style="padding: 14px;">
        <span>告警设备</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">操作按钮</el-button>
        </div>
      </div>
    </el-card>

     <el-card id="rig" :body-style="{ padding: '0px' }">
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

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
<style>
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


#lef{
  margin-left:20px;
}

#mid{
  float:right
}

#rig{
   float:right
}
</style>

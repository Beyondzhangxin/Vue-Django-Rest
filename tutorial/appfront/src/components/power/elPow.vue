<template>
  <div> 
    <el-row>
      <el-col :span="24"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
     <el-row :gutter="20">
      <el-col :span="12"><div class="grid-content bg-purple">
        <!-- 卡片一 -->
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>北京光伏电站</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <div class="text item">
              <img src="../../assets/BJGF.jpg" class="image1">
              <div>总装机容量：{{msg1}}</div>
              <div>当前运行功率：{{msg2}}</div>
              <div>当日有效时数：{{msg3}}</div>
              <div>当月有效时数：{{msg4}}</div>
            </div>
          </el-card>   
      </div></el-col>

      <el-col :span="12"><div class="grid-content bg-purple">
        <!-- 卡片二 -->
       <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>上海光伏电站</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <div class="text item">
               <img src="../../assets/SHGF.jpg" class="image2">
              <div>总装机容量：{{msg5}}</div>
              <div>当前运行功率：{{msg6}}</div>
              <div>当日有效时数：{{msg7}}</div>
              <div>当月有效时数：{{msg8}}</div>  
            </div>
          </el-card>
      </div></el-col>
    </el-row>

</div> 

 </template>

 <script>

 export default {
   name : 'Power',
   components: {
    
   },
   data () {
     return {
       msg1:1,
       msg2:2,
       msg3:3,
       msg4:4,
       msg5:5,
       msg6:6,
       msg7:7,
       msg8:8,
       
     }
   }
 }
</script>


<style>
.el-row {
    margin-bottom: 20px;
    margin-bottom: 0;
 }

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.bg-purple {
    background: #d3dce6;
}

 .text {
    font-size: 14px;
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
    width: 100%;
  }

.image1{
  height:300px;
  width:100%;
}

.image2{
  height:300px;
  width:100%;
}


</style>
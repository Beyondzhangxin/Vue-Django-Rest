<template>
  <div>
    <el-row>
      <el-col :span="24"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
     <el-row :gutter="20">
      <el-col :span="12"><div class="grid-content bg-purple">
        <!-- 卡片一 -->
          <el-card class="box-card" shadow="always">
            <div slot="header" class="clearfix">
              <span>北京光伏电站</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <div class="text item">
              <img src="../../assets/BJGF.jpg" class="image1">
              <el-row>
                <el-col :span="12"><div class="grid-content1">
                  <div class="tem1">总装机容量：{{msg1}}kwp</div>
                  <div class="tem2">当前运行功率：{{msg2}}kw</div>
                  <div class="tem3">当日有效时数：{{msg3}}h</div>
                  <div class="tem4">当月有效时数：{{msg4}}h</div>
                </div></el-col>
                <el-col :span="12"><div class="grid-content1">
                  <div class="con">正常&nbsp&nbsp&nbsp&nbsp<i class="el-icon-circle-check"></i></div>
                  <div class="mes">消息：{{msg9}}条</div>
                </div></el-col>
              </el-row>
            </div>
          </el-card>
      </div></el-col>

      <el-col :span="12"><div class="grid-content bg-purple">
        <!-- 卡片二 -->
       <el-card class="box-card" shadow="always">
            <div slot="header" class="clearfix">
              <span>上海光伏电站</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <div class="text item">
               <img src="../../assets/SHGF.jpg" class="image2">
              <el-row>
                <el-col :span="12"><div class="grid-content1">
                  <div class="tem5">总装机容量：{{msg5}}kwp</div>
                  <div class="tem6">当前运行功率：{{msg6}}w</div>
                  <div class="tem7">当日有效时数：{{msg7}}h</div>
                  <div class="tem8">当月有效时数：{{msg8}}h</div>
                </div></el-col>
                <el-col :span="12"><div class="grid-content1">
                  <div class="con">正常&nbsp&nbsp&nbsp&nbsp<i class="el-icon-circle-check"></i></div>
                  <div class="mes">消息：{{msg10}}条</div>
                </div></el-col>
                </el-row>
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
       msg1:623.16,
       msg2:88.46,
       msg3:4.77,
       msg4:61.17,
       msg5:37.5,
       msg6:3459.0,
       msg7:1.83,
       msg8:36.19,
       msg9:0,
       msg10:3
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

.tem3{
  margin-left:-18px;
}

.tem4{
  margin-left:-10px;
}

.tem5{
  margin-left:-2px;
}

.tem7{
  margin-left:-8px;
}

.con{
  padding-right:8px;
}

.grid-content1{
  margin-top:10px;
}
</style>

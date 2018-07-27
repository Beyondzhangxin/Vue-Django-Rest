<template>
  <div class="detection">
    <el-container>
      <el-container>
        <deHeader/>
          <el-main>
           <el-row>
        <el-col><div class="grid-content bg-purple-dark">
          <el-row>
          <!-- 卡片一 -->
        <el-col :span="8"><div class="grid-content bg-purple">
        <el-card :body-style="{ padding: '0px' }">
        <img src="../../assets/close.png" class="image">
        <div style="padding: 14px;">
        <span>停机设备</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">操作按钮</el-button>
        </div>
        </div>
        </el-card>    
        </div></el-col>
          <!-- 卡片二 -->
        <el-col :span="8"><div class="grid-content bg-purple"> 
        <el-card :body-style="{ padding: '0px' }">
        <img src="../../assets/alarm.png" class="image">
        <div style="padding: 14px;">
        <span>告警设备</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">操作按钮</el-button>
          </div>
        </div>
        </el-card>          
        </div></el-col>
        <!-- 卡片三 -->
        <el-col :span="8"><div class="grid-content bg-purple">
         <el-card :body-style="{ padding: '0px' }">
        <img src="../../assets/offline.png" class="image">
        <div style="padding: 14px;">
          <span>离线设备</span>
        <div class="bottom clearfix">
        <el-button type="text" class="button">操作按钮</el-button>
        </div>
        </div>
        </el-card> 
        </div></el-col>

          <div class="foot">设备异常检测</div>
        </el-row>    
        </div></el-col>
        </el-row>
            <!--通用list-->
            <ComList data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></ComList>
            <el-pagination
            background
            layout="prev, pager, next"
            :total="1000">
            </el-pagination>
          </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
    import ComList from '../el-simple-com/com-list.vue'
    import deHeader from './Head.vue'

  export default {
    name: 'faultdetection',
    components: {
        ComList: ComList,
        DeHeader: deHeader,
    },
    data(){
      return {

        // pageSize: 2
      }
    },
  }
</script>

<style scoped>
  /* 导入iconfont的css*/
  .el-header {
    height: 100px;
  }

  .detection {
    height: 100%;
  }

  .el-container {
    height: 100%;
  }

  .el-container font{
    font-size: 20px;
  }

  .detection-title {
    text-align: left;
    font-size: 11px;
    margin-bottom: 10px;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 200px;
  }

 .bg-purple-dark {
    background:white;
  }

  .el-row {
    margin-bottom: 20px;

  }

  .el-col {
    border-radius: 4px;
  }

 .bg-purple-light {
    background: #e5e9f2;
  }

.button {
    padding: 0;
    float: right;
  }

  .image {
    margin: 0 auto;
    display: block;
    margin-top:10px;
  
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

.foot{
  margin-bottom:50px;
}
</style>

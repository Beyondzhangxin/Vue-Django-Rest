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
      </el-row class="rowm">
            <!--通用list-->
            <!--请求如下 http://127.0.0.1:8000/pv/get/detection/2018/1/18/ -->
            <div class="rowmb">
            <!--赋值到this.data中 -->
            <ComList v-bind:data='data'></ComList>
            <!--<ComList v-bind:data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></ComList>-->

              <el-pagination
              background
              layout="prev, pager, next"
              :total="1000"
              @current-change="handleCurrentChange">
              </el-pagination>
            </div>
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
        data: 'http://127.0.0.1:8000/pv/get/detection/2018/1/18/',
        page: 1,
        // pageSize: 2
      }
    },
    methods: {
      handleCurrentChange(val) {
        this.data = 'http://127.0.0.1:8000/pv/get/detection/2018/1/18/' + '?page='+ val;
        console.log(this.data);
      }
    }
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

  .el-pagination {
    position: absolute;

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

.rowm{
  height: 400px;
}
.rowmb{
  height: 450px;
  background: #fff;
}
</style>

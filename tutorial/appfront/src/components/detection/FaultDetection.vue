<template>
  <div class="detection">
    <el-container>
          <el-main class="detectMain">
            <div>
              <el-card>
                <el-row>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '0px' }">
                     <img src="../../assets/close.png" class="image">
                     <div style="padding: 14px;">
                       <span>停机设备</span>
                       <div class="bottom clearfix">
                         <el-button type="text" class="button">操作按钮</el-button>
                       </div>
                     </div>
                   </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '0px' }">
                      <img src="../../assets/alarm.png" class="image">
                      <div style="padding: 14px;">
                        <span>告警设备</span>
                        <div class="bottom clearfix">
                          <el-button type="text" class="button">操作按钮</el-button>
                        </div>
                      </div>
                    </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '0px' }">
                      <img src="../../assets/offline.png" class="image">
                      <div style="padding: 14px;">
                        <span>离线设备</span>
                        <div class="bottom clearfix">
                          <el-button type="text" class="button">操作按钮</el-button>
                        </div>
                      </div>
                    </el-card>
                  </el-col>
                </el-row>
                <el-row>设备检查异常</el-row>
              </el-card>
            </div>
            <!--通用list-->
            <!--请求如下 http://127.0.0.1:8000/pv/get/detection/2018/1/18/ -->
            <el-card class="card2">
              <ComList v-bind:data='data'></ComList>
              <!--<ComList v-bind:data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></ComList>-->
              <el-pagination
                background
                layout="prev, pager, next"
                :total="1000"
                @current-change="handleCurrentChange">
              </el-pagination>
            </el-card>
          </el-main>
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
    },
    mounted: function() {
      this.$store.commit('showIt')
    },

    destroyed: function() {
      this.$store.commit('hideIt')
    },


  }
</script>

<style scoped>
  /* 导入iconfont的css*/
  .card2 {
    margin-top: 30px;
  }


  .cards {
    box-shadow: 0px 0px 10px 3px #9eabad;
  }

  .detectMain {
    margin-top: 70px;
    padding-left: 30px;
    padding-right: 30px;
    overflow-y: hidden;
  }

  .el-header {
    height: 100px;
  }

  .detection {
    height: 100%;
    overflow-y: hidden;
  }

  .el-container {
    height: 100%;
  }

  .el-container font{
    font-size: 20px;
  }

  .el-pagination {
    position: relative;
    float: left;
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

}

.rowm{
  height: 400px;
  margin: auto;
}

.rowmb{
  height: 450px;
  width: 1580px;
  background: #fff;
  float: left;
  overflow: hidden;
  margin-top: 20px;
  box-shadow: 0px 0px 10px 3px #9eabad;
}

.card2 .el-pagination {
  margin-left: 35%;
}

.bg-purple{
  background:white;
}
</style>

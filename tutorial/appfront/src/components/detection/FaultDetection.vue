<template>
  <div class="detection">
    <!-- <el-container> -->

        <!-- 调用canvas -->
        <!-- <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas> -->

          <el-main class="detectMain">

                <el-row>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '0px' }" id="card1">
                     <img src="../../assets/close.png" class="image">
                     <div style="padding: 14px;">
                       <span>停机设备</span>
                       <div class="bottom clearfix">
                         <el-button type="text" class="button"></el-button>
                       </div>
                     </div>
                   </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '0px' }" id="card1">
                      <img src="../../assets/alarm.png" class="image">
                      <div style="padding: 14px;">
                        <span>告警设备</span>
                        <div class="bottom clearfix">
                          <el-button type="text" class="button"></el-button>
                        </div>
                      </div>
                    </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '0px' }" id="card1">
                      <img src="../../assets/offline.png" class="image">
                      <div style="padding: 14px;">
                        <span>离线设备</span>
                        <div class="bottom clearfix">
                          <el-button type="text" class="button"></el-button>
                        </div>
                      </div>
                    </el-card>
                  </el-col>
                </el-row>
                <el-row>设备检查异常</el-row>


            <!--通用list-->
            <!--请求如下 http://127.0.0.1:8000/pv/get/detection/2018/1/18/ -->
            <el-card class="card2">
              <ComList v-bind:data='data'></ComList>
              <!--<ComList v-bind:data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></ComList>-->
              <!-- <el-pagination
                background
                layout="prev, pager, next"
                :total="1000"
                @current-change="handleCurrentChange">
              </el-pagination> -->
            </el-card>
               <el-pagination
                background
                layout="prev, pager, next"
                :total="1000"
                @current-change="handleCurrentChange">
              </el-pagination>

          </el-main>

    <!-- </el-container> -->
  </div>
</template>

<script>
    import ComList from '../el-simple-com/com-list.vue'
    import deHeader from './Head.vue'
    // import myCanvas from 'vue-atom-canvas'

  export default {
    name: 'faultdetection',
    components: {
        ComList: ComList,
        DeHeader: deHeader,
        //  myCanvas
    },
    data(){
      return {
        data: 'http://localhost:8000/system/getDetectionInfo?pageNum=1&pageSize=10',
        page: 1
        // pageSize: 2
      }
    },
    methods: {
      handleCurrentChange(val) {
        this.data = 'http://localhost:8000/system/getDetectionInfo?pageNum='+ val +'&pageSize=10';
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
    height: 550px;
  }

  .cards {
    box-shadow: 0px 0px 10px 3px #9eabad;
  }

  .detectMain {
    height: 100%;
    overflow-y: hidden;
    padding-left: 30px;
    padding-right: 30px;
    overflow-y: hidden;
    margin-top:-12px;
    /* background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D); */
  }

  /* .el-header {
    height: 100px;
  } */

  .el-container {
    height: 100%;
    /* margin-top:-23px; */
  }

  .el-container font{
    font-size: 20px;
  }

  .el-pagination {
    position: relative;
    bottom: 0;
    left: 0%;
  }

  /* .detection-title {
    text-align: left;
    font-size: 11px;
    margin-bottom: 10px;
  } */

  .grid-content {
    border-radius: 4px;
    min-height: 200px;
  }


  .el-row {
    margin-bottom: 20px;

  }

  .el-col {
    border-radius: 4px;
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

  /* .bottom {
    margin-top: 13px;
    line-height: 12px;
  } */


/* .rowm{
  height: 400px;
  margin: auto;
} */

/* .rowmb{
  height: 450px;
  width: 1580px;
  background: #fff;
  float: left;
  overflow: hidden;
  margin-top: 20px;
  box-shadow: 0px 0px 10px 3px #9eabad;
} */

/* .card2 .el-pagination {
  margin-left: 35%;

} */

/* #card0{

       background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
} */

#card1{
    /* background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, #373B44,#355C7D); */
    background-color:rgba(255, 255, 255, 0.2);
    margin-top:50px;
}

.card2{
    background-color:rgba(255, 255, 255, 0.2)
}

.detection{
    background: -webkit-linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    background: -o-linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    background: -moz-linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.1),#355C7D);
    height:100%;
    margin-left:-12px;
}


</style>

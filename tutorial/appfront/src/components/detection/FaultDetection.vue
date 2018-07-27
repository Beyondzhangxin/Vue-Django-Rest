<template>
  <div class="detection">
    <el-container>
      <el-container>
<<<<<<< HEAD
=======
        <deHeader/>
>>>>>>> 0aa05e8f74b925addf37d8d588f1f707783daf71
          <el-main>
           <el-row>
        <el-col :span="24"><div class="grid-content bg-purple-dark"><deHeader/></div></el-col>
        </el-row>
            <!--通用list-->
            <ComList data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></ComList>
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



</style>

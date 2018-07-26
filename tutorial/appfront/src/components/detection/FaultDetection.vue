<template>
  <div class="detection">
    <el-container>
      <el-aside width="200px"><DeAside/></el-aside>
      <el-container>
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
  import deAside from './Aside.vue'

  export default {
    name: 'faultdetection',
    components: {
      ComList: ComList,
      DeAside: deAside,
      DeHeader: deHeader,
    },
    data(){
      return {

        // pageSize: 2
      }
    },
  }
</script>

<style>
  /* 导入iconfont的css*/

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

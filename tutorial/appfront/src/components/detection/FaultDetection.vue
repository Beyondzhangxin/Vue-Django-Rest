<template>
  <div class="detection">
    <el-container>
      <el-aside width="200px"><DeAside/></el-aside>
      <el-container>
        <el-header>                                                                              
          <deHeader/>
        </el-header>
          <el-main>
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
</style>

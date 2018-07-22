<template>
  <div class="detection">
    <el-container>
      <el-aside width="200px"><aside/></el-aside>
      <el-container>
        <el-header>
          <header/>
        </el-header>
          <el-main>
            <!--通用list-->
            <ComList data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></comList>
          </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  import ComList from '../el-simple-com/com-list.vue'
  import header from './Head.vue'
  import aside from './Aside.vue'

  export default {
    name: 'faultdetection',
    components: {
      ComList: ComList
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

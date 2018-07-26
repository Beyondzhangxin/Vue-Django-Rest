<template>
  <div class="aside">
    <div class="aside0">
      列表名称
    </div>
    <div class="aside1">
      <el-row>
        <el-col :span="6"><el-button size="mini">名称</el-button></el-col>
        <el-col :span="6"><el-button size="mini">容量</el-button></el-col>
        <el-col :span="6"><el-button size="mini">地区</el-button></el-col>
        <el-col :span="6"><el-button size="mini">状态</el-button></el-col>
      </el-row>
    </div>
    <div class="aside2">123</div>
    <div class="aside3">123</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  mounted: function() {

  },
  methods: {

  }
}
</script>
<style scoped>
  .aside {
    width: 100%;
    height: 100%;
  }
  .aside .aside1 {
    width: 100%;
    height: 40px;
  }

  .aside1 ul {

  }



  .aside .aside2 {
    width: 100%;
    height: 40px;
  }
  .aside .aside3 {
    width: 100%;
    height: 700px;
  }
</style>

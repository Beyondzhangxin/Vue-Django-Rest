<template>
  <div class="top">
    <div class="aside">
      <el-row>
        <el-col :span="6"><el-button size="mini">名称</el-button></el-col>
        <el-col :span="6"><el-button size="mini">容量</el-button></el-col>
        <el-col :span="6"><el-button size="mini">地区</el-button></el-col>
        <el-col :span="6"><el-button size="mini">状态</el-button></el-col>
      </el-row>
    </div>
    <input id="input" v-model="message" placeholder="请输入电站名称">
    <div class="station">
      <i class="el-icon-loading"></i>
      <span v-html="msg2"></span>
    </div>
    <div class="station">
      <i class="el-icon-loading"></i>
      <span v-html="msg3"></span>
    </div>
  </div>
</template>


<script>
export default {
  name: 'deAside',
  data: function (){
    return {
        message:'',
        msg2:'北京光伏电站',
        msg3:'上海光伏电站'
    }
  },
}

</script>


<style>
.top {
  padding:10px;
}

.station{
  margin-top:10px;
  margin-left:-40px;
}

#input{
  border-radius: 4px;
}

</style>

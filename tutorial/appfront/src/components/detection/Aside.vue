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
      <span v-html="msg1"></span>
    </div>
    <div class="station">
      <i class="el-icon-loading"></i>
      <span v-html="msg2"></span>
    </div>
  </div>
</template>


<script>
export default {
  name: 'deAside',
  data: function (){
    return {
        message:'',
        msg1:'北京光伏电站',
        msg2:'上海光伏电站'
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

.aside{
  margin-bottom:10px;
  width:100%;
}

.el-button{
padding-left:8px;
height: 35px;
}

</style>

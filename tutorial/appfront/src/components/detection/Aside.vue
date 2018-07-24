<template>
  <div class="top">
    <p v-html="msg1"></p>
    <p {{message}} </p>
    <input v-model="message" placeholder="请输入电站名称">
    <P v-html="msg2"></p>
    <P v-html="msg3"></p>
  </div>
</template>


<script>
export default {
  name: 'deAside',
  data: function (){
    return {
        msg1:'<span>名称&nbsp&nbsp</span><span>容量&nbsp&nbsp</span><span>地区&nbsp&nbsp</span>状态&nbsp&nbsp<span></span>',
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
</style>

<template>
<div class=text>
    <p v-html="msg1"></p>
    <div class="obeject">
      <span class="obeject1">停机设备</span>
      <span class="obeject2">告警设备</span>
      <span class="obeject3">离线设备</span>
    </div>
</div>
</template>


<script>
export default {
  name: 'text',
  data: function (){
    return {
        msg1:'异常检测共3项',
    }
  },
}
</script>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
<style>
.text{
float:left;margin-top:-10px;
}

.obeject{
  margin-top:-10px;padding-left:20px;font-size:15px;
}

</style>

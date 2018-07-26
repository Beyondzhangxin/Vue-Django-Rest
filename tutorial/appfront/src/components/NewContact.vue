<template>
  <el-row>
    <el-button  @click="getNum()" type="success">{{ msg }}</el-button>
    <div class="circle">
      <i class="iconfont icon-lixian"/>
    </div>
    <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row>
  </el-row>

</template>
<script>
export default {
  name: 'NewContact',

  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted: function() {
    this.changeMsg()
  },
  methods: {
    changeMsg(){
      console.log(123);
    },
    getNum(){
      this.msg = 'wang'
    }
  }
}
</script>
<style>
  @import './iconfont/iconfont.css';
  .grid-content {
   border-radius: 4px;
   min-height: 36px;
 }

 .circle {
   width: 100px;
   height: 100px;
   background-color:red;
   border-radius: 50%;
   -moz-border-radius: 50%;
   -webkit-border-radius: 50%;
   display: flex;
   justify-content: center;
   align-items: center;
 }
 .el-row {
    margin-bottom: 20px;
      margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
</style>

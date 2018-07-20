<template>
  <div class="detection">
    <div class="head-left">
  		<span class="logo">光伏智能运维系统</span>
  	</div>

  	<div class="head-right">
  	   <span class="nav">
  		  <ul>
  			   <li><a href="#">系统设置</a></li>
  			   <li><a href="#">故障告警</a></li>
  			   <li><a href="#">数据分析</a></li>
  			   <li><a href="#">运行监测</a></li>
  			   <li><a href="#">首    页</a></li>
  		  </ul>
  	   </span>
  	   <div class="clearfloat"></div>
    </div>

  <div class="left">
  	<div class="row">
  		<div class="row"><span class="name">名称</span></div>
  		<div class="row"><span class="capacity">容量</span></div>
  		<div class="row"><span class="area">地区</span></div>
  		<div class="row"><span class="station">状态</span></div>
  	</div>
  	<div class="shuru">
  		<form>
  		<input type="text" name="text" size=35><br>
  		</form>
  	</div>
  	<div class="mulu1">北京光伏电站</div>
  	<div class="mulu2">上海光伏电站</div>
  </div>
    <div class="right">
      <el-container>
        <el-header style="height: 130px;">
          <div>
            <div class="detection-title">异常检测</div>
          </div>
          <div style="float: left;margin-right: 120px;font-size:17px;text-align:center;" v-for="{title, className} in items">
            <div class="circle">
              <i :class="className"/>
            </div>
            <div>{{ title }}</div>
          </div>
        </el-header>
        <el-row>
          <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
        </el-row>
        <el-main>
          <!--通用list-->
          <ComList data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></comList>
        </el-main>
      </el-container>
    </div>
  </div>
</template>

<script>
  import ComList from './el-simple-com/com-list.vue'

  export default {
    name: 'faultdetection',
    components: {
      ComList: ComList
    },
    data(){
      return {
        items: [
          {title: '停机设备', className:'iconfont icon-lixian'},
          {title: '告警设备', className:''},
          {title: '离线设备', className:''},
        ]
        // pageSize: 2
      }
    },
  }
</script>

<style>
    /* 导入iconfont的css*/
    @import './iconfont/iconfont.css';

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

    .circle {
      width: 51px;
      height: 51px;
      background-color: rgba(69, 217, 112, 1);
      border-radius: 50%;
      -moz-border-radius: 50%;
      -webkit-border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .grid-content {
      border-radius: 4px;
      min-height: 4px;
    }

    .el-row {
      margin-bottom: 20px;
      &:last-child {
        margin-bottom: 0;
      }
    }

    .el-col {
      border-radius: 4px;
    }

    .bg-purple-dark {
      background: #99a9bf;
    }

    .detection{
        margin:0; padding:0; font-size:30px; font-weight:bold
    }

    .head-left{
        width:20%;height:100px;background:#9CF;float:left
    }

    .head-right{
        width:80%;height:100px;background:#9CF;float:right
    }

    .left{
        width:20%; height:1000px; background:whitesmoke; float:left
    }

    .right{
        width:80%; height:1000px;background:whitesmoke; float:right
    }

    .logo{
        width:auto;line-height:100px;margin-left:10px;
    }

    .nav{
        width:80%;
    }

    .nav ul{
        list-style:none;
    }

    .nav li{
        float:right;padding:10px;
    }

    .clearfloat{
        clear:both
    }

    .nav ul li a{
        text-decoration:none;color:black;
    }

    .nav ul li a:hover{
        color:white;background:black;
    }

    .row {
        float:left;
        padding:5px;
    }

    .mulu1{
        margin-left:10px;
    }

    .mulu2{
        margin-left:10px;
    }

    .shuru{
        margin-left:10px;
    }
</style>

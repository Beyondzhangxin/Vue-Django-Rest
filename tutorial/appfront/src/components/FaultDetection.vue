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
  	  <img src="./images/u1141.png" alt="image1" width="100%">
      <comList></comList>
    </div>
  </div>
</template>

<script>
  import ComList from './el-simple-com/com-list.vue'

  export default {
    name: 'faultdetection',
    components: {
      comList: ComList
    },
  }
</script>

<style>
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

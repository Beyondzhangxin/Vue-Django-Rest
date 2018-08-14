<template>
	<div class="effect">

    <!-- 登陆框 -->
      <div class="login">
        <div class="mes">系统登录</div>
          <el-form inline-message :model="loginForm" :rules="loginRules" ref="loginForm">
           
    	      <el-input class="user" prefix-icon="el-icon-edit" v-model="account" @blur="inputBlur('user',account)" type="text" placeholder="请输入账号" ></el-input>
              <p></p> 
            <el-input class="password" prefix-icon="el-icon-circle-check" v-model="password" @blur="inputBlur('password',password)" type="password" placeholder="请输入密码" ></el-input>
            <div class="submit">
              <el-button  @click="loginForm" id="button1" >登录</el-button>
              <el-button @click="resetForm" id="button2">重置</el-button>
            </div>
          </el-form>
        </div>

    <!-- 调用canvas -->
        <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas>
 
	</div>
</template>


<script>
import myCanvas from 'vue-atom-canvas'
import Axios from 'axios'
export default {
  name: 'effect',
  components: {
    myCanvas
  },

  data () {
    return {
      dotsNum: 60,   
    }
  },

  methods: {
       loginForm:function(account) {
          this.$router.push("/home/first");
  }
}
}
</script>


<style scoped>
.login{
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -140px;
        margin-left: -175px;
        width: 350px;
        min-height: 300px;
        padding: 30px 20px 25px;
        border-radius: 8px;
        box-sizing: border-box;
        /* background:#808080; */
        background-color:rgba(247, 248, 248, 0.1)
}

.effect{
    width: 100%;
    height: 100%;
    background: -webkit-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: -o-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: -moz-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
}

/* .el-input{
  width:100%;
  height:36px;
  border-radius:6px;
   background-color:rgba(255, 255, 255, 0.5)
} */

.mes{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 24px;
  margin-bottom:20px;
}

#button1{
  margin-top:30px;
  float:left;
  margin-left:30px;
}

#button2{
  margin-top:30px;
  float:right;
  margin-right:30px;
}
</style>

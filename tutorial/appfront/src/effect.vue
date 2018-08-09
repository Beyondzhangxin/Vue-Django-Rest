<template>
	<div class="effect">

    <!-- 登陆框 -->
      <div class="login">
        <div class="mes">系统登录</div>
          <el-form>
    	      <input class="field" v-model="account"  type="text" placeholder="请输入账号" ></input>
            <p></p>
            <input class="field" v-model="password" type="password" placeholder="请输入密码"  @keyup.native.enter="check"></input>
            <div class="submit">
              <el-button  @click="loginForm" id="button1">登录</el-button>
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
        background-color:rgba(255, 255, 255, 0.1)
}

.effect{
    width: 100%;
    height: 100%;
    background: -webkit-linear-gradient(30deg, rgba(55,59,68,0.5),rgba(53,92,125,0.5));
    background: -o-linear-gradient(30deg, rgba(55,59,68,0.5), rgba(53,92,125,0.5));
    background: -moz-linear-gradient(30deg, rgba(55,59,68,0.5), rgba(53,92,125,0.5));
    background: linear-gradient(30deg, rgba(55,59,68,0.5),rgba(53,92,125,0.5));
}

.field{
  width:100%;
  height:36px;
  /* border:1px solid; */
  border-radius:6px;
   background-color:rgba(255, 255, 255, 0.5)
}

.mes{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 24px;
  margin-bottom:10px;
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

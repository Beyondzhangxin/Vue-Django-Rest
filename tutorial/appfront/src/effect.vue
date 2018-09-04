<template>
	<div class="effect">

    <!-- 登陆框 -->
      <div class="login">
        <div class="mes">系统登录</div>
        
          <el-form :model="ruleForm" :rules="rules" ref="ruleForm"  status-icon class="demo-ruleForm loginFrom" id="myform">
          <el-form-item prop="userName">
            <el-input placeholder="账号" prefix-icon="el-icon-edit" v-model="ruleForm.userName" id="input"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input  type="password"  prefix-icon="el-icon-circle-check-outline" v-model="ruleForm.password" placeholder="密码" id="input"></el-input>
          </el-form-item>
          <div style="padding: 1rem 0 2rem 0;" class="clear">
          <span class="lf" @click="open" style="color:#0489cc;float:left;margin-left:20px;">帮助</span>
          <div class="rt">
            <el-checkbox v-model="checked" style="margin-left:20px;">自动登录</el-checkbox>
            <span @click="clearCookie" style="cursor: pointer;color: #f19149;font-size: 0.75rem;margin-left: 5px;">取消自动登录？</span>
          </div>
          </div>
          <el-button type="primary" @click="submitForm('ruleForm')" style="width: 100%;">登录</el-button>
          </el-form>

        </div>

    <!-- 调用canvas -->
        <!-- <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas> -->
        <div class="info">Powered by 清华四川能源互联网研究院</div>
	</div>
</template>


<script>
import myCanvas from './canvas'
import Axios from 'axios'
export default {
  name: 'effect',
  components: {
    myCanvas
  },

  data () {
    return {
      dotsNum: 60, 

      // 表单验证
      rules:{
        userName:[{
          required:true,message:'用户名不能为空',trigger:'blur'
        }],
        password:[{
          required:true,message:'密码不能为空',trigger:'blur'
        }]
      },


      ruleForm: {
       userName: '', 
       password: ''  
     }, 
    }

  },

  methods: {
    
   //点击帮助显示提示内容
       open() {
        this.$alert('账号admin,密码password', '光伏智能运维系统', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
        });
      },
      
      //点击登录调用方法
    submitForm(formName) {     
      
          this.$refs.ruleForm.validate((valid)  => {
          if(valid){
            if(this.ruleForm.userName==='admin'&&this.ruleForm.password==='password')
              this.$notify({
                type:'success',
                message:'欢迎你 '+this.ruleForm.userName+'!',
                duration:3000,            
              })
              this.$router.push('/home/first')
          } else{
              this.$message({
                type:'error',
                message:'用户名或密码错误',
                showClose:true
              })
          }
        });
    

        var name=this.ruleForm.userName;   
        var pass=this.ruleForm.password;
         //判断复选框是否被勾选 勾选则调用配置cookie方法
        if(this.checked=true){
            //传入账号名，密码，和保存天数3个参数
          this.setCookie(name,pass,1);
        }
    },

  //设置cookie
  setCookie(c_name,c_pwd,exdays) {
    var exdate=new Date();//获取时间
    exdate.setTime(exdate.getTime() + 5*60*1000*exdays);//保存的时间
    //字符串拼接cookie
    window.document.cookie="userName"+ "=" +c_name+";path=/;expires="+exdate.toGMTString();
    window.document.cookie="userPwd"+"="+c_pwd+";path=/;expires="+exdate.toGMTString();
  },
  //读取cookie
  getCookie:function () {
    if (document.cookie.length>0) {
      var arr=document.cookie.split('; ');//这里显示的格式需要切割一下自己可输出看下
      for(var i=0;i<arr.length;i++){
        var arr2=arr[i].split('=');//再次切割
        //判断查找相对应的值
        if(arr2[0]=='userName'){
          this.ruleForm.userName=arr2[1];//保存到保存数据的地方
        }else if(arr2[0]=='userPwd'){
          this.ruleForm.password=arr2[1];
        }
      }
    }
  },

  //清除cookie
  clearCookie:function () {
      $(':input', '#myform')
      .not(':button, :submit, :reset, :hidden,:radio') // 去除不需要重置的input类型
      .val('')
      .removeAttr('checked')
      .removeAttr('selected');
    this.setCookie("","",-1);//修改2值都为空，天数为负1天就好了
    alert("账号密码信息已清除");
     window.location.reload();
  }
},

//页面加载调用获取cookie值
mounted(){
        this.getCookie()
        }
  }

</script>


<style scoped>
.login{
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -180px;
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
    /* background: -webkit-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: -o-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: -moz-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5)); */
}

.mes{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 24px;
  margin-bottom:20px;
  margin-top:-20px;
  font-weight: bold;
}

.info{
  position:absolute;
  left:50%;
  bottom:0;
  margin-left:-120px;
  margin-bottom:10px;
  font-size:13px;
}

</style>

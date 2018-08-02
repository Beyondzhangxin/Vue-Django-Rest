<template>
    
    <div class="index" :style="{backgroundImage:'url('+img+')'}">
        <div id="title">智能光伏云运维
            <!-- <img src="../../assets/logo.png" id="image">         -->
        </div>
		<div class="login">
      	<!-- <h2>登录</h2> -->
        <el-form>
            <el-form-item label="用户">
                <el-input type="te、xt" id="user" v-model="formName.user" @blur="inputBlur('user',formName.user)"></el-input>
                <p>{{formName.userError}}</p>
            </el-form-item>
            <el-form-item label="密码">
                <el-input type="password" id="password" v-model="formName.password" @blur="inputBlur('password',formName.password)"></el-input>
                <p>{{formName.passwordError}}</p>
            </el-form-item>
            <el-button type="primary" @click="submitForm('formName')" v-bind:disabled="formName.beDisabled" id="button1">登录</el-button>
            <el-button @click="resetForm" id="button2">重置</el-button>
        </el-form>   
		</div>     
	</div>

</template>


<script>
import Axios from 'axios'
import Img from '@/./assets/back7.jpg'

    export default {
        name: '',
        data () {
            return {
                // login:{
                //     backgroundImage:"url("+require("../asset/back1.jpg")+")",
                //     backgroundRepeat: "no-repeat",
                //     backgroundSize: "100px auto",
                //     marginTop: "5px",
                // },
                    img:Img,

                formName: {//表单中的参数
                    user: '',
                    userError: '',
                    password: '',
                    passwordError: '',
                    beDisabled: true
                },
                beShow: false//传值给父组件
            }           
        },
        /*props:[
                'fromParent'
        ],*/
        methods: {
            resetForm:function(){
                this.formName.user = '';
                this.formName.userError = '';
                this.formName.password = '';
                this.formName.passwordError = '';
            },
            submitForm:function(formName){
                //与父组件通信传值
                //this.$emit('showState', [this.beShow,this.formName.user])
                //提交user password
                var user = this.formName.user,
                    password = this.formName.password;
                    console.log(user,password)
                	Axios.get('../../src/php/login.php?user='+user+'&password='+password)
                     .then(function(res){
                        console.log(res)

                     })
                     .catch(function(){

                     })
            },
            inputBlur:function(errorItem,inputContent){
                if (errorItem === 'user') {
                    if (inputContent === '') {
                        this.formName.userError = '用户名不能为空'
                    }else{
                        this.formName.userError = '';
                    }
                }else if(errorItem === 'password') {
                    if (inputContent === '') {
                        this.formName.passwordError = '密码不能为空'
                    }else{
                        this.formName.passwordError = '';
                    }
                }
                //对于按钮的状态进行修改
                if (this.formName.user != '' && this.formName.password != '') {
                    this.formName.beDisabled = false;
                }else{
                    this.formName.beDisabled = true;
                }
            }
        }
    }
</script>



<style scoped>
/* html,body{
        margin: 0;
        padding: 0;
        position: relative;
	} */

.index{
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,.8);
    }

.login{
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -150px;
        margin-left: -175px;
        width: 350px;
        min-height: 300px;
        padding: 30px 20px 20px;
        border-radius: 8px;
        box-sizing: border-box;
        background-color: #fff;
    }
    
.login p{
        color: red;
        text-align: left;
}

#title{
    color:black;
    font-size: 25px;
    padding-top:200px;
}

#button1{
    margin-left:40px;
    float:left;
}

#button2{
    margin-right: 40px;
    float:right;
}   

</style>

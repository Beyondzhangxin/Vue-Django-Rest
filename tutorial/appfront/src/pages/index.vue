<template>

    <div class="index" :style="{backgroundImage:'url('+img+')'}">
        <div id="title">智能光伏云运维
            <!-- <img src="../../assets/logo.png" id="image">  -->
        </div>
		<div class="login">
      	<!-- <h2>登录</h2> -->
        <el-form>
            <el-form-item label="用户">
                <el-input type="text" id="user" v-model="formName.user" @blur="inputBlur('user',formName.user)"></el-input>
                <p>{{formName.userError}}</p>
            </el-form-item>
            <el-form-item label="密码">
                <el-input type="password" id="password" v-model="formName.password" @blur="inputBlur('password',formName.password)"></el-input>
                <p>{{formName.passwordError}}</p>
            </el-form-item>
            <el-button type="primary" @click="submitForm('formName')" v-bind:disabled="formName.user==''||formName.password==''" id="button1">登录</el-button>
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
                this.$router.push("/home/first");
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
        background-color:rgba(255, 255, 255, 0.3)
    
    }

.login p{
        color: red;
        text-align: left;
}

#title{
    font-size: 25px;
    padding-top:230px;

}

#button1{
    margin-left:40px;
    float:left;
}

#button2{
    margin-right: 40px;
    float:right;
}

#title{
color: #fafafa;
letter-spacing: 0;
text-shadow: 0px 1px 0px #999, 0px 2px 0px #888, 0px 3px 0px #777, 0px 4px 0px #666, 0px 5px 0px #555, 0px 6px 0px #444, 0px 7px 0px #333, 0px 8px 7px #001135 }

</style>

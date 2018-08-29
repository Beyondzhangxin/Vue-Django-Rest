<template>
    <div class="Gmm">
        <!-- 配置参数 -->
            <div class="text0">GMM参数配置</div>
        <!-- 分割线 -->
        <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="ruleForm">
            <el-card class="card0">    
                <el-form-item label="训练目标" style=font-weight:bold prop="system">
                    <el-select v-model="ruleForm.system" clearable placeholder="选择训练系统">
                        <el-option
                            v-for="item in options1"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>            
                </el-form-item>
                    
                    <!--<el-col :span="3">
                        <div class="text">训练目标</div>
                    </el-col>
                    <el-col :span="5">
                        <el-select v-model="value1" clearable placeholder="选择训练系统">
                            <el-option
                                v-for="item in options1"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                        </el-select>
                    </el-col>-->

                    
                    <el-form-item label="概率模型" style=font-weight:bold prop="options">
                        <el-select v-model="ruleForm.options" clearable placeholder="选择概率模型">
                                <el-option
                                    v-for="item in options2"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                </el-option>
                            </el-select>
                            
                        </el-form-item>
                        <!--<el-select v-model="value2"  
                        @change="chooseModel(value2)"
                        clearable 
                        placeholder="选择概率模型">
                            <el-option
                                v-for="item in options2"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                        </el-select>-->
                    
                        <el-form-item label="时间选择" required>
                            <el-col :span="11">
                                <el-form-item prop="start_time">
                                    <el-date-picker
                                        v-model="ruleForm.start_time"
                                        type="datetime"
                                        placeholder="选择日期时间"
                                        default-time="12:00:00">
                                    </el-date-picker>
                                </el-form-item>
                            </el-col>
                            <el-col :span="2">
                               至
                            </el-col>
                            <el-col :span="11">
                                <el-form-item prop="end_time">
                                    <el-date-picker
                                        v-model="ruleForm.end_time"
                                        type="datetime"
                                        placeholder="选择日期时间"
                                        default-time="12:00:00">
                                    </el-date-picker>
                                </el-form-item>
                            </el-col>
                        </el-form-item>
                    

                <!--
                <el-col :span="5">
                    <el-time-select
                            placeholder="起始时间"
                            v-model="startTime"
                            :picker-options="{
                            start: '08:30',
                            step: '00:15',
                            end: '18:30'
                            }">
                    </el-time-select>
                </el-col>

                <el-col :span="5">
                    <el-time-select
                            placeholder="结束时间"
                            v-model="endTime"
                            :picker-options="{
                            start: '08:30',
                            step: '00:15',
                            end: '18:30',
                            minTime: startTime
                            }">
                    </el-time-select>
                </el-col> -->
                </el-row>
            </el-card>

            <el-card class="card2">
                <el-row :gutter="20">
                    <el-form-item label="训练参数" style=font-weight:bold prop="j">
                            <el-col :span="4" style="margin-left:80px;">
                                <el-input
                                    placeholder="输入高斯个数"
                                    v-model.number="ruleForm.j"
                                    auto-complete="off"
                                    clearable>
                                </el-input>
                            </el-col>
                    </el-form-item>
                    <!--<el-col :span="3">
                        <div class="text">训练参数</div>
                    </el-col>

                    <el-col :span="3">
                        <el-input
                            placeholder="输入高斯个数"
                            v-model="input0"
                            clearable>
                        </el-input>
                    </el-col>-->

                    <el-form-item label="建模算法" style=font-weight:bold prop="method">
                            <el-col :span="6">
                                <el-select v-model="ruleForm.method"
                                clearable
                                @change="sendNoticeMessage(ruleForm.method)"
                                placeholder="选择算法">
                                    <el-option
                                        v-for="item in options3"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value">
                                    </el-option>
                                </el-select>
                            </el-col>
                    </el-form-item>
                    
                    <!--<el-col :span="5">
                    <el-select v-model="value3"
                    clearable
                    @change="sendNoticeMessage(value3)"
                    placeholder="选择算法">
                            <el-option
                                v-for="item in options3"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                    </el-select>   
                    </el-col>-->
                    
                    <el-form-item label="变量选择" prop="varables">
                        <el-col :span="6">
                            <el-select v-model="ruleForm.varables" multiple clearable placeholder="选择变量">
                                <el-option
                                    v-for="item in options4"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                </el-option>
                            </el-select>
                        </el-col>
                    </el-form-item>
                </el-row>
            </el-card>

            <el-card class="card3">
                <div class="top" v-show="value2=='conditional'">
                    <div class="text1">选择输入</div>
                    <div class="table">
                    <el-table
                        :data="tableData"
                        border
                        style="width:500px">
                        <el-table-column
                        prop="var"
                        label="变量"
                        width="250px">
                        </el-table-column>
                        <el-table-column
                        prop="value"
                        label="条件分布给定值"
                        width="250px">
                        </el-table-column>
                    </el-table>
                    </div>
                </div>
                <div class="clear"></div>
            <!--
            <div class="mid">
                <div class="text2">Y_hyper计算超参数训练集</div>
                <div class="model">
                    <span>筛选条件：</span>
                    <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全部</el-checkbox>
                        <div style="margin: 15px 0;"></div>
                        <el-checkbox-group v-model="checkedCities" @change="handleCheckedCitiesChange">
                            <el-checkbox v-for="city in cities" :label="city" :key="city">{{city}}</el-checkbox>
                        </el-checkbox-group>
                </div>      
            </div>
            <div class="clear"></div>

        
                <div class="fenye">
                    <span class="text">共7页，73条记录</span>
                    <el-pagination
                        small
                        background
                        layout="prev, pager, next"
                        :total="70">
                    </el-pagination>
                </div>
            
                <div>
                <el-input
                    placeholder="输入period"
                    v-model="input1"
                    clearable>
                </el-input>
                </div>
                -->
                <el-form-item>
                    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                    <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
            </el-card>
        </el-form>

    </div>
</template>


<script>


const cityOptions = ['类别1', '类别2', '类别3', ];
export default {
    name:'Gmm',
    componets:{
        
    },
    data(){
        //处理错误
        var checkVarables = (rule, value, callback) => {
            if (value.length == 0) {
                    callback(new Error('请输入变量'));
                    console.log(123414)
            }
            if (value === '') {
                callback(new Error('请输入变量'));
            } else {
                if (this.ruleForm.varables !== '') {
                    if(this.ruleForm.options == 'marginal') {
                        if(value.length > 1){
                            callback(new Error('在marginal模型下只能有一个变量'));
                        }
                    }
                }
                callback();
            }
        };
        return{
            ruleForm: {
                system: "",
                options: "",
                start_time: "",
                end_time: "",
                j: "",
                method: "",
                varables: [],
                y: null,
                period: null,
                y_hyper: null
            },
            rules: {
                system: [
                    // { required: true, message: '请输入活动名称', trigger: 'blur' },
                    // { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
                     { required: true, message: '请选择活动区域', trigger: 'change' }
                ],
                options: [
                    { required: true, message: '请选择建立的概率模型', trigger: 'change' }
                ],
                start_time: [
                    { type: 'date', required: true, message: '请选择初始时间', trigger: 'change' }
                ],
                end_time: [
                    { type: 'date', required: true, message: '请选择结束时间', trigger: 'change' }
                ],
                j: [
                    { required: true, message: '高斯个数不能为空', trigger: 'blur'},
                    { type: 'number', message: '高斯个数必须为数字值', trigger: 'blur'}
                ],
                method: [
                    { required: true, message: '请选择算法', trigger: 'change' }
                ],
                varables: [
                    { type: 'array', required: true, validator: checkVarables, trigger: 'change' }
                ],
            },

        mult: new Boolean(1),
        
        //建模功能需要的功能
        timeRange:[],
        input0:"",
        input1:"",
        options1:[{
            value:'图书馆微电网系统',
            label:'图书馆微电网系统',
        },
        {
            value:'多功能光伏电站系统',
            label:'多功能光伏电站系统',
        }
        ],
        value1:'',

        options2:[{
            value:'marginal',
            label:'marginal',
        },
        {
            value:'joint',
            label:'joint',
        },
        {
            value:'conditional',
            label:'conditional',
        }
        ],
        value2:'',

        options3:[{
          value:'EM',
          label:'EM',
        },
        {
          value:'MAP',
          label:'MAP',
        }],
        value3:'',

        options4:[{
            value:'NBQGL10',
            label:'NBQGL10',
        },
        {
            value:'FDZGL',
            label:'FDZGL',
        },
        {
            value:'FZ',
            label:'FZ',
        }
        ],
        value4:'',
        value5:'',
        startTime: '',
        endTime: '',
    
        tableData: [{
          var: 'NBQG10',
          value: '1',
        }, {
          var: 'FDZGL',
          value: '',
        }, {
          var: 'FZ',
          value: '',
        }],

      }
    },

    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.saveModel();
                } else {
                    console.log('没有传输成功!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },
        chooseModel(val) {
            console.log(this.value4)
            if(val == 'marginal') {
                this.mult = new Boolean(0);
            }
            if(val != 'marginal') {
                this.mult = new Boolean(1);
            }
        },
      sendNoticeMessage(val) {
        if(val == 'MAP') {
          const h = this.$createElement;
          this.$notify({
            title: '使用MAP函数的提示',
            message: h('i', { style: 'color: teal'}, '前提：对要刻画的随机变量有了深入的认识 方案：输入超参训练集，自动归纳超参数')
          });
        }
      },

      saveModel() {
        this.$prompt('请输入保存模型名称（四字以上）', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          //支持汉字和英文
          inputPattern: /^[\u4E00-\u9FA5A-Za-z0-9]{4,}$/,
          inputErrorMessage: '模型名称不正确'
        }).then(({ value }) => {
            this.$message({
            type: 'success',
            message: '模型名称是: ' + value
          });
          //发送POST请求
          // this.$router.push('/calculation')
          this.postDSTConfig('http://127.0.0.1:8000/GMM/model/distribution/')
          
        }
        ).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });
        });
      },

      postDSTConfig(url) {
        var instance = this.$ajax.create({
          headers: {'Content-Type': 'application/json'}
        });
        var v1 = "";
        for(var i=0; i < this.ruleForm.varables.length; i++) {
            v1 += this.ruleForm.varables[i] + " "
        }
        this.ruleForm.varables = v1;
        instance.post(url, this.ruleForm)
          .then(function (response) {
            //处理数据
            console.log(response)
          }.bind(this))
          .catch(function (error) {
            return 0;
          });
      },
      handleCheckAllChange(val) {
       this.checkedCities = val ? cityOptions : [];
       this.isIndeterminate = false;
      },
      handleCheckedCitiesChange(value) {
        let checkedCount = value.length;
        this.checkAll = checkedCount === this.cities.length;
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.cities.length;
      },
      
        }
    }
    
    

</script>


<style scoped>
.Gmm{
    background: -webkit-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: -o-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: -moz-linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    background: linear-gradient(30deg, rgb(0,65,106,0.7),rgba(53,92,125,0.5));
    height:100%;
}

.text0{
    font-weight: bold;
    padding-top:10px;
}

.text1{
    float:left;
    margin-top:50px;
    margin-right:20px;
}

.clear{
    clear:both;
}

.el-table{
    overflow-x: hidden;
}

.mid{
    float: left;
    margin-left:60px;
}

.fenye{
    float:left;
    margin-left:50px;
    margin-top:50px;
}
.card0{
    margin-top:10px;
    margin-bottom:10px;
    background-color:rgba(255, 255, 255, 0.2);
}

.card0:hover{
    background-color:rgba(53,92,125, 0.1);
}

.card3{
    margin-top:10px;
    margin-bottom:10px;
    background-color:rgba(255, 255, 255, 0.2);
}

.card2{
    background-color:rgba(255, 255, 255, 0.2);
}

.card2:hover{
    background-color:rgba(53,92,125, 0.1);
}

.card3:hover{
    background-color:rgba(53,92,125, 0.1);
}
</style>



<template>
    <div class="Gmm">
        <!-- 配置参数 -->
            <div class="text0">GMM参数配置</div>
        <!-- 分割线 -->
        <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="ruleForm">
            <el-card class="card0">    
                <el-form-item label="训练目标" prop="system">
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

                    
                    <el-form-item label="概率模型" prop="options">
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
                            <el-col :span="24">
                                <el-date-picker
                                    v-model="ruleForm.timeRange"
                                    type="datetimerange"
                                    range-separator="至"
                                    start-placeholder="开始日期"
                                    end-placeholder="结束日期">
                                </el-date-picker>
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
                    <el-form-item label="训练参数" prop="j">
                            <el-col :span="6">
                                <el-input
                                    placeholder="输入高斯个数"
                                    v-model.number="ruleForm.j"
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

                    <el-form-item label="建模算法" prop="method">
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
                    
                    <el-form-item label="变量选择" prop="varables1" v-show="ruleForm.options!='marginal'">
                        <el-col :span="5">
                            <el-select v-model="ruleForm.varables1" multiple clearable placeholder="选择变量">
                                <el-option
                                    v-for="item in options4"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                </el-option>
                            </el-select>
                        </el-col>
                    </el-form-item>
                    <el-form-item label="变量选择" prop="varables2" v-show="ruleForm.options=='marginal'">
                        <el-col :span="5">
                            <el-select v-model="ruleForm.varables2" clearable placeholder="选择变量">
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
                <div>
                <el-button type="primary" icon="el-icon-search" @click="saveModel">保存</el-button>
                </div>
            </el-card>
        </el-form>
    <!--上传文件界面 -->
    <!-- <el-card class="card2">
    <el-upload style="margin: 10px 0 10px 30px;"
              ref="upload"
              accept=".xls,xlsx,.doc,.txt"
              :action="uploadURL"
              :on-error="uploadError"
              :on-success="uploadSuccess"
              :auto-upload="false"
              name="uploadedFile"
              :data="queryParams">
                <el-button type="primary" icon="el-icon-circle-plus-outline" slot="trigger">
                    导入文件
                </el-button>
            </el-upload>

            <div class="buttons" style="margin: 10px 0 0 25px;">
                <el-button type="success" @click="submitUpload">提交</el-button>
                <el-button type="danger" @click="reset">重置</el-button>
            </div>
    </el-card> -->

    <!-- 下载按钮 -->
    <!-- <div class="button">
        <el-button v-on:click="$refs.download.downLoad()" type="primary" >下载</el-button>
        <download :pageParams="params" :downloadUrl="api.downloadUrl" ref="download"></download>
    </div> -->

    <!-- 展示界面 -->
    <!-- <el-card class="card3">
        <div class="text">展示界面</div>




    </el-card> -->

    </div>
</template>


<script>
// import download from '../download/download';

const cityOptions = ['类别1', '类别2', '类别3', ];
export default {
    name:'Gmm',
    componets:{
        // download
    },
    data(){
        return{
            ruleForm: {
                system: "",
                options: "",
                start_time: "",
                end_time: "",
                j: null,
                method: "",
                varables1: "",
                varables2: "",
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
                j: [
                    { required: true, message: '高斯个数不能为空'},
                    { type: 'number', message: '高斯个数必须为数字值'}
                ],
                method: [
                    { required: true, message: '请选择算法', trigger: 'change' }
                ],
                varables1: [
                    { type: 'array', required: true, message: '请至少选择一个变量', trigger: 'change' }
                ],
                varables2: [
                    { required: true, message: '请选择一个变量', trigger: 'change' }
                ],
            },

        mult: new Boolean(1),
        
        //建模功能需要的功能
        timeRange:[],
        input0:"",
        input1:"",
            // input1:"",
            // input2:"",
            // input3:"",
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


        checkAll: false,
            checkedCities: ['上海', '北京'],
            cities: cityOptions,
            isIndeterminate: true,
        // options1:[{
        //     value:'label1',
        //     label:'EM算法',
        // },
        // {
        //     value:'label2',
        //     label:'MAP算法',
        // }
        // ],
        // value:'',

        //  options2:[{
        //     value:'label1',
        //     label:'边际分布',
        // },
        // {
        //     value:'label2',
        //     label:'联合分布',
        // },
        // {
        //     value:'label3',
        //     label:'条件分布',
        // }
        // ],
        // value:'',

        fullscreenLoading: false,
            checkList: [],
            uploadURL: "",
            queryParams: {},

        created:function(){},

        form: {
            name: '',
            region: '',
            date1: '',
            date2: '',
            delivery: false,
            type: [],
            resource: '',
            desc: ''
        },
         api: {
          downloadUrl: `${this.urlBase}/adunit/download`
        },
        params: {}
      }
    },

    methods: {
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
        }).catch(() => {
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
        if(value2 == 'conditional'){
          this.fromData
        }else{

        }

        instance.post(url, this.fromData)
          .then(function (response) {
            //处理数据
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
        //     onSubmit() {
        //     console.log('submit!');
        //   },

        // openFullScreen() {
        //     this.fullscreenLoading = true;
        //     setTimeout(() => {
        //     this.fullscreenLoading = false;
        //     }, 2000);
        // },

        // uploadError(err, file, fileList) {
                
        //         this.$message.error(err);
        //         this.reset();
        // },
        // uploadSuccess(response, file, fileList) {
                
        //         console.log(response);
        //         console.log(file);
        //         console.log(fileList);
        //         this.reset();
        // },
        // submitUpload() {
        //         this.$set(this.queryParams, "params", this.checkList.toString());
        //         this.$refs.upload.submit();
        // },
        // reset() {
               
        //         this.checkList = [];
                
        //         this.$refs.upload.clearFiles();
        // },

        //  download(url) {
        //     window.open(url);
        //     loacation.href=url;
        // }
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



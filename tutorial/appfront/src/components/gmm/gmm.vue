<template>

    <div class="Gmm">
        <!-- 配置参数 -->
            <div class="text0">GMM参数配置</div>
        <!-- 分割线 -->
        <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">

        <el-card class="card0">
            <el-row :gutter="20">
                <el-col :span="3">
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
                </el-col>

                 <el-col :span="5">
                     <el-select v-model="value2"  
                     @change="chooseModel(value2)"
                     clearable 
                     placeholder="选择概率模型">
                        <el-option
                            v-for="item in options2"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </el-col>
                <div class="block">
                <el-date-picker
                v-model="timeRange"
                type="datetimerange"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期">
                </el-date-picker>
                </div>

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
                <el-col :span="3">
                    <div class="text">训练参数</div>
                </el-col>

                <el-col :span="3">
                    <el-input
                        placeholder="输入高斯个数"
                        v-model="input0"
                        clearable>
                    </el-input>
                 </el-col>

                <el-col :span="5">
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
                </el-col>
                <div>
                  <el-col :span="5" v-show="value2!='marginal'">
                    <el-select v-model="value4" multiple clearable placeholder="选择变量">
                      <el-option
                        v-for="item in options4"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
                  </el-col>
                </div>
                <div>
                    <el-col :span="5" v-show="value2=='marginal'">
                      <el-select v-model="value5" clearable placeholder="选择变量">
                        <el-option
                        v-for="item in options4"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                      </el-select>
                    </el-col>
                </div>
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
        mult: new Boolean(1),
        fromData: '',
        //建模功能需要的功能
        timeRange:[],
        input0:"",
        input1:"",
            // input1:"",
            // input2:"",
            // input3:"",
        options1:[{
            value:'label1',
            label:'天井光伏发电系统',
        },
        {
            value:'label2',
            label:'图书馆微电网系统',
        },
        {
            value:'label3',
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
            value:'label1',
            label:'NBQGL10',
        },
        {
            value:'label2',
            label:'FDZGL',
        },
        {
            value:'label3',
            label:'FZ',
        }
        ],
        value4:'',
        value5:'',
        startTime: '',
        endTime: '',
    
        tableData: [{
          var: 'NBQG10',
          value: '',
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
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });
        });
      },

      postDSTConfig() {
        var instance = this.$ajax.create({
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
        if(value2 == 'conditional'){
          this.fromData
        }else{
          this.fromData
        }

        instance.post(url, fromData)
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

        openFullScreen() {
            this.fullscreenLoading = true;
            setTimeout(() => {
            this.fullscreenLoading = false;
            }, 2000);
        },

        uploadError(err, file, fileList) {
                // 上传失败
                this.$message.error(err);
                this.reset();
        },
        uploadSuccess(response, file, fileList) {
                // 上传成功
                console.log(response);
                console.log(file);
                console.log(fileList);
                this.reset();
        },
        submitUpload() {
                this.$set(this.queryParams, "params", this.checkList.toString());
                this.$refs.upload.submit();
        },
        reset() {
                // 重置
                // 清空多选框
                this.checkList = [];
                // 清空上传列表
                this.$refs.upload.clearFiles();
        },

        //  download(url) {
        //     window.open(url);
        //     loacation.href=url;
        // }
        }
    }
    
    


</script>


<style scoped>
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
</style>



<template>
    <div class="calculation">

        <div class="text0">GMM计算</div>
        <!-- 分割线 -->
        <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">

        <el-card class="card1">
            <el-row :gutter="20">
                <el-col :span="4">
                <div class="select">
                <el-select v-model="formData.id1" clearable @change="updateConfig()" placeholder="选择模型配置">
                    <el-option
                    v-for="item in configList"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                </div>
                </el-col>

                <el-col :span="4">
                    <div class="select">
                    <el-select v-model="formData.option" clearable @change="updateOption()" placeholder="选择计算函数值">
                    <el-option
                    v-for="item in options2"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                    </el-select>
                    </div>
                </el-col>

                <el-col :span="4" v-if="formData.option == 'KL'||formData.option == 'RMSE'">
                    <div class="select">
                    <el-select v-model="formData.id2" clearable placeholder="KL或RMSE对比模型配置">
                    <el-option
                    v-for="item in configList"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                    </el-select>
                    </div>
                </el-col>
                <el-col :span="8" v-if="formData.option == 'pdf'||formData.option == 'cdf'">
                     <div class="table1">
                    <el-table
                        :data="tableData1"
                        border
                        style="width: 100%; margin-top: 20px">
                        <el-table-column
                            prop="id"
                            value="val"
                            label="参数y"
                            header-align="center">
                        </el-table-column>
                        <el-table-column
                            v-for="col in tableData1[0].list"
                            label="value"
                            header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-model="col.val" placeholder="请输入内容"  clearable @change="change"></el-input>
                        </template>
                        </el-table-column>
                    </el-table>
                    </div>
                </el-col>
            </el-row>
        </el-card>

        <el-card class="card2">
            <!--<el-row :gutter="20" v-if="formData.option == 'RMSE'">
                <div class="RMSE">
                <el-col :span="6">
                    <div class="text">
                        RMSE变量范围
                    </div>
                </el-col>

                <el-col :span="6">
                    <el-table
                        :data="tableData2"
                        border
                        style="width: 100%">
                        <el-table-column
                        prop="var1"
                        label="var1"
                        header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-mode="scope.row.date" clearable placeholder="请输入内容"  clearable @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                        <el-table-column
                        prop="var2"
                        label="var2"
                        header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-mode="scope.row.date" clearable placeholder="请输入内容" @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                        <el-table-column
                        prop="var3"
                        label="var3"
                        header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-mode="scope.row.date" clearable placeholder="请输入内容" @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                    </el-table>
                </el-col>
                </div>
            </el-row>-->

            <el-row :gutter="20">
                <div class="linear1" v-if="formData.option == 'linear'">
                <el-col :span="6">
                <div class="text1">
                        计算随机变量线性函数的<br>
                        分布式随机变量矩阵系数
                </div>
                </el-col>

                <el-col :span="6">
                    <el-table
                        :data="tableData3"
                        border
                        style="width: 100%">
                        <el-table-column
                        prop="var1"
                        label="var1"
                        header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-model="scope.row.var1" clearable placeholder="请输入内容"  clearable @change="change"></el-input>
                        </template>
                        </el-table-column>
                        <el-table-column
                        prop="var2"
                        label="var2"
                        header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-model="scope.row.var2" clearable placeholder="请输入内容"  clearable @change="change"></el-input>
                        </template>
                        </el-table-column>
                    </el-table>
                </el-col>



                <el-col :span="5">
                <div class="text1-1">
                        计算随机变量线性函数的<br>
                        分布式随机变量常数矩阵系数
                </div>
                </el-col>

                <el-col :span="6">
                   <el-table
                        :data="tableData4"
                        border
                        style="width: 100%">
                        <el-table-column
                        prop="var1"
                        label="var1"
                        header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-model="scope.row.var1" clearable placeholder="请输入内容"  clearable @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                    </el-table>
                </el-col>
                </div>
            </el-row>


            <el-row :gutter="50" v-show="formData.option =='qiantile'">
                <div class="linear2">
                <el-col :span="6">
                    <div class="text2">
                        计算输入分布的10%至100%<br>
                        分位时随机变量的范围
                    </div>

                </el-col>

                <el-col :span="4" >
                    <div class="input">
                    <span>n_min</span>
                    <el-input placeholder="输入最小值" v-model="formData.n_min" clearable></el-input>
                    </div>
                </el-col>
                <el-col :span="6">
                    <div class="input0">
                    <span>n_max</span>
                    <el-input placeholder="输入最大值" v-model="formData.n_max" clearable></el-input>
                    </div>
                </el-col>
                </div>
            </el-row>
        </el-card>

         <div class="start">
            <el-button type="primary" @click="postData('http://localhost:8000/GMM/calculation')" icon="el-icon-d-caret" v-loading.fullscreen.lock="fullscreenLoading">开始计算</el-button>
            <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width="40%"
            :before-close="handleClose">
            <div class="window">
                <span>{{this.result }}</span>
                <img class="image" :src="'http://localhost:8000/GMM/image?name='+pictureName1" v-if="pictureName1 != none"></img>
                <img class="image" :src="'http://localhost:8000/GMM/image?name='+pictureName2" v-if="pictureName2 != none"></img>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
            </el-dialog>
        </div>
    </div>
</template>


<script>
export default {
    data(){
      return{

          fullscreenLoading:false,
        
        result: 0,
        pictureName1: "",
        pictureName2: "",
        d: 0,
        configInfoList: [],
        chooseConfig: {},
        configList: [],
        formData: {
            id1: "",
            id2: "",
            option: "",
            y: "",
            x: "",
            A: "",
            b: "",
            n_min: "",
            n_max: "",
        },


        dialogVisible: false,


        input1:'',
        input2:'',

        // 控制显示
        show:false,


        options1: [{
            value: 'A',
            label: '配置A'
        }, {
            value: 'B',
            label: '配置B'
        }, {
            value: 'C',
            label: '配置C'
       }],
       value1: '',

        options2: [{
          value: 'pdf',
          label: 'PDF'
        }, {
          value: 'cdf',
          label: 'CDF'
        }, {
          value: 'qiantile',
          label: 'qiantile'
        },
        {
          value: 'KL',
          label: 'KL'
        },
        {
          value: 'RMSE',
          label: 'RMSE'
        },
        {
          value:'linear',
          label:'linear'
        }],
        value2: '',

         options3: [{
          value: 'A',
          label: '配置A'
        }, {
          value: 'B',
          label: '配置B'
        }, {
          value: 'C',
          label: '配置C'
        }],
        value3: '',

    tableData1: [{
        id: 'val',
        list: [],
    }],

     tableData2: [{
          var1: '1',
          var2: '1',
          var3: '1'
        }, {
          var1: '1',
          var2: '1',
          var3: '1'
        }],

    tableData3: [],

    tableData4:[{
          var1:'0',
    },{
          var1:'0',
    },{
          var1:'0',
    }],


      }
    },

    mounted: function() {
      this.getConfig()
    },


    methods:{
        postData(url) {

            // loading 5秒
             this.fullscreenLoading = true;
                setTimeout(() => {
                this.fullscreenLoading = false;
            }, 5000);

            var instance = this.$ajax.create({
                headers: {'Content-Type': 'application/json'}
            });
            this.formData.y = this.tableData1[0].list

            if (this.formData.option == "linear"){
                var list = []
                for(var i = 0; i < this.tableData3.length;i++) {
                    list.push([this.tableData3[i].var1, this.tableData3[i].var2])
                }
                this.formData.A = list
                var list1 = []
                for(var i = 0; i < this.tableData4.length; i++) {
                    list1.push(this.tableData4[i].var1)
                }
                this.formData.b = list1
                
            }
            
            instance.post(url, this.formData).then(function (response) {

                console.log(response)
                if (response.data.data.pictureName && response.data.data.pictureName.length == 2) {
                  this.pictureName1 = response.data.data.pictureName[0]
                  this.pictureName2 = response.data.data.pictureName[1]
                }

                // this.pictureName = "http://localhost:8000/GMM/image?name=" + response.data.data.pictureName
                // console.log(this.pictureName)
                this.result = response.data.data.pdf
                this.dialogVisible=true

                // if(true) {
                //     this.$ajax.get('http://localhost:8000/GMM/image').then(function (response) {
                        
                //     }.bind(this)).catch(function (error) {
                    
                //     });
                // }
                //处理数据   
            }.bind(this)).catch(function (error) {
                return 0;
            });
        },
        updateOption() {
            this.d = JSON.parse(this.chooseConfig.y).length
            console.log(this.chooseConfig)
            if(this.formData.option == 'pdf'||this.formData.option == 'cdf') {
                    this.tableData1[0].list = []
                    for(var j=0; j < JSON.parse(this.chooseConfig.y).length; j++) {
                        this.tableData1[0].list.push({val: 0})
                    }
            }
            if(this.formData.option == 'linear') {
                this.tableData3 = []
                for(var i = 0; i < this.d; i++) {
                    this.tableData3.push({var1: "", var2: ""})
                }
                console.log(this.tableData3)
            }
        },
        change() {
            console.log(this.tableData1)
            console.log(this.tableData2)
            console.log(this.tableData3)
            console.log(this.tableData4)
        },
        updateConfig() {
            for(var i=0; i < this.configInfoList.length; i++) {
                if(this.configInfoList[i].id == this.formData.id1) {
                    this.chooseConfig = this.configInfoList[i]
                    this.updateOption()
                    // if (this.chooseConfig.option == 'pdf'||this.chooseConfig.option == 'cdf') {
                    //     this.tableData1 = []
                    //     for(var j=0; j < JSON.parse(this.chooseConfig.y); j++) {
                    //         this.tableData1.push({value: 0})
                    //         console.log(this.tableData1)
                    //     }
                    // }
                }
            }
        },
        getConfig() {
            this.$ajax.get("http://127.0.0.1:8000/GMM/model/distribution/").then(function (response) {
                this.configInfoList = response.data
                console.log(response)
                //加载数据到配置中
                //初始化configList
                this.configList = []
                for(var i=0; i < response.data.length; i++){
                    this.configList.push({
                        value: response.data[i].id,
                        label: response.data[i].name
                    })
                }
            }.bind(this)).catch(function (error) {
                return 0;
            });
        },

        // 显示
        showCont(){
            this.show=!this.show;
        },

        // 关闭按钮
        handleClose(done) {
        this.$confirm('确认关闭？')
            .then(_ => {
                done();
            })
            .catch(_ => {});
        },


        // 表格内输入
        handleCurrentChange(row, event, column) {
                console.log(row, event, column, event.currentTarget)
            },
        handleEdit(index, row) {
                console.log(index, row);
            },
            // handleDelete(index, row) {
            //     console.log(index, row);
            // },
         
        }


}


</script>

<style scoped>
.image {
    width: 100%;
    height: 100%;
}

.calculation{
    height:120%;
    margin-left:-12px;
    margin-top:-12px;
}

.text0{
    font-weight: bold;
    padding-top:15px;
    font-size:18px;
}

.card1{
    background-color:rgba(255,255,255,0.9);
    margin-top:10px;
}

.card1:hover{
    background-color:rgba(53,92,125, 0.1);
}

.table1{
    margin-bottom:20px;
}

.select{
    margin-top:40px;
}

.text{
    margin-top:20px;
}

.card2{
    background-color:rgba(255,255,255,0.9);
    margin-top:20px;
}

.card2:hover{
    background-color:rgba(53,92,125, 0.1);
}

.start{
    margin-top:15px;
    /* margin-left:250px; */
}

.linear1{
    margin-top:20px;
}

.linear2{
    margin-top:20px;
}

.input{
    margin-left:-10px;
}

.input0{
    margin-left:150px;
}

.text{
    margin-left:-80px;
    margin-top:30px;
}

.text1{
    margin-top:50px;
    margin-left:-70px;
}

.text1-1{
    margin-top:50px;
    margin-left:-70px;
}
.text2{
    margin-left:-35px;
    margin-top:15px;
}

.tb-edit .el-input {
    display: none
}
.tb-edit  .current-row .el-input {
    display: block
}
.tb-edit  .current-row .el-input+span {
    display: none
}

</style>

<template>
    <div class="calculation">

        <div class="text0">GMM计算</div>
        <!-- 分割线 -->
        <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">

        <el-card class="card1">
            <el-row :gutter="20">
                <el-col :span="4">
                <div class="select">
                <el-select v-model="value1" clearable placeholder="选择模型配置">
                    <el-option
                    v-for="item in options1"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                </div>
                </el-col>

                <el-col :span="4">
                    <div class="select">
                    <el-select v-model="value2" clearable placeholder="选择输出结果">
                    <el-option
                    v-for="item in options2"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                    </el-select>
                    </div>
                </el-col>

                 <el-col :span="4">
                     <div class="select">
                    <el-select  v-model="value3" clearable placeholder="KL或RMSE对比模型配置">
                    <el-option
                    v-for="item in options3"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                    </el-select>
                     </div>
                </el-col>

               
                <el-col :span="10">
                     <div class="table1">
                    <el-table
                        :data="tableData1"
                        class="tb-edit"
                        highlight-current-row @row-click="handleCurrentChange"
                        border
                        style="width: 100%; margin-top: 20px">
                        <el-table-column
                            prop="id"
                            label="参数y"
                            header-align="center">
                        </el-table-column>
                        <el-table-column
                            prop="amount1"     
                            label="var1"
                            header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-mode="scope.row.amount1" placeholder="请输入内容"  clearable @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                        <el-table-column
                          
                            label="var2"
                            header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-mode="scope.row.date" placeholder="请输入内容" clearable @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                        <el-table-column          
                            label="var3"
                            header-align="center">
                         <template scope="scope">
                            <el-input size="small" v-mode="scope.row.date" placeholder="请输入内容" clearable @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                    </el-table>
                    </div>
                </el-col>
            </el-row>
        </el-card>

        <el-card class="card2">
            <el-row :gutter="20">
                <div class="RMSE">
                <el-col :span="6">
                    <div class="text">
                        RMSE变量范围
                    </div> 
                </el-col>

                <el-col :span="12">
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
            </el-row>

            <el-row :gutter="20">
                <div class="linear1">
                <el-col :span="5">           
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



                <el-col :span="5">
                <div class="text1">
                        计算随机变量线性函数的<br>
                        分布式随机变量常数矩阵系数
                </div>
                </el-col>

                <el-col :span="6">
                   <el-table
                        :data="tableData4"
                        border
                        class="tb-edit"
                        highlight-current-row @row-click="handleCurrentChange"
                        style="width: 100%">
                        <el-table-column
                        prop="var1"
                        label="var1"
                        header-align="center">
                        <template scope="scope">
                            <el-input size="small" v-mode="scope.row.date" clearable placeholder="请输入内容"  clearable @change="handleEdit(scope.$index,scope.row)"></el-input>
                        </template>
                        </el-table-column>
                    </el-table>
                </el-col>
                </div>
            </el-row>


            <el-row :gutter="50">
                <div class="linear2">
                <el-col :span="6">
                    <div class="text2">
                        计算输入分布的10%至100%<br>
                        分位时随机变量的范围
                    </div>

                </el-col>

                <el-col :span="4">
                    <div class="input">
                    <span>n_min</span>
                    <el-input placeholder="输入最小值" v-model="input1" clearable></el-input>
                    </div>
                </el-col>

                <el-col :span="6">
                    <div class="input0">
                    <span>n_max</span>
                    <el-input placeholder="输入最大值" v-model="input2" clearable></el-input>
                    </div>
                </el-col>


                </div>
            </el-row>
        </el-card>

         <div class="start">
            <el-button type="primary" @click="dialogVisible=true" icon="el-icon-d-caret">开始计算</el-button>
            <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width="40%"
            :before-close="handleClose">
            <div class="window">
            <span>This is a demo</span>
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

       dialogVisible: false,


        input1:'',
        input2:'',

 


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
          value: 'PDF',
          label: 'PDF'
        }, {
          value: 'CDF',
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
          id: 'value',
          amount1: '1',
          amount2: '1',
          amount3: '1',
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
    
    tableData3: [{
          var1: '1',
          var2: '1',
          var3: '1'
        }, {
          var1: '1',
          var2: '1',
          var3: '1'
        },
        {
          var1: '1',
          var2: '1',
          var3: '1'
        }],

    tableData4:[{
          var1:'1',
    }],


      }
    },

    methods:{

        handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },

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
.calculation{
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

.card1{
    background-color:rgba(255, 255, 255, 0.2);
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
    background-color:rgba(255, 255, 255, 0.2);
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

.input0{
    margin-left:150px;
}

.text{
    margin-left:-80px;
    margin-top:30px;
}

.text1{
    margin-top:25px;
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

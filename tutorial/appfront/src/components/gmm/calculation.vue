<template>
    <div class="calculation">

        <div class="text0">GMM计算</div>
        <!-- 分割线 -->
        <hr width=100%   size=1   color=#bbbcbc   style="FILTER: alpha(opacity=100,finishopacity=0)">

        <el-card class="card1">
            <el-row :gutter="20">
                <el-col :span="4">
                <div class="select">
                <el-select v-model="value" clearable placeholder="选择模型配置">
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
                    <el-select v-model="value1" clearable placeholder="选择输出结果">
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
                    <el-select  disabled v-model="value2" clearable placeholder="KL或RMSE对比模型配置">
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
                        border

                        style="width: 100%; margin-top: 20px">
                        <el-table-column
                            prop="id"
                            label="参数y"
                            width="180">
                        </el-table-column>
                        <el-table-column
                            prop="var"
                            label="var1">
                        </el-table-column>
                        <el-table-column
                            prop="amount1"
                            label="var2">
                        </el-table-column>
                        <el-table-column
                            prop="amount2"
                            label="var3">
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
                        prop="date"
                        label="var1"
                        >
                        </el-table-column>
                        <el-table-column
                        prop="name"
                        label="var2"
                        >
                        </el-table-column>
                        <el-table-column
                        prop="address"
                        label="var3"
                        >
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
                    :data="tableData"
                    border
                    style="width: 100%">
                    <el-table-column></el-table-column>
                    <el-table-column></el-table-column>
                    <el-table-column></el-table-column>
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
                    :data="tableData"
                    border
                    style="width: 100%">
                    <el-table-column></el-table-column>
                    <el-table-column></el-table-column>
                    <el-table-column></el-table-column>
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
          value: '',
          label: '配置A'
        }, {
          value: '',
          label: '配置B'
        }, {
          value: '',
          label: '配置C'
        }],
        value: '',

        options2: [{
          value: '',
          label: 'PDF'
        }, {
          value: '',
          label: 'CDF'
        }, {
          value: '',
          label: 'qiantile'
        },
        {
          value: '',
          label: 'KL'
        },
        {
          value: '',
          label: 'RMSE' 
        },
        {
          value:'',
          label:'linear'
        }],
        value1: '',

         options3: [{
          value: '',
          label: '配置A'
        }, {
          value: '',
          label: '配置B'
        }, {
          value: '',
          label: '配置C'
        }],
        value2: '',
        
    tableData1: [{
          id: 'value',
          var: '',
          amount1: '',
          amount2: '',
          amount3: '',
        }],

     tableData2: [{
          date: '',
          name: '',
          address: ''
        }, {
          date: '',
          name: '',
          address: ''
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
</style>

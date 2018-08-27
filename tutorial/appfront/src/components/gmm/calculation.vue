<template>
    <div class="calculation">
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
                        width="180">
                        </el-table-column>
                        <el-table-column
                        prop="name"
                        label="var2"
                        width="180">
                        </el-table-column>
                        <el-table-column
                        prop="address"
                        label="var3">
                        </el-table-column>
                    </el-table>
                </el-col>
                </div>
            </el-row>

            <el-row :gutter="20">
                <div class="linear1">
                <el-col :span="12">           
                

                </el-col>

                <el-col :span="12">

                </el-col>
                </div>
            </el-row>


            <el-row :gutter="20">
                <div class="linear2">
                <el-col :span="6">
                    <div class="text1">
                        计算输入分布的10%至100%<br>
                        分位时随机变量的范围
                    </div>

                </el-col>

                <el-col :span="6">
                    <div class="input">
                    <span>n_min</span>
                    <el-input placeholder="输入最小值" v-model="input1" clearable></el-input>
                    </div>
                </el-col>

                <el-col :span="6">
                    <div class="input">
                    <span>n_max</span>
                    <el-input placeholder="输入最大值" v-model="input2" clearable></el-input>
                    </div>
                </el-col>


                </div>
            </el-row>
        </el-card>

         <div class="start">
            <el-button type="primary" @click="openFullScreen" v-loading.fullscreen.lock="fullscreenLoading" icon="el-icon-d-caret">开始计算</el-button>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return{

        fullscreenLoading: false,

        input1:'',
        input2:'',


        options1: [{
          value: '选项1',
          label: '配置A'
        }, {
          value: '选项2',
          label: '配置B'
        }, {
          value: '选项3',
          label: '配置C'
        }],
        value: '',

        options2: [{
          value: '选项1',
          label: 'PDF'
        }, {
          value: '选项2',
          label: 'CDF'
        }, {
          value: '选项3',
          label: 'qiantile'
        },
        {
          value: '选项4',
          label: 'KL'
        },
        {
          value: '选项5',
          label: 'RMSE' 
        },
        {
          value:'选项6',
          label:'linear'
        }],
        value1: '',

         options3: [{
          value: '选项1',
          label: '配置A'
        }, {
          value: '选项2',
          label: '配置B'
        }, {
          value: '选项3',
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
         openFullScreen() {
        this.fullscreenLoading = true;
        setTimeout(() => {
          this.fullscreenLoading = false;
        }, 2000);
      },
    }


}


</script>

<style scoped>
.card1{
    width:60%;
    margin-top:10px;
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
    width:60%;
    margin-top:20px;
}

.start{
    margin-top:15px;
    margin-left:250px;
}
</style>

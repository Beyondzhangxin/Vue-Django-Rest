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
                            label="y"
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
    </div>
</template>


<script>
export default {
    data(){
        return{

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
        }]
      }
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


</style>

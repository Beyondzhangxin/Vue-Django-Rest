<template>
    <div class="calculation">
        <el-card class="card1">
            <el-select v-model="value4" clearable placeholder="选择模型配置">
                <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
                </el-option>
            </el-select>



        </el-card>
    </div>
</template>


<script>
export default {
    data(){
        return{
             options: [{
          value: '选项1',
          label: '配置A'
        }, {
          value: '选项2',
          label: '配置B'
        }, {
          value: '选项3',
          label: '配置C'
        }],
        value4: ''
      }
        
    }
}


</script>

<style scoped>

</style>

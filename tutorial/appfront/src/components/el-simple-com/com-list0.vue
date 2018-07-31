<template>
  <el-row class="list">
    <!-- tableData数据的映射 -->
    <el-table :data="tableData" border
    style="width: 100%" v-loading="false">
      <el-table-column
      v-for="{ prop, label } in tabConfigs"
      :key="prop"
      :prop="prop"
      :width="204"
      :label="label">
      </el-table-column>
      <el-pagination
      background
      layout="prev, pager, next"
      :total="1000">
      </el-pagination>
    </el-table>
    <!-- <el-row>
      <div class="block">
        <el-pagination
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="1000">
        </el-pagination>
      </div>
    </el-row> -->
  </el-row>
</template>

<script>
  export default {
    name: 'ComList',
    props: ['data', 'tabConfigs'],
    data() {
      return {
        tableData: []
        // pageSize: 2
      }
    },
    //mounted为vue对象的生命周期
    watch: {
    // 如果 `question` 发生改变，这个函数就会运行
      data: function (newData, oldData) {
        this.showAll();
      }
    },
    mounted: function() {
      this.showAll();
    },
    methods: {
      //通过异步请求，ajax用来获取数据
      showAll(){
        this.tableData = [];
        this.$ajax.get(this.data)
        .then(function (response) {
          for (var i = 0; i < response.data.results.length; i++) {
            this.setTableData(response.data.results[i])
          }
        }.bind(this))
        .catch(function (error) {
        });
        console.log(this.tableData);
      },
      //设置tableData对象
      //toFixed四舍五入
      setTableData(result){
        this.tableData.push(result)
      },
    }
  }
</script>
<style scoped>
  .list {
    margin: auto;
    position: relative;
  }

  .el-row {
    margin-bottom: 0px;
    padding-bottom: 295px;
  }
</style>

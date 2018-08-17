<template>
  <el-row class="list">
    <!-- tableData数据的映射 -->
    <el-table :data="tableData"
    border
    style="width: 100%"
    v-loading="loading">
      <el-table-column
      v-for="{ prop, label } in tabConfigs"
      :key="prop"
      :prop="prop"
      :width="263"
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
    props: ['data'],
    data() {
      this.tabConfigs = [
        {prop: 'dev_name', label: '设备名称'},
        {prop: 'dev_xh', label: '设备型号'},
        {prop: 'dev_dqgl', label: '设备当前功率'},
        {prop: 'dev_drdx', label: '设备当日等效'},
        {prop: 'dev_jrfd', label: '设备接入容量'},
        {prop: 'dev_cjqzt', label: '采集器状态'},
      ]
      return {
        loading: true,
        tableData: [],
        // pageSize: 2
      }
    },
    //mounted为vue对象的生命周期
    watch: {
      // 如果 `question` 发生改变，这个函数就会运行
      data: function (newQuestion, oldQuestion) {
        this.showAll();
      },

    },
    mounted: function() {
      this.showAll();
    },
    methods: {
      //通过异步请求，ajax用来获取数据
      showAll(){
        this.loading = true
        this.tableData = [];
        this.$ajax.get(this.data)
        .then(function (response) {
          for (var i = 0; i < response.data.data.tab.length; i++) {
            //在这里写过aside过滤
            // if (this.$store.state.chooseTree.length != 0) {
            //   for (var j = 0; j < this.$store.state.chooseTree.length; j++) {
            //   //如果设备和系统匹配则显示
            //     if (response.data.data.tab[i].dev_systemType == this.$store.state.chooseTree[j].system) {
            //       if(response.data.data.tab[i].dev_xh == this.$store.state.chooseTree[j].device) {
            //         this.setTableData(response.data.data.tab[i])
            //       }
            //     }
            //   }
            //   continue;
            // }
            this.setTableData(response.data.data.tab[i])
          }
          this.loading = false
        }.bind(this))
        .catch(function (error) {
          return 0;
        });
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

  }

  .el-row {
    margin-bottom: 0px;

  }
</style>

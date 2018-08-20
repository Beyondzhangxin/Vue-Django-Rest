<template>
  <!-- <div class="str"> -->

  <el-row class="list">
    <!-- tableData数据的映射 -->
    <!-- v-loading="loading" -->
    <el-table :data="showTable" border
    style="width: 100%" v-loading="loading">
      <el-table-column
      v-for="{ prop, label } in tabConfigs"
      :key="prop"
      :prop="prop"
      :width="220"
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
  <!-- </div> -->
</template>

<script>
  export default {
    name: 'ComList',
    props: ['data', 'tabConfigs', 'filterKey','pageNum', 'pageSize', 'type'],
    data() {
      return {
        loading: false,
        tableData: [],
        showTable: [],
        // pageSize: 2
      }
    },
    computed: {
      listenChooseTree() {
        return this.$store.state.chooseTree;
      }
    },
    watch: {
      type: function(val, oldval) {
        this.filterAll();
      },
      listenChooseTree: function(val, oldval) {
        this.filterAll();
      },
      // 如果 `question` 发生改变，这个函数就会运行
      pageNum: function (newPage, oldPage) {
        this.filterAll();
      }
    },
    //mounted为vue对象的生命周期
    mounted: function() {
      this.showAll();
    },
    methods: {
      filterAll () {
        this.showTable = [];
        var list = this.pageNumFilter();
        list = this.chooseTreeFilter(list);
        list = this.typeFilter(list);
        this.showTable = list;
      },
      pageNumFilter() {
        var list = [];
        for (var i = 0; i < this.pageSize ; i++) {
          if (this.pageNum*this.pageSize+i+1 > this.tableData.length) {
            break;
          }
          list.push(this.tableData[this.pageNum*this.pageSize+i])
        }
        return list;
      },
      chooseTreeFilter(pageNumFilterList) {
        var list = []
        //构造{system:x, device[]}
        for (var i = 0; i < this.$store.state.chooseTree.length; i++) {
          for (var j = 0; j < this.$store.state.chooseTree[i].devices.length; j++) {
            list.push({
              'system' : this.$store.state.chooseTree[i].system,
              'device' : this.$store.state.chooseTree[i].devices[j]
            });
          }
        }
          // if (this.tableData[i]) {
          //
          // }
        if (list == []) {
            return pageNumFilterList;
        }
        var list2 = []
        for (var i = 0; i < pageNumFilterList.length; i++) {
          for (var j = 0; j < list.length; j++) {
            if (pageNumFilterList[i].dev_systemType == list[j].system && pageNumFilterList[i].dev_xh == list[j].device) {
              list2.push(pageNumFilterList[i]);
            }
          }
        }
        return list2;
      },
      typeFilter(chooseTreeFilterList){
          var list = [];
          if (this.type == 'NBQ') {
            list = chooseTreeFilterList
          }
          return list
      },
      //通过异步请求，ajax用来获取数据
      showAll(){
        this.loading = true
        this.tableData = [];
        this.showTable = [];
        this.$ajax.get(this.data)
        .then(function (response) {
          this.setTableData(response.data.data.tab);
          this.tableData = response.data.data.tab;
          for (var i = 0; i < this.pageSize; i++) {
            this.showTable.push(this.tableData[this.pageNum*this.pageSize+i])
          }
          // for (var i = 0; i < response.data.results.length; i++) {
          //   //在这里写过aside过滤
          //   this.setTableData(response.data.results[i])
          // }
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
    margin: auto;
    position: relative;
  }

  .el-row {
    margin-bottom: 0px;
    padding-bottom: 10px;
  }


</style>

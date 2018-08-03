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
        {prop: 'dev_avg_p', label: '当前功率（w）'},
        {prop: 'dev_day_w', label: '今日发电量（kw*h）'},
        {prop: 'dev_effect_time', label: '当日的等效小时（h）'},
        {prop: 'dev_status', label: '采集器的状态'},
        {prop: 'dev_get_time', label: '数据采集的时间'},
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
        this.loading = true
        this.tableData = [];
        this.$ajax.get(this.data)
        .then(function (response) {
          for (var i = 0; i < response.data.results.length; i++) {
            //在这里写过aside过滤
            this.setTableData(response.data.results[i])
          }
          this.loading = false
        }.bind(this))
        .catch(function (error) {
        });
        console.log(this.tableData);
      },
      //设置tableData对象
      //toFixed四舍五入
      setTableData(result){
        var effect_time = result.time_sum/60
        var avg_p = result.p_avg
        var day_w = result.p_avg * result.time_sum/60/100
        var element = {
          dev_name: result.cityid + ' ' + result.pcbid,
          dev_avg_p: avg_p.toFixed(2),
          dev_day_w: day_w.toFixed(4),
          dev_effect_time: effect_time.toFixed(2),
          dev_status: '未知',
          dev_get_time: result.time_min+' 到 '+result.time_max
        }
        this.tableData.push(element)
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

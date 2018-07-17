  <template>
    <el-row>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="cityid"
          label="cid"
          width="50">
        </el-table-column>
        <el-table-column
          prop="updatetime"
          label="ut"
          width="50">
        </el-table-column>
        <el-table-column
          prop="pcbid"
          label="pid"
          width="50">
        </el-table-column>
        <el-table-column
          prop="channelid"
          label="cid"
          width="50">
        </el-table-column>
        <el-table-column
          prop="batid"
          label="bid"
          width="50">
        </el-table-column>
        <el-table-column
          prop="u"
          label="u"
          width="50">
        </el-table-column>
        <el-table-column
          prop="p"
          label="p"
          width="50">
        </el-table-column>
        <el-table-column
          prop="t"
          label="t"
          width="50">
        </el-table-column>
        <el-table-column
          prop="v12"
          label="v12"
          width="50">
        </el-table-column>
        <el-table-column
          prop="v5"
          label="v5"
          width="50">
        </el-table-column>
        <el-table-column
          prop="devicetime"
          label="dt"
          width="50">
        </el-table-column>
        <el-table-column
          prop="pcor"
          label="pc"
          width="50">
        </el-table-column>
      </el-table>
      <el-row>
        <div class="block">
          <span class="demonstration">==================</span>
          <el-pagination
            @current-change="handleCurrentChange"
            layout="prev, pager, next"
            :page-size="pageSize"
            :total="1000">
          </el-pagination>
        </div>
      </el-row>
    </el-row>
  </template>

  <script>
    export default {
      name: 'SimpleList',
      data() {
        return {
          tableData: [],
          pageSize: 2
        }
      },
      mounted: function() {
        this.showAll()
      },
      methods: {
        showAll(){
          this.$ajax.get('http://127.0.0.1:8000/pv/list/')
          .then(function (response) {
            console.log(response)
            console.log(response.data)
            this.tableData = response.data.results
          }.bind(this))
          .catch(function (error) {
          });
        },
        handleCurrentChange(val){
          this.$ajax.get('http://127.0.0.1:8000/pv/list/',{
              params:{
                page: val+1,
                page_size: this.pageSize,
              }
          })
          .then(function (response) {
            this.tableData = response.data.results
          }.bind(this))
          .catch(function (error) {
          });
        },
      }
    }
  </script>
  <style>

  </style>

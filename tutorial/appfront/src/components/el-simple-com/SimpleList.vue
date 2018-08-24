  <template>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="id"
        label="身份"
        width="180">
      </el-table-column>
      <el-table-column
        prop="code"
        label="说明"
        width="180">
      </el-table-column>
      <el-table-column
        prop="language"
        label="语言">
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      name: 'SimpleList',
      data() {
        return {
          tableData: []
        }
      },
      mounted: function() {
        this.showAll()
      },
      methods: {
        showAll(){
          this.$ajax.get('http://127.0.0.1:8000/api/snippets/')
          .then(function (response) {
            this.tableData = response.data
          }.bind(this))
          .catch(function (error) {
          });
        }
      }
    }
  </script>
  <style>

  </style>

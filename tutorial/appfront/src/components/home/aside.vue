<template>
  <div class="aside">
    <div class="aside0">
      列表名称
    </div>
    <div class="aside1">
      <el-row>
        <el-col :span="4"><el-button  size="mini" type="primary">名称</el-button></el-col>
        <el-col :span="4"><el-button class="b2" size="mini" type="success">容量</el-button></el-col>
        <el-col :span="4"><el-button class="b3" size="mini" type="warning">地区</el-button></el-col>
        <el-col :span="4"><el-button class="b4" size="mini" type="danger">状态</el-button></el-col>
      </el-row>
    </div>
    <div class="aside3">
      <el-input
      placeholder="输入关键字进行过滤"
      v-model="filterText">
      </el-input>
      <el-tree
      class="filter-tree"
      :data="data2"
      :props="defaultProps"
      default-expand-all
      :filter-node-method="filterNode"
      ref="tree2">
      </el-tree>
    </div>
  </div>
</template>

<script>
export default {
  props: [] ,
  data () {
    return {
      filterText: '',
        data2: [{
          id: 1,
          label: '一级 1',
          children: [{
            id: 4,
            label: '二级 1-1',
            children: [{
              id: 9,
              label: '三级 1-1-1'
            }, {
              id: 10,
              label: '三级 1-1-2'
            }]
          }]
        }, {
          id: 2,
          label: '一级 2',
          children: [{
            id: 5,
            label: '二级 2-1'
          }, {
            id: 6,
            label: '二级 2-2'
          }]
        }, {
          id: 3,
          label: '一级 3',
          children: [{
            id: 7,
            label: '二级 3-1'
          }, {
            id: 8,
            label: '二级 3-2'
          }]
        }],
        defaultProps: {
          children: 'children',
          label: 'label'
        }
    }
  },
  mounted: function() {
    this.loadAll();
  },
  watch: {
      filterText(val) {
        this.$refs.tree2.filter(val);
      }
    },

    methods: {
      filterNode(value, data) {
        if (!value) return true;
        return data.label.indexOf(value) !== -1;
      }
    },
}
</script>
<style scoped>
  .aside {
    width: 100%;
    height: 100%;
    overflow-x: hidden;
    overflow-y: hidden;
    background-color: #fff;
    box-sizing: content-box;
  }

  .aside .aside1 {
    width: 100%;
    height: 40px;
  }

  .aside3 {
    width: 80%;
    height: 700px;
    box-sizing: content-box;
    z-index: auto;
    line-height: 20px;
    border:1px solid #e9ebef;
    position: relative;
    top: -10px;
  }

  .el-button {
    border-bottom: 0px;
    z-index: auto;
    color: #fff;
  }

  .b1 {
    border-left-color:  #409eff;
    border-top-left-radius: 10px 7px;
    border-top-right-radius: 10px 7px;
  }

  .b2 {
    border-left-color: #67c23a;
    border-top-left-radius: 10px 7px;
    border-top-right-radius: 10px 7px;
  }

  .b3 {
    border-left-color: #e6a23c;
    border-top-left-radius: 10px 7px;
    border-top-right-radius: 10px 7px;
  }

  .b4 {
    border-left-color: #f56c6c;
    border-top-left-radius: 10px 7px;
    border-top-right-radius: 10px 7px;
  }

  .el-autocomplete {
    position: relative;
    top: -12px;
    right: 30px;
  }
</style>

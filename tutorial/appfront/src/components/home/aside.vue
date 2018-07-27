<template>
  <div class="aside">
    <div class="aside0">
      列表名称
    </div>
    <div class="aside1">
      <el-row>
        <el-col :span="4"><el-button class="b1" size="mini" type="primary"
           @click="clickButtom(buttoms[0])">{{ buttoms[0] }}</el-button></el-col>
        <el-col :span="4"><el-button class="b2" size="mini" type="success"
           @click="clickButtom(buttoms[1])">{{ buttoms[1] }}</el-button></el-col>
        <el-col :span="4"><el-button class="b3" size="mini" type="warning"
           @click="clickButtom(buttoms[2])">{{ buttoms[2] }}</el-button></el-col>
        <el-col :span="4"><el-button class="b4" size="mini" type="danger"
           @click="clickButtom(buttoms[3])">{{ buttoms[3] }}</el-button></el-col>
      </el-row>
    </div>
    <div class="aside3">
      <el-input
<<<<<<< HEAD

      placeholder="输入关键字进行过滤"
      v-model="filterText" clearable>
=======
      v-bind:placeholder="placeholder"
      v-model="filterText">
>>>>>>> a157127b24787a8ee10fb7ea6f5bc8a9b00d20bd
      </el-input>
      <el-tree
      class="filter-tree"
      :data="data2"
      :props="defaultProps"
      default-expand-all
      show-checkbox
      node-key="id"
      :filter-node-method="filterNode"
      @check="sendTree()"
      ref="tree2">
      </el-tree>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home_aside',
  props: ['request'] ,
  data () {
    return {
        buttoms: ['名称', '容量', '地区', '状态'],
        placeholder: "输入关键字进行过滤",
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
        }],
        defaultProps: {
          children: 'children',
          label: 'label'
        }
    }
  },
  mounted: function() {
    //this.load();
  },
  watch: {
     filterText(val) {
       this.$refs.tree2.filter(val);
     }
   },

   methods: {
     sendTree(){
       console.log(this.$refs.tree2.getCheckedKeys());
     },

     filterNode(value, data) {
       if (!value) return true;
       return data.label.indexOf(value) !== -1;
     },
     load(){
       this.$ajax.get(this.data)
       .then(function (response) {
         console.log(response)
       }.bind(this))
       .catch(function (error) {
       });
     },
     clickButtom(str){
       this.placeholder = "输入"+ str +"进行过滤";
     },
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

<template>
  <div class="aside">
    <div class="aside1">
      <el-row>
        <el-col :span="6"><el-button size="small"
           @click="clickButtom(buttoms[0])">{{ buttoms[0] }}</el-button></el-col>
        <el-col :span="6"><el-button size="small"
           @click="clickButtom(buttoms[1])">{{ buttoms[1] }}</el-button></el-col>
        <el-col :span="6"><el-button size="small"
           @click="clickButtom(buttoms[2])">{{ buttoms[2] }}</el-button></el-col>
        <el-col :span="6"><el-button size="small"
           @click="clickButtom(buttoms[3])">{{ buttoms[3] }}</el-button></el-col>
      </el-row>
    </div>
    <div class="aside3">
      <el-input
      placeholder="输入关键字进行过滤"
      v-bind:placeholder="placeholder"
      v-model="filterText">
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


  <!-- <div class="aside">
    <div class="aside1">
      <div><el-button class="b" size="mini" type="primary"
         @click="clickButtom(buttoms[0])">{{ buttoms[0] }}</el-button></div>
      <div><el-button class="b" size="mini" type="success"
         @click="clickButtom(buttoms[1])">{{ buttoms[1] }}</el-button></div>
      <div><el-button class="b" size="mini" type="warning"
         @click="clickButtom(buttoms[2])">{{ buttoms[2] }}</el-button></div>
      <div><el-button class="b" size="mini" type="danger"
         @click="clickButtom(buttoms[3])">{{ buttoms[3] }}</el-button></div>
    </div>
    <div class="aside3">
      <el-input
      placeholder="输入关键字进行过滤"
      v-bind:placeholder="placeholder"
      v-model="filterText">
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
  </div> -->
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
            id: 2,
            label: '二级 1-1',
          },{
            id: 3,
            label: '二级 1-1',
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

.el-tree{
  color: #3f5bdd;
}

.el-button {
  background: #3f5bdd;
  border: 0px;
  color: #fff;
  padding-left: 19px;
  padding-right: 19px;
}

.aside {
    height: 100%;
    width: 260px;
    overflow-x: hidden;
    overflow-y: hidden;
    background-color: #fff;
    box-sizing: content-box;

  }

  .aside0{
  margin-bottom:5px;
  margin-top:4px;
  margin-left:-80px;
  }

  .aside1 {
    position: relative;
    top: 20px;
    color: #fff;
    height: 60px;
    margin-bottom: 2px;
  }

.b{
  padding-right:1px;
  text-align:center;

}

  .aside3 {
    width: 100%;
    height: 900px;
    box-sizing: content-box;
    z-index: auto;
    line-height: 20px;
    position: relative;
    top: -10px;
    box-shadow: 2px 2px 10px #9eabad;
    background-color: #fff;
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

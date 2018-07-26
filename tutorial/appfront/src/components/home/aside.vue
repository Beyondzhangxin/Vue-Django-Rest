<template>
  <div class="aside">
    <div class="aside0">
      列表名称
    </div>
    <div class="aside1">
      <el-row>
        <el-col :span="6"><el-button size="mini">名称</el-button></el-col>
        <el-col :span="6"><el-button size="mini">容量</el-button></el-col>
        <el-col :span="6"><el-button size="mini">地区</el-button></el-col>
        <el-col :span="6"><el-button size="mini">状态</el-button></el-col>
      </el-row>
    </div>
    <div class="aside2">
      <el-autocomplete
      popper-class="my-autocomplete"
      v-model="state3"
      :fetch-suggestions="querySearch"
      placeholder="请输入内容"
      @select="handleSelect">
        <i
          class="el-icon-edit el-input__icon"
          slot="suffix"
          @click="handleIconClick">
        </i>
        <template slot-scope="{ item }">
          <div class="name">{{ item.value }}</div>
          <span class="addr">{{ item.address }}</span>
        </template>
      </el-autocomplete>
    </div>
    <div class="aside3">

    </div>
  </div>
</template>

<script>
export default {
  props: ['asideName', 'asideData'] ,
  data () {
    return {
      restaurants: [],
        state3: ''
    }
  },
  mounted: function() {
    this.loadAll();
  },
  methods: {
    loadAll() {
       this.restaurants = [
         { "value": "三全鲜食（北新泾店）", "address": "长宁区新渔路144号" },
         { "value": "Hot honey 首尔炸鸡（仙霞路）", "address": "上海市长宁区淞虹路661号" },
         { "value": "新旺角茶餐厅", "address": "上海市普陀区真北路988号创邑金沙谷6号楼113" },
         { "value": "泷千家(天山西路店)", "address": "天山西路438号" },
       ];
    },
    querySearch(queryString, cb) {
        var restaurants = this.restaurants;
        var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
        // 调用 callback 返回建议列表的数据
        cb(results);
      },
      createFilter(queryString) {
        return (restaurant) => {
          return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      handleSelect(item) {
        console.log(item);
      },
      handleIconClick(ev) {
        console.log(ev);
      }
  }
}
</script>
<style scoped>
  .aside {
    width: 100%;
    height: 100%;
    overflow-x: auto;
    overflow-y: auto;
    background-color: #fff;
  }
  .aside .aside1 {
    width: 100%;
    height: 40px;
  }

  .aside1 ul {

  }



  .aside .aside2 {
    width: 100%;
    height: 40px;
  }
  .aside .aside3 {
    width: 100%;
    height: 700px;
  }
</style>

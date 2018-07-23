<template>
  <div class="First">
    <el-container>
      <el-main>
        <el-row :gutter="20">
          <el-col :span="8"><Gauge v-bind="gauge1"/></el-col>
          <el-col :span="8"><Gauge v-bind="gauge2"/></el-col>
          <el-col :span="8"><Gauge v-bind="gauge3"/></el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
          <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
          <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
          <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
          <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
          <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
        </el-row>
      </el-main>
  </el-container>
  </div>
</template>
<script>
  import Gauge from '../echarts_elements/Gauge1'

  export default {
    name : 'First',
    components: {
      Gauge: Gauge,
    },
    data () {
      return {
        gauge1: {
          id : 'gauge1',
          value: 323,
        },
        gauge2: {
          id : 'gauge2',
        },
        gauge3: {
          id : 'gauge3',
        },

      }
    },
  }
</script>
<style>
  .First {
    height: 100%;
  }
  .el-container {
    height: 100%;
    overflow-y: hidden;
  }

  .el-row {
  height: 60%;
  margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
.el-col {
  border-radius: 4px;
  height: 100%;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}


</style>

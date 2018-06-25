<template>
  <el-row>
    <e1-row>
      <el-radio v-model="radio" label="1">加法</el-radio>
      <el-radio v-model="radio" label="2">乘法</el-radio>
    </e1-row>
    <el-row>
      <el-input v-model="input4" placeholder="请输入内容"></el-input>
    </el-row>
    <el-row>
      <el-input v-model="input5" placeholder="请输入内容"></el-input>
    </el-row>
    <el-row>
      <el-input v-model="input2" placeholder="请输入内容"></el-input>
    </el-row>
    <el-row>
      <el-button @click="get()" type="primary">开始</el-button>
    </el-row>
    </el-row>
</template>

<script>
export default {
  data() {
    return {
      radio: '1',
      input4: '',
      input5: '',
      input2: '',
    }
  },
  mounted: function() {
    this.get();
  },
  methods: {
    get(){
      console.log(this.radio);
      if (this.radio == '1') {
        this.$ajax.get('http://127.0.0.1:8000/celery/add',{
            params:{
              num1:this.input4,
              num2:this.input5,
            }
        })
        .then(function (response) {
          console.log(response);
          this.input2 = response.data.res;
        }.bind(this))
        .catch(function (error) {
        });
      } else {
        this.$ajax.get('http://127.0.0.1:8000/celery/mul',{
            params:{
              num1:this.input4,
              num2:this.input5,
            }
        })
        .then(function (response) {
          console.log(response);
          this.input2 = response.data.res;
        }.bind(this))
        .catch(function (error) {
        });
      }
    }
  }
}
</script>

<style>

</style>

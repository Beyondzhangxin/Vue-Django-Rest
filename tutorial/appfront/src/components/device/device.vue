<template>
    <div class="device">
            <el-main>
            <div class="top">

                <el-row>
                    <el-col :span="12"><div class="grid-content">
                        <el-card class="box-card">
<<<<<<< HEAD
                            
=======
>>>>>>> 0474351653d31dc89cf84f915861dab55bd4df18
                            <el-button  id="cirlce" circle>


                            </el-button>
                            <el-button id="cirlce" circle>汇流箱</el-button>
                            <el-button id="cirlce" circle>采集设备</el-button>

                        </el-card>
                   
                        
                    </div></el-col>

                    <el-col :span="12"><div class="grid-content">
                        <el-card class="box-card">
                        
                        </el-card>
                        
                     
            
                        
                    </div></el-col>
                </el-row>
            </div>
            </el-main>

            <el-main>
            <div class="mid">
                <div id="content">
                    <el-button round>逆变器</el-button>
                    <el-button round>汇流箱</el-button>
                    <el-button round>采集设备</el-button>
                </div>
            </div>
            </el-main>

        <el-container>
            <div class="foot">
                <div class="rowm">
                <!--通用list-->
                <!--请求如下 http://127.0.0.1:8000/pv/get/detection/2018/1/18/ -->
                <div class="rowmb">
                <!--赋值到this.data中 -->
                <ComList v-bind:data='data'></ComList>
                <!--<ComList v-bind:data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></ComList>-->
                <el-pagination
                    background
                    layout="prev, pager, next"
                    :total="1000"
                    @current-change="handleCurrentChange">
                </el-pagination>
                </div>
                </div>
            </div>
        </el-container>
    </div>     
</template>


<script>

import ComList from '../el-simple-com/com-list.vue'

export default {
    name:'device',

    components: {
        ComList: ComList,
     },

    data(){
      return {
        data: 'http://127.0.0.1:8000/pv/get/detection/2018/1/18/',
        page: 2,
        // pageSize: 2
      }
    },
    methods: {
      handleCurrentChange(val) {
        this.data = 'http://127.0.0.1:8000/pv/get/detection/2018/1/18/' + '?page='+ val;
        console.log(this.data);
      }
    },
    mounted: function() {
      this.$store.commit('showIt')
    },

    destroyed: function() {
      this.$store.commit('hideIt')
    },

}
</script>



<style>

.rowm{
  height: 400px;
  margin: auto;
}

.rowmb{
  height: 450px;
  background: #fff;
  float: left;
  position: relative;
  left: 5px;
  overflow: hidden;
  box-shadow: 0px 0px 10px 3px #9eabad;
}

.top{
    margin-bottom: 20px;
    background: #ffffff;
    height:200px;
    box-shadow: 0px 0px 10px 3px #9eabad;
}

.mid{
    margin-bottom:20px;
    background: #ffffff;
    height:80px;
    box-shadow: 0px 0px 10px 3px #9eabad;
}

#content{
    float:left;
    margin-top:20px;
}

.box-card{
    height:200px;
}

</style>

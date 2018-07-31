<template>
    <div class="device">
            <el-main>
            <div class="top">
                <el-row>
                    <el-col :span="12"><div class="grid-content">
                        <el-card class="box-card">
                            <div id="circle clearfix">
                                <el-row :gutter="20">
                                    <el-col :span="8"><div class="grid-content">
                                        <el-button  id="cirlce" round>
                                            <div class="text">当前功率：</div>
                                            <div class="text">{{msg1}}</div>
                                            <div class="text">KW</div>
                                        </el-button>

                                    </div></el-col>
                                    <el-col :span="8"><div class="grid-content">
                                        <el-button id="cirlce" round>
                                            <div class="text">今日发电：</div>
                                            <div class="text">{{msg2}}</div>
                                            <div class="text">KWh</div>
                                        </el-button>
                                    </div></el-col>
                                    <el-col :span="8"><div class="grid-content">
                                        <el-button id="cirlce" round>
                                            <div class="text">累计发电：</div>
                                            <div class="text">{{msg3}}</div>
                                            <div class="text">万KWh</div>
                                        </el-button>
                                    </div></el-col>
                                </el-row>
                            </div>

                            <div id="num">
                                <el-row :gutter="20">
                                    <el-col :span="8"><div class="grid-content">装机容量：{{msg4}} KWP</div></el-col>
                                    <el-col :span="8"><div class="grid-content">今日等效：{{msg5}} h</div></el-col>
                                    <el-col :span="8"><div class="grid-content">并网日期：2017-12-11</div></el-col>
                                </el-row>
                            </div>
                        </el-card>

                    </div></el-col>

                    <el-col :span="12"><div class="grid-content">
                        <el-card class="box-card">
                            <div class="inverter">
                                <el-row :gutter="20">
                                    <el-col :span="6"><div class="grid-content">
                                        <img src="../../assets/inverter.png" id="image1">
                                    </div></el-col>
                                    <el-col :span="6"><div class="grid-content1">
                                        <div id="text1">逆变器{{msg6}}台</div>
                                    </div></el-col>
                                    <el-col :span="12"><div class="grid-content"></div></el-col>
                                </el-row>

                            <el-row id="str">
                                <el-col :span="2"><div class="grid-content">
                                    <img src="../../assets/normal.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">{{msg7}}</div>
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                     <img src="../../assets/offline2.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">{{msg7}}</div>
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <img src="../../assets/alarm1.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">{{msg7}}</div>
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <img src="../../assets/close1.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">{{msg7}}</div>
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <img src="../../assets/repair.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">{{msg7}}</div>
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                     <img src="../../assets/offline1.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">{{msg7}}</div>
                                </div></el-col>
                            </el-row>
                            </div>
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
                <ComList v-bind="list"></ComList>
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

import ComList from '../el-simple-com/com-list0.vue'

export default {
    name:'device',

    components: {
        ComList: ComList,
     },

    data(){
      return {
        list: {
          //改数据改这里
          data: 'http://127.0.0.1:8000/pv/get/detection/2018/1/18/',
          //改表名改这里
          tabConfigs: [
            {prop: 'dev_name', label: '设备名称'},
            {prop: 'dev_scc', label: '设备厂家'},
            {prop: 'dev_xh', label: '设备型号'},
            {prop: 'dev_cjdz', label: '采集地址码'},
            {prop: 'dev_jrrl', label: '接入容量(kWp)'},
            {prop: 'dev_dqgl', label: '当前功率(W)'},
            {prop: 'dev_jrfd', label: '今日发电量(kWh)'},
            {prop: 'dev_drdx', label: '当日等效小时(h)'},
          ],
        },
        page: 2,
        // pageSize: 2
        msg1:23.93,
        msg2:3019.32,
        msg3:34.43,
        msg4:623.16,
        msg5:4.85,
        msg6:15,
        msg7:0
      }
    },
    methods: {
      handleCurrentChange(val) {
        //改分页
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



<style scope>
.el-main{
  overflow-x: hidden;
}

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
    position: relative;
    left: 5px;
}

.mid{
    margin-bottom:20px;
    background: #ffffff;
    height:80px;
    box-shadow: 0px 0px 10px 3px #9eabad;
    position: relative;
    left: 5px;
}

#content{
    float:left;
    margin-top:20px;
}

.box-card{
    height:200px;
}

.clearfix:after{
  content: "020";
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}

.clearfix {
  /* 触发 hasLayout */
  zoom: 1;
}

#num{
    margin-top:20px;
}

#text1{
    margin-top:18px;
    margin-left:-80px;
}

#text2{
    margin-top:5px;
    margin-left:-20px;
}

#str{
    margin-top:10px;
}
</style>

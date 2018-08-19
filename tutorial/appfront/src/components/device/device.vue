<template>
          <div class="device">

                <el-row class="row1">
                    <el-col :span="12">
                      <div class="grid-content">
                        <el-card class="box-card">
                            <div>
                                <el-row :gutter="15">
                                    <el-col :span="8">
                                      <div class="grid-content">
                                        <el-button  id="cirlce" round>
                                            <div class="text">当前功率：<strong>{{dqgl||0}}</strong></div>
                                            <div class="text">KW</div>
                                        </el-button>
                                      </div>
                                    </el-col>
                                    <el-col :span="8"><div class="grid-content">
                                        <el-button id="cirlce" round>
                                            <div class="text">今日发电：<strong>{{jrfd}}</strong></div>
                                            <div class="text">KWh</div>
                                        </el-button>
                                    </div></el-col>
                                    <el-col :span="8"><div class="grid-content">
                                        <el-button id="cirlce" round>
                                            <div class="text">累计发电：<strong>{{ljfd}}</strong></div>
                                            <div class="text">万KWh</div>
                                        </el-button>
                                    </div></el-col>
                                </el-row>
                            </div>
                            <div id="num">
                                <el-row :gutter="20">
                                    <el-col :span="8"><div class="grid-content1">装机容量：<strong>{{zjrl}}</strong> KWP</div></el-col>
                                    <el-col :span="8"><div class="grid-content1">今日等效：<strong>{{jrdx}}</strong> h</div></el-col>
                                    <el-col :span="8"><div class="grid-content1">并网日期：<strong>{{bwrq}}</strong></div></el-col>
                                </el-row>
                            </div>
                        </el-card>
                      </div>
                    </el-col>

                    <el-col :span="12">
                        <el-card class="box-card">
                            <div class="inverter">
                                <el-row :gutter="20">
                                    <el-col :span="6"><div class="grid-content">
                                        <img src="../../assets/inverter.png" id="image1">
                                    </div></el-col>
                                    <el-col :span="6"><div class="grid-content1">
                                        <div id="text1">逆变器<strong>{{msg6}}</strong>台</div>
                                    </div></el-col>
                                    <el-col :span="12"><div class="grid-content"></div></el-col>
                                </el-row>

                            <el-row id="str">
                                <el-col :span="2"><div class="grid-content">
                                    <img src="../../assets/normal.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">1</div>
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
                                    <div id="text2">4</div>
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <img src="../../assets/close1.png" id="image2">
                                </div></el-col>
                                <el-col :span="2"><div class="grid-content">
                                    <div id="text2">14</div>
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
                    </el-col>
                </el-row>

                <el-row>
                    <el-card class="box-card1">
                    <el-row>
                    <el-col :span="1" class="col1">
                      <el-button round id="text3" @click="type='NBQ'"><strong>逆变器</strong></el-button>
                    </el-col>
                    <el-col :span="1" class="col1">
                      <el-button  round id="text3" @click="type='HLX'"><strong>汇流箱</strong></el-button>
                    </el-col>
                    <el-col :span="1" class="col1">
                      <el-button  round id="text3" @click="type='CJSB'"><strong>采集设备</strong></el-button>
                    </el-col>
                    </el-row>
                    </el-card>
                </el-row>

            <el-card class="card0">
            <!-- <el-card class="box-card2"> -->
              <!--通用list-->
              <!--请求如下 http://127.0.0.1:8000/pv/get/detection/2018/1/18/ -->

              <!--赋值到this.data中 -->
              <ComList v-bind="list"></ComList>
              <!-- <ComList v-bind:data='http://127.0.0.1:8000/pv/get/detection/2018/1/18/'></ComList> -->
              <!-- <el-pagination
                  background
                  layout="prev, pager, next"
                  :total="1000"
                  @current-change="handleCurrentChange"> -->
              <!-- </el-pagination> -->
            <!-- </el-card> -->
             <el-pagination
                  background
                  layout="prev, pager, next"
                  :total="190"
                  @current-change="handleCurrentChange">
            </el-pagination>
            </el-card>


    </div>
</template>

<script>
import ComList from '../el-simple-com/com-list0.vue'


export default {
    name:'device',
    components: {
      ComList: ComList,
    },
    watch: {
      type: function(val, oldval) {
        if (val != 'NBQ') {
          this.list.data = '';
        }else {
          this.list.data = 'http://localhost:8000/system/getDeviceTable?pageNum=1&pageSize=5';
        }
      }
    },
    data(){
      return {
        type: 'NBQ',
        list: {
          //改数据改这里
          data: 'http://localhost:8000/system/getDeviceTable?pageNum=1&pageSize=5',
          //改表名改这里
          tabConfigs: [
            {prop: 'dev_name', label: '设备名称'},
            {prop: 'dev_xh', label: '设备型号'},
            {prop: 'dev_systemType', label: '系统类型'},
            {prop: 'dev_systemName', label: '系统名称'},
            {prop: 'dev_dqgl', label: '当前功率(W)'},
            {prop: 'dev_jrfd', label: '今日发电量(kWh)'},
            {prop: 'dev_drdx', label: '当日等效小时(h)'},
          ],
        },
        page: 2,
        // pageSize: 2
        dqgl:23.93,
        jrfd:3019.32,
        ljfd:34.43,
        zjrl:623.16,
        jrdx:4.85,
        msg6:19,
        msg7:0,
        bwrq:'2017-12-11',
      }
    },
    methods: {
      loadData(){
        this.$ajax.get('http://localhost:8000/system/getDeviceMonitor?systemType=PVMG&deviceName=NBQGL1')
        .then(function (response) {
          //处理数据
          this.bwrq = response.data.data.bwrq
          this.dqgl = response.data.data.dqgl
          this.jrfd = response.data.data.jrfd
          this.zjrl = response.data.data.zjrl
          this.jrdx = response.data.data.jrdx
          //{"bwrq": "2018-03-21", "ljfd": "5346.532596464663", "zjrl": 50.0, "dqgl": null, "jrdx": 0, "jrfd": 0.0}
        }.bind(this))
        .catch(function (error) {
          return 0;
        });
      },
      handleCurrentChange(val) {
        //改分页
        this.list.data = 'http://localhost:8000/system/getDeviceTable?pageNum='+ val +'&pageSize=5';

      },
    },
    mounted: function() {
      this.$store.commit('showIt');
      this.$store.commit('filter', '逆变器');
      this.loadData();
    },
    beforeUpdate: function() {

    },
    destroyed: function() {
      this.$store.commit('hideIt');
    },
}
</script>



<style scope>


.row1 {
  width: 100%;
  height: 300px;
}

/* .container{
  margin-top: 30px;
  padding-left: 15px;
  padding-right: 15px;
  overflow: auto;
} */


#image1 {
  position: relative;
  left: -30%;
  top: -8px;
}

.col1 {
  padding: 10px;
  margin-right: 80px;
}

.el-pagination {
  position: relative;
  left:0%;

}

.el-main{
  overflow-x: hidden;
}

#foo{
    width:100%;
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

}

.top {
    margin-bottom: 20px;
    background: #ffffff;
    height:200px;
    box-shadow: 0px 0px 10px 3px #9eabad;
    position: relative;
    left: 5px;
}

.mid {
    margin-bottom:20px;
    background: #ffffff;
    height:80px;
    box-shadow: 0px 0px 10px 3px #9eabad;
    position: relative;
    left: 5px;
}

.foot {
  box-shadow: 0px 0px 10px 3px #9eabad;
  height: 450px;
  position: relative;
  left: 5px;
}



.box-card{
    height:200px;
    padding: 20px;
    margin-bottom: 30px;
    margin-top: 40px;
    margin-left: 20px;
    margin-right: 20px;
     /* background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.3),#355C7D);*/
   background-color:rgba(180, 180, 180, 0.1);

}

.box-card:hover{
   background-color:rgba(53,92,125, 0.1);
}

.box-card1 {
  margin-bottom: 30px;
  margin-top:-20px;
   margin-left: 20px;
    margin-right: 20px;
   /* background: -webkit-linear-gradient(30deg, #373B44,#355C7D);
    background: -o-linear-gradient(30deg, #373B44, #355C7D);
    background: -moz-linear-gradient(30deg, #373B44, #355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.5),#355C7D); */
    background-color:rgba(180, 180, 180, 0.1);
}

.box-card1:hover{
    background-color:rgba(53,92,125, 0.1);
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

#cirlce {
  margin-top: -8px;
  width: 100%;
  background-color:rgba(223, 232, 235, 0.3);
}


#num{
    margin-top:20px;
}


#text1{
    margin-top:20px;
    margin-left: -110%;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size:16px;
}

#text2{
    margin-top:5px;
    margin-left:-20px;
}

#str{
    margin-top:10px;
}

#text3{
    font-size: 16px;
    background-color:rgba(255, 255, 255, 0.3);
    font-family: "PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}

.grid-content1{
    font-size: 16px;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    /* color: #909399; */
    position: relative;
    top: -2px;
    left: 1px;
}

.text{
    /* color: #909399; */
    font-size: 14px;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    padding-top: 13px;
    padding-bottom: 13px;
}

.card0{
    background: -webkit-linear-gradient(30deg, rgb(180,180,180,0.2),rgb(53,92,125,0.1));
    background: -o-linear-gradient(30deg, rgb(180,180,180,0.2),rgb(53,92,125,0.1));
    background: -moz-linear-gradient(30deg, rgb(180,180,180,0.2),rgb(53,92,125,0.1));
    background: linear-gradient(30deg, rgb(180,180,180,0.2),rgb(53,92,125,0.1));
    /* height:100%; */
}

.device{
    background: -webkit-linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
    background: -o-linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
    background: -moz-linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
    background: linear-gradient(30deg, rgb(180,180,180,0.2),#355C7D);
    margin-top:-12px;
    width:100%;
    height: 100%;
    margin-left:-13px;
}

</style>

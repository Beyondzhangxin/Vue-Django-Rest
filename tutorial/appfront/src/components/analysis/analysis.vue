<template>
    <div class="analysis">
        <!-- header -->
        <el-header id="header">
            <el-row>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/station.png" id="image">
                        <span id="text">电站对比</span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/self.png" id="image">
                        <span id="text">设备对比</span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/equipment.png" id="image">
                        <span id="text">自身对比</span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content"></div></el-col>
            </el-row>
        </el-header>
        <!-- main1 -->
        <el-main id="main1">
            <el-row>
                <el-col :span="12" id="span1">
                        <el-col :span="4" id="span0">对比内容:</el-col>
                        <el-col :span="4">
                            <el-button id="button1">功率</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button1">效率</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button1">等效时数</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button1">符合率</el-button>
                        </el-col>
                        <el-col :span="4">
                            <el-button id="button1">发电量</el-button>
                        </el-col>                
                </el-col>
                <el-col :span="12" id="span2">
                    <span id="text1">查询日期</span>
                  <!-- 日期选择器 -->
                        <span class="demonstration"></span>
                        <el-date-picker
                            v-model="value2"
                            align="right"
                            type="date"
                            placeholder="选择日期"
                            :picker-options="pickerOptions1">
                        </el-date-picker>                         
               </el-col>
            </el-row>
        </el-main>
        <!-- main2 -->
        <el-main id="main2">
            <el-row>
                <el-col :span="24">
                    <div class="text2">已选电站：</div>
                </el-col>
            </el-row>
            <div class="sel">
                <el-button type="primary" plain>北京光伏电站</el-button>
                <el-button type="primary" plain>上海光伏电站</el-button>
            </div>

        </el-main>

        <!-- main3 -->
        <el-main id="main3">
            功率图表


        </el-main>
        </div>
</template>



<script>


export default {
    name: 'analysis',
    data() {
      return {
        pickerOptions1: {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        },
        value1: '',
        value2: '',
      };
    },

    mounted: function() {
      this.$store.commit('showIt');
    },
    destroyed: function() {
      this.$store.commit('hideIt')
    },
}


</script>


<style scope>
#header{
    background:white;
    height:100px;
}

#button1{
    margin-top:5px;
}

#text{
   padding-bottom:2px;
   display: block;
}

#span1{
    background:white;
}

#span2{
    background:white;
}

#span0{
    margin-top:8px;
}

#main1{
    margin-top:20px;
}

#main2{
    background:white;
}
#text1{
    padding-right:20px;
}

.text2{
    float: left;
    margin-top:20px;
    margin-left:30px;
}

.sel{
    float:left;
    margin-top:20px;
    margin-left:30px;
    margin-bottom: 10px;
}
</style>

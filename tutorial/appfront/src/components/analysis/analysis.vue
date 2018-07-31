<template>
    <div class="analysis">
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

        <el-main>
            <el-row>
                <el-col :span="12"><div class="grid-content">
                    <el-row>
                        <el-col :span="4"><div class="grid-content">对比内容:</div></el-col>
                        <el-col :span="4"><div class="grid-content">
                            <el-button>功率</el-button>
                        </div></el-col>
                        <el-col :span="4"><div class="grid-content">
                            <el-button>效率</el-button>
                        </div></el-col>
                        <el-col :span="4"><div class="grid-content">
                            <el-button>等效时数</el-button>
                        </div></el-col>
                        <el-col :span="4"><div class="grid-content">
                            <el-button>符合率</el-button>
                        </div></el-col>
                        <el-col :span="4"><div class="grid-content">
                            <el-button>发电量</el-button>
                        </div></el-col>
                    </el-row>
                </div></el-col>
                <el-col :span="12"><div class="grid-content">
                    <span id="text1">查询时间</span>
                    <div class="block">
                        <span class="demonstration"></span>
                        <el-date-picker
                            v-model="value2"
                            align="right"
                            type="date"
                            placeholder="选择日期"
                            :picker-options="pickerOptions1">
                        </el-date-picker>
                    </div>
                    
                </div></el-col>
            </el-row>


        </el-main>

        <el-main>



        </el-main>

        <el-main>



        </el-main>
        </div>
</template>



<script>


export default {
    name: 'analysis',

    data(){
        return{
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

#button{
    /* margin-top:8px; */
}

#text{
   padding-bottom:2px;
   display: block;
}
</style>

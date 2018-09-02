<template>
  <div class="Gmm">
    <!-- 配置参数 -->
    <div class="text0">GMM参数配置</div>
    <!-- 分割线 -->
    <hr width=100% size=1 color=#bbbcbc style="FILTER: alpha(opacity=100,finishopacity=0)">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="ruleForm">
      <el-card class="card0">
        <el-form-item label="训练目标" style=font-weight:bold prop="system">
          <el-select v-on:change="indexSelect()" v-model="ruleForm.system" clearable placeholder="选择训练系统">
            <el-option
              v-for="item in options1"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="概率模型" style=font-weight:bold prop="options">
          <el-select v-model="ruleForm.options" clearable placeholder="选择概率模型">
            <el-option
              v-for="item in options2"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>

        </el-form-item>
        <el-form-item label="时间选择" style=font-weight:bold required>
          <el-col :span="11">
            <el-form-item prop="start_time">
              <el-date-picker
                v-model="ruleForm.start_time"
                type="datetime"
                value-format="yyyy-MM-dd HH:mm:ss"
                placeholder="选择日期时间"
                default-time="12:00:00">
              </el-date-picker>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            至
          </el-col>
          <el-col :span="11">
            <el-form-item prop="end_time">
              <el-date-picke
                v-model="ruleForm.end_time"
                type="datetime"
                value-format="yyyy-MM-dd HH:mm:ss"
                placeholder="选择日期时间"
                default-time="12:00:00">
              </el-date-picke>
            </el-form-item>
          </el-col>
        </el-form-item>
      </el-card>

      <el-card class="card2">
        <el-row :gutter="20">
          <el-form-item label="训练参数" style="font-weight:bold" prop="j">
            <el-input
              class="xlcs"
              placeholder="输入高斯个数"
              v-model.number="ruleForm.j"
              auto-complete="off"
              clearable>
            </el-input>
          </el-form-item>

          <el-form-item label="建模算法" style=font-weight:bold prop="method">
            <el-select v-model="ruleForm.method"
                       clearable
                       @change="sendNoticeMessage(ruleForm.method)"
                       placeholder="选择算法">
              <el-option
                v-for="item in options3"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="变量选择" style=font-weight:bold prop="varables">
            <el-select v-model="ruleForm.varables" multiple
                       placeholder="选择变量">
              <el-option
                v-for="item in options4"
                :key="item.pk"
                :label="item.fields.paramname"
                :value="item.fields.systemtype">
              </el-option>
            </el-select>
          </el-form-item>
        </el-row>
      </el-card>
      <el-card class="card3" v-show="ruleForm.options == 'conditional'">
        <el-form-item label="选择输入" style=font-weight:bold prop="y">
          <el-table :data="ruleForm.y" border class="tjfb">
            <el-table-column
              prop="var"
              label="变量"
              header-align="center"
              width="250px">
            </el-table-column>
            <el-table-column
              property="value"
              label="条件分布给定值"
              border
              width="250px">
              <template slot-scope="scope">
                <el-input v-model="scope.row.value" placeholder="请输入内容"></el-input>
              </template>
            </el-table-column>
          </el-table>
        </el-form-item>
      </el-card>

      <el-card class="card3">
        <div class="text" v-show="ruleForm.method == 'MAP'">此处为MAP方法必填的选项</div>
        <el-form-item label="选择输入" prop="y_hyper" style=font-weight:bold v-show="ruleForm.method == 'MAP'">
          <el-select v-model="ruleForm.y_hyper.system" clearable placeholder="系统">
            <el-option
              v-for="item in options1"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
          <el-date-picker
            v-model="ruleForm.y_hyper.start_time"
            type="datetime"
            placeholder="选择开始时间">
          </el-date-picker>
          <el-date-picker
            v-model="ruleForm.y_hyper.end_time"
            type="datetime"
            placeholder="选择结束时间">
          </el-date-picker>

        </el-form-item>
        <el-form-item label="选择输入" prop="period" style=font-weight:bold v-show="ruleForm.method == 'MAP'">
          <el-input
            class="period"
            placeholder="输入period"
            v-model.number="ruleForm.period"
            auto-complete="off"
            clearable>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-card>
    </el-form>

  </div>
</template>


<script>

  import API from '../../api/api_tasks';

  const cityOptions = ['类别1', '类别2', '类别3',];
  export default {
    name: 'Gmm',
    componets: {},
    data() {
      //处理错误
      var checkPeriod = (rule, value, callback) => {
        if (this.ruleForm.method != "MAP") {
          callback();
        }
        if (typeof(value) != "number") {
          callback(new Error('请输入数字'));
        }
        callback();
      };
      var checkY = (rule, value, callback) => {
        if (this.ruleForm.options != 'conditional') {
          callback();
        }
        if (value.length == 0) {
          callback(new Error('请选择变量'));
        }
        callback();
      };
      var checkVarables = (rule, value, callback) => {
        if (value.length == 0) {
          callback(new Error('请输入变量'));
        }
        if (value === '') {
          callback(new Error('请输入变量'));
        } else {
          if (this.ruleForm.varables !== '') {
            if (this.ruleForm.options == 'marginal') {
              if (value.length > 1) {
                callback(new Error('在marginal模型下只能有一个变量'));
              }
            }
          }
          callback();
        }
      };
      var checkY_hyper = (rule, value, callback) => {
        if (this.ruleForm.method != "MAP") {
          callback()
        }

        Object.keys(value).forEach(function (key) {
          if (value[key] === "") {
            console.log(value[key]);
            callback(new Error('特征未描述完整'))
          }
        });
        callback();
      }
      return {
        ruleForm: {
          system: "",
          options: "",
          start_time: "",
          end_time: "",
          j: "",
          method: "",
          varables: [],
          y: [],
          period: null,
          y_hyper: {
            system: "",
            start_time: "",
            end_time: "",
          },
        },
        rules: {
          system: [
            {required: true, message: '请选择活动区域', trigger: 'change'}
          ],
          options: [
            {required: true, message: '请选择建立的概率模型', trigger: 'change'}
          ],
          start_time: [
            {type: 'string', required: true, message: '请选择初始时间', trigger: 'change'}
          ],
          end_time: [
            {type: 'string', required: true, message: '请选择结束时间', trigger: 'change'}
          ],
          j: [
            {required: true, message: '高斯个数不能为空', trigger: 'blur'},
            {type: 'number', message: '高斯个数必须为数字值', trigger: 'blur'}
          ],
          method: [
            {required: true, message: '请选择算法', trigger: 'change'}
          ],
          varables: [
            {type: 'array', required: true, validator: checkVarables, trigger: 'change'}
          ],
          y: [
            {type: 'array', validator: checkY, required: true}
          ],
          period: [
            {type: 'number', validator: checkPeriod, required: true}
          ],
          y_hyper: [
            {validator: checkY_hyper, required: true}
          ],
        },

        mult: new Boolean(1),

        //建模功能需要的功能
        timeRange: [],
        input0: "",
        input1: "",
        options1: [{
          value: 'SPGS',
          label: '图书馆微电网系统',
        },
          {
            value: 'PVMG',
            label: '多功能光伏电站系统',
          }
        ],
        value1: '',

        options2: [{
          value: 'marginal',
          label: 'marginal',
        },
          {
            value: 'joint',
            label: 'joint',
          },
          {
            value: 'conditional',
            label: 'conditional',
          }
        ],
        value2: '',

        options3: [{
          value: 'EM',
          label: 'EM',
        },
          {
            value: 'MAP',
            label: 'MAP',
          }],
        value3: '',

        options4: [],
        value4: '',
        value5: '',
        startTime: '',
        endTime: '',
        B: 'test',
        tableData: [],

      }
    },
    methods: {
      indexSelect: function () {
        var systemType = this.ruleForm.system;
        API.getSystemVariables({"systemType": systemType}).then(data => {
          this.options4 = JSON.parse(data.data);
          console.log(this.options4);
        });
      }
    },
    updateVarible(val) {
      this.ruleForm.y = []
      for (var i = 0; i < val.length; i++) {
        this.ruleForm.y.push({
          var: val[i],
          value: '0',
        })
      }
    }
    ,
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.saveModel();
        } else {
          console.log('没有传输成功!!');
          return false;
        }
      });
    }
    ,

    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
    ,

    chooseModel(val) {
      console.log(this.value4)
      if (val == 'marginal') {
        this.mult = new Boolean(0);
      }
      if (val != 'marginal') {
        this.mult = new Boolean(1);
      }
    }
    ,

    sendNoticeMessage(val) {
      if (val == 'MAP') {
        const h = this.$createElement;
        this.$notify({
          title: '使用MAP函数的提示',
          message: h('i', {style: 'color: teal'}, '前提：对要刻画的随机变量有了深入的认识 方案：输入超参训练集，自动归纳超参数')
        });
      }
    }
    ,

    saveModel() {
      this.$prompt('请输入保存模型名称（四字以上）', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        //支持汉字和英文
        inputPattern: /^[\u4E00-\u9FA5A-Za-z0-9]{4,}$/,
        inputErrorMessage: '模型名称不正确'
      }).then(({value}) => {
        this.ruleForm.name = value
        this.$message({
          type: 'success',
          message: '模型名称是: ' + value
        });
        //发送POST请求
        this.$router.push('/calculation')
        this.postDSTConfig('http://127.0.0.1:8000/GMM/model/distribution/')
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        });
      });
    }
    ,

    postDSTConfig(url) {
      var instance = this.$ajax.create({
        headers: {'Content-Type': 'application/json'}
      });
      this.ruleForm.varables = JSON.stringify(this.ruleForm.varables)
      this.ruleForm.y = JSON.stringify(this.ruleForm.y)
      this.ruleForm.y_hyper = JSON.stringify(this.ruleForm.y_hyper)
      instance.post(url, this.ruleForm)
        .then(function (response) {
          //处理数据
          console.log(response)
        }.bind(this))
        .catch(function (error) {
          return 0;
        });
    }
    ,
    handleCheckAllChange(val) {
      this.checkedCities = val ? cityOptions : [];
      this.isIndeterminate = false;
    }
    ,
    handleCheckedCitiesChange(value) {
      let checkedCount = value.length;
      this.checkAll = checkedCount === this.cities.length;
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.cities.length;
    }
    ,

  }


</script>


<style scoped>
  .Gmm {
    height: 100%;
    margin-left: -12px;
    margin-top: -12px;
  }

  .text0 {
    font-weight: bold;
    padding-top: 15px;
    margin-left: 80px;
    font-size: 20px;
    font-family: "Microsoft YaHei"
  }

  .text1 {
    float: left;
    margin-top: 50px;
    margin-right: 20px;
  }

  .clear {
    clear: both;
  }

  .el-table {
    overflow-x: hidden;
  }

  .mid {
    float: left;
    margin-left: 60px;
  }

  /* .fenye{
      float:left;
      margin-left:50px;
      margin-top:50px;
  } */
  .card1 {
    margin-top: 10px;
    margin-bottom: 20px;
    background-color: rgba(255, 255, 255, 0.1);
    /* box-shadow: 10px 5px 20px #888888; */
  }

  .card1:hover {
    background-color: rgba(53, 92, 125, 0.1);
  }

  .card3 {
    margin-top: 20px;
    margin-bottom: 10px;
    background-color: rgba(255, 255, 255, 0.2);
    /* box-shadow: 10px 5px 20px #888888; */
  }

  .card2 {
    background-color: rgba(255, 255, 255, 0.2);
    /* box-shadow: 10px 5px 20px #888888; */
  }

  .card2:hover {
    background-color: rgba(53, 92, 125, 0.1);
  }

  .card3:hover {
    background-color: rgba(53, 92, 125, 0.1);
  }

  .xlcs {
    width: 12.3%;
  }

  .period {
    width: 12.5%
  }

  .tjfb {
    width: 40%;
    margin-left: auto;
    margin-right: auto;
  }

</style>

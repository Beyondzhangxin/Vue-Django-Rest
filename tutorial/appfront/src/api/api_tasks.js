/**
 * Created by user on 2018/8/5.
 */
import * as API from './'


export default {

  getPowerStations: params => {
    let config = {
      headers: {
        "Content-Type": "application/json;charset=utf-8"
      }
    }
    return API.GET('/system/powerStations', params, config);
  },

  getSystemVariables: params => {
    let config = {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
      },
    };
    API.GET('/system/getAllParamsBySystemType', params, config).then(data=>{
      return data;
    });
  }

}


Date.prototype.Format = function (fmt) {
  var o = {
    "M+": this.getMonth() + 1, //月份
    "d+": this.getDate(), //日
    "h+": this.getHours(), //小时
    "m+": this.getMinutes(), //分
    "s+": this.getSeconds(), //秒
    "q+": Math.floor((this.getMonth() + 3) / 3), //季度
    "S": this.getMilliseconds() //毫秒
  };
  if (/(y+)/.test(fmt))
    fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
  for (var k in o)
    if (new RegExp("(" + k + ")").test(fmt))
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
  return fmt;
}



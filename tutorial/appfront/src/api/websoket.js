/**
 * Created by user on 2018/7/27.
 */
import Env from './env'
threadPoxi()
{
  const agentData = "mymessage";
  if (
    this.websock !== undefined &&
    this.websock.readyState === this.websock.OPEN
  ) {
    this.websocketsend(agentData);
  } else if (
    this.websock !== undefined &&
    this.websock.readyState === this.websock.CONNECTING
  ) {
    let that = this; //保存当前对象this
    setTimeout(function () {
      that.websocketsend(agentData);
    }, 300);
  } else {
    // 若未开启 ，则等待500毫秒
    this.websock = this.initWebSocket("chat/rt_queue");
    let that = this; //保存当前对象this
    setTimeout(function () {
      let message = {type: "connect", message: "testconnect", queue: []};
      that.websocketsend(JSON.stringify(message));
    }, 500);
  }
}
initWebSocket(msg)
{
  //ws地址
  // const wsuri = 'ws://'+ location.host + "/"+msg;
  try {
    const wsuri = Env.ws + "/" + msg;
    let websock = new WebSocket(wsuri);
    websock.onmessage = this.websocketonmessage;
    websock.onclose = this.websocketclose;
    this.connectTimer = null;
    return websock;
  } catch (error) {
    console.log('连接错误')
    this.try_to_reconnect();

  }
}

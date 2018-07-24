<template>
  <div class="Power">
    <div id="pheader">
      <div id="">123</div>
      <div id="">213</div>
    </div>
    <div id="pmain"></div>
  </div>
</template>
<script>
import Gauge from '../echarts_elements/Gauge1'
import Line2 from '../echarts_elements/Line2'


export default {
  name : 'Power',
  components: {
  },
  data () {
    return {
      msg: "Hello world"
    }
  }
}
</script>
<style scoped>
  .Power {
    height: 100%;
    width: 100%;
  },
  #pheader {
    height: 100px;
  },
  #pheader div{
    margin: 0 auto;
    padding: 6px 0 8px;
    float: left;
  },
  #pmain{
    height: 400px;
    background-color: white;
  }
</style>

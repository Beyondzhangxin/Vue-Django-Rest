<template>
	<div class="effect">
        <div class="login">
          <el-form>
    	      <input></input>
            <p></p>
            <input></input>
          </el-form>



        </div>
    <!-- 调用canvas -->
      <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas>
 
	</div>
</template>


<script>
import myCanvas from 'vue-atom-canvas'
export default {
  name: 'effect',
  components: {
    myCanvas
  },
  data () {
    return {
      dotsNum: 60,
    
    }
  }
}
</script>


<style>

.effect{

}
</style>

<template>
	<diV class="effect">
      <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas>
      123456
	</diV>
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

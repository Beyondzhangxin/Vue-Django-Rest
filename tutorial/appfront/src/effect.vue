<template>
	<diV class="effect">
      <myCanvas :dotsNum="dotsNum" :isColor="false"></myCanvas>
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


<style scoped>

</style>

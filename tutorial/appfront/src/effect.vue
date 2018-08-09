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
      msg: 'Welcome to Your Vue.js App',
      dotsNum: 60,
      roundColor: "red",
      lineColor: ""
    }
  }
}
</script>


<style scoped>

</style>

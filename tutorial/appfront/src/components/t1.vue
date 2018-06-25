<template>
  <div class="snippet">
    <simpleComponent></simpleComponent>
  </div>
</template>

<script>
import HelloWorld from './HelloWorld.vue'

export default {
  name: 't1',
  components: {
    simpleComponent: HelloWorld
  }
}
</script>
<style>

</style>

<template>
  <div class="snippet">
    <simpleComponent></simpleComponent>
    <router-link to="newcontact"><h1>{{ msg }}</h1></router-link>
  </div>
</template>

<script>
import SimpleList from './el-simple-com/SimpleList.vue'

export default {
  name: 'snippet',
  components: {
    simpleComponent: SimpleList
  },
   data () {
    return {
      msg: 'wanghongtao'
    }
  }
}
</script>
<style>


</style>

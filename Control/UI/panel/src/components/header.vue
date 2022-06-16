<template>
<el-row class="row" :gutter="20"  type="flex" justify="space-around" align="middle">
  <el-col  :span="4" :offset="0" >   
      <el-switch rowitem v-model="h_isCollapse" />
  </el-col>
  <el-col :span="10"  :offset="10" >   
  <div class="rowitem timebox">
  <el-select v-model="timeSpeedValue" class="m-2" placeholder="Select">
    <el-option
      v-for="item in timeSpeedOptions"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    />
  </el-select>
  <el-button type="primary" plain>调节</el-button>
  <el-button type="info" plain>暂停</el-button>
  </div>
  </el-col>
</el-row>

</template>

<script lang="ts" setup>

</script>

<script lang="ts">
import { defineComponent} from 'vue';

let timer:any;
export default defineComponent({
  props:{ 'h_isCollapse':Boolean, },
  data(){
      return {
        session:'',
        timeSpeedValue:1,
        timeSpeedOptions:[
          {label:"1x:1秒->1秒",value:1},
          {label:"60x:1秒->1分",value:60},
          {label:"3600x:1秒->1时",value:3600},
          {label:"86400x:1秒->1天",value:86400},
        ],
    }
  },
  mounted(){
      console.log("header mounted")
      this.session = this.$cookies.get("session")
      if(this.session=="") this.$router.push("/login")
      timer = setInterval(() => {
        // console.log("开始---");
      }, 1000);
  },
  destroyed(){
      clearInterval(timer)
  },
  method:{
  }
})
</script>
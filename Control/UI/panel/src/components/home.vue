<template>
<el-container>
<el-header class="header">
<el-row class="row" :gutter="20"  type="flex" justify="space-around" align="middle">
  <el-col  :span="4" :offset="0" >   
      <el-switch rowitem v-model="isCollapse" />
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
</el-header>
<el-container>
<el-aside width="200px">
<sidebar :isCollapse="isCollapse"></sidebar>
</el-aside>
<el-main>
  <router-view/>
</el-main>
</el-container>
</el-container>
</template>



<script lang="ts" setup>
import { Document, Menu as IconMenu, Location,
  Setting, } from '@element-plus/icons-vue'
import Header from "../components/header.vue"
import sidebar from "./sidebar.vue"
</script>

<script lang="ts">
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus'
import {reactive, ref, toRefs } from 'vue';
import {onMounted,onBeforeUpdate,onUpdated,onBeforeMount,onBeforeUnmount,onUnmounted,computed,watch } from "vue";

import {defineExpose ,getCurrentInstance} from 'vue';
import cookies from 'vue-cookies'

// const addTodo = (user: User): void => {
//   console.log("nmsl")
// }

let timer:any;
import { defineComponent } from 'vue';
export default defineComponent({
  data(){
      return {
        isCollapse :true,
        search : '',
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
  computed:{
    
  },
  methods:{

  }
   
})
</script>

<style lang="scss" scoped>
@import '../assets/css/home.scss';
</style>

<style lang="css">

.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
</style>
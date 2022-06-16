<template>
<el-container>
<el-header class="header">
  <Header isCollapse="isCollapse"></Header>
</el-header>
<el-container>
<el-aside width="200px">
<sidebar></sidebar>
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

import { defineComponent}from 'vue';
export default defineComponent({
  data(){
      return {
        isCollapse :true,
        search : '',
        session: '',
    }
  },
  // mounted(){
  //     this.session = this.$cookies.get("session")
  //     if(this.session=="") this.$router.push("/login")
  //     console.log(this.session)
  // },
  destroyed(){
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
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
<el-menu
  default-active="2"
  class="el-menu-vertical-demo"
    :collapse="!isCollapse"
    @open="handleOpen"
    @close="handleClose"
  >
    <el-sub-menu index="1">
      <template #title>
        <el-icon><location /></el-icon>
        <span>学业</span>
      </template>
        <el-menu-item index="1-1" @click="viewclass">课程表</el-menu-item>
        <el-menu-item index="1-2" @click="viewmetal">资料</el-menu-item>
        <el-menu-item index="1-3" @click="viewhmwk">作业</el-menu-item>
        <!-- <el-sub-menu index="1-3" @click="viewexam">子菜单</el-sub-menu> -->
        <el-menu-item index="1-4" @click="viewhmwk">考试</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="2">
      <el-icon><icon-menu /></el-icon>
      <template #title>活动管理</template>
    </el-menu-item>
    <el-menu-item index="3">
      <el-icon><document /></el-icon>
      <template #title>日程提醒</template>
    </el-menu-item>
    <el-menu-item index="4">
      <el-icon><setting /></el-icon>
      <template #title>个人设置</template>
    </el-menu-item>
  </el-menu>
</el-aside>



<el-main>
   <el-table :data="filterTableData"  :key="refreshNum" style="width: 100%">
      <el-table-column
        v-for="(items,indexs) in tableHead"
        :key="indexs"
        :min-width="items.prop==='industryName'||items.prop==='investmentName'?100:150"
        :prop="items.prop"
        :label="items.label"
      ></el-table-column>
    <el-table-column align="right">
      <template #header>
        <el-input v-model="search" size="small" placeholder="Type to search" />
      </template>
      <template #default="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
          >Edit</el-button
        >
        <el-button
          size="small"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)"
          >Delete</el-button
        >
      </template>
    </el-table-column>
  </el-table>

</el-main>
</el-container>
</el-container>
</template>



<script lang="ts" setup>
import { Document, Menu as IconMenu, Location,
  Setting, } from '@element-plus/icons-vue'
</script>


<script lang="ts">
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus'
import {reactive, ref, toRefs } from 'vue';
import {onMounted,onBeforeUpdate,onUpdated,onBeforeMount,onBeforeUnmount,onUnmounted,computed,watch } from "vue";

import {defineExpose ,getCurrentInstance} from 'vue';
import cookies from 'vue-cookies'

interface User {
  name: string
  day: string
  speaker:string
  
}

let timer:any;

const addTodo = (user: User): void => {
  console.log("nmsl")
}

import { defineComponent}from 'vue';
export default defineComponent({
  data(){
      return {
        isCollapse :true,
        refreshNum:1,
        search : '',
        tableData: [
          {
            name: '数据结构',
            day: '星期一',
            speaker: '周丽',
          },
        ],
        _tableHead:[
            {label: '名称', prop: 'name'},
            {label: '星期', prop: 'day'},
            {label: '教授', prop: 'speaker'},
        ],
        form: {
          username: "2020211838",
          password: "111111",
        },
      session:"",
      timeSpeedValue:ref(1),
      timeSpeedOptions:[
        {label:"1x:1秒->1秒",value:1},
        {label:"60x:1秒->1分",value:60},
        {label:"3600x:1秒->1时",value:3600},
        {label:"86400x:1秒->1天",value:86400},
      ],
    }
  },
  mounted(){
      console.log("mounted")
      this.session = this.$cookies.get("session")
      if(this.session!="") console.log(this.session)
      timer = setInterval(() => {
        console.log("开始---");
      }, 1000);
  },
  destroyed(){
      clearInterval(timer)
  },
  computed:{
    tableHead:function(){
      return this._tableHead
    },
    filterTableData:function(){
      return this.tableData.filter(
      (data) =>
        !this.search ||
        data.name.toLowerCase().includes(this.search.toLowerCase())
      )
    }
  },
  methods:{
    viewhmwk(){
      this._tableHead.length=0;
      this._tableHead.pop()
      this._tableHead.pop()
      this._tableHead.push({label:"课程",prop:"className"})
      this._tableHead.push({label:"截止时间",prop:"ddl"})
    },
    handleEdit (index: number, row: User){
      console.log(index, row)
    },
    handleDelete (index: number, row: User){
      console.log(index, row)
    },

    handleOpen  (key: string, keyPath: string[]){
      console.log(key, keyPath)
    },
    handleClose(key: string, keyPath: string[]){
      console.log(key, keyPath)
    },
    viewmetal(){
      // this._tableHead.length=0;
      const user:User={
        name: '计算机系统基础',
        day: '星期一',
        speaker: '周峰',
      }
      this.tableData.push(user)
    },
    viewclass(){
      axios.post("http://192.168.1.88:1024/api/classlist",
      {
        session:this.session,
      })//传参
      .then((res: any)=>{
      if(res.data.code==1)
      {
          console.log(res.data.mess)
          ElMessage({
            type: 'info',
            message: `提示: 登录成功`,
          })
          // this.$router.push({name:'home',params: {id:'10001'}})
      }
      else{
        throw res.data.mess
      }
      })
      .catch(function(err: any){
          ElMessage({
            type: 'info',
            message: `提示: ${err}`,
          })
      });
}


  },

})
</script>

<style lang="scss" scoped>
@import '../assets/css/home.scss';
</style>

<style lang="css">
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 600px;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
</style>
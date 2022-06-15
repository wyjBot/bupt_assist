<template>
<el-container>
<el-header class="header">
<div>
<span class="timebox">3600倍</span>
<el-button type="primary" plain>调节</el-button>
<el-button type="info" plain>暂停</el-button>
</div>

</el-header>
<el-container>
<el-aside width="200px">
<el-switch v-model="isCollapse" />
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
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus'
import {reactive, ref, toRefs } from 'vue';
import {onMounted,onBeforeUpdate,onUpdated,onBeforeMount,onBeforeUnmount,onUnmounted,computed,watch } from "vue";

import {defineExpose ,getCurrentInstance} from 'vue';
import cookies from 'vue-cookies'
const session = cookies.get("session")
console.log(session)


interface User {
  name: string
  day: string
  speaker:string
  
}
const handleEdit = (index: number, row: User) => {
  console.log(index, row)
}
const handleDelete = (index: number, row: User) => {
  console.log(index, row)
}

const isCollapse = ref(true)

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const search = ref('')

const filterTableData = computed(() =>
  tableData.filter(
    (data) =>
      !search.value ||
      data.name.toLowerCase().includes(search.value.toLowerCase())
  )
)

const mounted=onMounted(()=>
{
      console.log("mounted")
      const user:User={
        name: '计算机系统基础',
        day: '星期一',
        speaker: '周峰',
      }
      addTodo(user)
      search.value="1"
      search.value=""
})

const tableData: User[] = [
  {
    name: '数据结构',
    day: '星期一',
    speaker: '周丽',
  },
]

const tableHead=[
      {label: '名称', prop: 'name'},
      {label: '星期', prop: 'day'},
      {label: '教授', prop: 'speaker'},
  ]

const viewmetal=()=>{
  tableHead.length=0;
}
const viewhmwk=()=>{
  tableHead.length=0;
  tableHead.push({label:"课程",prop:"className"})
}
const viewclass=()=>{
  axios.post("http://192.168.1.88:1024/api/classlist",
  {
    session:session,
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


const addTodo = (user: User): void => {
  tableData.push(user)
}
defineExpose({addTodo,search})
</script>


<script lang="ts">
import { defineComponent}from 'vue';
export default defineComponent({
  data(){
      return {
      form: {
        username: "2020211838",
        password: "111111",
      },
      refreshNum:1
    }
  },

})
</script>

<style lang="scss" scoped>
@import '../assets/css/home.scss';
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 600px;
}
</style>
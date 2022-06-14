<template>
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
        <span>Navigator One</span>
      </template>
      <el-menu-item-group title="Group One">
        <el-menu-item index="1-1-1">item one</el-menu-item>
        <el-menu-item index="1-1-2">item two</el-menu-item>
        <el-menu-item index="1-2">item three</el-menu-item>
      </el-menu-item-group>
      <el-sub-menu index="1-4">
        <template #title><span>item four</span></template>
        <el-menu-item index="1-4-1">1-4-1</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="2">
      <el-icon><icon-menu /></el-icon>
      <template #title>Navigator Two</template>
    </el-menu-item>
    <el-menu-item index="3">
      <el-icon><document /></el-icon>
      <template #title>Navigator Three</template>
    </el-menu-item>
    <el-menu-item index="4">
      <el-icon><setting /></el-icon>
      <template #title>Navigator Four</template>
    </el-menu-item>
  </el-menu>
</el-aside>



<el-main>
   <el-table :data="filterTableData" style="width: 100%">
    <el-table-column label="Date" prop="date" />
    <el-table-column label="Name" prop="name" />
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
</template>

<script lang="ts">
export default defineComponent({
  data(){
      return {
      form: {
        username: "2020211838",
        password: "111111",
      },
    }
  },
  onMounted(){
    console.log("mounted")
    const user:User={

    }
  }

})
</script>

<script lang="ts" setup>
import { Document, Menu as IconMenu, Location,
  Setting, } from '@element-plus/icons-vue'
import { defineComponent,computed, reactive, ref, toRefs } from 'vue';


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
const handleEdit = (index: number, row: User) => {
  console.log(index, row)
}
const handleDelete = (index: number, row: User) => {
  console.log(index, row)
}

interface User {
  name: string
  day: string
  

  address: string
}
const tableData: User[] = [
  {
    name: 'Tom',
    date: '2016-05-03',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    name: 'John',
    date: '2016-05-02',
    address: 'No. 189, Grove St, Los Angeles',
  },
]

const addTodo = (user: User): void => {
  tableData.push(user)
}

</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 600px;
}
</style>
<template>
  <el-table :data="filterTableData"  style="width: 100%">
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
         <el-button size="small"
          @click="handleDelete(scope.$index, scope.row)"
          type="info" >查看</el-button >
      </template>
    </el-table-column>
  </el-table>

</template>


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
        tableData: [
          {
            id: '0',
            名称: '军事理论',

          },
        ],
        _tableHead:[
            {label: '名称', prop: 'name'},
            {label: '星期', prop: 'day'},
            {label: '教授', prop: 'speaker'},
        ],
    }
  },
  mounted(){
      this.session = this.$cookies.get("session")
      if(this.session=="") this.$router.push("/login")
      this.listexam()
  },
  destroyed(){
  },
  computed:{
    tableHead:function(){
      return this._tableHead
    },
    filterTableData:function(){
      return this.tableData.filter(
      (data) =>
        !this.search ||
        data.名称.toLowerCase().includes(this.search.toLowerCase())
      )
    }
  },
  methods:{
    handleEdit (index: number, row: any){
      console.log(index, row)
    },
    handleDelete (index: number, row: any){
      console.log(index, row)
    },

    handleOpen  (key: string, keyPath: string[]){
      console.log(key, keyPath)
    },
    handleClose(key: string, keyPath: string[]){
      console.log(key, keyPath)
    },
    listexam(){
      axios.post("/api/exam/list",
      {
        "session":this.session
      })//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let data=res.data.mess;
          if(data.length==0) return;
          let item:any=data[0];
          // console.log(data)

          this._tableHead.length=0;
          for(var key in item){
            this._tableHead.push({label:key,prop:key})

          }
          this.tableData=data
        }
        else if(res.data.code==-1){
           ElMessage({
              type: 'info',
              message: `提示: 登录失效`,
           })
           this.$router.push({name:'login',params: {id:'10001'}})
        }
        else{
          console.log(res.data.code)
          throw res.data.mess
        }
      })
      .catch(function(err: any){
           ElMessage({
              type: 'info',
              message: `提示: ${err}`,
           })
      });
    },
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
<template>
   <el-select v-model="value" class="m-2" placeholder="Select">
    <el-option
      v-for="item in options"
      :key="item.id"
      :label="item.名称"
      :value="item.id"
    />
  </el-select> 
</template>

<script lang="ts" setup>
import { ref,reactive, onMounted, getCurrentInstance } from "vue";
import axios from "axios"
import cookies from 'vue-cookies' 

const value = ref('')

const options = [
  {
    名称: 'Option1',
    id: 'Option1',
  },
  ]

let session=cookies.get("session")

const initOptions=()=>{
 axios.post("/api/crouse/list",
      {
        "session":session
      })//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let data=res.data.mess;
          if(data.length==0) throw "无课程数据";
          for(var key in item){
            // console.log(key,item[key])
            this._tableHead.push({label:key,prop:key})

          }
          this.tableData=data
        }
        else if(res.data.code==-1){
           ElMessage({ type: 'info', message: `提示: 登录失效`, })
           this.$router.push({name:'login',params: {id:'10001'}})
        }
        else{
          console.log(res.data.code)
          throw res.data.mess
        }
      })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`, })
      });

}

onMounted(()=>{

})


]
</script>
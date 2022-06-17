<template>
   <div> 选择频率 </div>
   <el-select v-model="frequncy" class="m-2" placeholder="Select">
    <el-option
      v-for="item in fqData"
      :key="item.id"
      :label="item.name"
      :value="item.id"
    />
    </el-select>
   <div> 选择活动 </div><br>
   <el-select v-model="form.id" class="m-2" placeholder="Select">
    <el-option
      v-for="item in classOptions"
      :key="item.actvtId"
      :label="item.名称"
      :value="item.actvtId"
    />
  </el-select> 
  <el-button @click="submit">确定</el-button>
</template>

<script lang="ts" setup>
import { ref,reactive, onMounted, getCurrentInstance, computed } from "vue";
import axios from "axios"
import { ElMessage, ElMessageBox } from 'element-plus'
import cookies from 'vue-cookies' 
import { useRoute, useRouter } from "vue-router";
let session=cookies.get("session")
const  proxy:any  = getCurrentInstance();
const route = useRoute();
const router = useRouter();
const pr=ref(1);
const fqData=[
  {name:"仅一次",id:1},
  {name:"每天",id:2},
  {name:"每周",id:3},
]




const b2cDt=ref({
    b1:"6",
    b2:"2",
    pr:1,
    mode:"b2b",
    session:"",
  })
const b2tDt=ref( {
    session:"",
    b:"",
    t:"",
    pr:2,
    mode:"b2t"
  })

const classOptionData = [
  {
    名称: 'c1',
    actvtId: 'Option1',
  },
]

const classOptions=computed(()=>{
  return classOptionData
})



const frequncy=ref(1);
const form=ref({
    type:1,
    session:"",
    id:0,
    frequncy:0,
})
const submit=()=>{
 form.value.session=session
 form.value.frequncy=frequncy.value
  axios.post("/api/notice/update",form.value)//传参
    .then((res: any)=>{
        if(res.data.code==1)
        {
          var msg=res.data.mess;
          router.push("/notice")
          ElMessage({ type: 'info', message: "添加成功", })
        }
        else throw res.data.mess
      })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`, })
          //  router.push("/login")
      });
}
const initOptions=()=>{
 form.value.session=session
 form.value.frequncy=frequncy.value
 axios.post("/api/activity/list",form.value)//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let data:any=res.data.mess;
          if(data.length==0) throw "无actvt数据";
          classOptionData.length=0
          for (var item in data)
            classOptionData.push(data[item])
        }
        else if(res.data.code==-1){
           ElMessage({ type: 'info', message: `提示: 登录失效`, })
           router.push({name:'login',params: {id:'10001'}})
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
  initOptions();

})


</script>
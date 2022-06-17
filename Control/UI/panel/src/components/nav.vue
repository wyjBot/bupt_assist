<template>
   <div>

   <div> 选择策略 </div>
   <el-select v-model="pr" class="m-2" placeholder="Select">
    <el-option
      v-for="item in prData"
      :key="item.id"
      :label="item.name"
      :value="item.id"
    />
    </el-select>
   <div> 当前建筑物-> 上课地点 </div><br>
   <el-select v-model="b2cDt.b1" class="m-2" placeholder="Select">
    <el-option
      v-for="item in buildOptions"
      :key="item.Id"
      :label="item.名称"
      :value="item.Id"
    />
  </el-select> 
   <el-select v-model="b2cDt.b2" class="m-2" placeholder="Select">
    <el-option
      v-for="item in classOptions"
      :key="item.id"
      :label="item.名称"
      :value="item.buildId"
    />
  </el-select> 
  <el-button @click="b2c">确定</el-button>
  </div>
   <div>
   <div> 当前建筑物-> 选择的建筑物 </div><br>
   <el-select v-model="b2bDt.b1" class="m-2" placeholder="Select">
    <el-option
      v-for="item in buildOptions"
      :key="item.Id"
      :label="item.名称"
      :value="item.Id"
    />
  </el-select> 
   <el-select v-model="b2bDt.b2" class="m-2" placeholder="Select">
    <el-option
      v-for="item in buildOptions"
      :key="item.Id"
      :label="item.名称"
      :value="item.Id"
    />
  </el-select> 
  <el-button @click="b2b">确定</el-button>
  <div> 当前建筑物-> 日程中的地点 </div>
  </div>
   <el-row gutter="20">
     <el-col span="5" :offset="7">
   <el-select v-model="b2tDt.b" class="m-2" placeholder="Select">
    <el-option
      v-for="item in buildOptions"
      :key="item.Id"
      :label="item.名称"
      :value="item.Id"
    />
  </el-select></el-col> 
     <el-col span="5">
  <div class="demo-datetime-picker"></div>
  <div class="block">
      <el-date-picker
        v-model="b2tDt.t"
        type="datetime"
        placeholder="Pick a Date"
        format="YYYY/MM/DD hh:mm:ss"
        value-format="YYYY-MM-DD hh:mm:ss "
      />
    </div>
     </el-col>
     <el-col span="5">
  <el-button @click="b2t">确定</el-button>
  </el-col>
  </el-row>
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
const prData=[
  {name:"最短距离",id:1},
  {name:"最短时间",id:2},
  {name:"交通工具智行",id:3},
]

const b2bDt=ref({
    session:"",
    b1:"",
    b2:"",
    pr:0,
    mode:"b2b"
  
})

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
    buildId: 'Option1',
  },
]

const buildOptionData = [
  {
    名称: 'b1',
    Id: 'Option1',
  },
]
const classOptions=computed(()=>{
  return classOptionData
})

const buildOptions=computed(()=>{
  return buildOptionData
})

const b2c=()=>{
  b2cDt.value.pr=pr.value;
  b2cDt.value.session=session
  axios.post("/api/nav/explore",b2cDt.value)//传参
    .then((res: any)=>{
        if(res.data.code==1)
        {
          var data=res.data.mess;
          var step=data['step']
          var msg=`共需要${step}步 , `;
          for(var i=1;i<=step;i++)
          {
            msg+=i+": "
            msg+="\n"+data[i]['desc']
            msg+="\n With speed "+data[i]['speed']+"km/h"
            msg+="\n"+" and Cost "+data[i]['duration']+ " second  "
          }
          ElMessage({ type: 'info', message: `提示: ${msg}`, })
        }
        else throw res.data.mess
      })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`, })
           router.push("/login")
      });
}

const b2b=()=>{
  b2bDt.value.pr=pr.value;
  b2bDt.value.session=session
  axios.post("/api/nav/explore",b2bDt.value)//传参
    .then((res: any)=>{
        if(res.data.code==1)
        {
          var data=res.data.mess;
          var step=data['step']
          var msg=`共需要${step}步  .`;
          for(var i=1;i<=step;i++)
          {
            msg+=i+": "
            msg+="\n"+data[i]['desc']
            msg+="\n With speed "+data[i]['speed']+"km/h"
            msg+="\n"+" and Cost "+data[i]['duration']+ " second  "
          }
          ElMessage({ type: 'info', message: `提示: ${msg}`, })
        }
        else throw res.data.mess
          })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`, })
          //  router.push("/login")
      });

}
const b2t=()=>{
  b2tDt.value.pr=pr.value;
  b2tDt.value.session=session
  axios.post("/api/nav/explore",b2tDt.value)//传参
    .then((res: any)=>{
        if(res.data.code==1)
        {
          var data=res.data.mess;
          var step=data['step']
          var msg=`共需要${step}步 , `;
          for(var i=1;i<=step;i++)
          {
            msg+=i+": "
            msg+="\n"+data[i]['desc']
            msg+="\n With speed "+data[i]['speed']+"km/h"
            msg+="\n"+" and Cost "+data[i]['duration']+ " second  "
          }
          ElMessage({ type: 'info', message: `提示: ${msg}`, })
        }
        else throw res.data.mess
      })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`, })
           router.push("/login")
      });

}
const initOptions=()=>{
 axios.post("/api/crouse/list",
      {
        "session":session
      })//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let data:any=res.data.mess;
          if(data.length==0) throw "无课程数据";
          classOptionData.length=0
          for (var item in data)
            classOptionData.push(data[item])
        }
        else if(res.data.code==-1){
           ElMessage({ type: 'info', message: `提示: 登录失效`, })
           router.push({name:'login',params: {id:'10001'}})
        }
        else{
          // console.log(res.data.code)
          throw res.data.mess
        }
      })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`, })
      });
 axios.post("/api/nav/build",
      {
        "session":session
      })//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let data:any=res.data.mess;
          if(data.length==0) throw "无数据";
          buildOptionData.length=0
          for (var item in data)
            buildOptionData.push(data[item])
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
<style scoped>
.demo-datetime-picker {
  display: flex;
  width: 100%;
  padding: 0;
  flex-wrap: wrap;
}
.demo-datetime-picker .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  flex: 1;
}
.demo-datetime-picker .block:last-child {
  border-right: none;
}
.demo-datetime-picker .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
</style>
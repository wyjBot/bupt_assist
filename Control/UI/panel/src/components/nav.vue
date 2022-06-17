<template>
   <div>
   <el-select v-model="b2c_b" class="m-2" placeholder="Select">
    <el-option
      v-for="item in buildOptions"
      :key="item.id"
      :label="item.名称"
      :value="item.id"
    />
  </el-select> 
   <el-select v-model="b2c_c" class="m-2" placeholder="Select">
    <el-option
      v-for="item in classOptions"
      :key="item.id"
      :label="item.名称"
      :value="item.id"
    />
  </el-select> 
  <el-button>确定</el-button>
  </div>
</template>

<script lang="ts" setup>
import { ref,reactive, onMounted, getCurrentInstance, computed } from "vue";
import axios from "axios"
import { ElMessage, ElMessageBox } from 'element-plus'
import cookies from 'vue-cookies' 
import { useRoute, useRouter } from "vue-router";
const  proxy:any  = getCurrentInstance();
const route = useRoute();
const router = useRouter();

const b2c_b = ref('')
const b2c_c = ref('')
const b2b_b1 = ref('')
const b2b_b2 = ref('')
const b2t_b = ref('')
const b2t_t = ref('')

const classOptions=computed(()=>{
  return optionData
})

const b2bform=[
  {
    start:0,
    end:0,
  }
]

const b2cform=[
  {
    start:0,
    end:0,
  }
]
const b2tform=[
  {
    now:0,
    target:0,
  }
]


const ClassOptionData = [
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
          let data:any=res.data.mess;
          if(data.length==0) throw "无课程数据";
          optionData.length=0
          for (var item in data)
            optionData.push(data[item])
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
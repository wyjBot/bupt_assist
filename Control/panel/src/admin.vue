<template>

  <!-- <div>{{taskDt.task_name}} </div>
  <div>{{taskDt.task_}} </div> -->
  <div>上次提交：{{form.lastTime}}</div>
  <el-input
    v-model="form.text"
    class="txtarea"
    :autosize="{ minRows: 2, maxRows: 4 }"
    type="textarea"
    placeholder="Please input"
  />
  <el-upload
    class="upload-demo"
    :on-change="handleChange"
    :file-list="fileList"
    :auto-upload="false"
  >
    <el-button type="primary" plain> upload</el-button>
    <template #tip>
      <div class="el-upload__tip">
        多文件或文件夹请用压缩包上传
      </div>
    </template>
  </el-upload>
  <el-button type="success" @click="submit" >    OK   </el-button>
</template>

<script setup lang="ts">
import { ref,reactive, onMounted, getCurrentInstance } from "vue";
import type { UploadUserFile } from 'element-plus'
import axios from 'axios';
import { genFileId } from 'element-plus'
import type { UploadInstance, UploadProps, UploadFile } from 'element-plus'
import { ElMessage, ElMessageBox } from 'element-plus'
import cookies from 'vue-cookies' 
import { useRoute, useRouter } from "vue-router";
const  proxy:any  = getCurrentInstance();
const route = useRoute();
const router = useRouter();

const taskId=route.query.id

// const props = defineProps({
  // id:String
// })

const taskDt=ref({

  名称:"title",
  内容:"hello kitty"
})

const form=ref({
  "text":"",
  "fileid":0,
  "lastTime":"未提交",
  "task_des":"None",
  "task_name":"None",
})

var fileTosend:any;

let session=cookies.get("session")

onMounted(()=>{
 axios.post("/api/hmwk/view",{
   taskId:taskId,
   session:session,
 })//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let data:any=res.data.mess;
          if(data.length==0) return;
          form.value.text=data['文本']
          form.value.lastTime=data['提交时间']
          form.value.task_name=data['task_name']
          form.value.task_des=data['task_des']
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


})
const gologin=()=>{
           ElMessage({
              type: 'info',
              message: `提示: 登录失效`,
           })
          router.push({name:"login"})
}
const submit=()=>{
      console.log(fileTosend)
      let config = {
        headers: {'Content-Type': 'multipart/form-data'}
      }
      axios.post("/api/file/upload",
      {
        "session":session,
        "file":fileTosend,
        "text":form.value.text
      },config)//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          form.value.fileid=res.data.mess;
        }
        else if(res.data.code==-1){ gologin(); }
        else{
          console.log(res.data.code)
          throw res.data.mess
        }
      })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`,})
      });
      axios.post("/api/hmwk/update",
      {
        "session":session,
        "taskId":taskId,
        "fileId":form.value.fileid,
        "text":form.value.text
      },config)//传参
      .then((res: any)=>{
        var msg= res.data.mess;
        if(res.data.code==0) throw msg;
        else if(res.data.code==400){ throw msg}
        else if(res.data.code==-1){ gologin(); }
        else{
          router.push({name:"hmwk"})
          throw msg;
        }
      })
      .catch(function(err: any){
           ElMessage({ type: 'info', message: `提示: ${err}`, })
      });

}

const fileList = ref<UploadUserFile[]>([
  {
    name: 'food.jpeg',
    url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
  },
])

const handleChange: UploadProps['onChange'] = (uploadFile, uploadFiles) => {
  fileList.value = fileList.value.slice(-1)
  fileTosend=uploadFile
}
</script>

<script  lang="ts">
import { ref,defineComponent } from 'vue'
export default defineComponent({
  methods: {
    he(){},
  }
})
</script>
<style>
.txtarea{
  max-width:60vw;
}

</style>
<template>

  <div>{{task.名称}} </div>
  <div>{{task.内容}} </div>
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
import { useRoute, useRouter } from "vue-router";
import { genFileId } from 'element-plus'
import type { UploadInstance, UploadProps, UploadFile } from 'element-plus'
import { ElMessage, ElMessageBox } from 'element-plus'
import cookies from 'vue-cookies' 
const  proxy:any  = getCurrentInstance();
const route = useRoute();
const router = useRouter();


console.log(route.query.id)

// const props = defineProps({
  // id:String
// })

const task={

  名称:"title",
  内容:"hello kitty"
}
const textarea1 = ref('')

const form:any={
  "file":"",
  "text":"",
  "fileid":0,

}
let session=cookies.get("session")
const gologin=()=>{
           ElMessage({
              type: 'info',
              message: `提示: 登录失效`,
           })
          router.push({name:"login"})
}
const submit=()=>{
      form.file.name="attach"
      console.log(form.file)
      let config = {
        headers: {'Content-Type': 'multipart/form-data'}
      }
      axios.post("/api/file/upload",
      {
        "session":session,
        "file":form.file,
        "text":form.text
      },config)//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          form.fileid=res.data.mess;
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
        "fileid":form.fileid,
        "text":form.text
      },config)//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let msg=res.data.mess;
          ElMessage({ type: 'info', message: msg, })
          router.push({name:"hmwk"})
        }
        else if(res.data.code==-1){ gologin(); }
        else{
          console.log(res.data.code)
          throw res.data.mess
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
  {
    name: 'food2.jpeg',
    url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
  },
])

const handleChange: UploadProps['onChange'] = (uploadFile, uploadFiles) => {
  fileList.value = fileList.value.slice(-1)
  form.file=uploadFile
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
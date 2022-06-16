<template>

  <div>{{task.名称}} </div>
  <div>{{task.内容}} </div>
  <el-input
    v-model="textarea1"
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
import { ref } from 'vue'
import type { UploadUserFile } from 'element-plus'
import axios from 'axios';
import { genFileId } from 'element-plus'
import type { UploadInstance, UploadProps, UploadFile } from 'element-plus'
import { ElMessage, ElMessageBox } from 'element-plus'
const task={
  名称:"title",
  内容:"hello kitty"
}
const textarea1 = ref('')

const form:any={
  "file":"",
  "text":""

}
const submit=()=>{
      axios.post("/api/activity/list",
      {
        "session":this.session
      })//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
          let data=res.data.mess;
          if(data.length==0) return;
          let item:any=data[0];
          console.log(data)

          this._tableHead.length=0;
          for(var key in item){
            console.log(key,item[key])
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

<style>
.txtarea{
  max-width:60vw;
}

</style>
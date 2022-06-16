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
    <el-button type="primary">Click to upload</el-button>
    <template #tip>
      <div class="el-upload__tip">
        jpg/png files with a size less than 500kb
      </div>
    </template>
  </el-upload>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { UploadUserFile } from 'element-plus'
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
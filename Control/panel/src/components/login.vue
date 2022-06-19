<template>
  <div class="login-container">
    <el-form
      :model="form"
      status-icon
      :rules="rules"
      ref="form"
      label-width="100px"
      class="login-form"
    >
      <h1 class="title-zc">登录页</h1>
      <el-form-item label="账号" prop="username">
        <el-input v-model.number="form.username"></el-input>
      </el-form-item>
 
      <el-form-item label="密码" prop="password">
        <el-input
          type="password"
          v-model="form.password"
          autocomplete="off"
        ></el-input>
      </el-form-item>
 
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts">
import { ElMessage, ElMessageBox } from 'element-plus'
import { defineComponent, reactive, ref, toRefs } from 'vue';
import axios, { AxiosResponse, AxiosRequestConfig } from 'axios';


export default defineComponent({

  data(){
      return {
      form: {
        username: "2020211839",
        password: "12345678",
      },
      rules: {
        username: [{ required: true, message: "请输入账号", trigger: "blur" }],
        password: [{ required: true, message: "请输入昵称", trigger: "blur" }],
      },
      }
  },
  methods:{
    submitForm(){
      this.login(this.form.username, this.form.password)
    },
    login(username: string, password: string){
      axios.post("/api/signin",
      {
        "act":username,
        "pwd":password
      })//传参
      .then((res: any)=>{
        if(res.data.code==1)
        {
           ElMessage({
              type: 'info',
              message: `提示: 登录成功`,
           })
           this.$cookies.set("session",res.data.mess)
           this.$router.push({name:'home',params: {id:'10001'}})
        }
        else{
          throw res.data.mess
          console.log(res.data.code)
        }
      })
      .catch(function(err: any){
           ElMessage({
              type: 'info',
              message: `提示: ${err}`,
           })
      });
    },
  },
})
</script>


<style scoped>
.login-container {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-image: url("../assets/login_bg.jpg");
  background-size: 100% 100%;
  background-repeat: no-repeat;
}
.login-form {
  width: 350px;
  margin: 150px auto;
  background-color: rgba(189, 187, 188, 0.8);
  padding: 30px;
  border-radius: 5px;
}
.title-zc {
  text-align: center;
}
</style>

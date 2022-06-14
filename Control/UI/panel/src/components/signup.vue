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
      <el-form-item label="学号" prop="username">
        <el-input v-model.number="form.username"></el-input>
      </el-form-item>
 
      <el-form-item label="密码" prop="password">
        <el-input
          type="password" v-model="form.password"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      
      <el-form-item label="角色" prop="role">
        <el-input v-model="form.role"></el-input>
      </el-form-item>
 
      <el-form-item label="姓名" prop="name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>

      <el-form-item label="电话" prop="phone">
        <el-input v-model.number="form.phone"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
 
export default {
  data() {
    return {
      form: {
        username: "2020211838",
        password: "111111",
        role:"学生",
        name:"王昱杰",
        phone:"19509991727",
      },
      
      rules: {
        username: [{ required: true, message: "请输入账号", trigger: "blur" }],
        password: [{ required: true, message: "请输入昵称", trigger: "blur" }],
        role: [{ required: true, message: "学生/教师", trigger: "blur" }],
      },
    };
  },
  methods: {
    submitForm() {
      this.$axios.post("http://192.168.1.88:1024/api/signup",
      {
        "act":this.form.username,
        "pwd":this.form.password,
        "role":this.form.role,
        "name":this.form.name,
        "phone":this.form.phone
      })//传参
      .then(function(res){
          console.log(res)          
      })
      .catch(function(err){
            throw "请求失败233",err
      });
    },
  },
};


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

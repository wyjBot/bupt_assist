<template>
<el-container>
<el-header class="header">
<el-row class="row" :gutter="20"  type="flex" justify="space-around" align="middle">
  <el-col  :span="4" :offset="0" >   
      <el-switch rowitem v-model="isCollapse" />
  </el-col>
  <el-col :span="4"  :offset="6" >   
  <el-date-picker
    v-model="resetDt"
    @change="resetDtc"
    type="datetime"
    placeholder="Pick a Date"
    format="YYYY/MM/DD hh:mm:ss"
    value-format="YYYY-MM-DD hh:mm:ss "
    :readonly="notimeInput"
  />
  </el-col>
  <el-col :span="8"  :offset="0" >   
  <div class="rowitem timebox">
  <el-select v-model="timeSpeedValue" class="m-2" placeholder="Select">
    <el-option
      v-for="item in timeSpeedOptions"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    />
  </el-select>
  <el-button type="primary" plain @click="change">调节</el-button>
  <el-button type="info" plain @click="timeSwc">{{timeswcDt}}</el-button>
  </div>
  </el-col>
</el-row>
</el-header>
<el-container>
<el-aside width="200px">
<sidebar :isCollapse="isCollapse"></sidebar>
</el-aside>
<el-main>
  <router-view/>
</el-main>
</el-container>
</el-container>
</template>



<script lang="ts" setup>
import { Document, Menu as IconMenu, Location,
  Setting, } from '@element-plus/icons-vue'
import Header from "../components/header.vue"
import sidebar from "./sidebar.vue"
</script>

<script lang="ts">
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus'
import {reactive, ref, toRefs } from 'vue';
import {onMounted,onBeforeUpdate,onUpdated,onBeforeMount,onBeforeUnmount,onUnmounted,computed,watch } from "vue";

import {defineExpose ,getCurrentInstance} from 'vue';
import cookies from 'vue-cookies'

// const addTodo = (user: User): void => {
//   console.log("nmsl")
// }

let timer:any;
import { defineComponent } from 'vue';
export default defineComponent({
  data(){
      return {
        isCollapse :true,
        search : '',
        session:'',
        resetDt:"",
        notimeInput:true,
        timeswcDt:'开启中',
        timeSpeedValue:60,
        timeSpeedOptions:[
          {label:"1x:1秒->1秒",value:1},
          {label:"60x:1秒->1分",value:60},
          {label:"3600x:1秒->5分",value:300},
          {label:"3600x:1秒->1时",value:3600},
        ],
    }
  },
  mounted(){
      this.session = this.$cookies.get("session")
      if(this.session=="") this.$router.push("/login")
      else console.log("head mounted",this.session)
      timer = setInterval(() => {
        this.getNoiceWk();
      }, 1600);
  },
  methods:{
    dpickerFocusd(){
      console.log("focusde")
      if(this.timeswcDt=="开启中"){
        this.timeSwc();
        clearInterval(timer)
      }
    },

    change(){
      axios.post("/api/notice/setrate",{
        session: this.session,
        rate:this.timeSpeedValue,
      })//传参
        .then((res: any)=>{
            console.log(res.data.code)
            var msg=res.data.mess
            if(res.data.code==1)
            {
              throw "调节成功"+msg

            }
            else if(res.data.code==-1)
              this.$router.push("/login")
            else throw msg
          })
          .catch(function(err: any){
              ElMessage({ type: 'info', message: `提示: ${err}`, })
          });


    },

    timeSwc(){
      if(this.timeswcDt=="开启中")
        var url="/api/notice/timeStop";
      else
        var url="/api/notice/timeStart";
      axios.post(url,{
        session: this.session,
        rate:this.timeSpeedValue,
      })//传参
        .then((res: any)=>{
            console.log(res.data.code)
            var msg=res.data.mess
            if(res.data.code==1)
            {
              if(this.timeswcDt=="开启中"){
                  this.timeswcDt="暂停中"
                  this.notimeInput=false
                  clearInterval(timer)
              }
              else{
                  this.timeswcDt="开启中"
                  this.notimeInput=true
                  timer = setInterval(() => {
                    this.getNoiceWk();
                  }, 2400);

              }
            }
            else if(res.data.code==-1)
              this.$router.push("/login")
            else throw msg
          })
          .catch(function(err: any){
              ElMessage({ type: 'info', message: `提示: ${err}`, })
          });

    },
    getNoiceWk(){
      this.session=this.$cookies.get("session")
      axios.post("/api/notice/wk",{
        session: this.session

      })//传参
        .then((res: any)=>{
            console.log(res.data.code)
            var data=res.data.mess;
            var code=res.data.code;
            if(res.data.code==1)
            {
              for(var x in data){
                ElMessage({ type: 'info', message: data[x], })
              }
            }
            else if(code==2){
              this.notimeInput=true,
              this.resetDt=data[0]
              return
            }
            else if(res.data.code==-1){
              this.$router.push("/login")
            }
            else throw res.data.mess
          })
          .catch(function(err: any){
              ElMessage({ type: 'info', message: `提示: ${err}`, })
          });


      },

    resetDtcb(value:string){
      console.log("gggjs")
    },
    resetDtc(value:string){
      axios.post("/api/notice/timeReset",{
        session: this.session,
        time:this.resetDt

      })//传参
        .then((res: any)=>{
            console.log(res.data.code)
            var msg=res.data.mess
            if(res.data.code==1)
            {
              throw msg
            }
            else if(res.data.code==-1)
              this.$router.push("/login")
            else throw msg
          })
          .catch(function(err: any){
              ElMessage({ type: 'info', message: `提示: ${err}`, })
          });
    }
    
  },
  destroyed(){
      clearInterval(timer)
  },

})
</script>

<style lang="scss" scoped>
@import '../assets/css/home.scss';
</style>

<style lang="css">

.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}

</style>
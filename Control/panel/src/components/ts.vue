<template>
  <div>
    <label style="padding-left: 20px">刷新时间(秒)</label>
    <el-input-number v-model="formData.timer" :min="1" :max="1440" :disabled="formData.openState"></el-input-number>
    <el-switch v-model="formData.openState" @change="closeTimeClick()" active-color="#13ce66"></el-switch>
  </div>
</template>

<script >
export default {
  data() {
    return {
      interTimer: null,
      formData: {
        openState: false,
        timer: '1' // 定时器
      },
    }
  },
  methods: {
    closeTimeClick() {
      if (!this.formData.openState) {
        // 关闭定时器
        clearInterval(this.interTimer)
      } else {
        this.interTimer = setInterval(this.console, this.formData.timer * 1000)
      }
    },
    console() {
      console.log('调用定时刷新接口',new Date())
    }

  }
}
</script>

<style scoped>

</style>
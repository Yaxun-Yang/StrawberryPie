<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>设备提醒 {{warn}}</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 信号弱 -->
    <el-card shadow="hover" id="wx">
      <el-button class="iconn" icon="el-icon-search" circle></el-button>
      <span class="text">主卧室空调</span>
      <i class="el-icon-eleme"></i>
      <span class="warn_text" :class="{waning_style:is_air_warning}">{{air_message}}</span>
    </el-card>
    <!-- 门没关 -->
    <br>
    <el-card shadow="hover" id="wx-2">
      <el-button class="iconn" icon="el-icon-search" circle></el-button>
      <span class="text">主卧室门</span>
      <i class="el-icon-eleme"></i>
      <span class="warn_text" :class="{waning_style:is_warning}">{{door_message}}</span>
    </el-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        warn: "",
        is_warning: false,
        is_air_warning: false,
        air_message: "正常",
        door_message: "正常"
      }
    },
    methods: {
      async get_warning_information() {
        const { data: res } = await this.$http.get(`air`)
        this.air_message = res.data.airconditon
        this.is_air_warning = res.data.air_warning
      }
    },
    created() {
      this.get_warning_information()
      this.$root.Bus.$on('doorWarning', value => {
        alert(value)
        this.warn = value
        this.door_message = value
        this.is_warning = true
        // console.log(value)
      })
    },
    // 在组件销毁时别忘了解除事件绑定
    beforeDestroy() {
      this.$root.Bus.$off('doorWarning')
    }
  }
</script>

<style>
  #wx, #wx-2{
    position: relative;
    height: 100px;
    width: 330px;
  }
  .iconn{
    position: relative;
    left: -15px;
    top: 10px;
  }
  .text{
    position: absolute;
    left: 50px;
    top: 30px;
    font-size: 25px;
  }
  .el-icon-eleme{
    position: absolute;
    right: 70px;
    top: 45px
  }
  .warn_text{
    position: absolute;
    right: 3px;
    top: 40px
  }
  .waning_style {
    color: red;
  }
</style>

<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>设备提醒 {{warn}}</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 信号弱 -->
<!--    <el-card shadow="hover" id="wx">-->
<!--      <el-button class="iconn" icon="el-icon-search" circle></el-button>-->
<!--      <span class="text">主卧室空调</span>-->
<!--      <i class="el-icon-eleme"></i>-->
<!--      <span class="warn_text" :class="{waning_style:is_air_warning}">{{air_message}}</span>-->
<!--    </el-card>-->
<!--    &lt;!&ndash; 门没关 &ndash;&gt;-->
<!--    <br>-->
<!--    <el-card shadow="hover" id="wx-2">-->
<!--      <el-button class="iconn" icon="el-icon-search" circle></el-button>-->
<!--      <span class="text">主卧室门</span>-->
<!--      <i class="el-icon-eleme"></i>-->
<!--      <span class="warn_text" :class="{waning_style:is_warning}">{{door_message}}</span>-->
<!--    </el-card>-->
    <!-- 提示信息 -->
    <!-- room1 -->
    <div class="pad" v-show="value1">
      <el-alert title="卧室Wi-Fi已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!value1">
      <el-alert title="卧室Wi-Fi已关闭" type="info" show-icon></el-alert>
    </div>
    <div class="pad" v-show="wifi1OK">
      <el-alert title="卧室Wi-Fi信号正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!wifi1OK">
      <el-alert title="卧室Wi-Fi信号弱" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="temp1">
      <el-alert title="卧室温度正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!temp1">
      <el-alert title="卧室温度异常" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="hum1">
      <el-alert title="卧室湿度正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!hum1">
      <el-alert title="卧室湿度异常" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="light1">
      <el-alert title="卧室台灯已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!light1">
      <el-alert title="卧室台灯已断开连接" type="info" show-icon></el-alert>
    </div>
    <div class="pad" v-show="door1">
      <el-alert title="卧室门已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!door1">
      <el-alert title="卧室门已断开连接" type="info" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!doorClosed">
      <el-alert title="卧室门没关" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="doorClosed">
      <el-alert title="卧室门已关上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="air1">
      <el-alert title="卧室空调已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!air1">
      <el-alert title="卧室空调已断开连接" type="info" show-icon></el-alert>
    </div>
    <div class="pad" v-show="water1">
      <el-alert title="卧室饮水机已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!water1">
      <el-alert title="卧室饮水机已断开连接" type="info" show-icon></el-alert>
    </div>
    <!-- room2 -->
    <div class="pad" v-show="value2">
      <el-alert title="卫生间Wi-Fi已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!value2">
      <el-alert title="卫生间Wi-Fi已关闭" type="info" show-icon></el-alert>
    </div>
    <div class="pad" v-show="wifi2OK">
      <el-alert title="卫生间Wi-Fi信号正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!wifi2OK">
      <el-alert title="卫生间Wi-Fi信号弱" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="temp2">
      <el-alert title="卫生间温度正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!temp2">
      <el-alert title="卫生间温度异常" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="hum2">
      <el-alert title="卫生间湿度正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!hum2">
      <el-alert title="卫生间湿度异常" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="light2">
      <el-alert title="卫生间挂灯已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!light2">
      <el-alert title="卫生间挂灯已断开连接" type="info" show-icon></el-alert>
    </div>
    <!-- room3 -->
    <div class="pad" v-show="value3">
      <el-alert title="阳台Wi-Fi已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!value3">
      <el-alert title="阳台Wi-Fi已关闭" type="info" show-icon></el-alert>
    </div>
    <div class="pad" v-show="wifi3OK">
      <el-alert title="阳台Wi-Fi信号正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!wifi3OK">
      <el-alert title="阳台Wi-Fi信号弱" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="temp3">
      <el-alert title="阳台温度正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!temp3">
      <el-alert title="阳台温度异常" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="hum3">
      <el-alert title="阳台湿度正常" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!hum3">
      <el-alert title="阳台湿度异常" type="warning" show-icon></el-alert>
    </div>
    <div class="pad" v-show="light3">
      <el-alert title="阳台挂灯已连接上" type="success" show-icon></el-alert>
    </div>
    <div class="pad" v-show="!light3">
      <el-alert title="阳台挂灯已断开连接" type="info" show-icon></el-alert>
    </div>
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
        door_message: "正常",
        value1: true,
        wifi1OK: true,
        value2: true,
        wifi2OK: true,
        value3: false,
        wifi3OK: true,
        temp1: true,
        hum1: true,
        light1: true,
        door1: false,
        doorClosed: false,
        air1: true,
        water1: false,
        temp2: true,
        hum2: true,
        light2: true,
        temp3: true,
        hum3: true,
        light3: true
      }
    },
    methods: {
      // async get_warning_information() {
      //   // const { data: res } = await this.$http.get(`air`)
      //   // this.air_message = res.data.airconditon
      //   // this.is_air_warning = res.data.air_warning
      // },
      async get_warning_information() {
        const {data: res} = await this.$http.get('air')
        console.log(res)
        if (res.meta.status !== 200) {
          return this.$message.error('获取信息失败')
        }
        this.value1 = res.data.value1
        this.wifi1OK = res.data.wifi1OK
        this.value2 = res.data.value2
        this.value3 = res.data.value3
        this.wifi2OK = res.data.wifi2OK
        this.wifi3OK = res.data.wifi3OK
        this.temp1 = res.data.temp1
        this.temp2 = res.data.temp2
        this.temp3 = res.data.temp3
        this.hum1 = res.data.hum1
        this.hum2 = res.data.hum2
        this.hum3 = res.data.hum3
        this.light1 = res.data.light1
        this.light2 = res.data.light2
        this.light3 = res.data.light3
        this.door1 = res.data.door1
        this.doorClosed = res.data.doorClosed
        this.air1 = res.data.air1
        this.water1 = res.data.water1
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
  .pad {
    padding-top: 20px;
  }

  .el-alert {
    width: 30%;
  }
  /*#wx, #wx-2{*/
  /*  position: relative;*/
  /*  height: 100px;*/
  /*  width: 330px;*/
  /*}*/
  /*.iconn{*/
  /*  position: relative;*/
  /*  left: -15px;*/
  /*  top: 10px;*/
  /*}*/
  /*.text{*/
  /*  position: absolute;*/
  /*  left: 50px;*/
  /*  top: 30px;*/
  /*  font-size: 25px;*/
  /*}*/
  /*.el-icon-eleme{*/
  /*  position: absolute;*/
  /*  right: 70px;*/
  /*  top: 45px*/
  /*}*/
  /*.warn_text{*/
  /*  position: absolute;*/
  /*  right: 3px;*/
  /*  top: 40px*/
  /*}*/
  /*.waning_style {*/
  /*  color: red;*/
  /*}*/
</style>

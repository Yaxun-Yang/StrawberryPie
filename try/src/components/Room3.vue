<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/device_manage' }">设备管理</el-breadcrumb-item>
      <el-breadcrumb-item>主卧室</el-breadcrumb-item>
    </el-breadcrumb>
    <h1>您的阳台共1台设备，已连接{{value}}台</h1>
<!--    <el-card class="card1" shadow="always">-->
<!--      &lt;!&ndash; 安全范围 &ndash;&gt;-->
<!--      <el-popover placement="right" width="270" height="400" trigger="click">-->
<!--        温度<el-slider v-model="setTemp" range :marks="marks1"></el-slider>-->
<!--        <br>-->
<!--        湿度<el-slider v-model="sethumid" range :marks="marks2"></el-slider>-->
<!--        <el-button class="change" slot="reference" type="primary" plain>-->
<!--          <span class="change_text">点击以修改安全范围</span>-->
<!--        </el-button>-->
<!--      </el-popover>-->
<!--      &lt;!&ndash; 显示温度湿度 &ndash;&gt;-->
<!--        <span>-->
<!--          <el-button icon="el-icon-sunny" circle size="small"></el-button>-->
<!--          <b> {{temp}}</b>℃-->
<!--        </span>-->
<!--        <el-divider direction="vertical"></el-divider>-->
<!--        <span class="humidity">{{humid}}%</span>-->
<!--        <span class="humidity_text">空气湿度</span>-->
<!--      </el-card>-->
    <el-card class="card1" shadow="always" style="width: 300px;height: 280px;">
      <!-- 显示温度湿度 -->
      <div style="background-color: #fffeeb;width: 180px;">
       <span style="font-size: 20px">
         <span style="color: dimgray;">
           <i class="el-icon-sunny" ></i>
         </span>
         <b> {{temp}}</b>℃
       </span>
        <el-divider direction="vertical" style="width: 100%;"></el-divider>
        <div>
          <span class="humidity">{{humid}}%</span>
          <span class="humidity_text">空气湿度</span>
        </div>
      </div>
      <!-- 安全范围 -->
      <br>
      <div>
        <span style="color: gray; font-size: 10px;">您预定的安全范围为</span>
        <div style="color: #636363; font-size: 14px; background-color: #f9fafc;width: 280px">
          「温度」<el-slider v-model="setTemp" range :marks="marks1" @change="temChange()"></el-slider>
          <el-divider style="width: 100%;"></el-divider>
          「湿度」<el-slider v-model="setHumid" range :marks="marks2"></el-slider>
        </div>
      </div>
    </el-card>
    <!-- 挂灯 -->
    <br>
    <el-card class="card2" shadow="always">
      <br>
      <el-slider v-model="value1" vertical height="200px" :disabled="value2==false" format-tooltip="formatTooltip1" @change="tempLightChange"></el-slider>
      <div class="block">
        <h2>挂 灯</h2>
        <el-button class="icon" icon="el-icon-s-opportunity" circle size="big"></el-button>
        <span class="light" :hidden="value2==false">  {{value1}}%</span>
        <span class="light_text">亮度</span>
        <el-switch
          v-model="value2"
          active-text="已连接"
          inactive-text="未连接"
          @change="switchChange2">
        </el-switch>
        </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      value: 1,
      value1: 60,
      value2: true,
      temp: 26,
      humid: 60,
      setTemp: [30, 60],
      sethumid: [20, 70],
      marks1: {
        0: '0°C',
        8: '8°C',
        37: '37°C',
        50: {
          style: {
            color: '#1989FA'
          },
          label: this.$createElement('strong', '50°C')
        }
      },
      marks2: {
        0: '0%',
        20: '20%',
        60: '60%',
        50: {
          style: {
            color: '#1989FA'
          },
          label: this.$createElement('strong', '50%')
        }
      }
    }
  },
  methods: {
    formatTooltip1 (val) {
      return val + '%'
    },
    async getRoom3Infomation () {
      const { data: res } = await this.$http.get('room3')
      console.log(res)
      if (res.meta.status !== 200) {
        return this.$message.error('获取阳台信息失败')
      }
      this.value = res.data.value
      this.value1 = res.data.value1
      this.value2 = res.data.value2
      this.temp = res.data.temp
      this.humid = res.data.humid
      this.setTemp = res.data.setTemp
      this.setHumid = res.data.setHumid
    },
    async tempLightChange() {
      const { data: res } = await this.$http.put(
              `room3/templight/change/${this.value1}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      console.log(res.meta.status)
      this.$message.success('修改成功')
    },
    async switchChange2() {
      this.connectDev()
      const { data: res } = await this.$http.put(
              `room3/lightcon/change/${this.value2}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      console.log(res.meta.status)
      this.$message.success('修改成功')
    },
    connectDev(){
      let conNum = 0
      if(this.value2) {
        conNum++;
      }
      this.value = conNum
      console.log("conDev"+this.value)
    },
    async temChange() {
      let temperature = {
        "low_temp": this.setTemp[0],
        "high_temp": this.setTemp[1]
      }
      const {data: res} = await this.$http.get("room3/tem", {
        params: temperature
      })
      console.log(res)
    },
    async humChange() {
      let humid = {
        "low_hum": this.setHumid[0],
        "high_hum": this.setHumid[1]
      }
      const {data: res} = await this.$http.get("room3/hum", {
        params: humid
      })
      console.log(res)
    }
  },
  created() {
    this.getRoom2Infomation()
  }
}
</script>

<style>
  .card1{
    display: flex;
    justify-content: space-between;
    width: 180px;
    position: relative;
  }
  .humidity{
    position: absolute;
    right: 20px;
    top: 8px;
    font-size: 24px
  }
  .humidity_text{
    position: absolute;
    right: 17px;
    top: 35px;
    font-size: 13px
  }
  .card2{
    display: flex;
    justify-content: space-between;
    width: 300px;
    position: relative;
  }
  .block{
    position: absolute;
    right: 30px;
    top: 20px;
  }
  .icon{
    position: absolute;
    left: 0px;
    top: 90px;
  }
  .light{
    position: absolute;
    right: 60px;
    top: 85px;
    font-size: 20px;
  }
  .light_text{
    position: absolute;
    right: 65px;
    top: 114px;
    font-size: 12px;
  }
  .el-switch{
    position: absolute;
    right: 10px;
    top: 100px;
  }
</style>

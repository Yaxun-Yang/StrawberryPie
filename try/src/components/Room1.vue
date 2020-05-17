<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/device_manage' }">设备管理</el-breadcrumb-item>
      <el-breadcrumb-item>主卧室</el-breadcrumb-item>
    </el-breadcrumb>
    <h1>您的主卧室共3台设备，已连接{{value}}台</h1>
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
          「湿度」<el-slider v-model="setHumid" range :marks="marks2" @change="humChange()"></el-slider>
        </div>
      </div>
    </el-card>

    <!-- 门 -->
    <br>
    <el-card class="card2" shadow="always">
      <br><br>
      <el-progress type="circle" :percentage="timeD" :disabled="door_value==false"></el-progress>
      <br><font color="#409EFF">开门倒计时：{{openTime}}</font><br><br>
      <el-time-select
        v-model="openTime"
        size="mini"
        :picker-options="{
          start: '00:30',
          step: '00:15',
          end: '3:00'
        }"
        :disabled="door_value==false"
        @change="progressChange"
        placeholder="允许最长开门时间">
      </el-time-select>
      <!-- 未关门时长范围 -->
      <div class="eye">
        <el-switch
          v-model="door_value"
          active-text="已连接"
          inactive-text="未连接"
          @change="doorConnect()">
        </el-switch>
      </div>
      <div class="door">
        <h2>门</h2>
      </div>
    </el-card>
    <!-- 台灯 -->
    <br>
    <el-card class="card2" shadow="always">
      <br>
      <el-slider v-model="value1" vertical height="200px" :disabled="value2==false" format-tooltip="formatTooltip2" @change="tempLightChange">

      </el-slider>
      <div class="block">
        <h2>台 灯</h2>
<!--        <el-button class="icon" icon="el-icon-s-opportunity" circle size="big"></el-button>-->
        <el-tooltip effect="light" content="挂灯连接正常" placement="top">
          <div class="link"  v-if="value2">
            <i class="el-icon-s-opportunity"></i>
          </div>
        </el-tooltip>
        <el-tooltip effect="light" content="挂灯未连接" placement="top">
          <div class="no-link" v-if="!value2">
            <i class="el-icon-s-opportunity" ></i>
          </div>
        </el-tooltip>
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
  <!-- 空调 -->
    <br>
    <el-card class="card2" shadow="always">
      <el-slider v-model="value3" vertical height="200px" :disabled="value4==false" format-tooltip="formatTooltip2" @change="airconditionChange"></el-slider>
      <div class="block">
        <h2>空 调</h2>
<!--        <el-button class="icon" icon="el-icon-ice-cream-round" circle size="big"></el-button>-->
        <el-tooltip effect="light" content="空调连接正常" placement="top">
          <div class="link" v-if="value4">
            <i class="el-icon-ice-cream-round" ></i>
          </div>
        </el-tooltip>
        <el-tooltip effect="light" content="空调未连接" placement="top">
          <div class="no-link"  v-if="!value4">
            <i class="el-icon-ice-cream-round"></i>
          </div>
        </el-tooltip>
        <span class="light" :hidden="value4==false">  {{value3}}℃</span>
        <span class="light_text">温度</span>
        <el-switch
          v-model="value4"
          active-text="已连接"
          inactive-text="未连接"
          @change="switchChange4">
        </el-switch>
        </div>
    </el-card>
  <!-- 饮水机 -->
    <br>
    <el-card class="card2" shadow="always">
      <el-slider v-model="value5" dis vertical height="200px" :disabled="value6==false" format-tooltip="formatTooltip2" @change="waterChange"></el-slider>
      <div class="block">
        <h2>饮水机</h2>
<!--        <el-button class="icon" icon="el-icon-goblet-square-full" circle size="big"></el-button>-->
        <el-tooltip effect="light" content="饮水机连接正常" placement="top">
          <div class="link"  v-if="value6">
            <i class="el-icon-goblet-square-full"></i>
          </div>
        </el-tooltip>
        <el-tooltip effect="light" content="饮水机未连接" placement="top">
          <div class="no-link" v-if="!value6">
            <i class="el-icon-goblet-square-full" ></i>
          </div>
        </el-tooltip>
        <span class="light" :hidden="value6==false">  {{value5}}℃</span>
        <span class="light_text">温度</span>
        <el-switch
          v-model="value6"
          active-text="已连接"
          inactive-text="未连接"
          @change="switchChange6">
        </el-switch>
        </div>
    </el-card>
  </div>
</template>

<script>
  export default {
  data () {
    return {
      value: 3,
      value1: 0,
      value2: true,
      value3: 26,
      value4: true,
      value5: 60,
      value6: true,
      door_value: true,
      temp: 26,
      humid: 60,
      setTemp: [30, 60],
      setHumid: [20, 70],
      openTime: '',
      timeD: 100,
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
      },
      marks3: {
        0: '0',
        20: '20s',
        60: '60s',
        50: {
          style: {
            color: '#1989FA'
          },
          label: this.$createElement('strong', '50s')
        }
      }
    }
  },
  methods: {
    formatTooltip1 (val) {
      return val + '%'
    },
    formatTooltip2 (val) {
      return val + '℃'
    },
    async getRoom1Infomation () {
      const { data: res } = await this.$http.get('room1')
      console.log(res)
      if (res.meta.status !== 200) {
        return this.$message.error('获取主卧室信息失败')
      }
      this.value = res.data.value
      this.value1 = res.data.value1
      this.value2 = res.data.value2
      this.value3 = res.data.value3
      this.value4 = res.data.value4
      this.value5 = res.data.value5
      this.value6 = res.data.value6
      this.door_value = res.data.door_value
      this.temp = res.data.temp
      this.humid = res.data.humid
      this.setTemp = res.data.setTemp
      this.setHumid = res.data.setHumid
    },
    async temChange() {
      let temperature = {
        "low_temp": this.setTemp[0],
        "high_temp": this.setTemp[1]
      }
      const {data: res} = await this.$http.get("room1/tem", {
        params: temperature
      })
      console.log(res)
    },
    async humChange() {
      let humid = {
        "low_hum": this.setHumid[0],
        "high_hum": this.setHumid[1]
      }
      const {data: res} = await this.$http.get("room1/hum", {
        params: humid
      })
      console.log(res)
    },
    async tempLightChange() {
      const { data: res } = await this.$http.put(
              `room1/templight/change/${this.value1}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      console.log(res.meta.status)
      this.$message.success('修改成功')
    },
    async airconditionChange() {
      const { data: res } = await this.$http.put(
              `room1/aircondition/change/${this.value3}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      console.log(res.meta.status)
      this.$message.success('修改成功')
    },
    async waterChange() {
      const { data: res } = await this.$http.put(
              `room1/water/change/${this.value5}`
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
              `room1/lightcon/change/${this.value2}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      console.log(res.meta.status)
      this.$message.success('修改成功')
    },
    async switchChange4() {
      this.connectDev()
      const { data: res } = await this.$http.put(
              `room1/aircon/change/${this.value4}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      console.log(res.meta.status)
      this.$message.success('修改成功')
    },
    async switchChange6() {
      this.connectDev()
      const { data: res } = await this.$http.put(
              `room1/watercon/change/${this.value6}`
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
      if(this.value4) {
        conNum++;
      }
      if(this.value6) {
        conNum++;
      }
      this.value = conNum
      console.log("conDev"+this.value)
    },
    async progressChange() {
      let times = this.openTime.split(':')
      let time
      if(times[0] != 0){
        time = parseInt(times[0]) * 60 + parseInt(times[1])
      }
      else {
        time = parseInt(times[1])
      }
      let stop = setInterval(this.changeDoorTime, time*10)
      let t_this = this
      setTimeout(function (stop) {
        clearInterval(stop)
        alert("time out")
        t_this.sendWarningDoor()
        t_this.sendWarningDoorToCompo()
      }, time*1000,stop)
      // this.sendWarningDoor()
    },
    changeDoorTime() {
      this.timeD = this.timeD - 1
    },
    //给服务器发送门未关请求
    async sendWarningDoor(){
      alert("发送请求")
      const { data: res } = await this.$http.get('warning/door')
      console.log(res)
      if (res.meta.status !== 200) {
        return this.$message.error('获取主卧室信息失败')
      }
      this.$message.success('发送警告')
    },
    //给设备警告组件发送门未关信息
    sendWarningDoorToCompo() {
      alert("已向组件发送请求")
      this.$root.Bus.$emit('doorWarning', '门未关')
    },
    async doorConnect() {
      const { data: res } = await this.$http.put(
              `room1/door/change/${this.door_value}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      console.log(res.meta.status)
      this.$message.success('修改成功')
    }
  },
  created() {
    //主卧室 卫生间 阳台 分别是 room1 room2 room3
    this.getRoom1Infomation();
  }
}
</script>

<style>
  .card1{
    display: flex;
    justify-content: space-between;
    width: 180px;
    height: 100px;
    position: relative;
  }
  .change{
    position: absolute;
    right: 15px;
    bottom: 5px;
    font-size: 15px;
    width: 150px;
    height: 20px;
  }
  .change_text{
    position: absolute;
    right: 10px;
    bottom: 5px;
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
    height: 300px;
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
  .door{
    position: absolute;
    left: 200px;
    top: 20px;
  }
  .eye{
    position: absolute;
    left: 200px;
    top: 20px;
  }
  .link{
     background-color: #ffffff;
     padding-left: 5px;
     /*padding-bottom: 10px;*/
     width: 40px;
     height: 40px;
     border-radius: 30px;
     font-size: 30px;
     /*font-weight: 10px;*/
     font-weight: normal;
     color: #16b82c;
   }
  .no-link{
    background-color: #ffffff;
    padding-left: 5px;
    /*padding-bottom: 10px;*/
    width: 40px;
    height: 40px;
    border-radius: 30px;
    font-size: 30px;
    font-weight: normal;
    color: rgba(255, 0, 0, 0.79);
  }
</style>

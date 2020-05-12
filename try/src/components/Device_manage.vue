<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>设备管理</el-breadcrumb-item>
    </el-breadcrumb>
<!--    &lt;!&ndash; 主卧室 &ndash;&gt;-->
<!--    <el-card shadow="hover" @click.native="room1">-->
<!--      &lt;!&ndash; 路由占位符 &ndash;&gt;-->
<!--      <router-view></router-view>-->
<!--      <el-switch-->
<!--              v-model="value1"-->
<!--              active-text="已连接"-->
<!--              inactive-text="未连接">-->
<!--      </el-switch>-->
<!--      <div class="place">-->
<!--        主卧室-->
<!--      </div>-->
<!--      <div class="icon">-->
<!--        <el-button type="light" icon="el-icon-s-opportunity" circle></el-button>-->
<!--        <el-button type="temperature" icon="el-icon-sunny" circle></el-button>-->
<!--        <el-button type="humidity" icon="el-icon-light-rain" circle></el-button>-->
<!--      </div>-->
<!--    </el-card>-->
<!--    &lt;!&ndash; 卫生间 &ndash;&gt;-->
<!--    <br>-->
<!--    <el-card hadow="hover" @click.native="room2">-->
<!--      &lt;!&ndash; 路由占位符 &ndash;&gt;-->
<!--      <router-view></router-view>-->
<!--      <el-switch-->
<!--              v-model="value2"-->
<!--              active-text="已连接"-->
<!--              inactive-text="未连接">-->
<!--      </el-switch>-->
<!--      <div class="place">-->
<!--        卫生间-->
<!--      </div>-->
<!--      <div class="icon">-->
<!--        <el-button type="light" icon="el-icon-s-opportunity" circle></el-button>-->
<!--        <el-button type="temperature" icon="el-icon-sunny" circle></el-button>-->
<!--        <el-button type="humidity" icon="el-icon-light-rain" circle></el-button>-->
<!--      </div>-->
<!--    </el-card>-->
<!--    &lt;!&ndash; 阳台 &ndash;&gt;-->
<!--    <br>-->
<!--    <el-card shadow="hover" @click.native="room3">-->
<!--      &lt;!&ndash; 路由占位符 &ndash;&gt;-->
<!--      <router-view></router-view>-->
<!--      <el-switch-->
<!--              v-model="value3"-->
<!--              active-text="已连接"-->
<!--              inactive-text="未连接">-->
<!--      </el-switch>-->
<!--      <div class="place">-->
<!--        阳台-->
<!--      </div>-->
<!--      <div class="icon">-->
<!--        <el-button type="light" icon="el-icon-s-opportunity" circle></el-button>-->
<!--        <el-button type="temperature" icon="el-icon-sunny" circle></el-button>-->
<!--        <el-button type="humidity" icon="el-icon-light-rain" circle></el-button>-->
<!--      </div>-->
<!--    </el-card>-->
<!--    &lt;!&ndash; 添加 &ndash;&gt;-->
<!--    <br>-->
<!--    <el-card>-->
<!--      <el-button icon="el-icon-plus" circle class="plus"></el-button>-->
<!--    </el-card>-->
    <!-- 主卧室 -->
    <el-card shadow="hover" @click.native="room1" class="room1">
      <!-- 路由占位符 -->
      <!--      <router-view></router-view>-->
      <el-tooltip effect="light" content="Wi-Fi连接正常" placement="bottom">
        <div class="wifi" v-if="value1">
          <i class="el-icon-check"></i>
        </div>
      </el-tooltip>
      <el-tooltip effect="light" content="Wi-Fi未连接" placement="bottom">
        <div class="no-wifi" v-if="!value1">
          <i class="el-icon-close"></i>
        </div>
      </el-tooltip>
      <div class="place">
        主卧室
      </div>
      <div class="icon">
        <el-row :gutter="20">
          <el-col :span="4">
            <el-tooltip effect="light" content="温度正常" placement="top">
              <div class="link" v-if="temp1">
                <i class="el-icon-sunny" ></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="温度异常" placement="top">
              <div class="no-link" v-if="!temp1">
                <i class="el-icon-sunny" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="湿度正常" placement="top">
              <div class="link"  v-if="hum1">
                <i class="el-icon-light-rain"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="湿度异常" placement="top">
              <div class="no-link" v-if="!hum1">
                <i class="el-icon-light-rain" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="台灯连接正常" placement="top">
              <div class="link"  v-if="light1">
                <i class="el-icon-s-opportunity"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="台灯未连接" placement="top">
              <div class="no-link" v-if="!light1">
                <i class="el-icon-s-opportunity" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="门连接正常" placement="top">
              <div class="link"  v-if="door1">
                <i class="el-icon-s-home"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="门未连接" placement="top">
              <div class="no-link" v-if="!door1">
                <i class="el-icon-s-home" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="空调连接正常" placement="top">
              <div class="link" v-if="air1">
                <i class="el-icon-ice-cream-round" ></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="空调未连接" placement="top">
              <div class="no-link"  v-if="!air1">
                <i class="el-icon-ice-cream-round"></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="饮水机连接正常" placement="top">
              <div class="link"  v-if="water1">
                <i class="el-icon-goblet-square-full"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="饮水机未连接" placement="top">
              <div class="no-link" v-if="!water1">
                <i class="el-icon-goblet-square-full" ></i>
              </div>
            </el-tooltip>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <!-- 卫生间 -->
    <br>
    <el-card hadow="hover" @click.native="room2" class="room2">
      <!-- 路由占位符 -->
      <!--      <router-view></router-view>-->
      <el-tooltip effect="light" content="Wi-Fi连接正常" placement="bottom">
        <div class="wifi" v-if="value2">
          <i class="el-icon-check"></i>
        </div>
      </el-tooltip>
      <el-tooltip effect="light" content="Wi-Fi未连接" placement="bottom">
        <div class="no-wifi" v-if="!value2">
          <i class="el-icon-close"></i>
        </div>
      </el-tooltip>
      <div class="place">
        卫生间
      </div>
      <div class="icon">
        <el-row :gutter="20" class="el-row-2">
          <el-col :span="4">&nbsp;</el-col>
          <el-col :span="4">&nbsp;</el-col>
          <el-col :span="4">&nbsp;</el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="温度正常" placement="top">
              <div class="link" v-if="temp2">
                <i class="el-icon-sunny" ></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="温度异常" placement="top">
              <div class="no-link" v-if="!temp2">
                <i class="el-icon-sunny" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="湿度正常" placement="top">
              <div class="link"  v-if="hum2">
                <i class="el-icon-light-rain"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="湿度异常" placement="top">
              <div class="no-link" v-if="!hum2">
                <i class="el-icon-light-rain" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="挂灯连接正常" placement="top">
              <div class="link"  v-if="light2">
                <i class="el-icon-s-opportunity"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="挂灯未连接" placement="top">
              <div class="no-link" v-if="!light2">
                <i class="el-icon-s-opportunity" ></i>
              </div>
            </el-tooltip>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <!-- 阳台 -->
    <br>
    <el-card shadow="hover" @click.native="room3" class="room3">
      <!-- 路由占位符 -->
      <!--      <router-view></router-view>-->
      <el-tooltip effect="light" content="Wi-Fi连接正常" placement="bottom">
        <div class="wifi" v-if="value3">
          <i class="el-icon-check"></i>
        </div>
      </el-tooltip>
      <el-tooltip effect="light" content="Wi-Fi未连接" placement="bottom">
        <div class="no-wifi" v-if="!value3">
          <i class="el-icon-close"></i>
        </div>
      </el-tooltip>
      <div class="place">
        阳台
      </div>
      <div class="icon">
        <el-row :gutter="20" class="el-row-2">
          <el-col :span="4">&nbsp;</el-col>
          <el-col :span="4">&nbsp;</el-col>
          <el-col :span="4">&nbsp;</el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="温度正常" placement="top">
              <div class="link" v-if="temp3">
                <i class="el-icon-sunny" ></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="温度异常" placement="top">
              <div class="no-link" v-if="!temp3">
                <i class="el-icon-sunny" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="湿度正常" placement="top">
              <div class="link"  v-if="hum3">
                <i class="el-icon-light-rain"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="湿度异常" placement="top">
              <div class="no-link" v-if="!hum3">
                <i class="el-icon-light-rain" ></i>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="4">
            <el-tooltip effect="light" content="挂灯连接正常" placement="top">
              <div class="link"  v-if="light3">
                <i class="el-icon-s-opportunity"></i>
              </div>
            </el-tooltip>
            <el-tooltip effect="light" content="挂灯未连接" placement="top">
              <div class="no-link" v-if="!light3">
                <i class="el-icon-s-opportunity" ></i>
              </div>
            </el-tooltip>
          </el-col>
        </el-row>
      </div>
    </el-card>

  </div>
</template>

<script>
  export default {
    data () {
      return {
        value1: true,
        value2: true,
        value3: true,
        temp1: true,
        hum1: true,
        light1: true,
        door1: false,
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
      room1 () {
        console.log("room1 click ")
        this.$router.push({ path: '/room1' })
      },
      room2 () {
        this.$router.push({ path: '/room2' })
      },
      room3 () {
        this.$router.push({ path: '/room3' })
      },
      async get_manage_information() {
        const {data: res} = await this.$http.get('manage')
        console.log(res)
        if (res.meta.status !== 200) {
          return this.$message.error('获取信息失败')
        }
        this.value1 = res.data.value1
        // this.wifi1OK = res.data.wifi1OK
        this.value2 = res.data.value2
        this.value3 = res.data.value3
        // this.wifi2OK = res.data.wifi2OK
        // this.wifi3OK = res.data.wifi3OK
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
        // this.doorClosed = res.data.doorClosed
        this.air1 = res.data.air1
        this.water1 = res.data.water1
      }
    },
    created() {
      this.get_manage_information()
    }
  }
</script>

<style lang="less" scoped>
  /*.el-card{*/
  /*  display: flex;*/
  /*  justify-content: space-between;*/
  /*  height: 200px;*/
  /*  width: 550px;*/
  /*  position: relative;*/
  /*}*/
  /*.el-switch{*/
  /*  position: absolute;*/
  /*  right: 5%;*/
  /*  top: 10px;*/
  /*}*/
  /*.place{*/
  /*  position: absolute;*/
  /*  left: 5%;*/
  /*  top: 75%;*/
  /*}*/
  /*.icon{*/
  /*  position: absolute;*/
  /*  left: 65%;*/
  /*  top: 70%;*/
  /*}*/
  /*.plus{*/
  /*  position: absolute;*/
  /*  right: 50%;*/
  /*  top: 50%;*/
  /*}*/
  .el-row-2 {
    left: 100px;
  }
  .el-card{
    display: flex;
    justify-content: space-between;
    height: 200px;
    width: 550px;
    position: relative;
  }
  .el-switch{
    position: absolute;
    right: 5%;
    top: 10px;
  }
  .place{
    position: absolute;
    left: 5%;
    top: 75%;
    font-size: 25px;
    color: #767676;
    font-weight: bold;
  }
  .wifi{
    background-color: #ffffff;
    padding-left: 5px;
    padding-bottom: 10px;
    width: 40px;
    height: 40px;
    border-radius: 40px;
    position: absolute;
    right: 5%;
    font-size: 30px;
    /*font-weight: 10px;*/
    font-weight: normal;
    color: #16b82c;
  }
  .no-wifi{
    background-color: #ffffff;
    padding-left: 5px;
    padding-bottom: 10px;
    width: 40px;
    height: 40px;
    border-radius: 40px;
    position: absolute;
    right: 5%;
    font-size: 30px;
    /*font-weight: 10px;*/
    font-weight: normal;
    color: rgba(255, 0, 0, 0.79);
  }
  .icon{
    position: absolute;
    left: 55%;
    top: 70%;
    width: 210px;
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
  .room1{
    background-image: url("../assets/m1.jpeg");
  }
  .room2{
    background-image: url("../assets/m2.jpg");
  }
  .room3{
    background-image: url("../assets/m3.jpeg");
  }
</style>

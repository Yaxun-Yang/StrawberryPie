<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>智能养护</el-breadcrumb-item>
      <el-breadcrumb-item>植物管理</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card class="special_info">
      <el-row>
        <el-col :span="10" :offset="3">室内温度: {{indoor_temperature + '°C'}}</el-col>
        <el-col :span="10">室外温度: {{outdoor_temperature + '°C'}}</el-col>
      </el-row>
      <el-row>
        <el-col :span="10" :offset="3">室内湿度: {{indoor_humidity + '%rh'}}</el-col>
        <el-col :span="10">室外湿度: {{outdoor_humidity + '%rh'}}</el-col>
      </el-row>
    </el-card>

    <el-card v-for="item in plants" :key="item">
      <div class="info_layout">
        <el-row>
          <!-- 上传图片 -->
          <el-col :offset="8">
            <el-avatar shape="square" :size="100" :src="require('../assets/plant.png')" :fit="fill"></el-avatar>
            <div class="plant_name">盆栽</div>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="20">
            盆栽含水量:
            <el-progress :percentage="item.percent" stroke-width="10" :color="colors"></el-progress>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="24">
            浇水时间:
            <div class="water_time" v-for="subItem in item.timeList" :key="subItem">
<!--              <span v-if="subItem.time">-->
<!--                <el-time-picker-->
<!--                        v-model="subItem.time"-->
<!--                        value-format="HH:mm:ss"-->
<!--                        placeholder="任意时间点"-->
<!--                        size="mini"-->
<!--                        id="1"-->
<!--                        disabled-->
<!--                ></el-time-picker>-->
<!--              </span>-->
<!--              <span v-else>-->
                <el-time-picker
                        v-model="subItem.time"
                        placeholder="任意时间点"
                        value-format="HH:mm:ss"
                        size="mini"
                        id="1"
                        @change="getWaterTime(subItem)"
                ></el-time-picker>
<!--              </span>-->
              <el-button type="text" @click="deleteWaterTime(item.plantId, subItem.timeId)">删除</el-button>
            </div>
            <el-button type="text" @click="addWaterTime(item)">新建</el-button>
          </el-col>
        </el-row>
        <!-- 第五行 -->
        <el-row>
          <el-col :span="12">
            浇水量/ml:
            <div class="watering_amount">
              <el-input
                      class="water_input"
                      v-model="item.amount"
                      type="text"
                      placeholder="请输入具体数字"
                      size="mini"
                      @change="getWateringAmount(item)"
              ></el-input>
            </div>
          </el-col>
        </el-row>
      </div>
      <el-button class="delete_plant_btn" type="text" @click="removePlantById(item.plantId)">删除植物</el-button>
    </el-card>

    <el-button class="new_plant_btn" type="primary" @click="addPlant">新建植物</el-button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        indoor_temperature: '',
        outdoor_temperature: '',
        indoor_humidity: '',
        outdoor_humidity: '',
        // plants: [],
        colors: [
          //进度条颜色变化
          { color: '#f56c6c', percentage: 20 },
          { color: '#e6a23c', percentage: 40 },
          { color: '#5cb87a', percentage: 60 },
          { color: '#1989fa', percentage: 80 },
          { color: '#6f7ad3', percentage: 100 }
        ],
        plants: [
          {
            plantId: 28,
            percent: 30,
            amount: 200,
            imageUrl: '',
            timeList: [
              {
                // time: 'Thu Mar 19 2020 23:39:24 GMT+0800 (中国标准时间)',
                time: '23:39:24',
                timeId: 1
              }
            ]
          }
        ]
      }
    },
    created() {
      // 每过一小时刷新一次数据（为了刷新温度和湿度）
      this.getPlantInfomation(),
              window.setInterval(() => {
                setTimeout(this.getPlantInfomation, 0)
              }, 3600000)
    },
    methods: {
      async getPlantInfomation() {
        const { data: res } = await this.$http.get('plant')
        console.log(res)
        if (res.meta.status !== 200) {
          return this.$message.error('获取植物信息失败')
        }
        this.indoor_temperature = res.data.indoor_temperature
        this.outdoor_temperature = res.data.outdoor_temperature
        this.indoor_humidity = res.data.indoor_humidity
        this.outdoor_humidity = res.data.outdoor_humidity
        this.plants = res.data.plantList
      },

      // 点击按钮，删除浇水时间
      async deleteWaterTime(plantId, timeId) {
        // 弹框询问用户是否删除
        const confirmResult = await this.$confirm('是否删除该时间?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).catch(err => {
          return err
        })
        if (confirmResult !== 'confirm') {
          return this.$message.info('已取消删除')
        }
        // 确认删除
        const { data: res } = await this.$http.delete(
                `users/${plantId}/amount/${timeId}`
        )
        if (res.meta.status !== 200) {
          return this.$message.error('删除时间失败')
        }
        for (var a = 0; a < this.plants.length; a++) {
          if (this.plants[a].plantId === res.data.plantId) {
            this.plants[a].timeList = res.data.timeList
          }
        }
        this.$message.success('删除时间成功')
      },

      // 点击按钮，新建浇水时间
      async addWaterTime(item) {
        const { data: res } = await this.$http.post(`plant/${item.plantId}/time`)
        if (res.meta.status !== 201) {
          return this.$message.error('操作失败')
        }

        for (var a = 0; a < this.plants.length; a++) {
          if (this.plants[a].plantId == res.data.plantId) {
            this.plants[a].timeList = res.data.timeList
          }
        }
        // this.$message.success('添加时间成功')
      },
      //修改浇水时间
      async getWaterTime(subItem) {
        console.log('fixhhhkkjkkjjk')
        const { data: res } = await this.$http.put(
                `users/${subItem.timeId}/time/${subItem.time}`
        )
        if (res.meta.status !== 200) {
          return this.$message.error('修改失败，请重新输入')
        }
        this.$message.success('修改成功')
      },
      // 修改浇水量
      async getWateringAmount(item) {
        const { data: res } = await this.$http.put(
                `users/${item.plantId}/amount/${item.amount}`
        )
        if (res.meta.status !== 200) {
          return this.$message.error('修改失败，请重新输入')
        }
        this.plants = res.data.plantList
        this.$message.success('修改成功')
      },

      // 点击按钮，删除所在卡片
      async removePlantById(plantId) {
        // 弹框询问用户是否删除
        const confirmResult = await this.$confirm(
                '此操作将永久删除该植物, 是否继续?',
                '提示',
                {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
                }
        ).catch(err => {
          return err
        })
        if (confirmResult !== 'confirm') {
          return this.$message.info('已取消删除')
        }
        // 确认删除
        const { data: res } = await this.$http.delete(`plant/${plantId}`)
        if (res.meta.status !== 200) {
          return this.$message.error('删除植物失败')
        }
        this.$message.success('删除植物成功')
        this.plants = res.data.plantList
      },

      // 点击按钮，添加卡片
      async addPlant() {
        const { data: res } = await this.$http.post('plant')
        if (res.meta.status !== 201) {
          return this.$message.error('添加植物失败')
        }
        this.$message.success('添加植物成功')
        this.plants = res.data.plantList
      }
    }
  }
</script>

<style lang="less" scoped>
  // 卡片总布局
  .el-card {
    margin-top: 30px;
    padding: 0;
    background-color: #dcdfe6;
    border-radius: 5px;
    min-height: 100px;
    font-size: small;
  }
  .special_info {
    background-color: #eee;
  }
  // 上传图片
  .plant_name {
    position: relative;
    left: 40px;
  }

  // 右侧信息布局
  .info_layout {
    width: 90%;
    position: relative;
    left: 10%;
  }
  .el-row {
    margin: 15px 0 15px 0;
    &:first-child {
      margin-top: 0;
    }
  }
  .el-progress {
    // 含水量
    font-weight: normal;
  }
  .water_time {
    // 浇水时间
    margin-top: 5px;
  }
  .el-button {
    margin: 5px 0 0 10px;
    padding: 0;
    width: 10px;
  }
  .watering_amount {
    // 浇水量
    margin-top: 5px;
  }
  .el-input {
    width: 220px !important;
  }
  .delete_plant_btn {
    margin: 0;
    padding: 0;
    position: relative;
    left: 0%;
  }
  // 新建卡片
  .new_plant_btn {
    margin: 20px auto 0;
    width: 100px;
    height: 40px;
    font-size: 15px;
    position: relative;
    left: 40%;
  }
</style>

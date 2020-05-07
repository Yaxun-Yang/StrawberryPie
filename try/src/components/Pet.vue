<template>
    <div>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>智能养护</el-breadcrumb-item>
            <el-breadcrumb-item>宠物喂养</el-breadcrumb-item>
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

        <el-card v-for="item in pets" :key="item">
            <div class="info_layout">
                <el-row>
                    <!-- 上传图片 -->
                    <el-col :offset="8">
                        <el-avatar shape="square" :size="100" :src="require('../assets/pet.png')" :fit="fill"></el-avatar>
                        <div class="pet_name">{{item.petName}}</div>
                    </el-col>
                </el-row>

                <el-row>
                    <el-col :span="20">
                        食物剩余量:
                        <el-progress :percentage="item.percent" stroke-width="10" :color="colors"></el-progress>
                    </el-col>
                </el-row>

                <el-row>
                    <el-col :span="24">
                        喂食时间:
                        <div class="feed_time" v-for="subItem in item.timeList" :key="subItem">
<!--              <span v-if="subItem.time">-->
<!--                <el-time-picker-->
<!--                        v-model="subItem.time"-->
<!--                        placeholder="任意时间点"-->
<!--                        value-format="HH:mm:ss"-->
<!--                        size="mini"-->
<!--                        id="1"-->
<!--                        disabled-->
<!--                ></el-time-picker>-->
<!--              </span>-->
<!--                            <span v-else>-->
                <el-time-picker
                        v-model="subItem.time"
                        value-format="HH:mm:ss"
                        placeholder="任意时间点"
                        size="mini"
                        id="1"
                        @change="getfeedTime(subItem)">
                </el-time-picker>
<!--              </span>-->
                            <el-button type="text" @click="deletefeedTime(item.petId, subItem.timeId)">删除</el-button>
                        </div>
                        <el-button type="text" @click="addfeedTime(item)">新建</el-button>
                    </el-col>
                </el-row>
                <!-- 第五行 -->
                <el-row>
                    <el-col :span="12">
                        喂食量/mg:
                        <div class="feed_amount">
                            <el-input
                                    class="feed_input"
                                    v-model="item.amount"
                                    type="text"
                                    placeholder="请输入具体数字"
                                    size="mini"
                                    @change="getfeedAmount(item)"
                            ></el-input>
                        </div>
                    </el-col>
                </el-row>
            </div>
            <el-button class="delete_pet_btn" type="text" @click="removePetById(item.petId)">删除宠物</el-button>
        </el-card>

        <el-button class="new_pet_btn" type="primary" @click="addPet">新建宠物</el-button>
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
                // pets: [],
                colors: [
                    //进度条颜色变化
                    { color: '#f56c6c', percentage: 20 },
                    { color: '#e6a23c', percentage: 40 },
                    { color: '#5cb87a', percentage: 60 },
                    { color: '#1989fa', percentage: 80 },
                    { color: '#6f7ad3', percentage: 100 }
                ],
                pets: [
                  // {
                  //   peId: 28,
                  //   percent: 60,
                  //   amount: 200,
                  //   imageUrl: '',
                  //   timeList: [
                  //     {
                  //       time: 'Thu Mar 19 2020 12:24:04 GMT+0800 (中国标准时间)',
                  //       timeId: 1
                  //     }
                  //   ]
                  // }
                ]
            }
        },
        created() {
            this.getPetInfomation(),
                window.setInterval(() => {
                    setTimeout(this.getPetInfomation, 0)
                }, 3600000)
        },
        methods: {
            async getPetInfomation() {
                const { data: res } = await this.$http.get('pet')
                console.log(res)
                if (res.meta.status !== 200) {
                    return this.$message.error('获取宠物信息失败')
                }
                this.indoor_temperature = res.data.indoor_temperature
                this.outdoor_temperature = res.data.outdoor_temperature
                this.indoor_humidity = res.data.indoor_humidity
                this.outdoor_humidity = res.data.outdoor_humidity
                this.pets = res.data.petList
            },

            // 点击按钮，删除喂食时间
            async deletefeedTime(petId, timeId) {
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
                    `users/${petId}/time/${timeId}`
                )
                if (res.meta.status !== 200) {
                    return this.$message.error('删除时间失败')
                }
                for (var a = 0; a < this.pets.length; a++) {
                    if (this.pets[a].plantId === res.data.petId) {
                        this.pets[a].timeList = res.data.timeList
                    }
                }
                this.$message.success('删除时间成功')
            },

            // 点击按钮，新建喂食时间
            async addfeedTime(item) {
                const { data: res } = await this.$http.post(
                    `pet/${item.petId}/time`
                )
                if (res.meta.status !== 201) {
                    return this.$message.error('添加时间失败')
                }
                for (var a = 0; a < this.pets.length; a++) {
                    if (this.pets[a].petId === res.data.petId) {
                        this.pets[a].timeList = res.data.timeList
                    }
                }
                this.$message.success('添加时间成功')
            },
            //修改喂食时间
            async getfeedTime(subItem) {
                const { data: res } = await this.$http.put(
                    `pet/${subItem.timeId}/time/${subItem.time}`
                )
                if (res.meta.status !== 200) {
                    return this.$message.error('修改失败，请重新输入')
                }
                this.$message.success('修改成功')
            },
            // 修改喂食量
            async getfeedAmount(item) {
                const { data: res } = await this.$http.put(
                    `pet/${item.petId}/amount/${item.amount}`
                )
                if (res.meta.status !== 200) {
                    return this.$message.error('修改失败，请重新输入')
                }
                console.log(res.meta.status)
                this.$message.success('修改成功')
            },

            // 点击按钮，删除所在卡片
            async removePetById(petId) {
                // 弹框询问用户是否删除
                const confirmResult = await this.$confirm(
                    '此操作将永久删除该宠物, 是否继续?',
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
                const { data: res } = await this.$http.delete(`pet/${petId}`)
                if (res.meta.status !== 200) {
                    return this.$message.error('删除宠物失败')
                }
                this.$message.success('删除宠物成功')
                this.pets = res.data.petList
            },

            // 点击按钮，添加卡片
            async addPet() {
                const { data: res } = await this.$http.post('pet/add')
                if (res.meta.status !== 201) {
                    return this.$message.error('添加宠物失败')
                }
                this.$message.success('添加宠物成功')
                this.pets = res.data.petList
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
    .pet_name {
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
    .feed_time {
        // 浇水时间
        margin-top: 5px;
    }
    .el-button {
        margin: 5px 0 0 10px;
        padding: 0;
        width: 10px;
    }
    .feed_amount {
        // 浇水量
        margin-top: 5px;
    }
    .el-input {
        width: 220px !important;
    }
    .delete_pet_btn {
        margin: 0;
        padding: 0;
        position: relative;
        left: 0%;
    }
    // 新建卡片
    .new_pet_btn {
        margin: 20px auto 0;
        width: 100px;
        height: 40px;
        font-size: 15px;
        position: relative;
        left: 40%;
    }
</style>

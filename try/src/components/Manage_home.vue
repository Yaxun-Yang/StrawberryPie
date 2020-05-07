<template>
    <div class="back">
        <el-container class="home-container">
            <!-- 头部区域 -->
            <el-header>
                <div>
                    <img src="../assets/main.png"/>
                    <span>智能宿舍监控系统</span>
                </div>
                <el-menu
                        background-color="#373d41"
                        text-color="#fff"
                        active-text-color="#409eff"
                        mode="horizontal"
                        :default-active="activePath"
                        :router="true"
                >
<!--                    <el-menu-item index="/login" @click="saveNavState('/manage_home')">首页</el-menu-item>-->
                    <el-menu-item index="logout" @click="saveNavState('/logout')">退出</el-menu-item>
                </el-menu>
            </el-header>
            <!-- 页面主题区域 -->
            <el-container>
                <!-- 右侧内容主题 -->
                <el-main>
                    <!-- 路由占位符 -->
                    <router-view></router-view>
                    <el-card class="box-card" shadow="never">
                        <el-row gutter="10">
                            <el-col :span="4">
                                <el-avatar
                                        class="img"
                                        :size="70"
                                        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                                ></el-avatar>
                            </el-col>
                            <el-col :span="5" class="try">
                                <div class="container1">
                                    <div>{{manager.name}}</div>
                                    <div class="stu">管理员</div>
                                </div>
                            </el-col>
                            <el-col :span="10">
                                <div class="container1">
                                    <div class="name">{{manager.address}}</div>
                                    <div id="welcome">
                                        <strong>Hi~ 欢迎使用智能宿舍系统</strong>
                                    </div>
                                </div>
                            </el-col>
                        </el-row>
                    </el-card>
                    <br />
                    <el-card class="box" shadow="never">
                        <el-row>
                            <el-col :span="7">
                                <strong>宿舍信息:</strong>
                            </el-col>
                        </el-row>
                        <div>
                            <hr class="line" />
                        </div>
                        <el-row>
                            <el-col :span="6">
                                <i class="el-icon-s-data"></i>
                                楼栋数：
                                <span>{{manager.building}}</span>
                            </el-col>
                            <el-col :span="6">
                                <i class="el-icon-s-marketing"></i>
                                楼层数：
                                <span>{{manager.floor}}</span>
                            </el-col>
                            <el-col :span="6">
                                <i class="el-icon-s-home"></i>
                                房间数：
                                <span>{{manager.room}}</span>
                            </el-col>
                            <el-col :span="6">
                                <i class="el-icon-user-solid"></i>
                                总人数：
                                <span>{{manager.people}}</span>
                            </el-col>
                        </el-row>
                    </el-card>
                    <br />
                    <el-card class="box-card1" shadow="never">
                        <div class="status">
                            <strong>危险警报：</strong>
                            <span>一切正常</span>
                            <span>
                <i class="el-icon-circle-check"></i>
              </span>
                        </div>
                        <div class="select">
                            <strong>功能选择：</strong>
                        </div>
                        <el-row>
                            <el-col :span="12">
                                <router-link :to="{ path: '/exception'}">
                                    <el-card class="card1" shadow="never">
                                        <div>
                                            <br/>
                                            <img height="25px" width="200px" src="../assets/exception.png">
                                        </div>
                                    </el-card>
                                </router-link>
                            </el-col>
                            <el-col :span="12">
                                <router-link :to="{ path: '/lamp'}">
                                    <el-card class="card1">
                                        <div>
                                            <br/>
                                            <img class="lamp" height="45px" width="130px" src="../assets/lamp.png">
                                        </div>
                                    </el-card>
                                </router-link>
                            </el-col>
                        </el-row>
                        <br />
                        <el-row>
                            <el-col :span="12">
                                <router-link :to="{ path: '/students'}">
                                    <el-card class="card1">
                                        <div>
                                            <br/>
                                            <img class="students" height="40px" width="150px" src="../assets/students.png">
                                        </div>
                                    </el-card>
                                </router-link>
                            </el-col>
                            <el-col :span="12">
                                <router-link :to="{ path: '/informationadmin'}">
                                    <el-card class="card1">
                                        <div>
                                            <br/>
                                            <img class="" height="35px" width="240px" src="../assets/information.png">
                                        </div>
                                    </el-card>
                                </router-link>
                            </el-col>
                        </el-row>
                    </el-card>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                manager: {
                    name: '',
                    id: '',
                    type: '宿舍管理员',
                    dept: '后勤',
                    building: '',
                    floor: '',
                    room: '',
                    people: '',
                    address: '铁道校区-新1舍、新2舍'
                }
            }
        },
        created() {
            // this.getManager()
            //用户和管理员登录要用学工号和密码，username为学工号
            this.manager.id = window.sessionStorage.getItem('id')
            this.manager.name = window.sessionStorage.getItem('name')
            this.manager.type = window.sessionStorage.getItem('type')
            this.manager.dept = window.sessionStorage.getItem('dept')
            this.manager.building = window.sessionStorage.getItem('building')
            this.manager.floor = window.sessionStorage.getItem('floor')
            this.manager.room = window.sessionStorage.getItem('room')
            this.manager.people = window.sessionStorage.getItem('people')
            this.manager.address = window.sessionStorage.getItem('address')
        },
        methods: {
            async getManager() {
                const { data: res } = await this.$http.get('manager', {
                    param: this.manager.id
                })
                if (res.meta.status !== 200) {
                    return this.$message.error('获取管理员信息失败')
                }
                this.manager = res.data.manager
                console.log(res)
            }
        }
    }
</script>

<style lang='less' scoped>
    .lamp{
        margin-left: 45px;
        margin-top: 0px
    }

    .students {
        margin-left: 25px;
        margin-top: 0px
    }

    .exception {
        color: red;
        margin-left: 65px;
        margin-top: 0px
    }

    .picture {
        height: 40px;
        margin-left: 85px;
    }
    .building {
        margin-top: 0px;
    }
    .card2 {
        padding: 0px;
        width: 140px;
        height: 40px;
    }

    .status {
        margin-top: 8px;
    }

    .back {
        background-color: #eaedf1;
        height: 100%;
        width: 100%;
    }

    .home-container {
        height: 100%;
        width: 45%;
        position: absolute;
        left: 28%;
    }

    .el-header {
        background-color: #373d41;
        display: flex;
        justify-content: space-between;
        padding-left: 0;
        align-items: center;
        color: #fff;
        font-size: 20px;
        > div {
            display: flex;
            align-items: center;
            span {
                margin-left: 15px;
            }
        }
    }

    .el-aside {
        background-color: #333744;
        .el-menu {
            border-right: none;
        }
    }

    .el-main {
        background-color: #fff;
    }

    .select {
        margin-bottom: 10px;
    }

    .name {
        margin-top: 2px;
    }
    #welcome {
        margin-top: 10px;
        font-family: 'PingFang SC';
    }

    .stu {
        margin-top: 10px;
    }

    .container1 {
        margin-top: 2px;
        font-size: 17px;
    }


    .card1{
        width: 280px;
        height: 100px;
        border-color:#333744;
        border-radius: 15px;
        border-width: 2px;
    }

    .status {
        height: 32px;
    }

    .line {
        background-color: #2b4b6b;
    }

    .box-card {
        height: 100px;
        border-color: pink;
        border-radius: 15px;
        border-width: 2px;
    }

    .box {
        height: 110px;
        border-color: #2b4b6b;
        border-radius: 15px;
        border-width: 2px;
    }

    .user {
        height: 70px;
        width: 70px;
    }

    .box-card1 {
        height: 345px;
        border-color: #333744;
        border-radius: 15px;
        border-width: 2px;
    }

    .try {
        width: 86px;
    }

    .img {
        margin-top: 0px;
    }
    img {
        width: 100px;
    }
</style>

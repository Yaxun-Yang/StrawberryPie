<template>
    <!-- 上部 -->
    <div>
        <strong>首页</strong>
        <br />
        <br />
        <!-- 上部 -->
        <el-card class="box-card" shadow="never">
            <el-row gutter="10">
                <el-col :span="4">
                    <el-avatar class="user">user</el-avatar>
                </el-col>
                <el-col :span="5" class="try">
                    <div class="container1">
                        <div>{{users_info.username}}</div>
                        <div class="stu">学生</div>
                    </div>
                </el-col>
                <el-col :span="10">
                    <div class="container1">
                        <div class="name">{{users_info.classnum}}</div>
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
                    <strong>共享成员</strong>
                </el-col>
                <el-col :span="10">{{users_info.roomnumber}}</el-col>
            </el-row>
            <div>
                <hr class="line" />
            </div>
            <el-row>
                <div v-for="fre in users_info.roommate" :key="fre">
                    <el-col :span="2">
                        <el-avatar class="roommate">user</el-avatar>
                    </el-col>
                    <el-col :span="3">
                        <div class="name">{{fre}}</div>
                    </el-col>
                </div>
                <!--        <el-col :span="2">-->
                <!--          <el-avatar class="roommate">user</el-avatar>-->
                <!--        </el-col>-->
                <!--        <el-col :span="3">-->
                <!--          <div class="name">阳雅珣</div>-->
                <!--        </el-col>-->
            </el-row>
        </el-card>
        <br />
        <el-card class="box-card1" shadow="never">
            <div class="status">
                <strong>状态：</strong>
                <span>一切正常</span>
                <span>
          <i class="el-icon-circle-check"></i>
        </span>
            </div>
            <div class="select">
                <strong>场景选择：</strong>
            </div>
            <el-row>
                <el-col :span="8">
                    <el-card class="card1">
                        <div>
                            <img height="150px"  src="../assets/bedroom.png">
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card class="card1">
                        <div>

                            <img class="washroom" height="160px"  width="90px" src="../assets/washroom.png">

                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card class="card1">
                        <div>
                            <img class="yangtai" height="130px"  width="" src="../assets/yangai.png">
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </el-card>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                users_info: {
                },
                username:'',
            }
        },
        created() {
            this.getMenuList()

        },
        methods: {
            getMenuList() {
                // this.users_info = window.sessionStorage.getItem('data')
                // console.log("Welcome" + this.users_info)
                this.users_info["username"] = window.sessionStorage.getItem("user_name")
                this.users_info["roomnumber"] = window.sessionStorage.getItem("roomnumber")
                this.users_info["classnum"] = window.sessionStorage.getItem("classnum")
                this.users_info["roommate"] = window.sessionStorage.getItem("roommate").split("+")
            }
        }
    }
</script>
<style lang="less" scoped>
    .yangtai {
        margin-top: 10px;
        margin-left: 25px;
    }
    .washroom {
        margin-top: 0px;
        margin-left: 20px;
    }
    .select {
        margin-bottom: 10px;
    }

    .name {
        margin-top: 10px;
    }
    #welcome {
        margin-top: 10px;
        font-family: 'PingFang SC';
    }

    .stu {
        margin-top: 10px;
    }

    .container1 {
        margin-top: 7px;
        font-size: 17px;
    }
    .card1 {
        width: 170px;
        height: 180px;
    }
    .status {
        height: 32px;
    }

    .line {
        background-color: #2b4b6b;
    }

    .box-card {
        height: 110px;
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
        height: 290px;
        border-color: #373d41;
        border-radius: 15px;
        border-width: 2px;
    }

    .try {
        width: 86px;
    }
</style>

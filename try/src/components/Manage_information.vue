<template>
    <div class="back">
        <el-container class="home-container">
            <!-- 头部区域 -->
            <el-header>
                <div>
                    <img src="../assets/heima.png" alt />
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
                    <el-menu-item index="/welcome" @click="saveNavState('/manage_home')">首页</el-menu-item>
                    <el-menu-item index="logout" @click="saveNavState('/logout')">退出</el-menu-item>
                </el-menu>
            </el-header>
            <!-- 页面主题区域 -->
            <el-container>
                <!-- 右侧内容主题 -->
                <el-main>
                    <!-- 路由占位符 -->
                    <router-view></router-view>
                    <h4>个人信息查看和密码修改</h4>
                    <el-card class="box-card">
                        <el-card class="box-card1" shadow="never">
                            <strong>姓名：{{manager.name}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>学工号：{{manager.id}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>身份类型：{{manager.type}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>部门名称：{{manager.dept}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>楼栋数：{{manager.building}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>楼层数：{{manager.floor}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>房间数: {{manager.room}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>总人数: {{manager.people}}</strong>
                        </el-card>
                        <el-card class="box-card2" shadow="never">
                            <strong>管理宿舍地址：{{manager.address}}</strong>
                        </el-card>
                        <div>
                            <el-button class="button" type="text" @click="dialogFormVisible = true">修改密码</el-button>
                        </div>
                    </el-card>
                    <el-dialog title="修改密码" @close="closeDialog" :visible.sync="dialogFormVisible">
                        <el-form ref="form_ref" :model="form">
                            <el-form-item prop="oldpassword" label="输入新密码" :label-width="formLabelWidth">
                                <el-input v-model="queryInfo.oldpassword" type="password"></el-input>
                            </el-form-item>
                            <el-form-item prop="newpassword" label="确认密码" :label-width="formLabelWidth">
                                <el-input v-model="queryInfo.newpassword" type="password"></el-input>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button @click="dialogFormVisible = false">取 消</el-button>
                            <el-button type="primary" @click="reset_password">确 定</el-button>
                        </div>
                    </el-dialog>
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
                    address: '铁道校区-新1舍、铁道校区-新2舍'
                },
                dialogFormVisible: false,
                // form: {
                //      oldpassword: '',
                //      newpassword: '',
                // },
                formLabelWidth: '120px',
                queryInfo: {
                    oldpassword: '',
                    newpassword: '',
                }
            }
        },
        created(){
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
                    params: this.manager.id })
                if (res.meta.status !== 200) {
                    return this.$message.error('获取管理员信息失败')
                }
                this.manager = res.data.manager
                console.log(res)
            },
            closeDialog() {
                this.$refs.form_ref.resetFields()
            },
            async reset_password() {
                this.dialogFormVisible = false
                const { data: res } = await this.$http.get('admin/reset_password', {
                    params: this.queryInfo
                })
                if (res.meta.status !== 200) {
                    return this.$message.error('修改密码失败')
                }
                this.$message.success('修改成功')
            }
        }
    }
</script>

<style lang='less' scoped>
    .box-card {
        //   margin-top: 25px;
        //   margin-left: 42px;
        //   margin-right: 30px;
        //   height: 600px;
        margin-top: 30px;
        padding: 0;
        background-color: #dcdfe6;
        border-radius: 5px;
    }

    .box-card1 {
        margin-top: 25px;
        margin-left: 96px;
        width: 400px;
        height: 40px;
        border-radius: 0px;
        border-color: #999;
        border-width: 1.5px;
        margin-bottom: 0px;
        border-top-width: 2px;
        border-left-width: 2px;
        border-right-width: 2px;
        background-color: #dcdfe6;
    }

    .box-card2 {
        margin-top: 0px;
        margin-left: 96px;
        width: 400px;
        height: 40px;
        border-radius: 0px;
        border-color: #999;
        border-width: 1.5px;
        border-top-width: 0px;
        border-left-width: 2px;
        border-right-width: 2px;
        background-color: #dcdfe6;
    }

    .box-card3 {
        margin-top: 0px;
        margin-left: 96px;
        width: 400px;
        height: 85px;
        border-radius: 0px;
        border-color: #999;
        border-width: 1.5px;
        border-top-width: 0px;
        border-bottom-width: 2px;
        border-left-width: 2px;
        border-right-width: 2px;
    }

    .blank {
        width: 100px;
    }

    .button {
        margin-top: 20px;
        margin-left: 250px;
        font-size: 15px;

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
</style>

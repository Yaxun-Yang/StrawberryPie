<template>
    <div class="back">
        <el-container class="home-container">
            <!-- 头部区域 -->
            <el-header>
                <div>
                    <!--          <img src="../assets/heima.png" alt /> -->
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
                    <el-menu-item index="/login" @click="saveNavState('/login')">首页</el-menu-item>
                    <el-menu-item index="logout" @click="saveNavState('/logout')">退出</el-menu-item>
                </el-menu>
            </el-header>
            <!-- 页面主题区域 -->
            <el-container>
                <!-- 右侧内容主题 -->
                <el-main>
                    <!-- 路由占位符 -->
                    <router-view></router-view>
                    <h4>学生信息查询</h4>
                    <!-- 卡片视图区域 -->
                    <el-card shadow="hover">
                        <!-- 搜索 -->
                        <el-row :gutter="20">
                            <el-col :span="6">
                                <div>
                                    <el-select v-model="quertInfo.select" slot="prepend" placeholder="请选择">
                                        <el-option label="姓名" value="1"></el-option>
                                        <el-option label="宿舍号" value="2"></el-option>
                                        <el-option label="专业班级" value="3"></el-option>
                                    </el-select>
                                </div>
                            </el-col>
                            <el-col :span="11">
                                <div>
                                    <el-input placeholder="请输入" v-model="quertInfo.query" clearable @clear="getUserList"></el-input>
                                </div>
                            </el-col>
                            <el-col :span="3">
                                <div>
                                    <el-button type="primary" icon="el-icon-search" @click="getUserList"></el-button>
                                </div>
                            </el-col>
                        </el-row>
                        <!-- 列表 -->
                        <el-table :data="userList" border stripe>
                            <el-table-column type="index" label="#"></el-table-column>
                            <el-table-column label="宿舍号" prop="dorm"></el-table-column>
                            <el-table-column label="姓名" prop="name"></el-table-column>
                            <el-table-column label="角色" prop="type"></el-table-column>
                            <el-table-column label="专业班级" prop="class"></el-table-column>
                            <el-table-column label="学号" prop="number"></el-table-column>
                        </el-table>
                        <!-- 分页 -->
                        <el-pagination
                                @size-change="hasOwnProperty"
                                @current-change="handleCurrentChange"
                                :current-page="quertInfo.pagenum"
                                :page-sizes="[1, 2, 5, 10]"
                                :page-size="quertInfo.pagesize"
                                layout="total, sizes, prev, pager, next, jumper"
                                :total="total">
                        </el-pagination>
                    </el-card>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                // 获取用户列表参数
                quertInfo: {
                    query: '', // 查询参数
                    select: '', // 根据姓名/宿舍号/专业班级搜索
                    pagenum: 1, // 当前页数
                    pagesize: 2 // 每页显示多少条数据
                },
                userList: [], // 所有用户列表
                total: 0 //  一共多少页
            }
        },
        created () {
            this.getUserList()

        },
        methods: {
            async getUserList () {
                const { data: res } = await this.$http.get('users', { params: this.quertInfo })
                if (res.meta.status !== 200) {
                    return this.$message.error('获取宿舍信息失败')
                }
                this.userList = res.data.users
                this.total = res.data.total
                console.log(res)
            },
            // 监听
            hasOwnProperty (newSize) {
                alert(newSize)
                this.quertInfo.pagesize = newSize
                this.getUserList()
            },
            handleCurrentChange (newPage) {
                alert(newPage)
                this.quertInfo.pagenum = newPage
                this.getUserList()
            }
        }
    }
</script>

<style lang='less' scoped>
    .el-card{
        margin-top: 30px;
        padding: 0;
        background-color: #dcdfe6;
        border-radius: 5px;
        min-height: 100px;
        font-size: small;
    }
    .el-table{
        margin-top: 15px;
        font-size: 12px;
    }
    .el-pagination{
        margin-top: 15px;
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

<template>
    <div class="back">
        <el-container class="home-container">
            <!-- 头部区域 -->
            <el-header>
                <div>
                    <img src="../assets/main.png" alt />
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
                    <el-menu-item index="/manage_home" @click="saveNavState('/manage_home')">首页</el-menu-item>
                    <el-menu-item index="logout" @click="saveNavState('/logout')">退出</el-menu-item>
                </el-menu>
            </el-header>
            <!-- 页面主题区域 -->
            <el-container>
                <!-- 右侧内容主题 -->
                <el-main>
                    <!-- 路由占位符 -->
                    <router-view></router-view>
                    <h4>异常情况查看</h4>
                    <el-card>
                        <el-row :gutter="20">
                            <el-col :span="10">
                                <div>
                                    <el-input placeholder="请输入宿舍号查询" v-model="queryInfo.query" clearable @clear="getExceptionList"></el-input>    
                                </div>
                            </el-col>
                            <el-col :span="10">
                                <div>
                                    <el-button type="primary" icon="el-icon-search" @click="getExceptionList"></el-button>
                                </div>
                            </el-col>
                        </el-row>
                        <el-row>
                            <!-- 表格区域 -->
                            <el-table :data="exceptionList">
                                <el-table-column type="index"></el-table-column>
                                <el-table-column prop="time" label="时间"></el-table-column>
                                <el-table-column prop="dorm" label="宿舍"></el-table-column>
                                <el-table-column prop="type" label="类型"></el-table-column>
                                <el-table-column prop="video" label="视频记录"></el-table-column>
                            </el-table>

                            <!-- 分页区域 -->
                            <el-pagination
                                    @size-change="handleSizeChange"
                                    @current-change="handleCurrentChange"
                                    :current-page="queryInfo.pagenum"
                                    :page-sizes="[1, 2, 4, 8]"
                                    :page-size="queryInfo.pagesize"
                                    layout="total, sizes, prev, pager, next, jumper"
                                    :total="total"
                            ></el-pagination>
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
                queryInfo: {
                    query: '',
                    pagenum: 1,
                    pagesize: 7
                },
                exceptionList: [],
                total: 0
            }
        },
        created() {
            this.getExceptionList()
        },
        methods: {
            // 获取异常列表列表
            async getExceptionList() {
                const { data: res } = await this.$http.get('exceptions', {
                    params: this.queryInfo
                })
                console.log(res)
                if (res.meta.status !== 200)
                    return this.$message.error('获取异常情况列表失败')
                this.exceptionList = res.data.exceptions
                this.total = res.data.total
            },
            // 监听 Pagesize 改变
            handleSizeChange(newSize) {
                this.queryInfo.pagesize = newSize
                this.getExceptionList()
            },
            // 监听 页码值 改变
            handleCurrentChange(newPage) {
                this.queryInfo.pagenum = newPage
                this.getExceptionList()
            },
            saveNavState(activePath) {
                if (activePath == '/logout') {
                    window.sessionStorage.clear()
                    this.$router.push('/login')
                } else {
                    window.sessionStorage.setItem('activePath', activePath)
                    this.activePath = activePath
                }
            }
        }
    }
</script>

<style lang='less' scoped>
    .el-table {
        margin-top: 15px;
        background-color: #dcdfe6;
        border-radius: 5px;
    }

    .el-pagination {
        margin-top: 15px;
    }

    .el-row {
        margin: 15px;
        margin-left: 0;
        &:last-child {
            margin-left: 15px;
        }
    }

    .el-card {
        margin-top: 20px;
        padding: 0;
        background-color: #dcdfe6;
        border-radius: 5px;
        min-height: 100px;
        font-size: small;
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
    img {
        width: 100px;
    }

</style>

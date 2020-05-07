<template>
    <div>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item>首页</el-breadcrumb-item>
            <el-breadcrumb-item>监控查看</el-breadcrumb-item>
            <el-breadcrumb-item>历史监控</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card>
            <el-row>
                <!-- 表格区域 -->
                <el-table :data="exceptionList">
                    <el-table-column type="index"></el-table-column>
                    <el-table-column prop="time" label="时间"></el-table-column>
                    <el-table-column prop="type" label="类型"></el-table-column>
<!--                    <el-table-column prop="video" label="视频记录">-->
                    <el-table-column label="查看">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)" type="text" size="small">{{scope.row.video}}</el-button>
                        </template>
                    </el-table-column>
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
        <el-dialog
                title="Video"
                :visible.sync="dialogVisible"
                width="40%">
<!--            <span>这是一段信息</span>-->
<!--            <span slot="footer" class="dialog-footer">-->
<!--                <el-button @click="dialogVisible = false">取 消</el-button>-->
<!--                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>-->
<!--            </span>-->
            <video controls="" autoplay="" name="media" class="video"><source src="http://localhost:5000/api/video/history" type="video/mp4"></video>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                queryInfo: {
                    query: '',
                    pagenum: 1,
                    pagesize: 1
                },
                exceptionList: [],
                total: 0,
                video: "",
                dialogVisible: false
            }
        },
        created() {
            this.getExceptionList()
        },
        methods: {
            // 获取异常列表列表
            async getExceptionList() {
                const {data: res} = await this.$http.get("video/history/information", {
                    params: this.queryInfo
                })
                // console.log("video"+res)
                // this.video = res
                this.exceptionList = res.data.information
                this.total = res.total
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
            async handleClick(row){
                const {data: res} = await this.$http.get("video/time", {
                    params: row
                })
                console.log(res)
                this.dialogVisible = true
            }
        }
    }
</script>

<style lang="less" scoped>
    .el-table {
        margin-top: 15px;
        background-color: #dcdfe6;
        border-radius: 5px;
    }

    .el-pagination {
        margin-top: 15px;
    }

    .el-row {
        /*margin: 15px;*/
        /*margin-left: 0;*/
        margin: 15px 15px 15px 0;
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
    .video {
        width: 400px;
    }
</style>


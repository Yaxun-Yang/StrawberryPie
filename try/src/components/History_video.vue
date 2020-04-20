<template>
    <div>
      <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>监控查看</el-breadcrumb-item>
      <el-breadcrumb-item>历史监控</el-breadcrumb-item>
    </el-breadcrumb>
    </div>
</template>

<script>
export default {
    methods: {
        async get_history_video() {
            const {data: res} = await this.$http.get('video/history')
            console.log(res)
            if (res.meta.status !== 200) {
                return this.$message.error('获取视频信息失败')
            }
        }
    },
    created() {
        this.get_history_video()
    }
}
</script>

<style lang="less" scoped>
</style>

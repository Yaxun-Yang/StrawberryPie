<template>
    <div>
         <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>监控查看</el-breadcrumb-item>
      <el-breadcrumb-item>实时监控</el-breadcrumb-item>
    </el-breadcrumb>
        <img id="bg" src="http://127.0.0.1:5000/api/video/now">
<!--            <video controls="" autoplay="" name="media" class="video"><source src="http://127.0.0.1:5000/api/video/now" type="video/mp4"></video>-->
    </div>
</template>

<script>
export default {
    methods: {
        async get_now_video() {
            const {data: res} = await this.$http.get('video/now')
            console.log(res)
            if (res.meta.status !== 200) {
                return this.$message.error('获取视频信息失败')
            }
        }
    },
    created() {
        // this.get_now_video()
    }
}
</script>

<style lang="less" scoped>
</style>

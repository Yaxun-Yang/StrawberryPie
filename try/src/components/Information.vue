<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>信息查询</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card class="info_card">
      <el-row>
        <el-col :span="18">
          <!-- 搜索内容 -->
          <!-- <template slot-scope="scoped"> -->
          <el-date-picker
                  unlink-panels
                  v-model="queryInfo.dateRange"
                  type="daterange"
                  range-separator="至"
                  start-placeholder="开始日期"
                  end-placeholder="结束日期"
                  size="small"
                  value-format="yyyy-MM-dd"
                  @change="daterangeChange"
          ></el-date-picker>
          <!-- </template> -->
        </el-col>
        <el-col :span="4">
          <el-button type="primary" size="small" @click="dateRangeChangeClick">搜索</el-button>
        </el-col>
      </el-row>

      <!-- 电费水费消耗列表 -->
      <el-table :data="resumeList">
        <el-table-column type="index"></el-table-column>
        <el-table-column label="日期" prop="date"></el-table-column>
        <el-table-column label="电费" prop="electricity"></el-table-column>
        <el-table-column label="水费" prop="water"></el-table-column>
      </el-table>

      <!-- 分页区域 -->
      <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="queryInfo.pagenum"
              :page-sizes="[1, 7, 21, 28]"
              :page-size="queryInfo.pagesize"
              layout="total, sizes, prev, pager, next, jumper"
              :total="total"
      ></el-pagination>
    </el-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        queryInfo: {
          dateRange: [],
          query: '',
          pagenum: 1,
          pagesize: 7
        },
        resumeList: [],
        total: 0
      }
    },
    created() {
      this.getResumeList()
    },
    methods: {
      // 获取消费列表
      async getResumeList() {
        const { data: res } = await this.$http.get('information', {
          params: this.queryInfo
        })
        console.log(res)
        if (res.meta.status !== 200)
          return this.$message.error('获取消费列表失败')
        this.resumeList = res.data.information
        this.total = res.data.total
        if (!this.dateRange) return (this.dateRange = res.data.today)
      },
      // 监听 time-picker 的改变
      daterangeChange(newDateRange) {
        console.log(this.dateRange)
        this.queryInfo.dateRange = newDateRange
      },
      dateRangeChangeClick() {
        this.getResumeList()
      },
      // 监听 Pagesize 改变
      handleSizeChange(newSize) {
        this.queryInfo.pagesize = newSize
        this.getResumeList()
      },
      // 监听 页码值 改变
      handleCurrentChange(newPage) {
        this.queryInfo.pagenum = newPage
        this.getResumeList()
      }
    }
  }
</script>

<style lang="less" scoped>
  .info_card {
    margin-top: 30px;
    background-color: #dcdfe6;
    border-radius: 5px;
    min-height: 100px;
    font-size: small;
  }
  .el-table {
    margin-top: 15px;
    background-color: #dcdfe6;
    border-radius: 5px;
  }
  .el-pagination {
    margin-top: 15px;
  }
</style>

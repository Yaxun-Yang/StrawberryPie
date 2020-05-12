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
           <h4>灯控管理</h4>
          <el-card>
            <el-row>
              <!-- 关灯时间选择 -->
              <el-col :span="5" :offset="1">
                <span class="font_diff">关灯时间：</span>
              </el-col>
              <el-col :span="11">
                <el-time-picker v-model="close_time" format="HH:mm:ss" value-format="HH:mm:ss" placeholder="任意时间点"  size="small"></el-time-picker>
              </el-col>
              <el-col :span="4" :offset="1">
                <el-button type="primary" size="small" @click="closeTime">确定</el-button>
              </el-col>
            </el-row>

            <el-row>
              <!-- 提醒关灯时间选择 -->
              <el-col :span="5" :offset="1">
                <span class="font_diff">关灯提醒时间：</span>
              </el-col>
              <el-col :span="11">
                <el-time-picker v-model="remind_time" format="HH:mm:ss" value-format="HH:mm:ss" placeholder="任意时间点" size="small"></el-time-picker>
              </el-col>
              <el-col :span="4" :offset="1">
                <el-button type="primary" size="small" @click="remindTime">确定</el-button>
              </el-col>
            </el-row>

            <el-row>
              <!-- 表格区域 -->
              <el-table :data="dormList">
                <el-table-column type="index"></el-table-column>
                <el-table-column label="宿舍" prop="dorm"></el-table-column>
                <el-table-column label="宿舍成员" prop="student"></el-table-column>
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
      close_time: '23:00:00',
      remind_time: '22:50:00',
      dormList: [],
      total: 0
    }
  },
  created() {
    this.getDormList()
    this.close_time = "11:00:00"
  },
  methods: {
    // 修改关灯时间
    async closeTime() {
      alert(this.close_time)
      const { data: res } = await this.$http.put(
        `lamp/closetime/${this.close_time}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      this.$message.success('修改成功')
    },
    // 修改提醒关灯时间
    async remindTime() {
      alert(this.close_time)
      const { data: res } = await this.$http.put(
        `lamp/remindtime/${this.remind_time}`
      )
      if (res.meta.status !== 200) {
        return this.$message.error('修改失败，请重新输入')
      }
      this.$message.success('修改成功')
    },

    // 获取宿舍列表
    async getDormList() {
      const { data: res } = await this.$http.get('dorms', {
        params: this.queryInfo
      })
      console.log(res)
      if (res.meta.status !== 200)
        return this.$message.error('获取宿舍列表失败')
      this.dormList = res.data.dorms
      this.total = res.data.totalpage
      this.close_time = res.data.close_time
      this.remind_time = res.data.remind_time
    },
    // 监听 Pagesize 改变
    handleSizeChange(newSize) {
      this.queryInfo.pagesize = newSize
      this.getDormList()
    },
    // 监听 页码值 改变
    handleCurrentChange(newPage) {
      this.queryInfo.pagenum = newPage
      this.getDormList()
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

.el-card {
  margin-top: 30px;
  padding: 0;
  background-color: #dcdfe6;
  border-radius: 5px;
  min-height: 100px;
  font-size: small;
}
.el-row {
  margin: 15px;
  margin-left: 0;
  &:last-child {
    margin-left: 15px;
  }
}
.font_diff {
  font-family: 'PingFang SC', Arial, sans-serif;
  line-height: 1.7;
  font-size: 14px;
}
.el-table {
  margin-top: 15px;
  background-color: #dcdfe6;
  border-radius: 5px;
}
.el-pagination {
  margin-top: 15px;
}
img {
  width: 100px;
}
</style>

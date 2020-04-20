<template>
  <div class="back">
    <el-container class="home-container">
      <!-- 头部区域 -->
      <el-header>
        <div>
          <img src="../assets/main.png" alt />
          <span>智能宿舍管理系统</span>
        </div>
        <el-menu
          background-color="#373d41"
          text-color="#fff"
          active-text-color="#409eff"
          mode="horizontal"
          :default-active="activePath"
          :router="true"
        >
          <el-menu-item index="/welcome" @click="saveNavState('/welcome')">首页</el-menu-item>
          <el-menu-item index="logout" @click="saveNavState('/logout')">退出</el-menu-item>
        </el-menu>
        <!-- <el-button type="info" @click="logout">退出</el-button> -->
      </el-header>
      <!-- 页面主题区域 -->
      <el-container>
        <!-- 侧边栏 -->
        <el-aside width="200px">
          <!-- 侧边栏菜单区域 -->
          <el-menu
            background-color="#333744"
            text-color="#fff"
            active-text-color="#409eff"
            unique-opened
            :router="true"
            :default-active="activePath"
          >
            <el-submenu index="1">
              <!-- 监控查看 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-camera-solid"></i>
                <!-- 文本 -->
                <span>监控查看</span>
              </template>
              <el-menu-item index="/history_video" @click="saveNavState('/history_video')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-menu"></i>
                  <!-- 文本 -->
                  <span>历史监控</span>
                </template>
              </el-menu-item>
              <el-menu-item index="/now_video" @click="saveNavState('/now_video')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-menu"></i>
                  <!-- 文本 -->
                  <span>实时监控</span>
                </template>
              </el-menu-item>
            </el-submenu>
            <!-- 设备管理 -->
            <el-menu-item index="/device_manage" @click="saveNavState('/device_manage')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-cooperation"></i>
                <!-- 文本 -->
                <span>设备管理</span>
              </template>
            </el-menu-item>
            <!-- 设备提醒 -->
            <el-menu-item index="/device_warn" @click="saveNavState('/device_warn')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-message-solid"></i>
                <!-- 文本 -->
                <span>设备提醒</span>
              </template>
            </el-menu-item>
            <!-- 智能养护 -->
            <el-submenu index="2">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-home"></i>
                <!-- 文本 -->
                <span>智能养护</span>
              </template>
              <el-menu-item index="/pet" @click="saveNavState('/pet')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-menu"></i>
                  <!-- 文本 -->
                  <span>宠物喂养</span>
                </template>
              </el-menu-item>
              <el-menu-item index="/plant" @click="saveNavState('/plant')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-menu"></i>
                  <!-- 文本 -->
                  <span>植物管理</span>
                </template>
              </el-menu-item>
            </el-submenu>
            <!-- 信息查询 -->
            <el-menu-item index="/information" @click="saveNavState('/information')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-data"></i>
                <!-- 文本 -->
                <span>信息查询</span>
              </template>
            </el-menu-item>
            <!-- 个人信息修改 -->
            <el-menu-item index="/person" @click="saveNavState('/person')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-custom"></i>
                <!-- 文本 -->
                <span>个人信息修改</span>
              </template>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <!-- 右侧内容主题 -->
        <el-main>
          <!-- 路由占位符 -->
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      //被激活的链接地址
      activePath: ''
    }
  },
  created() {
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    //保存链接的激活状态
    saveNavState(activePath) {
      if (activePath == '/logout') {
        window.sessionStorage.clear()
        this.$router.push('/login')
      } else {
        window.sessionStorage.setItem('activePath', activePath)
        this.activePath = activePath
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
  width: 60%;
  position: absolute;
  left: 20%;
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

.iconfont {
  margin-right: 10px;
}
  img{
    width: 60px;
  }
</style>

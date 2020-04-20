<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>设备管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 主卧室 -->
    <el-card shadow="hover" @click.native="room1">
      <!-- 路由占位符 -->
      <router-view></router-view>
      <el-switch
              v-model="value1"
              active-text="已连接"
              inactive-text="未连接">
      </el-switch>
      <div class="place">
        主卧室
      </div>
      <div class="icon">
        <el-button type="light" icon="el-icon-s-opportunity" circle></el-button>
        <el-button type="temperature" icon="el-icon-sunny" circle></el-button>
        <el-button type="humidity" icon="el-icon-light-rain" circle></el-button>
      </div>
    </el-card>
    <!-- 卫生间 -->
    <br>
    <el-card hadow="hover" @click.native="room2">
      <!-- 路由占位符 -->
      <router-view></router-view>
      <el-switch
              v-model="value2"
              active-text="已连接"
              inactive-text="未连接">
      </el-switch>
      <div class="place">
        卫生间
      </div>
      <div class="icon">
        <el-button type="light" icon="el-icon-s-opportunity" circle></el-button>
        <el-button type="temperature" icon="el-icon-sunny" circle></el-button>
        <el-button type="humidity" icon="el-icon-light-rain" circle></el-button>
      </div>
    </el-card>
    <!-- 阳台 -->
    <br>
    <el-card shadow="hover" @click.native="room3">
      <!-- 路由占位符 -->
      <router-view></router-view>
      <el-switch
              v-model="value3"
              active-text="已连接"
              inactive-text="未连接">
      </el-switch>
      <div class="place">
        阳台
      </div>
      <div class="icon">
        <el-button type="light" icon="el-icon-s-opportunity" circle></el-button>
        <el-button type="temperature" icon="el-icon-sunny" circle></el-button>
        <el-button type="humidity" icon="el-icon-light-rain" circle></el-button>
      </div>
    </el-card>
    <!-- 添加 -->
    <br>
    <el-card>
      <el-button icon="el-icon-plus" circle class="plus"></el-button>
    </el-card>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        value1: true,
        value2: true,
        value3: true
      }
    },
    methods: {
      room1 () {
        console.log("room1 click ")
        this.$router.push({ path: '/room1' })
      },
      room2 () {
        this.$router.push({ path: '/room2' })
      },
      room3 () {
        this.$router.push({ path: '/room3' })
      }
    }
  }
</script>

<style lang="less" scoped>
  .el-card{
    display: flex;
    justify-content: space-between;
    height: 200px;
    width: 550px;
    position: relative;
  }
  .el-switch{
    position: absolute;
    right: 5%;
    top: 10px;
  }
  .place{
    position: absolute;
    left: 5%;
    top: 75%;
  }
  .icon{
    position: absolute;
    left: 65%;
    top: 70%;
  }
  .plus{
    position: absolute;
    right: 50%;
    top: 50%;
  }
</style>

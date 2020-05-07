<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区域 -->
      <div class="avatar_box">
        <img src="../assets/logon.png" alt />
      </div>
      <!-- 登录表单区域 -->
      <el-form
        ref="loginForm_ref"
        :model="loginForm"
        :rules="loginFormRules"
        label-width="0px"
        class="login_form"
      >
        <!-- 用户名 -->
        <el-form-item prop="username">
          <el-input v-model="loginForm.username" prefix-icon="iconfont icon-user"></el-input>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item prop="password">
          <el-input
            v-model="loginForm.password"
            prefix-icon="iconfont icon-3702mima"
            type="password"
          ></el-input>
        </el-form-item>
        <!-- 按钮区域 -->
        <el-form-item class="btns">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="info" @click="resetLoginForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      //这是登录表单的数据绑定对象
      loginForm: {
        username: '0102',
        password: '111111'
      },
      //这是表单的验证规则对象
      loginFormRules: {
        //验证用户名是否合法
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        //验证密码是否合法
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    //点击重置按钮，重置登录表单
    resetLoginForm() {
      this.$refs.loginForm_ref.resetFields()
    },
    login() {
      this.$refs.loginForm_ref.validate(async valid => {
        if (!valid) return
        const {data: res} = await this.$http.post('login', this.loginForm)
        if (res.meta.status !== 200) return this.$message.error('登录失败')

        //1. 将登录成功之后的token，保存道客户端的sessionStorage中
        //  1.1 项目中出来登录之外的其他API接口，必须在登录之后才能访问
        //  1.2 token只应在当前网站打开期间生效，所以将 token 保存在 sessionStorage 中
        if (res.status == 'student') {
          window.sessionStorage.setItem('token', res.data.token)
          window.sessionStorage.setItem('user_name', res.data.username)
          window.sessionStorage.setItem('roomnumber', res.data.roomnumber)
          window.sessionStorage.setItem('roommate', res.data.roommate)
          window.sessionStorage.setItem('classnum', res.data.classnum)
          window.sessionStorage.setItem('img', res.data.img)
          window.sessionStorage.setItem('college', res.data.college)
          window.sessionStorage.setItem('stuid', res.data.stuid)
          window.sessionStorage.setItem('stutype', res.data.stutype)
          window.sessionStorage.setItem('time', res.data.time)
          window.sessionStorage.setItem('phonenum', res.data.phonenum)
          // window.sessionStorage.setItem('data', res.data)
          //2. 通过编程式导航跳转到后台主页，路由地址是 /home
          this.$router.push('/home')
          this.$message.success("登陆成功")
        }
        else if(res.status == 'admin') {
          window.sessionStorage.setItem('token', res.data.token)
          window.sessionStorage.setItem('manager', res.data.manager)
          window.sessionStorage.setItem('name', res.data.manager.name)
          window.sessionStorage.setItem('id', res.data.manager.id)
          window.sessionStorage.setItem('type', res.data.manager.type)
          window.sessionStorage.setItem('dept', res.data.manager.dept)
          window.sessionStorage.setItem('building', res.data.manager.building)
          window.sessionStorage.setItem('floor', res.data.manager.floor)
          window.sessionStorage.setItem('room', res.data.manager.room)
          window.sessionStorage.setItem('people', res.data.manager.people)
          window.sessionStorage.setItem('address', res.data.manager.address)
          // window.sessionStorage.setItem('data', res.data)
          //2. 通过编程式导航跳转到后台主页，路由地址是 /home
          this.$router.push('/homeadmin')
          this.$message.success("登陆成功")
        }

      })
    }
  }
}
</script>

<style lang="less" scoped>
.login_container {
  background-color: #2b4b6b;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: #ffffff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.avatar_box {
  height: 130px;
  width: 130px;
  border: 1px solid #eeeeee;
  border-radius: 50%;
  padding: 10px;
  box-shadow: 0 0 10px #ddd;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  img {
    height: 100%;
    width: 100%;
    border-radius: 50%;
    background-color: #eee;
  }
}

.btns {
  display: flex;
  justify-content: flex-end;
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}
</style>

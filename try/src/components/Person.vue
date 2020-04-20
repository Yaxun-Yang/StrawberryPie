<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人信息修改</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
      <el-card class="box-card1" shadow="never">
        <strong>姓名：{{users_info.username}}</strong>
      </el-card>
      <el-card class="box-card2" shadow="never">
        <strong>学工号：{{users_info.stuid}}</strong>
      </el-card>
      <el-card class="box-card2" shadow="never">
        <strong>身份类型：{{users_info.stutype}}</strong>
      </el-card>
      <el-card class="box-card2" shadow="never">
        <strong>部门名称：{{users_info.college}}</strong>
      </el-card>
      <el-card class="box-card2" shadow="never">
        <strong>所在班级：{{users_info.classnum}}</strong>
      </el-card>
      <el-card class="box-card2" shadow="never">
        <strong>绑定手机号：{{users_info.phonenum}}</strong>
      </el-card>
      <el-card class="box-card2" shadow="never">
        <strong>宿舍地址：{{users_info.roomnumber}}</strong>
      </el-card>
      <el-card class="box-card2" shadow="never">
        <strong>入住时间：{{users_info.time}}</strong>
      </el-card>
      <el-card class="box-card3" shadow="never">
        <span>
          <strong>房间所住人员：软件工程1801李梦瑶</strong>
        </span>
        <br />
<!--        <div v-for="fre in users_info.roommate" :key="fre">-->
<!--          <span style="padding-left:112px;">-->
<!--            <strong>{{fre}}</strong>-->
<!--          </span>-->
<!--          <br />-->
          <span style="padding-left:112px;">
            <strong>软件工程1802阳雅珣</strong>
          </span>
                  <span style="padding-left:112px;">
                    <strong>软件工程1801刘毅菲</strong>
                  </span>
                  <span style="padding-left:112px;">
                    <strong>软件工程1802阳雅珣</strong>
                  </span>
<!--        </div>-->
      </el-card>
      <div class="button">
        <el-button type="text" @click="dialogFormVisible = true">修改密码</el-button>
        <span style="padding-left:112px;">
          <el-button type="text" @click="dialogForm1Visible = true">修改手机号</el-button>
        </span>
      </div>
    </el-card>
    <el-dialog title="修改密码" @close="closeDialog" :visible.sync="dialogFormVisible">
      <el-form ref="form_ref" :model="form">
        <el-form-item prop="oldpassword" label="输入新密码" :label-width="formLabelWidth">
          <el-input v-model="form.oldpassword" type="password"></el-input>
        </el-form-item>
        <el-form-item prop="newpassword" label="确认密码" :label-width="formLabelWidth">
          <el-input v-model="form.newpassword" type="password"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
    <el-dialog title="修改手机号" :visible.sync="dialogForm1Visible">
      <el-form :model="form1">
        <el-form-item prop="phonenumber" label="输入手机号" :label-width="form1LabelWidth">
          <el-input v-model="form1.phonenumber" autocomplete="off"></el-input>
          <el-button plain>发送验证码</el-button>
        </el-form-item>
        <el-form-item prop="yanzheng" label="输入验证码" :label-width="form1LabelWidth">
          <el-input v-model="form1.yanzheng" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogForm1Visible = false">取 消</el-button>
        <el-button type="primary" @click="dialogForm1Visible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogFormVisible: false,
      form: {
        oldpassword: '',
        newpassword: '',
      },
      formLabelWidth: '120px',
      dialogForm1Visible: false,
      form1: {
        phonenumber: '',
        yanzheng: ''
      },
      form1LabelWidth: '120px',
      users_info: {

      }
    }
  },
  methods: {
    closeDialog() {
      this.$refs.form_ref.resetFields()
    },
    getInformation() {
      console.log(window.sessionStorage.getItem("stutype"))
      this.users_info["username"] = window.sessionStorage.getItem("user_name")
      this.users_info["roomnumber"] = window.sessionStorage.getItem("roomnumber")
      this.users_info["classnum"] = window.sessionStorage.getItem("classnum")
      this.users_info["roommate"] = window.sessionStorage.getItem("roommate").split("+")
      this.users_info["stuid"] = window.sessionStorage.getItem("stuid")
      this.users_info["college"] = window.sessionStorage.getItem("college")
      this.users_info["stutype"] = window.sessionStorage.getItem("stutype")
      this.users_info["phonenum"] = window.sessionStorage.getItem("phonenum")
      this.users_info["time"] = window.sessionStorage.getItem("time")
    }
  },
  created() {
    this.getInformation()
  }
}
</script>

<style lang="less" scoped>
.box-card {
  margin-top: 25px;
  margin-left: 42px;
  margin-right: 30px;
  height: 600px;
}

.box-card1 {
  margin-top: 25px;
  margin-left: 75px;
  width: 400px;
  height: 40px;
  border-radius: 0px;
  border-color: #999;
  border-width: 1.5px;
  margin-bottom: 0px;
  border-top-width: 2px;
  border-left-width: 2px;
  border-right-width: 2px;
}

.box-card2 {
  margin-top: 0px;
  margin-left: 75px;
  width: 400px;
  height: 40px;
  border-radius: 0px;
  border-color: #999;
  border-width: 1.5px;
  border-top-width: 0px;
  border-left-width: 2px;
  border-right-width: 2px;
}

.box-card3 {
  margin-top: 0px;
  margin-left: 75px;
  width: 400px;
  height: 85px;
  border-radius: 0px;
  border-color: #999;
  border-width: 1.5px;
  border-top-width: 0px;
  border-bottom-width: 2px;
  border-left-width: 2px;
  border-right-width: 2px;
}

.blank {
  width: 100px;
}

.button {
  margin-top: 20px;
  margin-left: 135px;
  font-size: 25px;
}
</style>

<template>
  <div class="bigdiv">
    <div class="bigbackground"></div>

    <el-carousel class="powerpoint" height="911.9px" arrow="never" :interval="intervalNum">
      <el-carousel-item v-for="item in 4" :key="item"></el-carousel-item>
    </el-carousel>
    <title-bar></title-bar>
    <div class="loginpage">
      <div class="logodiv">
        <img src="../assets/EdStarsLogo.jpg" class="logoposition" height="300px" width="330px" />
      </div>
      <div class="loginlabel">
        <table class="logintable">
          <tr>
            <td colspan="2" align="center">
              <font size="6" face="微软雅黑" color="#554287">用户登录</font>
            </td>
          </tr>
          <tr>
            <td id="smallfont">您的账号:</td>
            <td>
              <input
                class="inputbox"
                type="text"
                name="name"
                autofocus="autofocus"
                v-model="admin_name"
              />
            </td>
          </tr>
          <tr>
            <td id="smallfont">您的密码:</td>
            <td>
              <input class="inputbox" type="password" name="password" v-model="admin_password" />
            </td>
          </tr>
          <tr>
            <td colspan="2" class="btm" align="center">
              <input id="btm" type="submit" name="login" value="登录" @click="loginevent" face="微软雅黑" />
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'LoginPage',
  components: { TitleBar },
  props: {},
  data() {
    return {
      intervalNum: 7000,
      admin_name: '',
      admin_password: '',
      loginRespons: 'http://117.50.34.200:8002/adminForLogin/'
    }
  },
  methods: {
    login() {
      this.$router.push({
        name: 'RegistrationManagePage'
      })
    },
    loginevent() {
      const _this = this
      if (_this.admin_password !== '' && _this.admin_name !== '') {
        axios({
          url: _this.loginRespons,
          method: 'post',
          data: {
            admin_name: _this.admin_name,
            admin_password: _this.admin_password
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === 'ok') {
            this.$message({
              showClose: true,
              message: '恭喜你，登录成功！',
              type: 'success'
            })
            this.$store.commit('setName', this.admin_name)
            this.$store.commit('setPwd', this.admin_password)
            axios({
              url: 'http://117.50.34.200:8002/specificAdministrator/',
              method: 'post',
              data: {
                name: this.admin_name
              },
              transformRequest: [
                function(data) {
                  return Qs.stringify(data)
                }
              ]
            }).then(response => {
              let power = response.data
              this.$store.commit('setPowerCamp', power[0].power_create_camp)
              this.$store.commit('setPowerCourse', power[0].power_create_course)
              this.$store.commit(
                'setPowerActivity',
                power[0].power_create_activity
              )
              this.$store.commit(
                'setPowerAdministrator',
                power[0].power_create_administrator
              )
            })
            this.login()
            this.$emit('loginsuccess')
          } else if (response.data.code === 'no') {
            this.$message({
              showClose: true,
              message: '账号或密码错误，请重新输入！',
              type: 'error',
              duration: 5000
            })
            this.admin_password = ''
          } else {
            _this.$notify,
              error({
                title: 'Error',
                message: response.data
              })
            _this.admin_password = ''
          }
        })
      } else {
        this.$message({
          showClose: true,
          message: '输入的账号或密码不得为空！',
          type: 'warning',
          duration: 5000
        })
      }
    }
  },
  created() {
    let adminName = localStorage['name']
    let adminPwd = localStorage['pwd']
    if (typeof adminName !== 'undefined' && adminName !== '') {
      axios({
        url: 'http://117.50.34.200:8002/adminForLogin/',
        method: 'post',
        data: {
          admin_name: adminName,
          admin_password: adminPwd
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        if (response.data.code === 'ok') {
          this.$message({
            type: 'success',
            message: '登录成功!'
          })
          this.login()
        } else if (response.data.code === 'no') {
        } else {
          this.$notify,
            error({
              title: 'Error',
              message: response.data
            })
          this.admin_password = ''
        }
      })
    }
  }
}
</script>

<style scoped type="type/css">
.bigbackground {
  position: absolute;
  height: 100%;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
}
.bigdiv {
  position: relative;
  height: 120%;
}
.loginpage {
  display: flex;
  position: relative;
  margin: 4% auto;
  width: 1000px;
  height: 700px;
  margin-top: 0px;
}
.loginlabel {
  float: left;
  position: relative;
  width: 700px;
  height: 500px;
}
.logo {
  position: relative;
  margin: auto;
}
.logodiv {
  position: relative;
  float: left;
  width: 700px;
  height: 500px;
}
.logintable {
  width: 450px;
  background-color: rgba(45, 96, 192, 0.15);
  border-radius: 20px;
  height: 350px;
  position: relative;
  top: 32.5%;
  text-align: center;
}
.inputbox {
  width: 230px;
  height: 30px;
  margin-left: -30px;
  border: 0 none;
  border-radius: 20px;
  outline: none;
  padding-left: 10px;
  font-size: 22px;
}
#btm {
  width: 150px;
  height: 33px;
  background-color: rgba(45, 96, 192, 0.45);
  border: none;
  margin-bottom: 20px;
  color: rgb(255, 255, 255);
  cursor: pointer;
}
.btm {
  width: 100px;
  height: 40px;
}
#smallfont {
  font: 20px '微软雅黑';
  text-align: right;
}
.logoposition {
  position: relative;
  left: 50px;
  top: 180px;
}
.el-carousel__item:nth-child(1) {
  background-image: url(../assets/backgroundImage4.jpg);
}
.el-carousel__item:nth-child(2) {
  background-image: url(../assets/backgroundImage2.jpg);
}
.el-carousel__item:nth-child(3) {
  background-image: url(../assets/backgroundImage1.jpg);
}
.el-carousel__item:nth-child(4) {
  background-image: url(../assets/backgroundImage3.jpg);
}
.powerpoint {
  position: absolute;
  width: 100%;
  z-index: -100;
}
</style>

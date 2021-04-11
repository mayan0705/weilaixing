<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <el-page-header @back="goBack" content></el-page-header>
    <div class="form-div">
      <h1>报名设置</h1>
      <el-card shadow="hover" class="box-card">
        <el-form
          :model="pioneerCampSettings"
          ref="pioneerCampSettings"
          label-width="120px"
          class="demo-ruleForm"
        >
          <el-form-item
            class="form-row"
            label="创新院名称"
            prop="campName"
            :rules="[
            { required: true, message: '创新院名称不能为空'}
          ]"
          >
            <el-input class="input" v-model="pioneerCampSettings.campName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item
            class="form-row"
            label="创新院介绍"
            prop="campIntroduce"
            :rules="[
            { required: true, message: '创新院介绍不能为空'}
          ]"
          >
            <el-input
              class="textarea"
              type="textarea"
              :autosize="{ minRows: 3, maxRows: 5}"
              v-model="pioneerCampSettings.campIntroduce"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item
            class="form-row"
            label="面向人群"
            prop="peopleOriented"
            :rules="[
            { required: true, message: '面向人群不能为空'}
          ]"
          >
            <el-input class="input" v-model="pioneerCampSettings.peopleOriented" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item
            class="form-row"
            label="报名须知"
            prop="signInTips"
            :rules="[
            { required: true, message: '报名须知不能为空'}
          ]"
          >
            <el-input
              class="textarea"
              type="textarea"
              :autosize="{ minRows: 3, maxRows: 5}"
              v-model="pioneerCampSettings.signInTips"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item
            class="form-row"
            label="持续时间"
            prop="campTime"
            :rules="[
            { required: true, message: '持续时间不能为空'}
          ]"
          >
            <el-date-picker
              class="input"
              v-model="campTime"
              type="daterange"
              format="yyyy-MM-dd"
              value-format="yyyy-MM-dd"
              range-separator="至"
              :start-placeholder="startCampTime"
              :end-placeholder="endCampTime"
            ></el-date-picker>
          </el-form-item>
          <el-form-item
            class="form-row"
            label="报名时间"
            prop="dueDate"
            :rules="[
            { required: true, message: '报名时间不能为空'}
          ]"
          >
            <el-date-picker
              class="input"
              v-model="dueDate"
              type="daterange"
              format="yyyy-MM-dd"
              value-format="yyyy-MM-dd"
              range-separator="至"
              :start-placeholder="startDueDate"
              :end-placeholder="endDueDate"
            ></el-date-picker>
          </el-form-item>
          <el-form-item class="form-row" label="开放权限" prop="dueDate">
            <el-select v-model="permission" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item class="form-row" label="报名人数">
            <input
              class="number-input"
              v-model.number="pioneerCampSettings.applicantNumber"
              autocomplete="off"
              disabled="true"
            />
          </el-form-item>
          <el-form-item class="form-row" label="录取人数">
            <input
              class="number-input"
              v-model.number="pioneerCampSettings.admittedNumber"
              autocomplete="off"
              disabled="true"
            />
          </el-form-item>
        </el-form>
      </el-card>
      <br />
      <br />
      <el-button icon="el-icon-check" class="longbutton" type="primary" @click="test">提 交</el-button>
      <el-button icon="el-icon-refresh" class="longbutton" type="primary" @click="reset">重 置</el-button>
      <el-button
        icon="el-icon-s-custom"
        class="longbutton"
        type="primary"
        @click="showClassManage"
      >班级管理</el-button>
      <el-button
        icon="el-icon-tickets"
        class="longbutton"
        type="primary"
        @click="showApplicantList"
      >报名列表</el-button>
      <br />
      <br />
      <br />
      <br />
    </div>

    <el-drawer
      direction="btt"
      size="50%"
      title
      :visible.sync="drawer"
      :modal="isModal"
      :modal-append-to-body="isModal"
    >
      <class-manage
        :camp-index="pioneerCampIndex"
        class="class-manage-style"
        @closeClassManage="closeClassManage"
      ></class-manage>
    </el-drawer>
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import ClassManage from '../components/ClassManage'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'PioneerCampForm',
  data() {
    return {
      isModal: true,
      drawer: false,
      isOnLoad: true,
      isShowClassManage: false,
      specialColor: 1,
      pioneerCampSettings: {},
      campTime: [],
      dueDate: [],
      startCampTime: '',
      endCampTime: '',
      startDueDate: '',
      endDueDate: '',
      pioneerCampIndex: 0,
      permission: 0,
      options: [{
        value: 0,
        label: '不对任何人开放'
      }, {
        value: 1,
        label: '仅对参加过（或正在参加）本期创新院的校友开放'
      }, {
        value: 2,
        label: '对所有校友开放'
      }, {
        value: 3,
        label: '对所有用户开放'
      }]
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
          this.createPioneerCampForm()
        } else if (response.data.code === 'no') {
          this.$store.commit('setName', '')
          this.$store.commit('setPwd', '')
          this.$store.commit('setPowerCamp', 'false')
          this.$store.commit('setPowerCourse', 'false')
          this.$store.commit('setPowerActivity', 'false')
          this.$store.commit('setPowerAdministrator', 'false')
          this.$router.push({
            name: 'Index'
          })
        } else {
          this.$notify,
            error({
              title: 'Error',
              message: response.data
            })
          this.$store.commit('setName', '')
          this.$store.commit('setPwd', '')
          this.$store.commit('setPowerCamp', 'false')
          this.$store.commit('setPowerCourse', 'false')
          this.$store.commit('setPowerActivity', 'false')
          this.$store.commit('setPowerAdministrator', 'false')
          this.$router.push({
            name: 'Index'
          })
        }
      })
    } else {
      this.$router.push({
        name: 'Index'
      })
    }
  },
  watch: {
    campTime: function() {
      this.pioneerCampSettings.campTime =
        this.campTime[0] + ',' + this.campTime[1]
    },
    dueDate: function() {
      this.pioneerCampSettings.dueDate = this.dueDate[0] + ',' + this.dueDate[1]
    }
  },
  methods: {
    test() {
      let power = localStorage['powerCamp']
      if (power === 'true') {
        if (
          this.pioneerCampSettings.campName !== '' &&
          this.pioneerCampSettings.campTime !== '' &&
          this.pioneerCampSettings.campIntroduce !== '' &&
          this.pioneerCampSettings.peopleOriented !== '' &&
          this.pioneerCampSettings.signInTips !== '' &&
          this.pioneerCampSettings.dueDate !== '' &&
          this.permission !== ''
        ) {
          axios({
            url: 'http://117.50.34.200:8002/modifyCampMsg/',
            method: 'post',
            data: {
              id: this.pioneerCampIndex,
              name: this.pioneerCampSettings.campName,
              time: this.pioneerCampSettings.campTime,
              introduce: this.pioneerCampSettings.campIntroduce,
              people_oriented: this.pioneerCampSettings.peopleOriented,
              signin_tips: this.pioneerCampSettings.signInTips,
              signin_deadline: this.pioneerCampSettings.dueDate,
              permission: this.permission
            },
            transformRequest: [
              function(data) {
                return Qs.stringify(data)
              }
            ]
          }).then(response => {
            if (response.data.code === '1') {
              this.$message('创新院修改成功！')
              this.goBack()
            }
          })
        } else {
          this.$message('表单信息填写不全，请填写完毕后再提交！')
        }
      } else if (power === 'false') {
        this.createPioneerCampForm()
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    createPioneerCampForm() {
      this.pioneerCampIndex = parseInt(sessionStorage['campIndex'])
      axios({
        url: 'http://117.50.34.200:8002/specificCampMsg/',
        method: 'post',
        data: {
          id: this.pioneerCampIndex
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        let camp = response.data
        this.$set(this.pioneerCampSettings, 'campName', camp[0].name)
        this.$set(this.pioneerCampSettings, 'campIntroduce', camp[0].introduce)
        this.$set(
          this.pioneerCampSettings,
          'peopleOriented',
          camp[0].people_oriented
        )
        this.$set(this.pioneerCampSettings, 'campTime', camp[0].time)
        this.startCampTime = this.pioneerCampSettings.campTime.substr(0, 10)
        this.endCampTime = this.pioneerCampSettings.campTime.substr(11, 10)
        this.$set(this.pioneerCampSettings, 'signInTips', camp[0].signin_tips)
        this.$set(this.pioneerCampSettings, 'dueDate', camp[0].signin_deadline)
        this.startDueDate = this.pioneerCampSettings.dueDate.substr(0, 10)
        this.endDueDate = this.pioneerCampSettings.dueDate.substr(11, 10)
        Date.prototype.Format = function(fmt) {
          var o = {
            'M+': this.getMonth() + 1,
            'd+': this.getDate(),
            'h+': this.getHours(),
            'm+': this.getMinutes(),
            's+': this.getSeconds(),
            'q+': Math.floor((this.getMonth() + 3) / 3),
            S: this.getMilliseconds()
          }
          if (/(y+)/.test(fmt))
            fmt = fmt.replace(
              RegExp.$1,
              (this.getFullYear() + '').substr(4 - RegExp.$1.length)
            )
          for (var k in o)
            if (new RegExp('(' + k + ')').test(fmt))
              fmt = fmt.replace(
                RegExp.$1,
                RegExp.$1.length == 1
                  ? o[k]
                  : ('00' + o[k]).substr(('' + o[k]).length)
              )
          return fmt
        }
        let nowDate = parseInt(new Date().Format('yyyyMMdd'))
        let timeNumber = parseInt(
          this.pioneerCampSettings.dueDate.substr(0, 4) +
            this.pioneerCampSettings.dueDate.substr(5, 2) +
            this.pioneerCampSettings.dueDate.substr(8, 2)
        )
        let status = false
        if (nowDate >= timeNumber) {
          status = false
        } else {
          status = true
        }
        this.permission = camp[0].permission
        this.$set(this.pioneerCampSettings, 'applicantNumber', camp[1])
        this.$set(this.pioneerCampSettings, 'admittedNumber', camp[2])
        this.$set(this.pioneerCampSettings, 'campStatus', status)
      })
    },
    showApplicantList() {
      this.$store.commit('setCampIndex', this.pioneerCampIndex)
      this.$router.push({
        name: 'PioneerCampUserInformation'
      })
    },
    showClassManage() {
      this.drawer = true
      this.$store.commit('setCampIndex', this.pioneerCampIndex)
      this.$store.commit('setSigninStatus', this.pioneerCampSettings.campStatus)
    },
    closeClassManage() {
      this.drawer = false
    },
    reset() {
      this.createPioneerCampForm()
    },
    goBack() {
      this.$router.push({
        name: 'RegistrationManagePage'
      })
    }
  },
  components: {
    TitleBar,
    NavBar,
    ClassManage
  }
}
</script>

<style scoped>
.longbutton {
  float: left;
  position: relative;
  left: 17%;
  width: 150px;
  margin-right: 20px;
}
.form-div {
  position: relative;
  width: 1055px;
  margin: auto;
}
h1 {
  text-align: center;
}
.form-row {
  margin-top: 20px;
}
.input {
  width: 30%;
}
.textarea {
  width: 50%;
}
.number-input {
  border: none;
  background-color: white;
}
.date-picker {
  width: 30%;
}
.class-manage-style {
  position: relative;
  width: 1000px;
  margin: auto;
}
.box-card {
  top: 20px;
  width: 1100px;
  position: relative;
  margin: auto;
  margin-top: 0;
}
</style>

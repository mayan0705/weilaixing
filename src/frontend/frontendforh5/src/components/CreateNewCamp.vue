<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <el-page-header @back="goBack" content></el-page-header>
    <div class="form-div">
      <h1>创建新创新院</h1>
      <el-card shadow="hover">
        <el-form
          :model="pioneerCampSettings"
          ref="pioneerCampSettings"
          label-width="120px"
          class="demo-ruleForm"
        >
          <el-form-item class="form-row" label="创新院名称" prop="campName">
            <el-input class="input" v-model="pioneerCampSettings.campName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item class="form-row" label="创新院介绍" prop="campIntroduce">
            <el-input
              class="textarea"
              type="textarea"
              :autosize="{ minRows: 3, maxRows: 5}"
              v-model="pioneerCampSettings.campIntroduce"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item class="form-row" label="面向人群" prop="peopleOriented">
            <el-input class="input" v-model="pioneerCampSettings.peopleOriented" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item class="form-row" label="报名须知" prop="signInTips">
            <el-input
              class="textarea"
              type="textarea"
              :autosize="{ minRows: 3, maxRows: 5}"
              v-model="pioneerCampSettings.signInTips"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item class="form-row" label="持续时间" prop="campTime">
            <el-date-picker
              class="input"
              v-model="campTime"
              type="daterange"
              format="yyyy-MM-dd"
              value-format="yyyy-MM-dd"
              range-separator="至"
              :start-placeholder="startCampTime"
              :end-placeholder="endCampTime"
              :disabled="!pioneerCampSettings.campStatus"
            ></el-date-picker>
          </el-form-item>
          <el-form-item class="form-row" label="报名时间" prop="dueDate">
            <el-date-picker
              class="input"
              v-model="dueDate"
              type="daterange"
              format="yyyy-MM-dd"
              value-format="yyyy-MM-dd"
              range-separator="至"
              :start-placeholder="startDueDate"
              :end-placeholder="endDueDate"
              :disabled="!pioneerCampSettings.campStatus"
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
          <el-form-item class="button-form-item">
            <el-button type="primary" @click="test">提交</el-button>
            <el-button @click="reset">重置</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'CreateNewCamp',
  data() {
    return {
      isOnLoad: true,
      specialColor: 1,
      pioneerCampSettings: {},
      campTime: [],
      dueDate: [],
      startCampTime: '',
      endCampTime: '',
      startDueDate: '',
      endDueDate: '',
      isShowApplicantList: false,
      permission: '',
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
  watch: {
    campTime: function() {
      this.pioneerCampSettings.campTime =
        this.campTime[0] + ',' + this.campTime[1]
      this.pioneerCampSettings.dueDate = this.dueDate[0] + ',' + this.dueDate[1]
    }
  },
  created() {
    let newCampCreatable = localStorage['newCampCreatable']
    let adminName = localStorage['name']
    let adminPwd = localStorage['pwd']
    let power = localStorage['powerCamp']
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
          if (power === 'true') {
            if (
              typeof newCampCreatable === 'undefined' ||
              newCampCreatable === 'false'
            ) {
              this.$router.push({
                name: 'RegistrationManagePage'
              })
            } else if (newCampCreatable === 'true') {
              this.createPioneerCampForm()
              this.startCampTime = this.pioneerCampSettings.campTime.substr(
                0,
                10
              )
              this.endCampTime = this.pioneerCampSettings.campTime.substr(
                11,
                10
              )
              this.$store.commit('setNewCampCreatable', 'false')
            }
          } else if (power === 'false') {
            this.$message({
              type: 'warning',
              message: '权限不足!'
            })
            this.$router.push({
              name: 'RegistrationManagePage'
            })
          }
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
  methods: {
    test() {
      if (
        this.pioneerCampSettings.campName !== '' &&
        this.pioneerCampSettings.campTime !== '' &&
        this.pioneerCampSettings.campIntroduce !== '' &&
        this.pioneerCampSettings.peopleOriented !== '' &&
        this.pioneerCampSettings.signInTips !== '' &&
        this.dueDate[0] !== '' &&
        this.dueDate[1] !== '' &&
        this.permission !== ''
      ) {
        axios({
          url: 'http://117.50.34.200:8002/createNewCamp/',
          method: 'post',
          data: {
            name: this.pioneerCampSettings.campName,
            time: this.pioneerCampSettings.campTime,
            introduce: this.pioneerCampSettings.campIntroduce,
            people_oriented: this.pioneerCampSettings.peopleOriented,
            signin_tips: this.pioneerCampSettings.signInTips,
            signin_deadline: this.dueDate[0] + ',' + this.dueDate[1],
            permission: this.permission
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === '1') {
            this.$message('创新院创建成功！')
            this.goBack()
          }
        })
      } else {
        this.$message('表单信息填写不全，请填写完毕后再提交！')
      }
    },
    createPioneerCampForm() {
      this.$set(this.pioneerCampSettings, 'campName', '')
      this.$set(this.pioneerCampSettings, 'campIntroduce', '')
      this.$set(this.pioneerCampSettings, 'peopleOriented', '')
      this.$set(this.pioneerCampSettings, 'campTime', '')
      this.$set(this.pioneerCampSettings, 'signInTips', '')
      this.$set(this.pioneerCampSettings, 'dueDate', '')
      this.$set(this.pioneerCampSettings, 'campStatus', true)
      this.campTime = []
      this.dueDate = []
      this.startCampTime = ''
      this.endCampTime = ''
      this.startDueDate = ''
      this.endDueDate = ''
      this.permission = ''
    },
    reset() {
      this.$store.commit('setNewCampCreatable', 'true')
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
    NavBar
  }
}
</script>

<style scoped>
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
.date-picker {
  width: 30%;
}
.button-form-item {
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
}
.back-btn {
  display: block;
  position: relative;
  top: -20px;
  left: 550px;
}
</style>

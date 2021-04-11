<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <div>
      <el-page-header @back="goBack" content></el-page-header>
      <div>
        <h1>活动详情</h1>
        <el-card :class="allow_change==0?'box-card':'box-card-allow'" shadow="hover">
          <div slot="header" class="clearfix">
          </div>
          <div class="bigForm">
            活动时间：&nbsp;&nbsp;&nbsp;&nbsp;
            <el-date-picker
              type="datetimerange"
              v-model="activity_time"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              align="right"
            ></el-date-picker>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            当前活动状态：&nbsp;&nbsp;{{activity_status}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;活动内部编号：&nbsp;&nbsp;{{activityIndex}}
            <br />
            <br />活动目标人数：&nbsp;&nbsp;&nbsp;&nbsp;
            <el-input-number size="medium" v-model="activity_peopleneed" />
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            已报名人数：&nbsp;&nbsp;{{activity_peopleSignUp}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <br />
            <br />活动名称：&nbsp;&nbsp;&nbsp;&nbsp;
            <el-input class="normalInputbox" v-model="activity_name" placeholder="请输入" />
            <br />
            <br />活动地点：&nbsp;&nbsp;&nbsp;&nbsp;
            <el-input class="normalInputbox" v-model="activity_location" placeholder="请输入"></el-input>
            <br />
            <br />活动描述：&nbsp;&nbsp;&nbsp;&nbsp;
            <el-input class="normalInputbox" v-model="activity_abstract" placeholder="请输入"></el-input>
            <br />
            <br /><span style="text-align: left">活动具体流程：</span>&nbsp;&nbsp;&nbsp;&nbsp;
            <div class="nextLine"></div>
            <el-input
              class="textField"
              type="textarea"
              :autosize="{ minRows: 5}"
              placeholder="请输入内容"
              v-model="activity_items"
            ></el-input>
            <br />
            <br />活动注意事项：&nbsp;&nbsp;&nbsp;&nbsp;
            <div class="nextLine"></div>
            <el-input
              class="textField"
              type="textarea"
              :autosize="{ minRows: 5}"
              placeholder="请输入内容"
              v-model="activity_tips"
            ></el-input>
            <br />
            <br />
            <el-collapse class="peoplesignup">
              <div class="AttendPeople">
                <el-collapse-item title="当前已报名人员">
                  <el-table :data="schoolMateInfo" stripe class="fillTable">
                    <el-table-column prop="name" label="姓名" width="200"></el-table-column>
                    <el-table-column prop="gender" label="性别" width="200"></el-table-column>
                    <el-table-column prop="phoneNumber" label="联系方式" width="349"></el-table-column>
                  </el-table>
                </el-collapse-item>
              </div>
            </el-collapse>
          </div>
        </el-card>
        <br />
        <br />
        <br />
        <br />
        <el-button
          type="primary"
          icon="el-icon-edit"
          class="operbutton0"
          @click="changePage()"
          v-if="allow_change==0"
        >修改内容</el-button>
        <el-button
          type="primary"
          icon="el-icon-check"
          class="operbutton"
          @click="modifyAct"
          v-if="allow_change==1"
        >保存修改</el-button>
        <el-button
          type="primary"
          icon="el-icon-close"
          class="operbutton2"
          @click="changePage()"
          v-if="allow_change==1"
        >取消修改</el-button>
        <br />
        <br />
        <br />
        <br />
      </div>
    </div>
  </div>
</template>

<script>
import { access } from 'fs'
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'ActivityInfoForm',
  props: {},
  data() {
    return {
      targetUrl: 'http://117.50.34.200:8002/specificActivityMsg/',
      activityIndex: 0,
      isOnLoad: true,
      specialColor: 3,
      allow_change: 0,
      activity_name: '',
      activity_time: [],
      activity_location: '',
      activity_abstract: '',
      activity_peopleneed: 0,
      activity_tips: '',
      activity_items: '',
      activity_status: '未开始',
      activity_peopleSignUp: 0,
      schoolMateInfo: []
    }
  },
  methods: {
    goBack() {
      this.$router.push({
        name: 'ActivityManagePage'
      })
    },
    modifyAct() {
      this.modifyActivity()
      this.changePage()
    },
    changePage() {
      let power = localStorage['powerActivity']
      if (power === 'true') {
        if (this.allow_change == 0) {
          this.allow_change = 1
        } else {
          this.allow_change = 0
        }
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    readSpecificActivity() {
      const _this = this
      axios({
        url: _this.targetUrl,
        method: 'post',
        data: {
          id: _this.activityIndex
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        var data = response.data
        var startEnd = data[0].activity_time.split(',')
        this.activity_time.push(startEnd[0])
        this.activity_time.push(startEnd[1])
        var starttime = new Date(Date.parse(startEnd[0]))
        var endtime = new Date(Date.parse(startEnd[1]))
        if (new Date() < starttime) {
          this.activity_status = '未开始'
        } else if (new Date() < endtime) {
          this.activity_status = '进行中'
        } else {
          this.activity_status = '已结束'
        }
        this.activity_name = data[0].activity_name
        this.activity_location = data[0].activity_location
        this.activity_abstract = data[0].activity_abstract
        this.activity_peopleneed = data[0].activity_peopleneed
        this.activity_tips = data[0].activity_tips
        this.activity_items = data[0].activity_items
        this.activity_peopleSignUp = data[1]
      })
    },
    getSchoolInfo() {
      axios({
        url: 'http://117.50.34.200:8002/queryActivityAttenders/',
        method: 'post',
        data: {
          id: this.activityIndex
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        let userData = response.data
        for (let index = 0; index < userData.length; index++) {
          let userGender = ''
          if (userData[index].user_gender === 'm') {
            userGender = '男'
          } else if (userData[index].user_gender === 'f') {
            userGender = '女'
          }
          this.$set(this.schoolMateInfo, index, {})
          this.$set(
            this.schoolMateInfo[index],
            'name',
            userData[index].user_name
          )
          this.$set(this.schoolMateInfo[index], 'gender', userGender)
          this.$set(
            this.schoolMateInfo[index],
            'phoneNumber',
            userData[index].user_telephone
          )
        }
      })
    },
    modifyActivity() {
      if (
        this.activity_name !== '' &&
        this.activity_time !== [] &&
        this.activity_location !== '' &&
        this.activity_abstract !== '' &&
        this.activity_peopleneed !== 0
      ) {
        axios({
          url: 'http://117.50.34.200:8002/modifyActivity/',
          method: 'post',
          data: {
            id: this.activityIndex,
            activity_name: this.activity_name,
            activity_time: this.activity_time[0] + ',' + this.activity_time[1],
            activity_location: this.activity_location,
            activity_abstract: this.activity_abstract,
            activity_peopleneed: this.activity_peopleneed,
            activity_tips: this.activity_tips,
            activity_status: '',
            activity_items: this.activity_items
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === '1') {
            this.$message('活动信息修改成功！')
            this.activity_time = []
            this.readSpecificActivity()
          }
        })
      } else {
        this.$message('表单信息填写不全，请填写完毕后再提交！')
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
          this.activityIndex = parseInt(sessionStorage['activityIndex'])
          this.readSpecificActivity()
          this.getSchoolInfo()
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
  components: {
    TitleBar,
    NavBar
  }
}
</script>


<style scoped>
h1 {
  text-align: center;
}
.peoplesignup {
  pointer-events: auto !important;
}
.textField {
  width: 85%;
}
.normalInputbox {
  width: 75%;
}
.text {
  font-size: 20px;
}
.item {
  margin-bottom: 18px;
  height: 30px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: '';
}
.clearfix:after {
  clear: both;
}
.box-card {
  top: 20px;
  width: 1100px;
  position: relative;
  margin: auto;
  pointer-events: none;
  background-color: rgb(255, 255, 255);
}
.box-card-allow {
  top: 20px;
  width: 1100px;
  position: relative;
  margin: auto;
  pointer-events: auto;
}
.operbutton0 {
  width: 160px;
  left: 45%;
  position: relative;
  margin: auto;
}
.operbutton {
  width: 160px;
  left: 40%;
  position: relative;
  margin: auto;
}
.operbutton2 {
  width: 160px;
  left: 41%;
  position: relative;
  margin: auto;
}
.AttendPeople {
  position: relative;
  margin: auto;
  width: 750px;
}
.bigForm {
  text-align: center;
}
.nextLine {
  margin: 10px 0;
}
.fillTable {
  width: 100%;
}
</style>
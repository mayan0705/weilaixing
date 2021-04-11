<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <el-page-header @back="goBack" content></el-page-header>
    <div>
      <h1>创建新的校友活动</h1>
      <el-card class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
        </div>
        <div class="activityForm">
          活动名称：&nbsp;&nbsp;&nbsp;&nbsp;
          <el-input class="normalInputbox" v-model="activity_name" placeholder="请输入"></el-input>
          <br />
          <br />活动地点：&nbsp;&nbsp;&nbsp;&nbsp;
          <el-input class="normalInputbox" v-model="activity_location" placeholder="请输入"></el-input>
          <br />
          <br />活动描述：&nbsp;&nbsp;&nbsp;&nbsp;
          <el-input class="normalInputbox" v-model="activity_abstract" placeholder="请输入"></el-input>
          <br />
          <br />活动目标人数：&nbsp;&nbsp;&nbsp;&nbsp;
          <el-input-number size="medium" v-model="activity_peopleneed"></el-input-number>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          活动时间：&nbsp;&nbsp;&nbsp;&nbsp;
          <el-date-picker
            type="datetimerange"
            v-model="activity_time"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            align="right"
            value-format="yyyy-MM-dd HH:mm:ss"
            @change="format"
          ></el-date-picker>
          <br />
          <br />活动具体流程：&nbsp;&nbsp;&nbsp;&nbsp;
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
        </div>
      </el-card>
      <br />
      <br />
      <br />
      <br />
      <el-button
        @click="activity_create"
        type="primary"
        icon="el-icon-circle-plus-outline"
        class="operbutton"
      >确认并新建</el-button>
      <br />
      <br />
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'ActivityFillingForm',
  props: {},
  data() {
    return {
      isOnLoad: true,
      specialColor: 3,
      activity_name: '',
      activity_time: '',
      activity_location: '',
      activity_abstract: '',
      activity_peopleneed: 0,
      activity_status: '',
      activity_tips: '',
      activity_items: '',
      targetURL: 'http://117.50.34.200:8002/createActivity/'
    }
  },
  methods: {
    format(val) {
      this.activity_time = val
    },
    test() {
      this.goBack()
    },
    goBack() {
      this.$router.push({
        name: 'ActivityManagePage'
      })
    },
    activity_create() {
      const _this = this
      if (
        _this.activity_name !== '' &&
        _this.activity_time !== '' &&
        _this.activity_location !== '' &&
        _this.activity_abstract !== '' &&
        _this.activity_peopleneed !== 0 &&
        _this.activity_tips !== '' &&
        _this.activity_items !== ''
      ) {
        axios({
          url: _this.targetURL,
          method: 'post',
          data: {
            activity_name: _this.activity_name,
            activity_time: _this.activity_time.join(','),
            activity_location: _this.activity_location,
            activity_abstract: _this.activity_abstract,
            activity_peopleneed: _this.activity_peopleneed,
            activity_tips: _this.activity_tips,
            activity_status: 'N',
            activity_items: _this.activity_items
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === '1') {
            this.$alert('活动创建成功！', '页面提示您：')
            this.$emit('turnPage')
            this.test()
          }
        })
      } else {
        this.$alert('表单信息填写不全，请填写完毕后再提交！', '页面提示您：')
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
          let power = localStorage['powerActivity']
          if (power === 'true') {
          } else if (power === 'false') {
            this.$router.push({
              name: 'ActivityManagePage'
            })
            this.$message({
              type: 'warning',
              message: '权限不足!'
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
  components: {
    TitleBar,
    NavBar
  }
}
</script>


<style scoped>
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
}
.operbutton {
  width: 160px;
  left: 45%;
  position: relative;
  margin: auto;
}
.activityForm {
  text-align: center;
}
.nextLine {
  margin: 10px 0;
}
h1 {
  text-align: center;
}
</style>
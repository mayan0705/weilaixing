<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <el-page-header @back="goBack" content></el-page-header>
    <div class="form-div">
      <h1>报名列表</h1>
      <el-table
        :data="userList.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
        stripe
      >
        <el-table-column prop="name" label="姓名" width="100">
          <template slot-scope="scope">
            <el-popover trigger="hover" placement="left">
              <p>点此查看该用户详细信息</p>
              <div slot="reference" class="name-wrapper" @click="enterInfoPage(scope.row.id)">
                <el-link>
                  <el-badge is-dot>{{ scope.row.name }}</el-badge>
                </el-link>
              </div>
            </el-popover>
          </template>
        </el-table-column>
        <el-table-column prop="gender" label="性别" width="80"></el-table-column>
        <el-table-column prop="phoneNumber" label="手机号码" width="160"></el-table-column>
        <el-table-column prop="mail" label="邮箱" width="190"></el-table-column>
        <el-table-column prop="company" label="公司" width="220"></el-table-column>
        <el-table-column prop="position" label="职务" width="120"></el-table-column>
        <el-table-column prop="class" label="报名班级" width="180"></el-table-column>
        <el-table-column width="200" label="操作">
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" size="middle" placeholder="输入关键字搜索" />
          </template>
          <template slot-scope="scope">
            <el-switch v-model="scope.row.status" active-color="#13ce66" active-text="录取"></el-switch>
          </template>
        </el-table-column>
      </el-table>
      <el-button type="primary" @click="saveChange">保存</el-button>
      <el-button @click="reset">重置</el-button>
    </div>
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'PioneerCampUserInformation',
  data() {
    return {
      isOnLoad: true,
      specialColor: 1,
      pioneerCamp: 0,
      search: '',
      userList: [],
      initUserList: []
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
          this.createUserInformation()
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
    reset() {
      this.createUserInformation()
    },
    saveChange() {
      let power = localStorage['powerCamp']
      if (power === 'true') {
        let changeData = []
        let dataIndex = 0
        for (let index = 0; index < this.userList.length; index++) {
          if (this.userList[index].status !== this.initUserList[index].status) {
            this.$set(changeData, dataIndex, {})
            this.$set(changeData[dataIndex], 'camp_id', this.pioneerCamp)
            this.$set(changeData[dataIndex], 'user_id', this.userList[index].id)
            let attendStatus = 0
            if (this.userList[index].status === true) {
              attendStatus = 1
            } else if (this.userList[index].status === false) {
              attendStatus = 0
            }
            this.$set(changeData[dataIndex], 'status', attendStatus)
            dataIndex += 1
          }
        }
        axios({
          url: 'http://117.50.34.200:8002/modifyCampattend/',
          method: 'post',
          data: { users: JSON.stringify(changeData) },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === '1') {
            this.$message('保存成功！')
          }
        })
        this.createUserInformation()
      } else if (power === 'false') {
        this.createUserInformation()
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    enterInfoPage(temp) {
      this.$store.commit('setAddicantIndex', temp)
      this.$router.push({
        name: 'AddicantInformation'
      })
    },
    createUserInformation() {
      this.pioneerCamp = parseInt(sessionStorage['campIndex'])
      axios({
        url: 'http://117.50.34.200:8002/queryCampSignup/',
        method: 'post',
        data: {
          camp_id: this.pioneerCamp
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        let users = response.data
        for (let index = 0; index < users.length / 5; index++) {
          let userGender = ''
          let userPosition = ''
          if (users[index * 5].user_gender === 'm') {
            userGender = '男'
          } else if (users[index * 5].user_gender === 'f') {
            userGender = '女'
          }
          if (users[index * 5 + 2] === 'F') {
            userPosition = '创始人'
          } else if (users[index * 5 + 2] === 'CF') {
            userPosition = '联合创始人'
          } else if (users[index * 5 + 2] === 'P') {
            userPosition = '董事长'
          } else if (users[index * 5 + 2] === 'CEO') {
            userPosition = 'CEO'
          } else if (users[index * 5 + 2] === 'Others') {
            userPosition = '其他'
          }
          this.$set(this.userList, index, {})
          this.$set(this.userList[index], 'id', users[index * 5].id)
          this.$set(this.userList[index], 'name', users[index * 5].user_name)
          this.$set(this.userList[index], 'gender', userGender)
          this.$set(
            this.userList[index],
            'phoneNumber',
            users[index * 5].user_telephone
          )
          this.$set(this.userList[index], 'mail', users[index * 5].user_email)
          this.$set(this.userList[index], 'company', users[index * 5 + 1])
          this.$set(this.userList[index], 'position', userPosition)
          this.$set(this.userList[index], 'class', users[index * 5 + 3])
          let attendStatus = false
          if (users[index * 5 + 4] === 0) {
            attendStatus = false
          } else if (users[index * 5 + 4] === 1) {
            attendStatus = true
          }
          this.$set(this.userList[index], 'status', attendStatus)
          this.$set(this.initUserList, index, {})
          this.$set(this.initUserList[index], 'id', users[index * 5].id)
          this.$set(this.initUserList[index], 'status', attendStatus)
        }
      })
    },
    goBack() {
      this.$router.push({
        name: 'PioneerCampForm'
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
.form-div {
  text-align: center;
}
.el-table {
  position: relative;
  width: 1250px;
  margin: auto;
}
.el-button {
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
}
</style>

<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <el-collapse-transition>
      <div class="setcenter">
        <el-tag color="rgba(255,255,255,0)" type effect="plain">创建新活动</el-tag>
        <el-button class="bigButton" icon="el-icon-circle-plus-outline" @click="createNew"></el-button>
        <el-tag color="rgba(255,255,255,0)" type effect="plain">活动列表</el-tag>
        <div>
          <label v-for="item in currentList" :key="item.index">
            <Activity
              :activity-status="item.activity_status"
              :init-activity-name="item.activity_name"
              :activity-index-msg="item.ID"
            />
          </label>
          <div class="newpagination">
            <el-pagination
              @current-change="handleCurrentChange"
              :page-size="8"
              :pager-count="7"
              :hide-on-single-page="value"
              layout="prev, pager, next"
              :total="total"
            ></el-pagination>
          </div>
        </div>
      </div>
    </el-collapse-transition>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import Activity from '../components/Activity'
export default {
  name: 'RegistrationManagePage',
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
          this.queryActivity()
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
  data() {
    return {
      queryActivityUrl: 'http://117.50.34.200:8002/queryActivity/',
      isOnLoad: true,
      specialColor: 3,
      currentPage: 0,
      tempTable: [],
      ActivityTable: [],
      total: 0,
      currentList: [],
      value: true
    }
  },
  methods: {
    handleCurrentChange: function(currentPage) {
      this.currentList = []
      if (typeof this.ActivityTable[(currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          0,
          this.ActivityTable[(currentPage - 1) * 8]
        )
      }
      if (
        typeof this.ActivityTable[1 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          1,
          this.ActivityTable[1 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.ActivityTable[2 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          2,
          this.ActivityTable[2 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.ActivityTable[3 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          3,
          this.ActivityTable[3 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.ActivityTable[4 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          4,
          this.ActivityTable[4 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.ActivityTable[5 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          5,
          this.ActivityTable[5 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.ActivityTable[6 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          6,
          this.ActivityTable[6 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.ActivityTable[7 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          7,
          this.ActivityTable[7 + (currentPage - 1) * 8]
        )
      }
    },
    queryActivity() {
      const _this = this
      axios({
        url: _this.queryActivityUrl,
        method: 'post'
      }).then(response => {
        var returnTable = response.data
        for (var i = 0; i < returnTable.length; i++) {
          var startEnd = returnTable[i].activity_time.split(',')
          var starttime = new Date(Date.parse(startEnd[0]))
          var endtime = new Date(Date.parse(startEnd[1]))
          var status
          if (new Date() < starttime) {
            status = '未开始'
          } else if (new Date() < endtime) {
            status = '进行中'
          } else {
            status = '已结束'
          }
          let newName = ''
          if (returnTable[i].activity_name.length > 9) {
            newName = returnTable[i].activity_name.slice(0, 8) + '...'
          } else if (returnTable[i].activity_name.length <= 9) {
            newName = returnTable[i].activity_name
          }
          this.tempTable.push({
            ID: returnTable[i].id,
            activity_name: newName,
            activity_status: status
          })
        }
        for (var j = 0; j < this.tempTable.length; j++) {
          if (this.tempTable[j].activity_status === '未开始') {
            this.ActivityTable.push(this.tempTable[j])
          }
        }
        for (var k = 0; k < this.tempTable.length; k++) {
          if (this.tempTable[k].activity_status === '进行中') {
            this.ActivityTable.push(this.tempTable[k])
          }
        }
        for (var l = 0; l < this.tempTable.length; l++) {
          if (this.tempTable[l].activity_status === '已结束') {
            this.ActivityTable.push(this.tempTable[l])
          }
        }
        this.total = this.ActivityTable.length
        this.currentList = []
        if (typeof this.ActivityTable[0] !== 'undefined') {
          this.$set(this.currentList, 0, this.ActivityTable[0])
        }
        if (typeof this.ActivityTable[1] !== 'undefined') {
          this.$set(this.currentList, 1, this.ActivityTable[1])
        }
        if (typeof this.ActivityTable[2] !== 'undefined') {
          this.$set(this.currentList, 2, this.ActivityTable[2])
        }
        if (typeof this.ActivityTable[3] !== 'undefined') {
          this.$set(this.currentList, 3, this.ActivityTable[3])
        }
        if (typeof this.ActivityTable[4] !== 'undefined') {
          this.$set(this.currentList, 4, this.ActivityTable[4])
        }
        if (typeof this.ActivityTable[5] !== 'undefined') {
          this.$set(this.currentList, 5, this.ActivityTable[5])
        }
        if (typeof this.ActivityTable[6] !== 'undefined') {
          this.$set(this.currentList, 6, this.ActivityTable[6])
        }
        if (typeof this.ActivityTable[7] !== 'undefined') {
          this.$set(this.currentList, 7, this.ActivityTable[7])
        }
      })
    },
    createNew() {
      let power = localStorage['powerActivity']
      if (power === 'true') {
        this.$router.push({
          name: 'ActivityFillingForm'
        })
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    }
  },
  components: {
    Activity,
    TitleBar,
    NavBar
  }
}
</script>

<style scoped>
span {
  display: block;
  border: none;
  margin-top: 20px;
  margin-left: 40px;
  font-size: 30px;
  font-family: 'PingFang SC', 'Helvetica Neue';
}
.setcenter {
  position: relative;
  margin: 0 5% 0 5%;
}
button {
  display: inline-block;
  height: 150px;
  width: 300px;
  margin-top: 20px;
  margin-left: 40px;
  font-size: 50px;
}
.bigButton {
  background-color: rgba(255, 255, 255, 0.5);
  margin-bottom: 70px;
  height: 200px;
  width: 300px;
}
.newpagination {
  width: 700px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
</style>

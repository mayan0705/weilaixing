<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <el-collapse-transition>
      <div class="setcenter">
        <el-tag color="rgba(255,255,255,0)" type effect="plain">当前进行中创新院</el-tag>
        <el-tag color="rgba(255,255,255,0)" v-if="processingCampTable==[]" class="setColor">没有正在进行的创新院</el-tag>
        <label v-for="item in processingCampTable" :key="item.index">
          <LessonLabel
            :camp-status="item.camp_status"
            :camp-name="item.camp_name"
            :camp-index-msg="item.ID"
          />
        </label>
        <el-tag color="rgba(255,255,255,0)" type effect="plain" class="campLabel">往期创新院</el-tag>
        <label v-for="item in currentList" :key="item.index">
          <LessonLabel
            :camp-status="item.camp_status"
            :camp-name="item.camp_name"
            :camp-index-msg="item.ID"
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
    </el-collapse-transition>
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import LessonLabel from '../components/LessonLabel'
import axios from 'axios'
import Qs from 'qs'
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
          this.queryCourseCamp()
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
      queryClassUrl: 'http://117.50.34.200:8002/queryCourseCamp/',
      isOnLoad: true,
      specialColor: 2,
      tempTable: [],
      processingCampTable: [],
      currentList: [],
      total: 0,
      currentList: [],
      value: true
    }
  },
  methods: {
    handleCurrentChange: function(currentPage) {
      this.currentList = []
      if (typeof this.tempTable[(currentPage - 1) * 8] !== 'undefined') {
        this.$set(this.currentList, 0, this.tempTable[(currentPage - 1) * 8])
      }
      if (typeof this.tempTable[1 + (currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          1,
          this.tempTable[1 + (currentPage - 1) * 8]
        )
      }
      if (typeof this.tempTable[2 + (currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          2,
          this.tempTable[2 + (currentPage - 1) * 8]
        )
      }
      if (typeof this.tempTable[3 + (currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          3,
          this.tempTable[3 + (currentPage - 1) * 8]
        )
      }
      if (typeof this.tempTable[4 + (currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          4,
          this.tempTable[4 + (currentPage - 1) * 8]
        )
      }
      if (typeof this.tempTable[5 + (currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          5,
          this.tempTable[5 + (currentPage - 1) * 8]
        )
      }
      if (typeof this.tempTable[6 + (currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          6,
          this.tempTable[6 + (currentPage - 1) * 8]
        )
      }
      if (typeof this.tempTable[7 + (currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          7,
          this.tempTable[7 + (currentPage - 1) * 8]
        )
      }
    },
    queryCourseCamp() {
      const _this = this
      axios({
        url: _this.queryClassUrl,
        method: 'post'
      }).then(response => {
        var returnTable = response.data
        for (var i = 0; i < returnTable.length; i++) {
          var startEnd = returnTable[i].time.split(',')
          var starttime = new Date(Date.parse(startEnd[0]))
          var endtime = new Date(Date.parse(startEnd[1]))
          var status
          if (new Date() < starttime) {
            status = 'waiting'
          } else if (new Date() < endtime) {
            status = 'processing'
          } else {
            status = 'over'
          }
          let newCampName = ''
          if (returnTable[i].name.length > 12) {
            newCampName = returnTable[i].name.slice(0, 11) + '...'
          } else if (returnTable[i].name.length <= 12) {
            newCampName = returnTable[i].name
          }
          if (status === 'over') {
            this.tempTable.push({
              ID: returnTable[i].id,
              camp_name: newCampName,
              camp_status: status
            })
          } else {
            this.processingCampTable.push({
              ID: returnTable[i].id,
              camp_name: newCampName,
              camp_status: status
            })
          }
        }
        this.total = this.tempTable.length
        this.currentList = []
        if (typeof this.tempTable[0] !== 'undefined') {
          this.$set(this.currentList, 0, this.tempTable[0])
        }
        if (typeof this.tempTable[1] !== 'undefined') {
          this.$set(this.currentList, 1, this.tempTable[1])
        }
        if (typeof this.tempTable[2] !== 'undefined') {
          this.$set(this.currentList, 2, this.tempTable[2])
        }
        if (typeof this.tempTable[3] !== 'undefined') {
          this.$set(this.currentList, 3, this.tempTable[3])
        }
        if (typeof this.tempTable[4] !== 'undefined') {
          this.$set(this.currentList, 4, this.tempTable[4])
        }
        if (typeof this.tempTable[5] !== 'undefined') {
          this.$set(this.currentList, 5, this.tempTable[5])
        }
        if (typeof this.tempTable[6] !== 'undefined') {
          this.$set(this.currentList, 6, this.tempTable[6])
        }
        if (typeof this.tempTable[7] !== 'undefined') {
          this.$set(this.currentList, 7, this.tempTable[7])
        }
      })
    }
  },
  components: {
    LessonLabel,
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
.setColor {
  color: black;
}
.newpagination {
  width: 700px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
.campLabel {
  margin-top: 70px;
}
</style>
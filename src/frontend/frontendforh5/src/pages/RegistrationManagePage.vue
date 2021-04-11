<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <div class="setcenter">
      <div @mousemove="enter1()" @mouseleave="leave1()">
        <el-tag color="rgba(255,255,255,0)" type effect="plain">
          新建创新院
          <transition name="el-zoom-in-center">
            <i v-if="this.iAppear1==1" class="el-icon-s-operation el-icon--right" />
          </transition>
        </el-tag>
      </div>
      <el-button icon="el-icon-circle-plus-outline" class="createButton" @click="createNewCamp"></el-button>
      <div @mousemove="enter1()" @mouseleave="leave1()" class="campLabel">
        <el-tag color="rgba(255,255,255,0)" type effect="plain">
          当前进行中创新院
          <transition name="el-zoom-in-center">
            <i v-if="this.iAppear1==1" class="el-icon-s-operation el-icon--right" />
          </transition>
        </el-tag>
      </div>
      <pioneer-camp
        v-for="(processingCamp,index) in processingList"
        :key="index"
        :pioneer-camp-index="processingCamp.pioneerCamp"
        :camp-name="processingCamp.campName"
        :processing-signal="isProcessing"
      ></pioneer-camp>
      <div @mousemove="enter2()" @mouseleave="leave2()" class="campLabel">
        <el-tag color="rgba(255,255,255,0)" type effect="plain">
          往期创新院
          <transition name="el-zoom-in-center">
            <i v-if="this.iAppear2==1" class="el-icon-s-operation el-icon--right" />
          </transition>
        </el-tag>
      </div>
      <div>
        <pioneer-camp
          v-for="(currentCamp,index) in currentList"
          :key="index"
          :pioneer-camp-index="currentCamp.pioneerCamp"
          :camp-name="currentCamp.campName"
          :processing-signal="processing"
        ></pioneer-camp>
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
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import PioneerCamp from '../components/PioneerCamp'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'RegistrationManagePage',
  data() {
    return {
      iAppear1: 0,
      iAppear2: 0,
      test: 2,
      isOnLoad: true,
      specialColor: 1,
      pioneerCampList: [],
      total: 0,
      processingList: [],
      currentList: [],
      value: true,
      isProcessing: 'true',
      processing: 'false'
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
          this.createPioneerCampButton()
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
    handleCurrentChange: function(currentPage) {
      this.currentList = []
      if (typeof this.pioneerCampList[(currentPage - 1) * 8] !== 'undefined') {
        this.$set(
          this.currentList,
          0,
          this.pioneerCampList[(currentPage - 1) * 8]
        )
      }
      if (
        typeof this.pioneerCampList[1 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          1,
          this.pioneerCampList[1 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.pioneerCampList[2 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          2,
          this.pioneerCampList[2 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.pioneerCampList[3 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          3,
          this.pioneerCampList[3 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.pioneerCampList[4 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          4,
          this.pioneerCampList[4 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.pioneerCampList[5 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          5,
          this.pioneerCampList[5 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.pioneerCampList[6 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          6,
          this.pioneerCampList[6 + (currentPage - 1) * 8]
        )
      }
      if (
        typeof this.pioneerCampList[7 + (currentPage - 1) * 8] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          7,
          this.pioneerCampList[7 + (currentPage - 1) * 8]
        )
      }
    },
    enter1() {
      this.iAppear1 = 1
    },
    leave1() {
      this.iAppear1 = 0
    },
    enter2() {
      this.iAppear2 = 1
    },
    leave2() {
      this.iAppear2 = 0
    },
    createPioneerCampButton() {
      let index = 0
      let processingIndex = 0
      let campIndex = []
      let campName = []
      let campTime = []
      axios.get('http://117.50.34.200:8002/queryCamps/').then(response => {
        let camps = response.data
        for (let i = 0; i < camps.length; i++) {
          campIndex[i] = camps[i].id
          campName[i] = camps[i].name
          campTime[i] = camps[i].time
        }
        for (
          let pioneerCampIndex = 0;
          pioneerCampIndex < camps.length;
          pioneerCampIndex++
        ) {
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
            campTime[pioneerCampIndex].substr(11, 4) +
              campTime[pioneerCampIndex].substr(16, 2) +
              campTime[pioneerCampIndex].substr(19, 2)
          )
          let newCampName = ''
          if (campName[pioneerCampIndex].length > 12) {
            newCampName = campName[pioneerCampIndex].slice(0, 11) + '...'
          } else if (campName[pioneerCampIndex].length <= 12) {
            newCampName = campName[pioneerCampIndex]
          }
          if (this.processingSignal !== 'false') {
            this.backguoundType = 'processing'
          }
          if (nowDate > timeNumber) {
            this.$set(this.pioneerCampList, index, {})
            this.$set(
              this.pioneerCampList[index],
              'pioneerCamp',
              campIndex[pioneerCampIndex]
            )
            this.$set(this.pioneerCampList[index], 'campName', newCampName)
            index += 1
          } else {
            this.$set(this.processingList, processingIndex, {})
            this.$set(
              this.processingList[processingIndex],
              'pioneerCamp',
              campIndex[pioneerCampIndex]
            )
            this.$set(this.processingList[processingIndex], 'campName', newCampName)
            processingIndex += 1
          }
        }
        this.total = this.pioneerCampList.length
        this.currentList = []
        if (typeof this.pioneerCampList[0] !== 'undefined') {
          this.$set(this.currentList, 0, this.pioneerCampList[0])
        }
        if (typeof this.pioneerCampList[1] !== 'undefined') {
          this.$set(this.currentList, 1, this.pioneerCampList[1])
        }
        if (typeof this.pioneerCampList[2] !== 'undefined') {
          this.$set(this.currentList, 2, this.pioneerCampList[2])
        }
        if (typeof this.pioneerCampList[3] !== 'undefined') {
          this.$set(this.currentList, 3, this.pioneerCampList[3])
        }
        if (typeof this.pioneerCampList[4] !== 'undefined') {
          this.$set(this.currentList, 4, this.pioneerCampList[4])
        }
        if (typeof this.pioneerCampList[5] !== 'undefined') {
          this.$set(this.currentList, 5, this.pioneerCampList[5])
        }
        if (typeof this.pioneerCampList[6] !== 'undefined') {
          this.$set(this.currentList, 6, this.pioneerCampList[6])
        }
        if (typeof this.pioneerCampList[7] !== 'undefined') {
          this.$set(this.currentList, 7, this.pioneerCampList[7])
        }
      })
    },
    createNewCamp() {
      let power = localStorage['powerCamp']
      if (power === 'true') {
        this.$store.commit('setNewCampCreatable', 'true')
        this.$router.push({
          name: 'CreateNewCamp'
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
    TitleBar,
    NavBar,
    PioneerCamp
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
button {
  display: inline-block;
  height: 150px;
  width: 300px;
  margin-top: 20px;
  margin-left: 40px;
  font-size: 50px;
}
.setcenter {
  position: relative;
  margin: 0 5% 0 5%;
}
.newpagination {
  width: 700px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
.createButton {
  position: relative;
  display: inline-block;
  height: 200px;
  width: 300px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
  cursor: pointer;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
}
.campLabel {
  margin-top: 70px;
}
</style>

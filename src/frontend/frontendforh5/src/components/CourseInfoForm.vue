<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <div>
      <el-page-header @back="goBack" content></el-page-header>
      <div>
        <div id="app">
          <h1>课程设置</h1>
          <el-card class="box-card" shadow="hover">
            <el-tabs type="border-card" v-if="isEmpty">
              <h6 @click="gotoCreate">该创新院尚未创建班级，请到报名管理新建班级！(点我进入该创业营编辑班级信息)</h6>
            </el-tabs>
            <el-tabs v-model="editableTabsValue" type="border-card" v-if="!isEmpty">
              <el-tab-pane
                v-for="item in editableTabs"
                :key="item.name"
                :label="item.title"
                :name="item.name"
              >
                <div>
                  <section>本班课程信息：</section>
                  <el-divider></el-divider>
                  <section>
                    创新院期数：
                    <el-input v-model="campIndex" readonly="readonly" />
                  </section>
                  <section>
                    班级序号（内部序号）：
                    <el-input v-model="item.classID" readonly="readonly" />
                  </section>
                  <br />
                  <section>
                    班级名称：
                    <el-input v-model="item.className" readonly="readonly" />
                  </section>
                  <br />
                </div>
                <el-collapse v-model="activeNames">
                  <el-collapse-item title="本班级课时列表" name="2" width="500px">
                    <template>
                      <el-table :data="returnTable()" stripe class="elemeTable">
                        <el-table-column label="课时名称" prop="name">
                          <template slot-scope="scope">
                            <el-popover trigger="hover" placement="left">
                              <p>点此查看该课时详细信息</p>
                              <div
                                slot="reference"
                                class="name-wrapper"
                                @click="enterInfoPage(scope.row.course_id)"
                              >
                                <el-link>
                                  <el-badge is-dot>{{ scope.row.name }}</el-badge>
                                </el-link>
                              </div>
                            </el-popover>
                          </template>
                        </el-table-column>
                        <el-table-column label="上课时间" width="400px" prop="time_with_connect"></el-table-column>
                        <el-table-column label="上课地点" prop="location"></el-table-column>
                      </el-table>
                    </template>
                    <el-button
                      class="addLesson"
                      @click="createNewCourse"
                      round
                      icon="el-icon-circle-plus-outline"
                    >新建课时</el-button>
                  </el-collapse-item>
                </el-collapse>
              </el-tab-pane>
            </el-tabs>
          </el-card>
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
        </div>

        <el-dialog title="添加课程" :visible.sync="addLessonDialog" width="30%">
          <div>
            <span class="infoSpan">
              课时名称：
              <el-input v-model="fillLessonName" placeholder="请输入" class="nameInputBox" />
            </span>
          </div>
          <div>
            <span class="infoSpan">
              课时描述：
              <el-input
                v-model="fillLessonAbstract"
                class="textField"
                type="textarea"
                :autosize="{ minRows: 3}"
                placeholder="请输入内容"
              />
            </span>
          </div>
          <div>
            <span class="infoSpan">
              上课时间：
              <el-date-picker
                type="datetimerange"
                class="dateInput"
                v-model="fillLessonTime"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                align="right"
                value-format="yyyy-MM-dd HH:mm:ss"
                @change="format"
              />
            </span>
          </div>
          <div>
            <span class="infoSpan">
              上课地点：
              <el-input v-model="fillLessonLocation" placeholder="请输入" class="nameInputBox" />
            </span>
          </div>
          <div>
            <span class="infoSpan">
              讲师姓名：
              <el-input v-model="fillLessonInstructor" placeholder="请输入" class="nameInputBox" />
            </span>
          </div>
          <div>
            <span class="infoSpan">
              允许旁听人数：
              <el-input-number v-model="fillStanderAmount" size="medium" />
            </span>
          </div>
          <div v-if="fillStanderAmount>0">
            <span class="infoSpan">
              旁听人员注意事项：
              <el-input
                v-model="fillStanderTips"
                class="textField"
                type="textarea"
                :autosize="{ minRows: 3}"
                placeholder="请输入内容"
              />
            </span>
          </div>
          <span class="dialog-footer">
            <span slot="footer">
              <el-button @click="addLessonDialog = false">取 消</el-button>
              <el-button type="primary" @click="addLesson()">确 定</el-button>
            </span>
          </span>
        </el-dialog>
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
  name: 'CourseInfoForm',
  watch: {
    editableTabsValue: function() {
      var temp = parseInt(this.editableTabsValue)
      if (this.editableTabs[temp].classID) {
        this.currentClassID = this.editableTabs[temp].classID
      }
    },
    currentClassID: function() {
      this.refreshLessonList()
    }
  },
  data() {
    return {
      isEmpty: false,
      readonly: true,
      currentClassID: 0,
      editableTabsValue: '0',
      isOnLoad: true,
      campIndex: 0,
      specialColor: 2,
      tabAmount: 0,
      activeNames: ['1', '2', '3', '4'],
      addLessonDialog: false,
      dialogVisible: false,
      editableTabs: [],
      tabIndex: 0,
      tempClassID: null,
      tempClassName: '',
      fillLessonName: '',
      fillLessonTime: '',
      fillLessonLocation: '',
      fillLessonInstructor: '',
      fillLessonAbstract: '',
      fillStanderAmount: 0,
      fillStanderTips: '',
      lessonInfo: [],
      specificClassUrl: 'http://117.50.34.200:8002/specificClassMsg/',
      querySpecificLessonList: 'http://117.50.34.200:8002/specificLessonList/'
    }
  },
  methods: {
    gotoCreate () {
      this.$store.commit('setCampIndex', this.campIndex)
      this.$router.push({
        name: 'PioneerCampForm'
      })
    },
    enterInfoPage(id) {
      this.$store.commit('setCourseId', id)
      this.$store.commit('setCampIndex', this.campIndex)
      this.$store.commit('setClassId', this.currentClassID)
      this.$router.push({
        name: 'CourseInformation'
      })
    },
    createNewCourse() {
      let power = localStorage['powerCourse']
      if (power === 'true') {
        this.addLessonDialog = true
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    refreshLessonList() {
      const _this = this
      axios({
        url: _this.querySpecificLessonList,
        method: 'post',
        data: {
          belongto_camp: this.campIndex,
          belongto_campclass: this.currentClassID
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        this.lessonInfo = []
        var data = response.data
        for (var i = 0; i < data.length; i++) {
          this.lessonInfo.push({
            course_id: data[i].id,
            name: data[i].name,
            time: [data[i].time.split(',')[0], data[i].time.split(',')[1]],
            location: data[i].location,
            teacher: data[i].teacher,
            abstract: data[i].abstract,
            number_bystander: data[i].number_bystander,
            bystand_tips: data[i].bystand_tips,
            time_with_connect:
              data[i].time.split(',')[0] + ' 至 ' + data[i].time.split(',')[1]
          })
        }
      })
    },
    goBack() {
      this.$router.push({
        name: 'ClassManagePage'
      })
    },
    createFailFun() {
      this.$message('最多为本期创新院创建3个班级！')
    },
    returnTable() {
      return this.lessonInfo
    },
    format(val) {
      this.activity_time = val
    },
    addLesson() {
      if (
        this.fillLessonName != '' &&
        this.fillLessonTime != '' &&
        this.fillLessonLocation != '' &&
        this.fillLessonInstructor != '' &&
        this.fillLessonAbstract
      ) {
        axios({
          url: 'http://117.50.34.200:8002/addLesson/',
          method: 'post',
          data: {
            name: this.fillLessonName,
            time: this.fillLessonTime[0] + ',' + this.fillLessonTime[1],
            location: this.fillLessonLocation,
            teacher: this.fillLessonInstructor,
            abstract: this.fillLessonAbstract,
            number_bystander: this.fillStanderAmount,
            bystand_tips: this.fillStanderTips,
            belongto_camp: this.campIndex,
            belongto_campclass: this.currentClassID
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === '1') {
            this.addLessonDialog = false
            this.$message('课时新建成功')
            this.fillLessonName = ''
            this.fillLessonTime = ''
            this.fillLessonLocation = ''
            this.fillLessonInstructor = ''
            this.fillLessonAbstract = ''
            this.fillStanderAmount = 0
            this.fillStanderTips = ''
            this.refreshLessonList()
          }
        })
      } else {
        this.$message('信息填写不全，请填写完毕后再确认提交')
      }
    },
    querySpecificClass() {
      const _this = this
      axios({
        url: _this.specificClassUrl,
        method: 'post',
        data: {
          camp_id: this.campIndex
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        var dataTable = response.data
        if (dataTable.length === 0) {
          this.isEmpty = true
        } else {
          this.isEmpty = false
          for (var i = 0; i < dataTable.length; i++) {
            this.editableTabs.push({
              classID: dataTable[i].id,
              className: dataTable[i].name,
              studentNumber: dataTable[i].student_number,
              title: dataTable[i].name + '班信息'
            })
          }
          this.currentClassID = this.editableTabs[0].classID
        }
      })
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
          this.campIndex = parseInt(sessionStorage['campIndex'])
          this.querySpecificClass()
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
h6 {
  text-align: center;
  font-size: 18px;
}
.box-card {
  top: 20px;
  width: 1100px;
  position: relative;
  margin: auto;
  margin-top: 0;
}
.addLesson {
  position: relative;
  left: 40%;
  width: 150px;
  margin-top: 15px;
}
.nameInputBox {
  width: 80%;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
.elemeTable {
  width: 130%;
  position: relative;
  margin: auto;
}
.widthPx700 {
  width: 700px;
}
.dateInput {
  width: 80%;
}
.textField {
  width: 80%;
}
.infoSpan {
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
h6:hover {color:rgb(0, 26, 255);}
h6 {
  cursor: pointer;
}
.dialog-footer {
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
  position: relative;
  width: 60%;
  text-align: center;
  margin: auto;
}
</style>
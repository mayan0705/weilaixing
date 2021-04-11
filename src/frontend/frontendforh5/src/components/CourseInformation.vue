<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <div>
      <el-page-header @back="goBack" content></el-page-header>
      <div>
        <div id="app">
          <h1>课时详情</h1>
          <el-card class="box-card" shadow="hover" v-if="!isModifyPage">
            <template>
              <div class="infoDiv">
                <el-form label-position="left" inline class="demo-table-expand">
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">课时名称：</span>
                      <el-input
                        class="shortInputBox"
                        v-model="name"
                        placeholder="请输入"
                        readonly="readonly"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">讲师：</span>
                      <el-input
                        class="shortInputBox"
                        v-model="teacher"
                        placeholder="请输入"
                        readonly="readonly"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">上课地点：</span>
                      <el-input
                        class="shortInputBox"
                        v-model="location"
                        placeholder="请输入"
                        readonly="readonly"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">允许旁听人数：</span>
                      <el-input
                        class="shortInputBox"
                        v-model="number_bystander"
                        placeholder="请输入"
                        readonly="readonly"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">上课时间：</span>
                      <el-date-picker
                        class="widthPx700"
                        type="datetimerange"
                        v-model="time"
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期"
                        align="right"
                        value-format="yyyy-MM-dd HH:mm:ss"
                        @change="format"
                        readonly="readonly"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">课时描述：</span>
                      <el-input
                        v-model="abstract"
                        class="widthPx700"
                        type="textarea"
                        :autosize="{ minRows: 3}"
                        placeholder="请输入"
                        readonly="readonly"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item v-if="number_bystander>0" label>
                    <span class="infoSpan">
                      <span class="spanLong">旁听人员注意事项：</span>
                      <el-input
                        v-model="bystand_tips"
                        class="widthPx700"
                        type="textarea"
                        :autosize="{ minRows: 3}"
                        placeholder="请输入"
                        readonly="readonly"
                      />
                    </span>
                  </el-form-item>
                </el-form>
                <span class="formSpan">
                  <label for="ppt" class="listSpan">上传PPT文件：</label>
                  <input
                    type="file"
                    class="fileInput"
                    ref="file1"
                    id="ppt"
                    accept=".ppt, .pptx, application/pdf"
                  />
                  <input type="submit" class="submitButton" @click="pptSubmitEvent" />
                  <span class="infoSpan">
                    <span class="listSpan">
                      已上传文件：
                      <span class="fileSpan">{{ppt_name}}</span>
                    </span>
                  </span>
                </span>
                <span class="formSpan">
                  <label for="video" class="listSpan">上传视频文件：</label>
                  <input type="file" class="fileInput" ref="file2" id="video" accept="video/*" />
                  <input type="submit" class="submitButton" @click="videoSubmitEvent" />
                  <span class="infoSpan">
                    <span class="listSpan">
                      已上传文件：
                      <span class="fileSpan">{{video_name}}</span>
                    </span>
                  </span>
                </span>
                <span class="formSpan">
                  <label for="text" class="listSpan">上传文本文件：</label>
                  <input
                    type="file"
                    class="fileInput"
                    ref="file3"
                    id="text"
                    accept=".doc, .docx, application/pdf, text/*"
                  />
                  <input type="submit" class="submitButton" @click="textSubmitEvent" />
                  <span class="infoSpan">
                    <span class="listSpan">
                      已上传文件：
                      <span class="fileSpan">{{text_name}}</span>
                    </span>
                  </span>
                </span>
                <span class="formSpan">
                  <label for="others" class="listSpan">上传其它文件：</label>
                  <input type="file" class="fileInput" ref="file4" id="others" />
                  <input type="submit" class="submitButton" @click="othersSubmitEvent" />
                  <span class="infoSpan">
                    <span class="listSpan">
                      已上传文件：
                      <span class="fileSpan">{{others_name}}</span>
                    </span>
                  </span>
                </span>
                <el-button
                  type="primary"
                  icon="el-icon-edit"
                  class="operbutton0"
                  @click="changePage"
                >修改内容</el-button>
              </div>
            </template>
          </el-card>
          <el-card class="box-card" shadow="hover" v-if="isModifyPage">
            <template>
              <div class="infoDiv">
                <el-form label-position="left" inline class="demo-table-expand">
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">课时名称：</span>
                      <el-input class="shortInputBox" v-model="name" placeholder="请输入" />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">讲师：</span>
                      <el-input class="shortInputBox" v-model="teacher" placeholder="请输入" />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">上课地点：</span>
                      <el-input class="shortInputBox" v-model="location" placeholder="请输入" />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">允许旁听人数：</span>
                      <el-input
                        class="shortInputBox"
                        type="number"
                        v-model="number_bystander"
                        placeholder="请输入"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">上课时间：</span>
                      <el-date-picker
                        class="widthPx700"
                        type="datetimerange"
                        v-model="time"
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期"
                        align="right"
                        value-format="yyyy-MM-dd HH:mm:ss"
                        @change="format"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item label>
                    <span class="infoSpan">
                      <span class="spanShort">课时描述：</span>
                      <el-input
                        v-model="abstract"
                        class="widthPx700"
                        type="textarea"
                        :autosize="{ minRows: 3}"
                        placeholder="请输入"
                      />
                    </span>
                  </el-form-item>
                  <br />
                  <el-form-item v-if="number_bystander>0" label>
                    <span class="infoSpan">
                      <span class="spanLong">旁听人员注意事项：</span>
                      <el-input
                        v-model="bystand_tips"
                        class="widthPx700"
                        type="textarea"
                        :autosize="{ minRows: 3}"
                        placeholder="请输入"
                      />
                    </span>
                  </el-form-item>
                </el-form>
                <el-button
                  type="primary"
                  icon="el-icon-check"
                  class="operbutton"
                  @click="modifyCourseInfo"
                >保存修改</el-button>
                <el-button
                  type="primary"
                  icon="el-icon-close"
                  class="operbutton2"
                  @click="quitModify"
                >取消修改</el-button>
              </div>
            </template>
          </el-card>
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TitleBar from '../components/TitleBar.vue'
import NavBar from '../components/NavBar.vue'
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'CourseInformation',
  data() {
    return {
      isModifyPage: false,
      readonly: true,
      currentClassID: 0,
      editableTabsValue: '0',
      isOnLoad: true,
      courseIndex: 0,
      specialColor: 2,
      lessonInfo: [],
      name: '',
      time: [],
      location: '',
      teacher: '',
      abstract: '',
      number_bystander: 0,
      bystand_tips: '',
      uploadDialog: false,
      campIndex: 0,
      ppt_name: '（空）',
      video_name: '（空）',
      text_name: '（空）',
      others_name: '（空）'
    }
  },
  methods: {
    goBack() {
      this.$router.push({
        name: 'CourseInfoForm'
      })
    },
    format(val) {
      this.activity_time = val
    },
    changePage() {
      let power = localStorage['powerCourse']
      if (power === 'true') {
        if (this.isModifyPage === true) {
          this.isModifyPage = false
        } else if (this.isModifyPage === false) {
          this.isModifyPage = true
        }
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    quitModify() {
      this.createCourseInfo()
      this.changePage()
    },
    modifyCourseInfo() {
      if (
        this.name === '' ||
        this.time === [] ||
        this.location === '' ||
        this.abstract === '' ||
        this.teacher === '' ||
        this.number_bystander === ''
      ) {
        this.$message('表单信息填写不全，请填写完毕后再提交！')
      } else {
        if (this.number_bystander === 0) {
          this.bystand_tips = ''
        }
        axios({
          url: 'http://117.50.34.200:8002/modifyCourse/',
          method: 'post',
          data: {
            id: this.courseIndex,
            name: this.name,
            time: this.time[0] + ',' + this.time[1],
            teacher: this.teacher,
            location: this.location,
            abstract: this.abstract,
            number_bystander: this.number_bystander,
            bystand_tips: this.bystand_tips,
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
            this.$message({
              showClose: true,
              message: '课时信息修改成功！',
              type: 'success'
            })
            this.createCourseInfo()
            this.changePage()
          }
        })
      }
    },
    getFilesList() {
      this.ppt_name = '（空）'
      this.video_name = '（空）'
      this.text_name = '（空）'
      this.others_name = '（空）'
      axios({
        url: 'http://117.50.34.200:8002/getCoursefileName/',
        method: 'post',
        data: {
          id: this.courseIndex
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        this.lessonInfo = []
        let data = response.data
        if (data.length === 4) {
          if (data[0].ppt_name !== '') {
            this.ppt_name = data[0].ppt_name
          }
          if (data[1].video_name !== '') {
            this.video_name = data[1].video_name
          }
          if (data[2].text_name !== '') {
            this.text_name = data[2].text_name
          }
          if (data[3].others_name !== '') {
            this.others_name = data[3].others_name
          }
        }
      })
    },
    refreshLessonList() {
      this.campIndex = parseInt(sessionStorage['campIndex'])
      this.currentClassID = parseInt(sessionStorage['classId'])
      this.courseIndex = parseInt(sessionStorage['courseId'])
      axios({
        url: 'http://117.50.34.200:8002/specificLessonList/',
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
          if (data[i].id === this.courseIndex) {
            this.name = data[i].name
            this.time = [data[i].time.split(',')[0], data[i].time.split(',')[1]]
            this.location = data[i].location
            this.teacher = data[i].teacher
            this.abstract = data[i].abstract
            this.number_bystander = data[i].number_bystander
            this.bystand_tips = data[i].bystand_tips
            this.getFilesList()
            break
          }
        }
      })
    },
    createCourseInfo() {
      this.refreshLessonList()
    },
    pptSubmitEvent() {
      let power = localStorage['powerCourse']
      if (power === 'true') {
        const _this = this
        let formData = new FormData()
        formData.append('id', this.courseIndex)
        formData.append('ppt_name', _this.$refs.file1.files[0].name)
        formData.append('ppt', _this.$refs.file1.files[0])
        axios
          .post('http://117.50.34.200:8002/operateFiles/', formData, {
            'Content-Type': 'multipart/form-data'
          })
          .then(response => {
            if (response.data.code === '1') {
              this.$message({
                showClose: true,
                message: '文件上传成功！',
                type: 'success'
              })
              this.getFilesList()
            }
          })
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    videoSubmitEvent() {
      let power = localStorage['powerCourse']
      if (power === 'true') {
        const _this = this
        let formData = new FormData()
        formData.append('id', this.courseIndex)
        formData.append('video_name', _this.$refs.file2.files[0].name)
        formData.append('video', _this.$refs.file2.files[0])
        axios
          .post('http://117.50.34.200:8002/operateFiles/', formData, {
            'Content-Type': 'multipart/form-data'
          })
          .then(response => {
            if (response.data.code === '1') {
              this.$message({
                showClose: true,
                message: '文件上传成功！',
                type: 'success'
              })
              this.getFilesList()
            }
          })
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    textSubmitEvent() {
      let power = localStorage['powerCourse']
      if (power === 'true') {
        const _this = this
        let formData = new FormData()
        formData.append('id', this.courseIndex)
        formData.append('text_name', _this.$refs.file3.files[0].name)
        formData.append('text', _this.$refs.file3.files[0])
        axios
          .post('http://117.50.34.200:8002/operateFiles/', formData, {
            'Content-Type': 'multipart/form-data'
          })
          .then(response => {
            if (response.data.code === '1') {
              this.$message({
                showClose: true,
                message: '文件上传成功！',
                type: 'success'
              })
              this.getFilesList()
            }
          })
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    othersSubmitEvent() {
      let power = localStorage['powerCourse']
      if (power === 'true') {
        const _this = this
        let formData = new FormData()
        formData.append('id', this.courseIndex)
        formData.append('others_name', _this.$refs.file4.files[0].name)
        formData.append('others', _this.$refs.file4.files[0])
        axios
          .post('http://117.50.34.200:8002/operateFiles/', formData, {
            'Content-Type': 'multipart/form-data'
          })
          .then(response => {
            if (response.data.code === '1') {
              this.$message({
                showClose: true,
                message: '文件上传成功！',
                type: 'success'
              })
              this.getFilesList()
            }
          })
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    toUploadFiles() {
      let power = localStorage['powerCourse']
      if (power === 'true') {
        this.uploadDialog = true
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
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
          this.createCourseInfo()
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
.addLesson {
  position: relative;
  left: 40%;
  width: 150px;
}
.box-card {
  top: 60px;
  width: 1100px;
  position: relative;
  margin: auto;
  margin-top: 0;
}
.demo-table-expand {
  font-size: 0;
  width: 130%;
  position: relative;
  margin: auto;
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
.widthPx700 {
  width: 700px;
}
.spanShort {
  display: inline-block;
  width: 8em;
  text-align: left;
  font-size: 18px;
}
.spanLong {
  display: inline-block;
  width: 10em;
  text-align: left;
  font-size: 18px;
}
.shortInputBox {
  width: 190px;
}
.infoDiv {
  width: 800px;
  margin: auto;
}
.infoSpan {
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.formSpan {
  display: block;
  margin-top: 30px;
  margin-bottom: 30px;
}
.fileSpan {
  color: blue;
}
.listSpan {
  font-size: 18px;
}
.fileInput {
  border: 1px solid burlywood;
}
.submitButton {
  border: 1px solid burlywood;
  height: 28px;
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
</style>
<template>
  <div class="managetable">
    <div :class="ifEdit==0?'NoAllow':'DoAllow'">
      <ul :class="ifEdit==0?'th1':'th2'">
        <li class="lili">管理员账号</li>
        <li class="lili">管理员密码</li>
        <li class="lili">新建创新院权限</li>
        <li class="lili">课程管理权限</li>
        <li class="lili">新建活动权限</li>
        <li class="lili">新建管理员权限</li>
        <li class="lili" v-if="ifEdit==0">暂不可操作</li>
        <li class="lili" v-if="ifEdit==1">操作</li>
      </ul>
      <ul v-for="item in tableData" :key="item.index">
        <li>
          <input
            :class="inputStyle"
            :disabled="ifInput"
            v-model="item.admin_name"
            readonly="readonly"
          />
        </li>
        <li>
          <input :class="inputStyle" :disabled="ifInput" v-model="item.admin_password" />
        </li>
        <li>
          <el-switch
            class="switchcss"
            v-model="item.power_create_camp"
            active-text="有"
            inactive-text="无"
          ></el-switch>
        </li>
        <li>
          <el-switch
            class="switchcss"
            v-model="item.power_create_course"
            active-text="有"
            inactive-text="无"
          ></el-switch>
        </li>
        <li>
          <el-switch
            class="switchcss"
            v-model="item.power_create_activity"
            active-text="有"
            inactive-text="无"
          ></el-switch>
        </li>
        <li>
          <el-switch
            class="switchcss"
            v-model="item.power_create_administrator"
            active-text="有"
            inactive-text="无"
          ></el-switch>
        </li>
        <transition name="el-zoom-in-left">
          <li v-if="ifEdit==1">
            <el-button
              class="deleteButton"
              @click="deleteMember(item.admin_password,item.admin_name,
                                  item.power_create_camp,item.power_create_course,
                                  item.power_create_activity,item.power_create_administrator)"
              type="danger"
              icon="el-icon-delete"
            >删除</el-button>
          </li>
        </transition>
      </ul>
    </div>
    <br />
    <el-button
      v-if="ifEdit==0"
      type="primary"
      icon="el-icon-edit"
      class="NewButton"
      @click="editRight();inputStyle='inputStyle2'"
    >编 辑</el-button>
    <el-button
      v-if="ifEdit==0"
      type="primary"
      icon="el-icon-plus"
      class="InsertButton"
      @click="createNewAdmin"
    >新建管理员</el-button>
    <el-button
      v-if="ifEdit==1"
      type="primary"
      icon="el-icon-check"
      class="operbutton"
      @click="saveChange();inputStyle='inputStyle1'"
    >保存</el-button>
    <br />
    <br />
    <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <div>新建一位管理员</div>
      <br />
      <div>
        用户名：
        <el-input v-model="tempUser" placeholder="请输入" />
      </div>
      <div>
        密码：
        <el-input v-model="tempPassword" placeholder="请输入" />
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="newManager();dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'SuperUserManageTable',
  props: {},
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
          this.queryManager()
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
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    editRight() {
      let power = localStorage['powerAdministrator']
      if (power === 'true') {
        this.ifEdit = 1
        this.ifInput = false
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    createNewAdmin() {
      let power = localStorage['powerAdministrator']
      if (power === 'true') {
        this.dialogVisible = true
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    saveChange() {
      const _this = this
      axios({
        url: _this.modifyAdministrator,
        method: 'post',
        data: { admin: JSON.stringify(_this.tableData) },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        if (response.data.code === '1') {
          this.$message('管理员信息修改成功！')
        }
      })
      this.ifEdit = 0
      this.ifInput = true
    },
    deleteMember(temp1, temp2, temp3, temp4, temp5, temp6) {
      var i = 0
      for (; i < this.tableData.length; i++) {
        if (
          this.tableData[i].admin_password == temp1 &&
          this.tableData[i].admin_name == temp2 &&
          this.tableData[i].power_create_camp == temp3 &&
          this.tableData[i].power_create_course == temp4 &&
          this.tableData[i].power_create_activity == temp5 &&
          this.tableData[i].power_create_administrator == temp6
        ) {
          break
        }
      }
      this.tableData.splice(i, 1)
    },
    queryManager() {
      const _this = this
      axios({
        url: _this.queryAdministrator,
        method: 'post'
      }).then(response => {
        var admin = response.data
        for (var i = 0; i < admin.length; i++) {
          this.tableData.push({
            admin_name: admin[i].admin_name,
            admin_password: admin[i].admin_password,
            power_create_camp: admin[i].power_create_camp,
            power_create_course: admin[i].power_create_course,
            power_create_activity: admin[i].power_create_activity,
            power_create_administrator: admin[i].power_create_administrator
          })
        }
      })
    },
    newManager() {
      const _this = this
      if (this.tempPassword != '' && this.tempUser != '') {
        axios({
          url: _this.addAdministrator,
          method: 'post',
          data: {
            admin_name: _this.tempUser,
            admin_password: _this.tempPassword,
            power_create_camp: 0,
            power_create_course: 0,
            power_create_activity: 0,
            power_create_administrator: 0
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === '1') {
            this.$message('用户创建成功！')
            this.tableData.push({
              admin_password: this.tempPassword,
              admin_name: this.tempUser,
              power_create_camp: false,
              power_create_course: false,
              power_create_activity: false,
              power_create_administrator: false
            })
            this.tempPassword = ''
            this.tempUser = ''
          } else if (response.data.code === '3') {
            this.$message('该账号在数据库内已存在，请重新创建！')
            this.tempPassword = ''
            this.tempUser = ''
          }
        })
      } else {
        this.$message('用户名或密码不得为空，请重新输入！')
        this.tempPassword = ''
        this.tempUser = ''
      }
    }
  },
  data() {
    return {
      ifInput: true,
      readonly: true,
      addAdministrator: 'http://117.50.34.200:8002/addAdministrator/',
      queryAdministrator: 'http://117.50.34.200:8002/queryAdministrator/',
      modifyAdministrator: 'http://117.50.34.200:8002/modifyAdministrator/',
      tempUser: '',
      tempPassword: '',
      dialogVisible: false,
      ifEdit: 0,
      tableData: [],
      inputStyle: 'inputStyle1'
    }
  }
}
</script>


<style scoped>
.NoAllow {
  pointer-events: none;
  background-size: 1280px 70px;
  background-image: url(../assets/pro.jpg);
  background-repeat: repeat-y;
}
.DoAllow {
  pointer-events: Auto;
  background-size: 1280px 70px;
  background: rgba(255, 255, 255, 0.8);
  background-repeat: repeat-y;
}
.managetable {
  position: relative;
  width: 1280px;
  margin: auto;
}
.operbutton {
  width: 100px;
  left: 45.5%;
  position: relative;
  margin: auto;
}
.NewButton {
  width: 120px;
  left: 37.5%;
  position: relative;
  margin: auto;
}
.InsertButton {
  width: 120px;
  left: 42.5%;
  position: relative;
  margin: auto;
}
ul {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 1280px;
  height: 45px;
  line-height: 20px;
  border: 1px solid #7e7cf3;
}
ul li {
  display: block;
  width: 14.2857%;
  float: left;
  font-family: '微软雅黑';
  color: rgba(120, 120, 120, 1);
  font-size: 18px;
  text-align: center;
}
.th1 {
  background-size: 1280px 70px;
  background-image: url(../assets/prox.jpg);
  background-repeat: repeat-y;
  position: relative;
}
.th2 {
  background-size: 1280px 70px;
  background: rgba(211, 229, 240, 0.25);
  background-repeat: repeat-y;
  position: relative;
}
.lili {
  line-height: 45px;
  font-size: 23px;
}
input {
  width: 95%;
  height: 30px;
  position: relative;
  text-align: center;
  top: 6px;
}
.deleteButton {
  width: 85px;
  height: 30px;
  position: relative;
  top: 9px;
  padding-top: 7px;
}
.switchcss {
  position: relative;
  top: 12px;
}
div {
  font-family: '微软雅黑';
}
.inputStyle1 {
  background-color: rgba(238, 225, 223, 0.399);
  border: 1 none;
  border-radius: 20px;
  outline: none;
}
.inputStyle2 {
  background-color: rgba(255, 255, 255, 0.7);
  border: 1 none;
  border-radius: 20px;
  outline: none;
}
</style>
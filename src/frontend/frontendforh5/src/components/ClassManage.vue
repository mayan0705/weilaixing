<template>
  <div class="form-div">
    <h1>班级管理</h1>
    <el-table height="200px" class="el-table-style" :data="classList" stripe>
      <el-table-column prop="className" label="班级名称" width="300px" align="center"></el-table-column>
      <el-table-column prop="classNumber" label="人数上限" width="300px" align="center"></el-table-column>
      <el-table-column label="删除班级" width="300px" align="center">
        <template slot-scope="scope">
          <el-button @click="isDeleteClass(scope.row.classId)" class="deletebutton">移除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button round icon="el-icon-plus" type="primary" @click="toNewClass">新建</el-button>
    <el-button round icon="el-icon-back" type="danger" @click="$emit('closeClassManage')">退出</el-button>
    <el-dialog
      contenteditable="true"
      class="set-top"
      title="新建班级"
      :visible.sync="dialogVisible"
      width="30%"
      :modal="isModal"
    >
      <div>
        班级名：
        <el-input v-model="newClassName" ref="inputVal" placeholder="请输入" />
      </div>
      <div>
        人数上限：
        <el-input v-model="newClassNumber" placeholder="请输入" />
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="newClass();dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'ClassManage',
  data() {
    return {
      isModal: false,
      classList: [],
      dialogVisible: false,
      newClassName: '',
      newClassNumber: 0,
      deleteAble: false
    }
  },
  props: {
    campIndex: {
      type: Number,
      default: 0
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
          this.newClassName = ''
          this.newClassNumer = 0
          this.createClassManage()
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
    createClassManage() {
      this.deleteAble = sessionStorage['signinStatus'] === 'true'
      axios({
        url: 'http://117.50.34.200:8002/queryCampClass/',
        method: 'post',
        data: {
          camp_id: parseInt(sessionStorage['campIndex'])
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        this.classList = []
        let classes = response.data
        for (let i = 0; i < classes.length; i++) {
          this.$set(this.classList, i, {})
          this.$set(this.classList[i], 'classId', classes[i].id)
          this.$set(this.classList[i], 'className', classes[i].name)
          this.$set(this.classList[i], 'classNumber', classes[i].student_number)
        }
      })
    },
    toNewClass() {
      let power = localStorage['powerCamp']
      if (power === 'true') {
        this.dialogVisible = true
        this.$nextTick(function() {
          this.$refs.inputVal.focus()
        })
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    newClass() {
      if (this.newClassName != '' && this.newClassNumber != 0) {
        axios({
          url: 'http://117.50.34.200:8002/createCampClass/',
          method: 'post',
          data: {
            class_name: this.newClassName,
            class_number: this.newClassNumber,
            camp_id: parseInt(sessionStorage['campIndex'])
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === '1') {
            this.$message('班级创建成功！')
            this.createClassManage()
          }
        })
        this.createClassManage()
      } else {
        this.$message('班级名和人数上限不能为空，请重新输入！')
        this.newClassName = ''
        this.newClassNumber = 0
        this.toNewClass()
      }
    },
    isDeleteClass(temp) {
      let power = localStorage['powerCamp']
      if (power === 'true') {
        if (this.deleteAble === true) {
          this.$confirm('确定删除班级?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
            .then(() => {
              this.deleteClass(temp)
            })
            .catch(() => {
              this.$message({
                type: 'info',
                message: '已取消'
              })
            })
        } else {
          this.$alert('报名已开始，无法删除班级', '警告', {
            confirmButtonText: '确定',
            callback: action => {
              this.$message({
                type: 'info',
                message: `已取消`
              })
            }
          })
        }
      } else if (power === 'false') {
        this.$message({
          type: 'warning',
          message: '权限不足!'
        })
      }
    },
    deleteClass(temp) {
      axios({
        url: 'http://117.50.34.200:8002/deleteCampclass/',
        method: 'post',
        data: {
          class_id: temp
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        if (response.data.code === '1') {
          this.$message({
            type: 'success',
            message: '班级删除成功!'
          })
          this.createClassManage()
        }
      })
    }
  }
}
</script>

<style scoped>
h1 {
  text-align: center;
}
.form-div {
  text-align: center;
  border: 4px solid grey;
}
.el-table {
  position: relative;
  width: 1035px;
  margin: auto;
}
.el-button {
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
}
.el-table-style {
  position: relative;
  margin: auto;
  width: 900px;
}
.set-top {
  z-index: +100;
}
.deletebutton {
  position: relative;
  margin: auto;
}
</style>

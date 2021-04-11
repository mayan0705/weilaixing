<template>
  <div>
    <h1>校友列表</h1>
    <el-card shadow="hover" class="box-card">
      <div class="matetable" v-if="isSearch">
        <br />
        <el-table :data="currentList" stripe class="widthSet">
          <el-table-column>
            <el-table-column prop="UserID" label="用户ID" width="200px"></el-table-column>
            <template slot="header" slot-scope="scope">
              <el-select v-model="value" size="medium" placeholder="请选择">
                <el-option v-for="item in tablex" :key="item.index" :value="item"></el-option>
              </el-select>
              <el-input
                v-model="search"
                size="medium"
                suffix-icon="el-icon-edit"
                placeholder="输入关键字搜索"
                width="660px"
                disabled
              ></el-input>
            </template>
            <el-table-column prop="name" label="姓名" width="200px">
              <template slot-scope="scope">
                <el-popover trigger="hover" placement="left">
                  <p>点此查看该用户详细信息</p>
                  <div
                    slot="reference"
                    class="name-wrapper"
                    @click="enterInfoPage(scope.row.UserID,scope.row.belongto_camp,scope.row.belongto_campclass)"
                  >
                    <el-link>
                      <el-badge is-dot>{{ scope.row.name }}</el-badge>
                    </el-link>
                  </div>
                </el-popover>
              </template>
            </el-table-column>
            <el-table-column prop="telephoneNum" label="手机号" width="479px"></el-table-column>
            <el-table-column prop="belongto_camp" label="隶属创新院" width="200px"></el-table-column>
            <el-table-column prop="belongto_campclass" label="隶属班级" width="200px"></el-table-column>
          </el-table-column>
        </el-table>
        <div class="newpagination">
          <el-pagination
            @current-change="handleCurrentChange"
            :page-size="10"
            :pager-count="7"
            :hide-on-single-page="newValue"
            layout="prev, pager, next"
            :total="total"
          ></el-pagination>
        </div>
      </div>
      <div class="matetable" v-if="!isSearch">
        <br />
        <el-table :data="moreList" stripe class="widthSet">
          <el-table-column>
            <el-table-column prop="UserID" label="用户ID" width="200px"></el-table-column>
            <template slot="header" slot-scope="scope">
              <el-select v-model="value" size="medium" placeholder="请选择" class="choose-length">
                <el-option v-for="item in tablex" :key="item.index" :value="item"></el-option>
              </el-select>
              <el-input
                :disabled="value==''"
                v-model="search"
                size="medium"
                suffix-icon="el-icon-edit"
                placeholder="输入关键字搜索"
                width="660px"
              ></el-input>
            </template>
            <el-table-column prop="name" label="姓名" width="200px">
              <template slot-scope="scope">
                <el-popover trigger="hover" placement="left">
                  <p>点此查看该用户详细信息</p>
                  <div
                    slot="reference"
                    class="name-wrapper"
                    @click="enterInfoPage(scope.row.UserID,scope.row.belongto_camp,scope.row.belongto_campclass)"
                  >
                    <el-link>
                      <el-badge is-dot>{{ scope.row.name }}</el-badge>
                    </el-link>
                  </div>
                </el-popover>
              </template>
            </el-table-column>
            <el-table-column prop="telephoneNum" label="手机号" width="479px"></el-table-column>
            <el-table-column prop="belongto_camp" label="隶属期数" width="200px"></el-table-column>
            <el-table-column prop="belongto_campclass" label="隶属班级" width="200px"></el-table-column>
          </el-table-column>
        </el-table>
        <div class="newpagination">
          <el-pagination
            @current-change="handleCurrentChangeForSearch"
            :page-size="10"
            :pager-count="7"
            :hide-on-single-page="newValue"
            layout="prev, pager, next"
            :total="searchTotal"
          ></el-pagination>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'SchoolmateTable',
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
          this.querySchoolmate()
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
      queryschoolmate: 'http://117.50.34.200:8002/querySchoolmate/',
      tempID: null,
      search: '',
      value: '',
      tablex: ['姓名', '用户ID', '手机号', '隶属期数'],
      schoolMateInfo: [],
      total: 0,
      searchTotal: 0,
      currentList: [],
      searchList: [],
      newValue: true,
      moreList: [],
      isSearch: false
    }
  },
  watch: {
    value: function() {
      if (this.value === '') {
        this.isSearch = true
      } else if (this.value !== '') {
        this.search = ''
        this.isSearch = false
        this.searchList = this.schoolMateInfo
        this.searchTotal = this.searchList.length
        this.moreList = []
        if (typeof this.searchList[0] !== 'undefined') {
          this.$set(this.moreList, 0, this.searchList[0])
        }
        if (typeof this.searchList[1] !== 'undefined') {
          this.$set(this.moreList, 1, this.searchList[1])
        }
        if (typeof this.searchList[2] !== 'undefined') {
          this.$set(this.moreList, 2, this.searchList[2])
        }
        if (typeof this.searchList[3] !== 'undefined') {
          this.$set(this.moreList, 3, this.searchList[3])
        }
        if (typeof this.searchList[4] !== 'undefined') {
          this.$set(this.moreList, 4, this.searchList[4])
        }
        if (typeof this.searchList[5] !== 'undefined') {
          this.$set(this.moreList, 5, this.searchList[5])
        }
        if (typeof this.searchList[6] !== 'undefined') {
          this.$set(this.moreList, 6, this.searchList[6])
        }
        if (typeof this.searchList[7] !== 'undefined') {
          this.$set(this.moreList, 8, this.searchList[7])
        }
        if (typeof this.searchList[8] !== 'undefined') {
          this.$set(this.moreList, 7, this.searchList[8])
        }
        if (typeof this.searchList[9] !== 'undefined') {
          this.$set(this.moreList, 9, this.searchList[9])
        }
      }
    },
    search: function() {
      if (this.value === '姓名') {
        this.isSearch = false
        this.searchList = this.schoolMateInfo.filter(
          data =>
            !this.search ||
            data.name.toLowerCase().includes(this.search.toLowerCase())
        )
        this.searchTotal = this.searchList.length
        this.moreList = []
        if (typeof this.searchList[0] !== 'undefined') {
          this.$set(this.moreList, 0, this.searchList[0])
        }
        if (typeof this.searchList[1] !== 'undefined') {
          this.$set(this.moreList, 1, this.searchList[1])
        }
        if (typeof this.searchList[2] !== 'undefined') {
          this.$set(this.moreList, 2, this.searchList[2])
        }
        if (typeof this.searchList[3] !== 'undefined') {
          this.$set(this.moreList, 3, this.searchList[3])
        }
        if (typeof this.searchList[4] !== 'undefined') {
          this.$set(this.moreList, 4, this.searchList[4])
        }
        if (typeof this.searchList[5] !== 'undefined') {
          this.$set(this.moreList, 5, this.searchList[5])
        }
        if (typeof this.searchList[6] !== 'undefined') {
          this.$set(this.moreList, 6, this.searchList[6])
        }
        if (typeof this.searchList[7] !== 'undefined') {
          this.$set(this.moreList, 8, this.searchList[7])
        }
        if (typeof this.searchList[8] !== 'undefined') {
          this.$set(this.moreList, 7, this.searchList[8])
        }
        if (typeof this.searchList[9] !== 'undefined') {
          this.$set(this.moreList, 9, this.searchList[9])
        }
      } else if (this.value === '用户ID') {
        this.isSearch = false
        this.searchList = this.schoolMateInfo.filter(
          data =>
            !this.search ||
            data.stringUserID.toLowerCase().includes(this.search.toLowerCase())
        )
        this.searchTotal = this.searchList.length
        this.moreList = []
        if (typeof this.searchList[0] !== 'undefined') {
          this.$set(this.moreList, 0, this.searchList[0])
        }
        if (typeof this.searchList[1] !== 'undefined') {
          this.$set(this.moreList, 1, this.searchList[1])
        }
        if (typeof this.searchList[2] !== 'undefined') {
          this.$set(this.moreList, 2, this.searchList[2])
        }
        if (typeof this.searchList[3] !== 'undefined') {
          this.$set(this.moreList, 3, this.searchList[3])
        }
        if (typeof this.searchList[4] !== 'undefined') {
          this.$set(this.moreList, 4, this.searchList[4])
        }
        if (typeof this.searchList[5] !== 'undefined') {
          this.$set(this.moreList, 5, this.searchList[5])
        }
        if (typeof this.searchList[6] !== 'undefined') {
          this.$set(this.moreList, 6, this.searchList[6])
        }
        if (typeof this.searchList[7] !== 'undefined') {
          this.$set(this.moreList, 8, this.searchList[7])
        }
        if (typeof this.searchList[8] !== 'undefined') {
          this.$set(this.moreList, 7, this.searchList[8])
        }
        if (typeof this.searchList[9] !== 'undefined') {
          this.$set(this.moreList, 9, this.searchList[9])
        }
      } else if (this.value === '手机号') {
        this.isSearch = false
        this.searchList = this.schoolMateInfo.filter(
          data =>
            !this.search ||
            data.telephoneNum.toLowerCase().includes(this.search.toLowerCase())
        )
        this.searchTotal = this.searchList.length
        this.moreList = []
        if (typeof this.searchList[0] !== 'undefined') {
          this.$set(this.moreList, 0, this.searchList[0])
        }
        if (typeof this.searchList[1] !== 'undefined') {
          this.$set(this.moreList, 1, this.searchList[1])
        }
        if (typeof this.searchList[2] !== 'undefined') {
          this.$set(this.moreList, 2, this.searchList[2])
        }
        if (typeof this.searchList[3] !== 'undefined') {
          this.$set(this.moreList, 3, this.searchList[3])
        }
        if (typeof this.searchList[4] !== 'undefined') {
          this.$set(this.moreList, 4, this.searchList[4])
        }
        if (typeof this.searchList[5] !== 'undefined') {
          this.$set(this.moreList, 5, this.searchList[5])
        }
        if (typeof this.searchList[6] !== 'undefined') {
          this.$set(this.moreList, 6, this.searchList[6])
        }
        if (typeof this.searchList[7] !== 'undefined') {
          this.$set(this.moreList, 8, this.searchList[7])
        }
        if (typeof this.searchList[8] !== 'undefined') {
          this.$set(this.moreList, 7, this.searchList[8])
        }
        if (typeof this.searchList[9] !== 'undefined') {
          this.$set(this.moreList, 9, this.searchList[9])
        }
      } else if (this.value === '隶属期数') {
        this.isSearch = false
        this.searchList = this.schoolMateInfo.filter(
          data =>
            !this.search ||
            data.stringCampId.toLowerCase().includes(this.search.toLowerCase())
        )
        this.searchTotal = this.searchList.length
        this.moreList = []
        if (typeof this.searchList[0] !== 'undefined') {
          this.$set(this.moreList, 0, this.searchList[0])
        }
        if (typeof this.searchList[1] !== 'undefined') {
          this.$set(this.moreList, 1, this.searchList[1])
        }
        if (typeof this.searchList[2] !== 'undefined') {
          this.$set(this.moreList, 2, this.searchList[2])
        }
        if (typeof this.searchList[3] !== 'undefined') {
          this.$set(this.moreList, 3, this.searchList[3])
        }
        if (typeof this.searchList[4] !== 'undefined') {
          this.$set(this.moreList, 4, this.searchList[4])
        }
        if (typeof this.searchList[5] !== 'undefined') {
          this.$set(this.moreList, 5, this.searchList[5])
        }
        if (typeof this.searchList[6] !== 'undefined') {
          this.$set(this.moreList, 6, this.searchList[6])
        }
        if (typeof this.searchList[7] !== 'undefined') {
          this.$set(this.moreList, 8, this.searchList[7])
        }
        if (typeof this.searchList[8] !== 'undefined') {
          this.$set(this.moreList, 7, this.searchList[8])
        }
        if (typeof this.searchList[9] !== 'undefined') {
          this.$set(this.moreList, 9, this.searchList[9])
        }
      }
    }
  },
  methods: {
    handleCurrentChange: function(currentPage) {
      this.currentList = []
      if (typeof this.schoolMateInfo[(currentPage - 1) * 10] !== 'undefined') {
        this.$set(
          this.currentList,
          0,
          this.schoolMateInfo[(currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[1 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          1,
          this.schoolMateInfo[1 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[2 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          2,
          this.schoolMateInfo[2 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[3 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          3,
          this.schoolMateInfo[3 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[4 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          4,
          this.schoolMateInfo[4 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[5 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          5,
          this.schoolMateInfo[5 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[6 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          6,
          this.schoolMateInfo[6 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[7 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          7,
          this.schoolMateInfo[7 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[8 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          8,
          this.schoolMateInfo[8 + (currentPage - 1) * 10]
        )
      }
      if (
        typeof this.schoolMateInfo[9 + (currentPage - 1) * 10] !== 'undefined'
      ) {
        this.$set(
          this.currentList,
          9,
          this.schoolMateInfo[9 + (currentPage - 1) * 10]
        )
      }
    },
    handleCurrentChangeForSearch: function(currentPage) {
      this.moreList = []
      if (typeof this.searchList[(currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 0, this.searchList[(currentPage - 1) * 10])
      }
      if (typeof this.searchList[1 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 1, this.searchList[1 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[2 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 2, this.searchList[2 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[3 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 3, this.searchList[3 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[4 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 4, this.searchList[4 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[5 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 5, this.searchList[5 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[6 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 6, this.searchList[6 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[7 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 7, this.searchList[7 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[8 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 8, this.searchList[8 + (currentPage - 1) * 10])
      }
      if (typeof this.searchList[9 + (currentPage - 1) * 10] !== 'undefined') {
        this.$set(this.moreList, 9, this.searchList[9 + (currentPage - 1) * 10])
      }
    },
    enterInfoPage(temp1, temp2, temp3) {
      this.$store.commit('setSchoolmateIndex', temp1)
      this.$store.commit('setSchoolmateCampIndex', temp2)
      this.$store.commit('setSchoolmateCampClassIndex', temp3)
      this.$router.push({
        name: 'SmInfoForm'
      })
    },
    querySchoolmate() {
      const _this = this
      axios({
        url: _this.queryschoolmate,
        method: 'post'
      }).then(response => {
        var returnMate = response.data
        for (var i = 0; i < returnMate.length; i = i + 5) {
          this.schoolMateInfo.push({
            UserID: returnMate[i].user_id,
            stringUserID: String(returnMate[i].user_id),
            name: returnMate[i + 1].user_name,
            telephoneNum: returnMate[i + 1].user_telephone,
            stringCampId: String(returnMate[i].camp_id),
            belongto_camp: returnMate[i + 4].name,
            belongto_campclass: returnMate[i + 3].name
          })
        }
        this.total = this.schoolMateInfo.length
        this.currentList = []
        if (typeof this.schoolMateInfo[0] !== 'undefined') {
          this.$set(this.currentList, 0, this.schoolMateInfo[0])
        }
        if (typeof this.schoolMateInfo[1] !== 'undefined') {
          this.$set(this.currentList, 1, this.schoolMateInfo[1])
        }
        if (typeof this.schoolMateInfo[2] !== 'undefined') {
          this.$set(this.currentList, 2, this.schoolMateInfo[2])
        }
        if (typeof this.schoolMateInfo[3] !== 'undefined') {
          this.$set(this.currentList, 3, this.schoolMateInfo[3])
        }
        if (typeof this.schoolMateInfo[4] !== 'undefined') {
          this.$set(this.currentList, 4, this.schoolMateInfo[4])
        }
        if (typeof this.schoolMateInfo[5] !== 'undefined') {
          this.$set(this.currentList, 5, this.schoolMateInfo[5])
        }
        if (typeof this.schoolMateInfo[6] !== 'undefined') {
          this.$set(this.currentList, 6, this.schoolMateInfo[6])
        }
        if (typeof this.schoolMateInfo[7] !== 'undefined') {
          this.$set(this.currentList, 8, this.schoolMateInfo[7])
        }
        if (typeof this.schoolMateInfo[8] !== 'undefined') {
          this.$set(this.currentList, 7, this.schoolMateInfo[8])
        }
        if (typeof this.schoolMateInfo[9] !== 'undefined') {
          this.$set(this.currentList, 9, this.schoolMateInfo[9])
        }
        this.isSearch = true
        this.moreList = []
        this.searchList = []
      })
    }
  }
}
</script>


<style scoped>
h1 {
  text-align: center;
}
.matetable {
  position: relative;
  width: 1280px;
  margin: auto;
}
.selector {
  width: 200px;
  position: relative;
  margin: auto;
}
.el-input {
  width: 460px;
}
.widthSet {
  width: 100%;
}
.newpagination {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
.el-input__inner {
  width: 650px;
}
.choose-length {
  width: 500px;
}
.box-card {
  top: 20px;
  width: 1280px;
  position: relative;
  margin: auto;
  margin-top: 0;
}
</style>
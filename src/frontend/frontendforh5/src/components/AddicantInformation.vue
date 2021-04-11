<template>
  <div>
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <div>
      <el-page-header @back="goBack" content></el-page-header>
      <div>
        <el-card class="box-card" shadow="hover">
          <div slot="header" class="clearfix">
            <h1>报名资料</h1>
          </div>
          <h2 class="title">基本资料</h2>
          <el-divider></el-divider>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">姓名：</span>
              <el-input class="shortInputBox" v-model="user_name" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">账户ID（唯一识别码）：</span>
              <el-input class="shortInputBox" v-model="user_id" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">性别：</span>
              <el-input class="shortInputBox" v-model="user_gender" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">电子邮箱：</span>
              <el-input class="shortInputBox" v-model="user_email" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">手机号：</span>
              <el-input class="shortInputBox" v-model="user_telephone" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">微信号：</span>
              <el-input class="shortInputBox" v-model="user_weixinnumber" readonly="readonly" />
            </span>
          </div>
          <el-divider></el-divider>
          <h2 class="title">报名信息</h2>
          <el-divider></el-divider>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">出生日期：</span>
              <el-input class="shortInputBox" v-model="user_birthday" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">所在城市：</span>
              <el-input class="shortInputBox" v-model="user_city" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">学历：</span>
              <el-input class="shortInputBox" v-model="educated_condition" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">是否认可缺勤制度：</span>
              <el-input
                class="shortInputBox"
                v-model="user_other_tips_message_question_for_absenceitem"
                readonly="readonly"
              />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              报名信息获取来源：
              <el-input class="mediumInputBox" v-model="messageway_to_camp" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">一号推荐人信息：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="user_referee1_message"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">二号推荐人信息：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="user_referee2_message"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">三号推荐人信息：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="user_referee3_message"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">参加创新院理由：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="reasons_for_signin"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">能为他人带来什么：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="contribution_to_others"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">用户最高学历时间情况：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="user_educondition_time_detials"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">用户创业前从业情况：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="user_beforestartup_company_condition"
            readonly="readonly"
          />
          <br />
          <br />
          <el-divider></el-divider>
          <h2 class="title">职业信息</h2>
          <el-divider></el-divider>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">公司名称：</span>
              <el-input class="shortInputBox" v-model="company_name" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">公司ID（唯一识别码）：</span>
              <el-input class="shortInputBox" v-model="user_company" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">公司职位：</span>
              <el-input class="shortInputBox" v-model="user_post" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">公司成立时间：</span>
              <el-input class="shortInputBox" v-model="startup_time" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">公司品牌：</span>
              <el-input class="shortInputBox" v-model="brand_name" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">公司总部所在城市：</span>
              <el-input class="shortInputBox" v-model="center_city" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">收入规模：</span>
              <el-input class="shortInputBox" v-model="income_scale" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">公司人员数量：</span>
              <el-input class="shortInputBox" v-model="membership" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">融资情况：</span>
              <el-input class="shortInputBox" v-model="financing_situation" readonly="readonly" />
            </span>
            <span class="spanright">
              <span class="spanLong">公司应用或公众号：</span>
              <el-input class="shortInputBox" v-model="app_or_publicAccounts" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              <span class="spanShort">市场估值：</span>
              <el-input class="shortInputBox" v-model="value_of_assessment" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">
              公司网站：
              <el-input class="longInputBox" v-model="website" readonly="readonly" />
            </span>
          </div>
          <div class="text item">
            <span class="spanleft">公司/项目介绍：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="abstract"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">主要运营数据：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="main_operational_data"
            readonly="readonly"
          />
          <br />
          <br />
          <div class="text item">
            <span class="spanleft">公司补充说明：</span>
          </div>
          <el-input
            class="shortInputBox bigText"
            type="textarea"
            :autosize="{ minRows: 1}"
            v-model="additions"
            readonly="readonly"
          />
          <br />
          <br />
        </el-card>
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
  name: 'AddicantInformation',
  components: {
    TitleBar,
    NavBar
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
          this.user_id = parseInt(sessionStorage['addicantIndex'])
          this.querymessage()
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
      isOnLoad: true,
      specialColor: 1,
      readonly: true,
      user_name: '',
      user_gender: '',
      user_weixinnumber: '',
      user_telephone: '',
      user_email: '',
      user_id: null,
      user_birthday: '',
      user_company: '',
      user_post: '',
      user_city: '',
      user_referee1_message: '',
      user_referee2_message: '',
      user_referee3_message: '',
      user_other_tips_message_question_for_absenceitem: '',
      reasons_for_signin: '',
      contribution_to_others: '',
      messageway_to_camp: '',
      educated_condition: '',
      user_educondition_time_detials: '',
      user_beforestartup_company_condition: '',
      company_name: '',
      brand_name: '',
      website: '',
      app_or_publicAccounts: '',
      startup_time: '',
      center_city: '',
      membership: '',
      abstract: '',
      main_operational_data: '',
      income_scale: '',
      financing_situation: '',
      value_of_assessment: '',
      additions: '',
      selectSpecificSchoolmate:
        'http://117.50.34.200:8002/selectSpecificSchoolmate/'
    }
  },
  methods: {
    goBack() {
      this.$router.push({
        name: 'PioneerCampUserInformation'
      })
    },
    querymessage() {
      const _this = this
      axios({
        url: _this.selectSpecificSchoolmate,
        method: 'post',
        data: {
          id: _this.user_id
        },
        transformRequest: [
          function(data) {
            return Qs.stringify(data)
          }
        ]
      }).then(response => {
        var data = response.data
        let userGender = ''
        let userPosition = ''
        let userEducate = ''
        let userWay = ''
        let userFinancial = ''
        if (data[0].user_gender === 'm') {
          userGender = '男'
        } else if (data[0].user_gender === 'f') {
          userGender = '女'
        }
        if (data[1].user_post === 'F') {
          userPosition = '创始人'
        } else if (data[1].user_post === 'CF') {
          userPosition = '联合创始人'
        } else if (data[1].user_post === 'P') {
          userPosition = '董事长'
        } else if (data[1].user_post === 'CEO') {
          userPosition = 'CEO'
        } else if (data[1].user_post === 'Others') {
          userPosition = '其他'
        }
        if (data[1].educated_condition === 'PhD') {
          userEducate = '博士研究生'
        } else if (data[1].educated_condition === 'MBA') {
          userEducate = '硕士研究生'
        } else if (data[1].educated_condition === 'Bachelor') {
          userEducate = '本科'
        } else if (data[1].educated_condition === 'College') {
          userEducate = '专科'
        } else if (data[1].educated_condition === 'Others') {
          userEducate = '其他'
        }
        if (data[1].messageway_to_camp === 'weixin') {
          userWay = '微信朋友圈'
        } else if (data[1].messageway_to_camp === 'friend') {
          userWay = '朋友推荐'
        } else if (data[1].messageway_to_camp === 'Pubaccount') {
          userWay = '未来之星公众号：EdStars未来同学会'
        } else if (data[1].messageway_to_camp === 'web') {
          userWay = '好未来官网'
        } else if (data[1].messageway_to_camp === 'media') {
          userWay = '媒体报道'
        } else if (data[1].messageway_to_camp === 'others') {
          userWay = '其他'
        }
        if (data[2].financing_situation === 'N') {
          userFinancial = '尚未获得融资'
        } else if (data[2].financing_situation === 'seed/angel') {
          userFinancial = '已完成种子/天使融资'
        } else if (data[2].financing_situation === 'pre-A') {
          userFinancial = '已完成pre-A轮融资'
        } else if (data[2].financing_situation === 'A') {
          userFinancial = '已完成A轮融资'
        } else if (data[2].financing_situation === 'refuse') {
          userFinancial = '不方便透露'
        } else if (data[2].financing_situation === 'others') {
          userFinancial = '其他'
        }
        this.user_name = data[0].user_name
        this.user_gender = userGender
        this.user_weixinnumber = data[0].user_weixinnumber
        this.user_telephone = data[0].user_telephone
        this.user_email = data[0].user_email
        this.user_id = data[1].user_id
        this.user_birthday = data[1].user_birthday
        this.user_company = data[1].user_company
        this.user_post = userPosition
        this.user_city = data[1].user_city
        this.user_referee1_message = data[1].user_referee1_message
        this.user_referee2_message = data[1].user_referee2_message
        this.user_referee3_message = data[1].user_referee3_message
        this.user_other_tips_message_question_for_absenceitem =
          data[1].user_other_tips_message_question_for_absenceitem
        this.reasons_for_signin = data[1].reasons_for_signin
        this.contribution_to_others = data[1].contribution_to_others
        this.messageway_to_camp = userWay
        this.educated_condition = userEducate
        this.user_educondition_time_detials =
          data[1].user_educondition_time_detials
        this.user_beforestartup_company_condition =
          data[1].user_beforestartup_company_condition
        this.company_name = data[2].name
        this.brand_name = data[2].brand_name
        this.website = data[2].website
        this.app_or_publicAccounts = data[2].app_or_publicAccounts
        this.startup_time = data[2].startup_time
        this.center_city = data[2].center_city
        this.membership = data[2].membership
        this.abstract = data[2].abstract
        this.main_operational_data = data[2].main_operational_data
        this.income_scale = data[2].income_scale
        this.financing_situation = userFinancial
        this.value_of_assessment = data[2].value_of_assessment
        this.additions = data[2].additions
      })
    }
  }
}
</script>


<style scoped>
.spanShort {
  display: inline-block;
  width: 6em;
  text-align: center;
}
.spanLong {
  display: inline-block;
  width: 12em;
  text-align: center;
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
  top: 60px;
  width: 1000px;
  position: relative;
  margin: auto;
}
.spanleft {
  position: absolute;
  left: 10%;
}
.spanright {
  position: absolute;
  left: 48%;
}
.title {
  text-indent: 2em;
}
.shortInputBox {
  width: 190px;
}
.mediumInputBox {
  width: 430px;
}
.longInputBox {
  width: 600px;
}
.bigText {
  position: relative;
  width: 700px;
  left: 10%;
}
</style>
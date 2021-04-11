<template>
  <view class="content">
    <view class="self-info">
      <view class="input-column-top">
        <text class="input-huge-title">
          <text class="highlight">*</text>您想要报名的班级
        </text>
        <radio-group class="class-group">
          <radio  v-for="campClass in campClasses" :key="campClass.id" :value="campClass.id" @click="classesChange" :data-classes="campClass.id">{{campClass.name}}</radio>
        </radio-group>
      </view>
      <text class="input-huge-title">一、基本信息</text>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>1.申请人姓名</text>
        <input class="input-column-box" type="text" v-model="name" />
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>2.性别</text>
        <radio-group class="gender-group">
          <radio value="m" @click="genderChange" data-gender="m">男</radio>
          <radio value="f" @click="genderChange" data-gender="f">女</radio>
        </radio-group>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>3.出生日期</text>
          <picker mode="date" :value="birthday" start="1900-01-01" :end="endDate" @change="birthdayChange">
            <view class="input-column-box">{{birthday}}</view>
          </picker>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>4.联系电话</text>
        <input class="input-column-box" type="text" v-model="telephone" />
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>5.常用微信</text>
        <input class="input-column-box" type="text" v-model="wechat"/>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>6.常用邮箱</text>
        <input class="input-column-box" type="text" v-model="email" @blur="checkEmail()"/>
      <view class="alertion" v-show="showAlert">邮箱不合法</view>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>7.常驻城市</text>
        <input class="input-column-box" type="text" v-model="city"/>
      </view>
      <text class="input-huge-title">二、教育/工作背景</text>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>1.最高学历</text>
        <radio-group class="class-group">
          <radio value="PhD" @click="educationChange" data-education="PhD">博士研究生</radio>
          <radio value="MBA" @click="educationChange" data-education="MBA">硕士研究生</radio>
          <radio value="Bachelor" @click="educationChange" data-education="Bachelor">本科</radio>
          <radio value="College" @click="educationChange" data-education="College">专科</radio>
          <radio value="Others" @click="educationChange" data-education="Others">其他</radio>
        </radio-group>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>2.最高学历毕业毕业院校及起止时间</text>
        <text class="explanation">如：2004-2008/北京大学/计算机科学/学士</text>
        <textarea class="long-text" v-model="educationTime" ></textarea>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>3.您创业前所在公司、职位及时间（包括国王创业经历）</text>
        <text class="explanation">如：2010-2015/好未来/产品经理</text>
        <textarea class="long-text" v-model="experience" ></textarea>
      </view>
      <text class="input-huge-title">三、公司/项目信息</text>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>1.公司品牌名称</text>
        <text class="explanation">公司主营业务/产品名称，请确保据此能够搜索到您的网站/公众号/App；
        <br>如尚未发布，填写“无”</text>
        <input class="input-column-box" type="text" v-model="brand" />
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>2.公司网址</text>
        <text class="explanation">如尚未发布，填写“无”</text>
        <input class="input-column-box" type="text" v-model="website" />
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>3.App或公众号名称</text>
        <text class="explanation">如尚未发布，填写“无”</text>
        <input class="input-column-box" type="text" v-model="application" />
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>4.公司成立时间</text>
          <picker mode="date" :value="date" start="1900-01-01" :end="endDate" @change="bindDateChange">
            <view class="input-column-box">{{date}}</view>
          </picker>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>5.公司总部所在城市</text>
        <input class="input-column-box" type="text" v-model="companyCity"/>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>6.公司员工数量（单位：人）</text>
        <input class="input-column-box" type="number" v-model="membership"/>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>7.您在企业中的职位</text>
        <radio-group class="class-group">
          <radio value="F" @click="educationChange" data-education="F">创始人</radio>
          <radio value="CF" @click="educationChange" data-education="CF">联合创始人</radio>
          <radio value="P" @click="educationChange" data-education="P">董事长</radio>
          <radio value="CEO" @click="educationChange" data-education="CEO">CEO</radio>
          <radio value="Others" @click="educationChange" data-education="Others">其他</radio>
        </radio-group>
     </view>
     <view class="input-column">
       <text class="input-column-title"><text class="highlight">*</text>8.公司项目介绍</text>
       <text class="explanation">为使面试组更好的了解您的公司/项目，烦请您认真填写</text>
       <textarea class="long-text" v-model="abstract" /></textarea>
     </view>
     <view class="input-column">
       <text class="input-column-title"><text class="highlight">*</text>9.公司主要运营数据</text>
       <text class="explanation">如：对于在线类业务，如注册用户量、应用下载量、日活/周活/月活等；对于线下业务，如学员数/用户数、市场覆盖率等</text>
       <textarea class="long-text" v-model="output" /></textarea>
     </view>
     <view class="input-column">
       <text class="input-column-title"><text class="highlight">*</text>10.上一年公司收入规模（单位：万元）</text>
       <text class="explanation">最近一年的收入</text>
       <input class="input-column-box" type="text" v-model="income"/>
     </view>
     <view class="input-column-top">
       <text class="input-column-title">
         <text class="highlight">*</text>11.公司目前融资情况
       </text>
       <radio-group class="class-group">
         <radio value="N" @click="financeChange" data-finance="N">尚未获得投资</radio>
         <radio value="seed/angel" @click="financeChange" data-finance="seed/angel">已完成种子/天使融资</radio>
         <radio value="pre-A" @click="financeChange" data-finance="pre-A">已完成pre-A轮融资</radio>
         <radio value="A" @click="financeChange" data-finance="A">已完成A轮融资</radio>
         <radio value="refuse" @click="financeChange" data-finance="refuse">不方便透露</radio>
         <radio value="others" @click="financeChange" data-finance="others">其他</radio>
       </radio-group>
     </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>12.公司目前估值（单位：万元）</text>
        <text class="explanation">如果暂无估值或不方便透露，可填写“0”</text>
        <input class="input-column-box" type="number" v-model="price"/>
      </view>
      <view class="input-column">
        <text class="input-column-title">13.关于您的公司/项目还有哪些补充说明，请在此填写</text>
        <textarea class="long-text" v-model="addition"/></textarea>
      </view>
      <text class="input-huge-title">四、关于推荐人</text>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>推荐人信息1:（姓名／公司／职位）</text>
        <textarea class="long-text" v-model="referee1"/></textarea>
      </view>
      <view class="input-column">
        <text class="input-column-title">推荐人信息2:（姓名／公司／职位）</text>
        <textarea class="long-text" v-model="referee2"/></textarea>
      </view>
      <view class="input-column">
        <text class="input-column-title">推荐人信息3:（姓名／公司／职位）</text>
        <textarea class="long-text" v-model="referee3"/></textarea>
      </view>
      <text class="input-huge-title">五、其他信息</text>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>
        1.未来之星创新院名额宝贵，培训统一安排时间内，不接受因个人活动冲突的请假理由，如缺勤达到总课程的1/3将被劝退，您是否接受此考勤要求？（是/否）</text>
        <input class="input-column-box" type="text" v-model="ifagree"/>
      </view>
      <view class="input-column">
        <text class="input-column-title"><text class="highlight">*</text>2.请简述您的申请理由（100字以内）</text>
        <textarea class="long-text" length="100" v-model="reason"/></textarea>
      </view>
      <view class="input-column">
        <text class="input-column-title">3.您能为创新院的其他学员做出哪些贡献？</text>
        <textarea class="long-text" v-model="contribution"/></textarea>
      </view>
      <view class="input-column">
         <text class="input-column-title"><text class="highlight">*</text>4.您通过何种渠道了解到“未来创新院”？</text>
          <radio-group class="class-group">
            <radio value="weixin" @click="financeChange" data-finance="weixin">微信朋友圈</radio>
            <radio value="friend" @click="financeChange" data-finance="friend">朋友推荐</radio>
            <radio value="Pubaccount" @click="financeChange" data-finance="Pubaccount">未来之星公众号：EdStars未来同学会</radio>
            <radio value="web" @click="financeChange" data-finance="web">好未来官网</radio>
            <radio value="media" @click="financeChange" data-finance="media">媒体报道</radio>
            <radio value="others" @click="financeChange" data-finance="others">其他</radio>
          </radio-group>
      </view>
      <view class="input-column">
        <text class="promise">未来之星创新院组委会承诺：以上所有信息仅供组委会了解申请人及项目情况，组委会承诺不会向任何第三方透露；祝您一切顺利！</text>
        <button class="save-btn" @tap="saveMessage">确认报名</button></view>
      </view>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data() {
    const currentDate = this.getDate({
      format: true
    })
    return {
      id: 0,
      userId: 0,
			campClasses: [],
      post: '',
      way: '',
      name: '',
      wechat: '',
      endDate: currentDate,
      birthday: '年-月-日',
      gender: '',
      education: '',
      classes: '',
      educationTime: '',
      experience: '',
      email: '',
      telephone: '',
      city: '',
      brand: '',
      website: '',
      application: '',
      date: '年-月-日',
      companyCity: '',
      membership: '',
      abstract: '',
      output: '',
      income: '',
      finance: '',
      price: '',
      addition: '',
      referee1: '',
      referee2: '',
      referee3: '',
      ifagree: '',
      reason: '',
      contribution: '',
      showAlert: false,
    }
  },
  methods: {
    genderChange(e) {
      const vm = this
      vm.gender = e.currentTarget.dataset.gender
    },
    educationChange(e) {
      const vm = this
      vm.education = e.currentTarget.dataset.education
    },
    classesChange(e) {
      const vm = this
      vm.classes = e.currentTarget.dataset.classes
    },
    financeChange(e) {
      const vm = this
      vm.finance = e.currentTarget.dataset.finance
    },
    bindDateChange: function(e) {
      this.date = e.target.value
    },
    birthdayChange: function(e) {
      this.birthday = e.target.value
    },
    postChange(e) {
      const vm = this
      vm.post = e.currentTarget.dataset.post
    },
    wayChange(e) {
      const vm = this
      vm.way = e.currentTarget.dataset.way
    },
    checkEmail() {
      const mail = this.email
      const reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
      if(reg.test(mail) === true) {
        this.showAlert = false
      }
      else this.showAlert = true
    },
    getDate(type) {
      const date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      if (type === 'start') {
        year = year - 60;
      } else if (type === 'end') {
        year = year + 2;
      }
      month = month > 9 ? month : '0' + month;
      day = day > 9 ? day : '0' + day;
      return `${year}-${month}-${day}`;
    },
    
    saveMessage() {
      const vm = this
      request
        .get('alterApplyData/', {
          user_id: vm.userId,
          user_birthday: vm.birthday,
          user_post: vm.post,
          user_referee1_message: vm.referee1,
          user_referee2_message: vm.referee2,
          user_referee3_message: vm.referee3,
          user_other_tips_message_question_for_absenceitem: vm.ifagree,
          reasons_for_signin: vm.reason,
          contribution_to_others: vm.contribution,
          messageway_to_camp: vm.way,
          educated_condition: vm.education,
          user_educondition_time_detials: vm.educationTime,
          user_beforestartup_company_condition: vm.experience,
          user_gender:vm.gender,
          user_weixinnumber: vm.wechat,
          user_telephone: vm.telephone,
          user_email: vm.email,
          user_name: vm.name,
          user_company: vm.brand,
          user_city: vm.city,
          website: vm.website,
          app_or_publicAccounts: vm.application,
          startup_time: vm.date,
          center_city: vm.companyCity,
          membership: vm.membership,
          abstract: vm.abstract,
          main_operational_data: vm.output,
          income_scale: vm.income,
          financing_situation: vm.finance,
          value_of_assessment: vm.price,
          additions: vm.addition,
        })
        .then(res => {
          if(res.data.statuscode === '400') {
            uni.showToast({
              title: '报名失败',
              duration: 1000,
            })
          }
          else if(res.data.statuscode === '200') {
            uni.showToast({
              title: '报名成功！',
              duration: 1000,
            })
            uni.redirectTo({
              url: '../apply/campDetail'
            })
          }
					else {
						uni.showToast({
							title: '请检查信息是否填写完整！',
							duration: 1000,
						})
					}
        })
      request
        .get('signupCamp',{
			    user_id: vm.userId,
			    camp_id: vm.id,
          class_id: vm.classes,
        })
        .then(res => {
          if(res.data.statuscode === '200') {  
            uni.showToast({
              title: '报名成功',
              duration: 1000
            })
          }
        })
    }
  },
  onLoad(options) {
    uni.getStorage({
      key: 'GetId',
      success: res => {
        this.userId = res.data
      }
    }),
    uni.getStorage({
      key: 'CampId',
      success: res => {
        this.id = res.data
				request
					.post('queryCampClass/', {
						camp_id: this.id,
					})
					.then(res => {
						this.campClasses = res.data
					})
      }
    })
  },
}
</script>

<style>
   .input-column-top,.input-column {
    display: flex;
    flex-direction: column;
    position: relative;
    border: 1px;
    border-color: black;
    padding: 5px;
    font-size: 18px;
    background-color: #ffffff;
    margin: 10px;
  }
  
  .input-column-top {
    margin-top: 10px;
  }
  
  .input-column-title {
    font-weight: bold;
    margin: 5px;
    font-size: 16px;
  }
  
  .promise,.input-huge-title {
    font-weight: bold;
    padding-left: 10px;
    margin: 5px;
    font-size: 18px;
  }
  
  .promise {
    text-indent: 2em;
  }
  
  .input-column-box {
    width: 90%;
    line-height: 30px;
    border: 1px solid grey;
    height: 30px;
    padding: 0 5px;
    margin: 5px auto;
  }
  
  .highlight {
    color: red;
  }
  
  .save-btn {
    width: 200px;
    margin: 4% auto;
    margin-bottom: 20px;
    height: 40px;
    line-height: 40px;
    background-color: #0FAEFF;
    color: white;
  }
   
  .self-info {
    background-color: #FFFFFF;
    width: 100%;
    margin: 10px auto;
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.3);
  }
  
  .gender-group {
    display: flex;
    flex-direction: row;
    position: relative;
    margin-left: 10px;
    font-size: 16px;
  }
  
  .class-group {
    display: flex;
    flex-direction: column;
    position: relative;
    padding: 10px;
    margin-left: 10px;
    font-size: 16px;
  }
  
  .explanation {
    padding-left: 10px;
    margin: 5px 0 10px;
    font-size: 14px;
    color: #808080;
  }
  
  .long-text {
    width: 90%;
    height: 90px;
    line-height: 30px;
    font-size: 16px;
    padding: 5px;
    margin: 0 auto;
    border: 1px solid grey;
  }
  
  radio-group radio{
    margin-bottom: 5px;
  }
</style>

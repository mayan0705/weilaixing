<template>
  <view class="content">
    <view class="input-row-top">
      <text class="input-row-title">手机号</text>
      <input class="input-row-box-for-others" type="text" v-model="telephone" placeholder="请输入您的手机号" />
    </view>
    <view class="input-row">
      <text class="input-row-title">验证码</text>
      <input class="input-row-box-for-vertification" type="text" v-model="authcode" placeholder="请输入验证码" />
      <button class="vertification-btn" @tap="sendAuthcode">获取验证码</button>
    </view>
    <button v-show="showCheckBtn" class="check-btn" @tap="checkAuthcode">验证</button>
    <view v-show="showMoreInfo">
      <view class="input-row">
        <text class="input-row-short-title">姓名</text>
        <input class="input-row-box-for-others" type="text" v-model="name" placeholder="请输入您的姓名" />
      </view>
      <view class="input-row">
        <text class="input-row-short-title">性别</text>
        <radio-group class="radio-group">
          <radio value="m" @click="genderChange" data-gender="m">男</radio>
          <radio value="f" @click="genderChange" data-gender="f">女</radio>
        </radio-group>
      </view>
      <view class="input-row">
        <text class="input-row-short-title">邮箱</text>
        <input class="input-row-box-for-others" type="text" v-model="email"
        placeholder="请输入您的邮箱" @blur="checkEmail()"/>
        <view class="alertion" v-show="showAlert">邮箱不合法</view>
      </view>
      <view class="input-row">
        <text class="input-row-title">微信号</text>
        <input class="input-row-box-for-others" type="text" v-model="wechat" placeholder="请输入您的微信号" />
      </view>
      <view>
        <button class="register-btn" @tap="showRegister">注册</button>
      </view>
    </view>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data() {
    return {
      name: '',
      gender: '',
      telephone: '',
      correctAuthcode: '',
      authcode: '',
      email: '',
      wechat: '',
      showMoreInfo: false,
      showCheckBtn: true,
      showAlert: false,
    }
  },
  methods: {
    sendAuthcode() {
      const vm = this;
      request
        .get('weixinRegister/', {
          user_telephone: vm.telephone,
        })
        .then(res => {
          if(res.data.auth_code === '000000') {
            uni.showToast({
              title: '号码已被注册！',
              duration: 1000,
            })
          }
          else if(res.data.statuscode === '400') {
            uni.showToast({
              title: '发送失败！',
              duration: 1000,
            })
          }
          else{
            vm.correctAuthcode = res.data.auth_code;
            uni.showToast({
              title: '发送成功',
              duration: 1000,
            })
          }
        })
    },
    checkAuthcode() {
      const vm = this;
      if(vm.authcode === vm.correctAuthcode) {
        vm.showMoreInfo = true;
        vm.showCheckBtn = false;
        request
          .get('weixinAddUser/', {
            user_telephone: vm.telephone,
          })
          .then(res => {
          })
      }
      else {
        uni.showToast({
          title: '验证码错误！',
          duration: 1000,
        })
      }
    },
    genderChange(e) {
      this.gender = e.currentTarget.dataset.gender
    },
    showRegister() {
      const vm = this;
      request
        .get('initializeData/', {
          user_telephone: vm.telephone,
          user_name: vm.name,
          user_weixinnumber: vm.wechat,
          user_gender: vm.gender,
          user_email: vm.email,
        })
        .then(res => {
          if(res.data.statuscode === '400') {
            uni.showToast({
              title: '注册失败！',
              duration: 1000,
            })
          }
          else{
            uni.showToast({
              title: '注册成功！',
              duration: 1000,
            });
            uni.navigateTo({
              url: '../user/user'
            });
          }
        })
    },
    checkEmail() {
      const mail = this.email
      const reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
      if(reg.test(mail) === true) {
        this.showAlert = false
      }
      else this.showAlert = true
    }
  },
};
</script>
>
<style>
  .moreInfo {
    display: none;
  }
  .register-btn {
    width: 50%;
    margin: 2% auto;
    height: 40px;
    line-height: 40px;
    background-color: #0faeff;
    color: white;
  }
  .vertification-btn {
    width: 105px;
    margin: auto auto;
    font-size: 15px;
    background-color: #efeff4;
    color: black;
    height: 30px;
    line-height: 30px;
  }
  .input-row-box-for-vertification {
    width: 110px;
    line-height: 30px;
    border: 1px;
    height: 30px;
  }
  .check-btn {
    width: 50%;
    margin: 2% auto;
    height: 40px;
    line-height: 40px;
    background-color: #0faeff;
    color: white;
  }
  .alertion {
    color: red;
    font-size: 14px;
    padding-right: 5px;
    float: right;
    
   }
   .input-row-top {
     margin-top: 10%;
   }
</style>

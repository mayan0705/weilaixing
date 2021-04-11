<template>
  <view class="content">
    <view class="photo">
      <img class="photo" src="/static/img/EdStarsLogo.png" />
    </view>
    <view class="input-group">
      <view class="input-row">
        <text class="input-row-title">手机号</text>
        <input class="input-row-box-for-others" type="text" v-model="telephone" placeholder="请输入您的手机号" />
      </view>
      <view class="input-row">
        <text class="input-row-title">验证码</text>
        <input class="input-row-box-for-vertification" type="text" v-model="authcode" placeholder="请输入验证码" />
        <button class="vertification-btn" @tap="sendAuthcode">获取验证码</button>
      </view>
    </view>
    <view>
      <button class="login-btn" @tap="checkAuthcode">登录</button>
    </view>
    <view class="to-register">
      <navigator url="../register/register">注册新用户</navigator>
    </view>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data() {
    return {
      id: '100',
      telephone: '',
      correctAuthcode: '1234567890',
      authcode: '',
    }
  },
  methods: {
    checkAuthcode() {
      const vm = this;
      request
        .get('getId/', {
          user_telephone: vm.telephone,
        })
        .then(res => {
          vm.id = res.data.user_id;
          if(vm.authcode === vm.correctAuthcode) {
            uni.setStorage({
              key: 'GetId',
              data: vm.id
            });
            uni.reLaunch({
              url: '../user/user'
            });
          }
          else {
            uni.showToast({
              title: '验证码错误！',
              duration: 1000,
            })
          }
        })
    },
    sendAuthcode() {
      const vm = this;
      request
        .get('weixinLogin/', {
          user_telephone: vm.telephone,
        })
        .then(res => {
          if(res.data.auth_code === '000000') {
            uni.showToast({
              title: '请先注册新用户！',
              duration: 1000,
            })
          }
          else if(res.data.statuscode === '400') {
            uni.showToast({
              title: '发送失败！',
              duration: 1000,
            })
          }
          else {
            uni.showToast({
              title: res.data.auth_code,
              duration: 1000,
            })
            vm.correctAuthcode = res.data.auth_code;
          }
        })
    }
  }
};
</script>
>

<style>
  .login-btn {
    width: 50%;
    margin: 2% auto;
    height: 40px;
    line-height: 40px;
    background-color: #0faeff;
    color: white;
  }

  .to-register {
    border: 0;
    border-color: rgba(0, 0, 0, 0);
    background-color: rgba(0, 0, 0, 0);
    font-size: 15px;
    margin: 2% auto;
    color: #0faeff;
  }

  .weixinLogo {
    height: 40px;
    width: 40px;
  }

  .vertification-btn {
    width: 105px;
    margin: 0 5px 0 50px;
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
</style>

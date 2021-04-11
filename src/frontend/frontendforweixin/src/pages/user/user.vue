<template>
  <view class="content">
    <view class="welcome">
      <view>
        <img class="photo" src="/static/img/EdStarsLogo.png" />
      </view>
      <view class="welcome-title">欢迎您！{{name}}</view>
    </view>
    <view class="self-info">
      <view class="self-info-title">个人信息</view>
      <ul class="self-intro">
        <li class="self-intro-raw">
          <text class="self-intro-title">姓名</text>
          <text class="self-intro-content">{{name}}</text>
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">性别</text>
          <text class="self-intro-content">{{sex}}</text>
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">微信</text>
          <text class="self-intro-content">{{wechat}}</text>
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">电话</text>
          <text class="self-intro-content">{{telephone}}</text>
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">邮箱</text>
          <text class="self-intro-content">{{email}}</text>
        </li>
      </ul>
      <button class="edit-btn" @tap="toEdit">编辑资料</button>
    </view>
    <view>
      <button class="logout-btn" @tap="toLogin">注销</button>
    </view>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data() {
    return {
      id: '',
      photo: '未填写',
      name: '未填写',
      wechat: '未填写',
      telephone: '未填写',
      birthday: '未填写',
      sex: '未填写',
      email: '未填写',
    }
  },
  mounted() {
    let vm = this;
    request
      .get('schoolmateData/', {
        schoolmate_id: vm.id,
      })
      .then(res => {
        vm.name = res.data[0].user_name
        if (res.data[0].user_gender === 'm') {
          vm.sex = '男'
        } 
        else {
          vm.sex = '女'
        }
        vm.telephone = res.data[0].user_telephone
        vm.email = res.data[0].user_email
        vm.wechat = res.data[0].user_weixinnumber
      })
  },
  methods: {
    toLogin() {
      uni.reLaunch({
        url: '../login/login'
      });
    },
    toEdit() {
      uni.navigateTo({
        url: '../edit/edit'
      });
    }
  },
  onLoad(options) {
    uni.getStorage({
      key: 'GetId',
      success: res => {
        console.log(res);
        let self = this;
        self.id = res.data;
      }
    })
  },
};
</script>

<style>
  .self-info {
    background-color: #FFFFFF;
    width: 95%;
    margin: 0 auto;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.3);
  }

  .self-info-title {
    font-weight: bold;
    text-align: center;
    margin: 10px auto;
    font-size: 20px;
  }

  .self-intro-raw {
    display: flex;
    flex-direction: row;
    position: relative;
    padding: 5px;
    font-size: 18px;
    background-color: rgba(0, 0, 0, 0);
    height: 30px;
    margin: 5px;
    border-bottom: 1px solid grey;
  }

  .self-intro {
    margin: 5px auto;
    width: 300px;
  }

  .self-intro-title {
    text-align: justify;
    width: 80px;
    height: 30px;
    line-height: 30px;;
  }

  .self-intro-content {
    height: 30px;
    line-height: 30px;
    text-align: right;
  }

  .welcome {
    display: flex;
    flex-direction: column;
    position: relative;
    margin: 0 auto 20px;
    width: 100%;
    background-image: url('/static/img/IntroBackground.png')
  }

  .welcome-title {
    font-size: 16px;
    height: 40x;
    line-height: 40px;
    margin: 5px auto;
    color: #F8F8F8;
  }

  .logout-btn {
    width: 50%;
    margin: 5% auto;
    height: 40px;
    line-height: 40px;
    background-color: #0faeff;
    color: white;
  }

  .edit-btn {
    width: 200px;
    margin: 4% auto;
    margin-bottom: 20px;
    height: 40px;
    line-height: 40px;
    background-color: #EFEFF4;
    color: gray;
  }
  .photo {
    display: flex;
    height: 100px;
    width: 100px;
    border-radius: 50px;
    margin: 10% auto 0;
  }
</style>

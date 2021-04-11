<template>
  <view class="content">
    <view class="self-info">
      <view class="self-info-title">{{name}}的个人信息</view>
      <img class="photo" src="/static/img/EdStarsLogo.png" />
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
    </view>
    </view>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data() {
    return {
      userId: 0,
      id: 0,
      photo: '未填写',
      name: '未填写',
      wechat: '未填写',
      telephone: '未填写',
      birthday: '未填写',
      sex: '未填写',
      email: '未填写'
    }
  },
  methods: {
    onLoad(options) {
      uni.getStorage({
        key: 'StudentInfo',
        success: res => {
          this.id = res.data
        }
      });
      uni.getStorage({
        key: 'GetId',
        success: res => {
          let self = this;
          self.userId = res.data;
        }
      })
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
        vm.city = res.data[0].user_city
      })
  }
};
</script>

<style>
  .self-info {
    background-color: #FFFFFF;
    width: 95%;
    margin: 30px auto;
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
    border-bottom: 1px solid black;
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

  .photo {
    display: flex;
    height: 120px;
    width: 120px;
    border-radius: 60px;
    margin: 10% auto 10%;
  }
</style>

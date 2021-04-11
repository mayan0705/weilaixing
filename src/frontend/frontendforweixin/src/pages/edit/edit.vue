<template>
  <view class="content">
    <view class="self-info">
      <ul class="self-intro">
        <li class="photo-row" @tap="setPhoto">
          <text class="photo-title">头像</text>
          <img class="photo-top" src="/static/img/EdStarsLogo.png" />
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">姓名</text>
          <input type="text" class="self-intro-content" v-model="name" />
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">性别</text>
          <radio-group class="gender-group">
            <radio value="m" @click="genderChange" data-gender="m">男</radio>
            <radio value="f" @click="genderChange" data-gender="f">女</radio>
          </radio-group>
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">微信</text>
          <input type="text" class="self-intro-content" v-model="wechat" />
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">电话</text>
          <input type="text" class="self-intro-content" v-model="telephone" />
        </li>
        <li class="self-intro-raw">
          <text class="self-intro-title">邮箱</text>
          <input type="text" class="self-intro-content" v-model="email" />
        </li>
      </ul>
      <button class="save-btn" @tap="saveMessage">保存</button>
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
      gender: '',
      email: '未填写',
    }
  },
  mounted() {
    const vm = this
    request
      .get('schoolmateData/', {
        schoolmate_id: vm.id,
      })
      .then(res => {
        vm.name = res.data[0].user_name
        vm.gender = res.data[0].user_gender
        vm.telephone = res.data[0].user_telephone
        vm.email = res.data[0].user_email
        vm.wechat = res.data[0].user_weixinnumber
      })
  },
  onLoad(options) {
    uni.getStorage({
      key: 'GetId',
      success: res => {
        this.id = res.data
      }
    })
  },
  methods: {
    genderChange(e) {
      const vm = this
      vm.gender = e.currentTarget.dataset.gender
    },
    saveMessage() {
      const vm = this
      request
        .get('alterUserData/', {
          user_id: vm.id,
          user_name: vm.name,
          user_gender:vm.gender,
          user_weixinnumber: vm.wechat,
          user_email: vm.email,
        })
        .then(res => {
          if(res.data.statuscode === '400') {
            uni.showToast({
              title: '编辑失败',
              duration: 1000,
            })
          }
          else if(res.data.statuscode === '200') {
            uni.showToast({
              title: '编辑成功！',
              duration: 1000,
            })
            uni.reLaunch({
              url: '../user/user'
            })
          }
        })
    }
  },
}
</script>

<style>
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
    width: 90%;
    margin: 10px auto;
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.3);
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
    border-bottom: 1px solid #999999;
  }
  
  .self-intro {
    margin: 5px auto;
    padding-bottom: 20px;
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
  .photo-top {
    width: 80px;
    height: 80px;
    margin-left: 45px;
    border-radius: 40px;
    margin-bottom: 5px;
    border: 1px solid #EFEFF4;
  }
  .photo-title {
      text-align: justify;
      width: 150px;
      height: 80px;
      line-height: 80px;;
  }
  .photo-row {
    display: flex;
    flex-direction: row;
    position: relative;
    padding: 5px;
    font-size: 18px;
    background-color: rgba(0, 0, 0, 0);
    height: 80px;
    margin: 5px;
    border-bottom: 1px solid #999999;
   } 
   
  .gender-group {
    display: flex;
    flex-direction: row;
    position: relative;
    margin-left: 135px;
    font-size: 18px;
  }
</style>

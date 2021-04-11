<template>
  <view class="content">
    <img class="camp-logo" src="/static/img/camp.png" />
    <view class="camp-content">
      <view class="title">关于{{name}}</view>
      <view class="main-content">
        {{introduce}}
      </view>
	  </view>
      <view class="title">招生及报名</view>
      <text class="text-highlight">招生对象：</text>
      {{peopleOriented}}
      <br />
	  <view class="text-highlight">
	  		开始时间：{{startTime}}
	  </view>
	  <br />
	  <view class="text-highlight">
	  		结束时间：{{endTime}}
	  </view>
	  <br />
      <text class="text-highlight">申请介绍：</text>
      {{signinTips}}
      <br />
      <text class="text-highlight">
	  首轮报名开始时间：{{signinStartTime}}
	  </text>
	  <br />
	  <text class="text-highlight">
	  首轮报名截止时间：{{signinEndTime}}</text>
    <button class='apply-btn' v-if='!ifSignup&&status==="进行中"' @tap='toApply'>点击报名</button>
    <button class='hasapplied-btn' v-if='ifSignup&&status==="进行中"'>您已报名</button>
    <button class='refuse-btn' v-if='status==="已结束"'>报名已截止</button>
    <button class='refuse-btn' v-if='status==="未开始"'>报名未开始</button>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data()
  {
    return {
      userId: 0,
      id: 0,
      name: '',
      startTime: '',
      endTime: '',
      introduce: '',
      peopleOriented: '',
      signinTips: '',
      signinStartTime: '',
      signinEndTime: '',
      ifSignup: '',
      status: '',
    }
  },
  onLoad(options) {
    uni.getStorage({
      key: 'CampId',
      success: res => {
        let self = this
        self.id = res.data
      }
    });
    uni.getStorage({
      key: 'GetId',
      success: res => {
        let self = this;
        self.userId = res.data;
      }
    })
  },
  mounted() {
    const vm = this
    let time = []
    request
      .post('specificCampMsg/', {
        id: vm.id,
      })
      .then(res => {
        vm.name = res.data[0].name
        time = (res.data[0].time).split(',')
        vm.startTime = time[0]
        vm.endTime = time[1]
        vm.introduce = res.data[0].introduce
        vm.peopleOriented = res.data[0].people_oriented
        vm.signinTips = res.data[0].signin_tips
        vm.signinStartTime = (res.data[0].signin_deadline).split(',')[0]
        vm.signinEndTime = (res.data[0].signin_deadline).split(',')[1]
        let now = new Date()
        if(now<new Date(Date.parse(vm.signinStartTime)))
        {
          vm.status = "未开始"
        }
        else if (now>=new Date(Date.parse(vm.signinEndTime)))
        {
          vm.status = "已结束"
        }
        else {
          vm.status = "进行中"
        }
      })
    request
      .get('ifSignupCamp', {
        user_id: vm.userId,
        camp_id: vm.id,
      })
      .then(res => {
        vm.ifSignup = (res.data.statuscode === '200')
      })
  },
  methods: {
    toApply() {
      uni.navigateTo({
        url: '../apply/applyTable'
      })
    },
    ifGone(time) {
      var tempTime = new Date(Date.parse(time))
      if(new Date() < tempTime) {
        return false
      } else {
        return true
      }
    }
  }
};
</script>


<style>
  .camp-logo {
    width: 100%;
    height: 156px;
  }

  .camp-content {
    width: 90%;
    background-color: white;
    padding: 20px;
  }

  .text-highlight {
    color: rgb(50, 64, 161);
  }

  .title {
    font-weight: bold;
    font-size: 20px;
    color: rgb(50, 64, 161);
    margin: 5px 0;
  }

  .main-content {
    text-indent: 2em;
  }
</style>
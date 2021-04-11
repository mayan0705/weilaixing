<template>
  <view class="content">
	  <img class="camp-logo" src="/static/img/camp.png" />
	  <view class="course-title">未开始报名创新院</view>
	  <view>
	    <ul>
		<li v-for="camp in camps" :key="camp.id" v-if="!ifStarted(camp.signin_deadline)">
	      <view class="camps-raw">
	        <img class="photo" src="/static/img/EdStarsLogo.png" />
	        <view class="camps-title" @tap="toCamp(camp.id)">{{camp.name}}</view>
		  </view>
		  <img class="logo" src="/static/img/notstarted.png" />
		  </li>
	    </ul>
	  </view>
    <view class="course-title">正在报名中创新院</view>
    <view>
      <ul>
		<li v-for="camp in camps" :key="camp.id" v-if="ifStarted(camp.signin_deadline) && !ifGone(camp.signin_deadline)">
        <view class="camps-raw">
          <img class="photo" src="/static/img/EdStarsLogo.png" />
          <view class="camps-title" @tap="toCamp(camp.id)">{{camp.name}}</view>
        </view>
        <img class="logo" src="/static/img/underway.png" />
        </li>
      </ul>
    </view>
    <view class="course-title">报名已结束创新院</view>
    <view class="course-content">
      <ul>
		<li v-for="camp in camps" :key="camp.id" v-if="ifStarted(camp.time)">
        <view class="camps-raw">
          <img class="photo" src="/static/img/EdStarsLogo.png" />
          <view class="camps-title" @tap="toCamp(camp.id)">{{camp.name}}</view>
        </view>
        <img class="logo" src="/static/img/closed.png" />
        </li>
      </ul>
    </view>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data() {
    return {
      userId: 0,
      camps: [],
    }
  },
  onLoad(options) {
    this.id = options.id
    uni.getStorage({
      key: 'GetId',
      success: res => {
      }
    })
  },
  methods: {
    toCamp(a) {
      uni.setStorage({
        key: 'CampId',
        data: a,
      })
      uni.navigateTo({
        url: '../apply/campDetail'
      })
    },

    ifStarted(time) {
      var startEnd = time.split(',')
      var starttime = new Date(Date.parse(startEnd[0]))
      if(new Date() < starttime) {
        return false
      } else {
        return true
      }
    },
    ifGone(time) {
      var startEnd = time.split(',')
      var endtime = new Date(Date.parse(startEnd[1]))
      if(new Date()<endtime) {
        return false
      } else {
        return true
      }
    }
  },
  mounted() {
    const vm = this
    request
      .get('Camp/', {
        
      })
      .then(res => {
        vm.camps = res.data
      })
  },
};
</script>

<style>
  .course-title {
    font-weight: bold;
    font-size: 14px;
    text-align: left;
    padding-left: 5px;
    margin-top: 5px;
  }

  .camps-raw {
    display: flex;
    flex-direction: row;
    position: relative;
    margin: 20px auto;
    border: solid 1px gray;
    border-radius: 3px;
    box-shadow: 1px 2px 4px 0 rgba(0, 0, 0, 0.3);
    background-color: white;
  }
  
  .camps-title {
    height: 80px;
    line-height: 80px;
    font-family: '微软雅黑';
    font-size: 18px;
    padding-left: 5px;
    background-color: #fff;
    width: 240px;
    font-weight: bold;
  }

  .photo {
    display: flex;
    width: 120px;
    height: 80px;
    border-radius: 5px;
    margin: 0;
    padding: 0;
  }
  
  .camp-logo {
    width: 100%;
    height: 156px;
  }
  
  .logo {
    position: absolute;
    height: 80px;
    width: 90px;
    margin: -100px 0 0 65%;
    z-index: 300;
  }
</style>

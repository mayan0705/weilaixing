<template>
  <view class="content">
    <view>
      <view class="schoolmates-title">校友资料库</view>
      <button class="dataBank-btn" @tap="toDataBank">
        <img class="smallLogo" src="/static/img/dataBank.png" />
        <text>校友资料库</text>
      </button>
    </view>
    <view>
      <view class="schoolmates-title">校友活动</view>
      <ul>
        <li class="event" v-for="event in events" :key="event.id" @tap="toEvent(event.id)">
          <view class="event-content">{{event.activity_name}}</view>
          <view v-show="!ifPassed(event.activity_time)" class="operable">
            <img class="logo" src="/static/img/underway.png" />
          </view>
          <view v-show="ifPassed(event.activity_time)" class="operable">
            <img class="logo" src="/static/img/closed.png" />
          </view>
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
      id: 0,
      events: [],
    };
  },
  mounted() {
    const vm = this
    request
      .get('Activity/', {
		
      })
      .then(res => {
        vm.events = res.data
      })
  },
  onLoad(options) {
    uni.getStorage({
      key: 'GetId',
      success: res => {
        let self = this;
        self.userId = res.data;
      }
    })
  },
  methods: {
    toEvent(a) {
      uni.setStorage({
        key: 'ActivityId',
        data: a
      })
      uni.navigateTo({
        url: '../schoolmates/event'
      });
    },
    toDataBank() {
      uni.navigateTo({
        url: '../schoolmates/dataBank'
      });
    },
    ifPassed(time) {
      const vm = this
	  let endTime = new Date(Date.parse(time.split(',')[1]))
	  let now = new Date()
	  if(endTime<now)
	  {
		  return true
	  } else {
		  return false
	  }
    },
  },
};
</script>

<style>
  ul {
    list-style: none;
    padding: 0;
  }

  .schoolmates-title {
    font-weight: bold;
    font-size: 14px;
    text-align: left;
    padding-left: 5px;
    margin-top: 30px;
  }

  .dataBank-btn {
    display: flex;
    flex: 1;
    flex-direction: row;
    width: 90%;
    border-radius: 10px;
    height: 75px;
    line-height: 75px;
    font-size: 24px;
    background-color: #fff;
    margin: 10px auto;
    box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.3);
  }

  .smallLogo {
    width: 50px;
    height: 50px;
    margin: 12.5px;
    padding-right: 20px;
  }

  .event {
    display: flex;
    flex: 1;
    flex-direction: row;
    width: 100%;
    height: 80px;
    margin-top: 15px;
    background-color: #fff;
    box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.3);
  }

  .event-content {
    padding-left: 30px;
    font-size: 20px;
    height: 40px;
    line-height: 40px;
    text-align: left;
    margin: auto 0;
    width: 60%;
    border: 1 solid grey;
  }

  .operable {
    background-color: (0,0,0,0);
  }
  .logo {
    width: 88px;
    height: 77px; 
  }
</style>
<template>
  <view class="content">
    <view class="concrete-content">
      <ul class="content-list">
        <li class="content-raw">
          <text class="title">{{name}}：</text>
          <text class="contents">{{status}}</text>
        </li>
		<li class="content-raw">
		  <text class="title">活动介绍：</text>
		  <text class="contents">{{abstract}}</text>
		</li>
        <li class="content-raw">
          <text class="title">报名情况：</text>
          <text class="contents">{{number}}人/{{peopleneed}}人</text>
        </li>
        <li>
          <progress
            class="progress"
            stroke-width="20px"
            :percent="number/peopleneed*100"
            activeColor="#4CD964"
            active-mode="backwards"/>
        </li>
      </ul>
    </view>
   <button class="apply-btn" v-if="((status === '未开始' || status === '进行中') && !ifFull() && !ifSignup)" @tap="apply">
     我要报名
   </button>
   <button class="refuse-btn" v-if="((status === '已结束') || ifFull())">报名已截止！</button>
   <button class="hasapplied-btn" v-if="((status === '未开始' || status === '进行中') && ifSignup)">已报名</button>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  onLoad(options) {
	  uni.getStorage({
	    key: 'ActivityId',
	    success: res => {
	      let self = this
	      self.id = res.data
	    }
	  })
    uni.getStorage({
      key: 'GetId',
      success: res => {
        let self = this;
        self.userId = res.data;
      }
    })
  },
  data() {
    return { 
      id: '',
      userId: '',
      number: '0',
      name: '',
      startTime: '',
      endTime: '',
      location: '',
      abstract: '',
      peopleneed: '',
      tips: '',
      status: '',
      items: '',
      ifSignup: '',
    };
  },
  methods: {
    apply() {
      const vm = this
      request
        .get('attendActivity/', {
          attender_id: vm.userId,
          activity_id: vm.id
        })
        .then(res => {
          if(res.data.statuscode === "200") {
            uni.showToast({
              title: "报名成功！",
              duration: 1000
            });
          }
        })
    },
    ifFull() {
      const vm = this
      if(vm.number < vm.peopleneed)
      {
        return false
      } else {
        return true
      }
    }
  },
  mounted() {
	  const vm = this
	  let time = []
    request
      .post('specificActivityMsg/', {
        id: vm.id,
      })
      .then(res => {
        vm.number = res.data[1]
        vm.name = res.data[0].activity_name
        time = (res.data[0].activity_time).split(',')
        vm.startTime = time[0]
        vm.endTime = time[1]
        let start = new Date(Date.parse(vm.startTime))
        let end = new Date(Date.parse(vm.endTime))
        let now = new Date()
        if(now < start) {
          vm.status = '未开始'
        } else if(now >= start && now <= end) {
          vm.status = '进行中'
        } else {
          vm.status = '已结束'
        }
        vm.location = res.data[0].activity_location
        vm.abstract = res.data[0].activity_abstract
        vm.peopleneed = res.data[0].activity_peopleneed
        vm.tips = res.data[0].activity_tips
        vm.items = res.data[0].activity_items
      })
    request
      .get("ifinActivity/", {
        attender_id: vm.userId,
        activity_id: vm.id
      })
      .then(res => {
        vm.ifSignup = res.data.statuscode === "200";
      });
  },
};
</script>

<style>
  .apply-btn,
  .refuse-btn {
    width: 50%;
    margin: 2% auto;
    height: 40px;
    line-height: 40px;
    color: white;
  }

  .apply-btn {
    margin-top: 50px;
    background-color: lightgreen;
  }

  .refuse-btn {
    background-color: lightgray;
  }

  .concrete-content {
    background-color: #FFFFFF;
    width: 95%;
    margin: 30px auto;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.3);
  }

  .content-raw {
    display: flex;
    flex-direction: row;
    position: relative;
    border: 1px;
    border-color: black;
    padding: 5px;
    font-size: 18px;
    background-color: rgba(0, 0, 0, 0);
    height: 30px;
    margin: 5px;
    border-bottom: 1px solid grey;
  }

  .content-list {
    margin: 5px auto;
  }

  .contents {
    height: 30px;
    line-height: 30px;
    float: left;
    margin-left: 30px;
  }
  
  .progress {
    border-radius: 10px;
    width: 80%;
    margin: 20px auto;
  }
</style>

<template>
  <view class="content">
    <img class="class-logo" src="/static/img/class.png" />
    <view class="course-title">本期创新院</view>
    <view>
      <ul>
    	<li class="camps-raw" v-for="camp in camps" :key="camp.id" v-if="ifStarted(camp.signin_deadline) && !ifGone(camp.signin_deadline)">
          <img class="photo" src="/static/img/EdStarsLogo.png" />
          <view class="camps-title" @tap="toCourse(camp.id)">{{camp.name}}</view>
        </li>
      </ul>
    </view>
    <view class="course-title">往期创新院</view>
    <view class="course-content">
		<ul>
    	<li class="camps-raw" v-for="camp in camps" :key="camp.id" v-if="ifStarted(camp.time)">
          <img class="photo" src="/static/img/EdStarsLogo.png" />
          <view class="camps-title" @tap="toCourse(camp.id)">{{camp.name}}</view>
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
      allCamps: [],
      campAttends: []
    }
  },
  methods: {
    ifStarted(time) {
      var startEnd = time.split(',')
      var starttime = new Date(Date.parse(startEnd[0]))
      if(new Date()<starttime) {
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
    },
    toCourse(a) {
      uni.setStorage({
        key: 'CampId',
        data: a
      });
	     uni.navigateTo({
	       url: '../course/someCourse'
	     });
	   }
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
  mounted() {
    const vm = this
    request
      .get('Campattendup/', {
    	
      })
      .then(res => {
        vm.campAttends = res.data
      })
    request
	    .get('Camp/', {
			
      })
      .then(res => {
	      vm.allCamps = res.data
        let index = 0
        for (let i = 0; i < vm.allCamps.length; i++) {
          if(vm.allCamps[i].permission === 3) {
            vm.camps[index] = vm.allCamps[i]
            index += 1
          } else if (vm.allCamps[i].permission === 2) {
            for(let j = 0; j < vm.campAttends.length; j++) {
              if(vm.campAttends[j].user_id === vm.userId) {
                vm.camps[index] = vm.allCamps[i]
                index += 1
                break
              }
            }
          } else if (vm.allCamps[i].permission === 1) {
            for(let j = 0; j < vm.campAttends.length; j++) {
              if(vm.campAttends[j].user_id === vm.userId && 
                vm.campAttends[j].camp_id === vm.allCamps[i].id) {
                vm.camps[index] = vm.allCamps[i]
                index += 1
                break
              }
            }
          }
        }
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
    margin: 5px 0;
    background-color: rgba(0,0,0,0);
  }

  .camps-title {
    height: 80px;
    line-height: 80px;
    font-family: '微软雅黑';
    font-size: 18px;
    padding-left: 5px;
    width: 240px;
    background-color: white;
  }

  .camps-raw {
    display: flex;
    flex-direction: row;
    position: relative;
    margin: 10px auto;
    border: solid 1px gray;
    background-color: white;
    border-radius: 3px;
    box-shadow: 1px 2px 4px 0 rgba(0, 0, 0, 0.3);
  }

  .course-title {
    font-weight: bold;
    font-size: 14px;
    text-align: left;
    padding-left: 5px;
    margin-top: 5px;
  }

  .photo {
    display: flex;
    width: 120px;
    height: 80px;
    border-radius: 5px;
    margin: 0;
    padding: 0;
  }
  .class-logo {
    width: 100%;
  }
</style>

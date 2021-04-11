<template>
  <view class="content">
    <view>
      <img class="course-top" src="/static/img/classroom.png" />
	  <view class="title">关于{{name}}</view>
	  <view class="main-content">
	    {{introduce}}
	  </view>
    </view>
    <view class="course-body">
      <view class="course-title">{{name}}课程列表</view>
      <ul class="course-column">
        <li v-for="course in courses" :key="course.id">
          <view class="vice-title">
            <text>{{course.name}}</text>
            <view class="arrow" v-show="!showMoreInfo[course.id]" @tap="showMore(course.id)"> 
              <img class="smallLogo" src="/static/img/downarrow.png" />
            </view>
            <view class="arrow" v-show="showMoreInfo[course.id]" @tap="showLess(course.id)">
              <img class="smallLogo" src="/static/img/arrow.png" />
            </view>
          </view>
          <view v-show="showMoreInfo[course.id]">
            <view v-if="ifstarted(course.id)">
              <view class="synopsis">{{course.abstract}}</view>
              <view class="course-text-light">上课时间：{{course.time.split(",")[0]}}至{{course.time.split(",")[1]}}</view>
              <view class="course-text-light">上课地点：{{course.location}}</view>
              <view class="course-detail" @tap="showTeacher(course.id)">
                <img class="smallLogo" src="/static/img/teacher.png" />讲师名片
                <view v-if="ifshowTeacher[course.id]">{{course.teacher}}</view>
              </view>
              <view class="course-detail" @tap="showPPT(course.id)">
                <img class="smallLogo" src="/static/img/PPT.png" />课程课件
              </view>
              <view class="course-detail" @tap="showVideo(course.id)">
                <img class="smallLogo" src="/static/img/video.png" />课程视频
              </view>
							<view class="video"><video v-if="ifshowVideo[course.id]" :src="videofiles[course.id]"></video></view>
              <view class="course-detail" @tap="showNotes(course.id)">
                <img class="smallLogo" src="/static/img/note.png" />学员速记
              </view>
              <view class="course-detail" @tap="showOther(course.id)">
                <img class="smallLogo" src="/static/img/course.png" />其他资料
              </view>
            </view>
            <view v-if="!ifstarted(course.id)">
              <view class="synopsis">该课程暂时没有开启！</view>
            </view>
          </view>
          <br />
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
      id: 0,
      name: [],
      introduce: '',
      courses: '',
      showMoreInfo: [],
      ifshowTeacher: [],
      ifshowVideo: [],
      ifshowPPT: [],
      ifshowNotes: [],
      ifshowOther: [],
      pptfiles: [],
      notesfiles: [],
      videofiles: [],
      otherfiles: [],
      ppt: [],
      notes: [],
      video: [],
      other: [],
    };
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
  methods: {
    showMore(e) {
      this.$set(this.showMoreInfo, e, true)
    },
    showLess(e) {
      this.$set(this.showMoreInfo, e, false)
    },
    ifstarted(id) {
      const vm = this
      let time = new Date()
      for(let course of vm.courses)
      {
        if(course.id === id) {
          time = new Date(Date.parse(course.time.split(',')[0]))
          if(new Date() < time) {
            return false
          } else {
            return true
          }
        }
      }
    },
    showTeacher(id)
    {
			const vm = this
      this.$set(this.ifshowTeacher, id, !vm.ifshowTeacher[id])
    },
    showPPT(id)
    {
			let myurl = 'http://117.50.34.200:8002' + this.pptfiles[id]
      uni.downloadFile({
        url: myurl,
        success: function (res) {
          var filePath = res.tempFilePath;
          uni.openDocument({
            filePath: filePath,
            success: function (res) {
              console.log('打开文档成功');
            }
          });
        }
      });
    },
    showVideo(id)
    {
      const vm = this
      this.$set(this.ifshowVideo, id, !vm.ifshowVideo[id])
    },
    showNotes(id)
    {
      let myurl = 'http://117.50.34.200:8002' + this.notesfiles[id]
      uni.downloadFile({
        url: myurl,
        success: function (res) {
          var filePath = res.tempFilePath;
          uni.openDocument({
            filePath: filePath,
            success: function (res) {
              console.log('打开文档成功');
            }
          });
        }
      });
      
    },
    showOther(id)
    {
      let myurl = 'http://117.50.34.200:8002' + this.otherfiles[id]
      uni.downloadFile({
        url: myurl,
        success: function (res) {
          var filePath = res.tempFilePath;
          uni.openDocument({
            filePath: filePath,
            success: function (res) {
              console.log('打开文档成功');
            }
          });
        }
      });
      
    },
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
  			vm.introduce = res.data[0].introduce
  		})
    request
      .get('courseinCamp/', {
        camp_id: vm.id,
	    })
      .then(res => {
        vm.courses = res.data
				request
				  .get('getFiles/', {
				    courses: this.courses,
				  })
				  .then(res => {
				    let i=0
				    for(i=0;i<res.data.length;i++)
				    {
				      this.$set(vm.showMoreInfo, vm.courses[i].id, false)
				      this.$set(vm.ifshowPPT, vm.courses[i].id, false)
				      this.$set(vm.ifshowTeacher, vm.courses[i].id, false)
				      this.$set(vm.ifshowNotes, vm.courses[i].id, false)
				      this.$set(vm.ifshowVideo, vm.courses[i].id, false)
				      this.$set(vm.ifshowOther, vm.courses[i].id, false)
							this.$set(vm.pptfiles, vm.courses[i].id, res.data[i].ppt)
							this.$set(vm.ppt, vm.courses[i].id, res.data[i].ppt_name)
							this.$set(vm.videofiles, vm.courses[i].id, 'http://117.50.34.200:8002'+res.data[i].video)
							this.$set(vm.video, vm.courses[i].id, res.data[i].video_name)
							this.$set(vm.notesfiles, vm.courses[i].id, res.data[i].text)
							this.$set(vm.notes, vm.courses[i].id, res.data[i].text_name)
							this.$set(vm.otherfiles, vm.courses[i].id, res.data[i].others)
							this.$set(vm.other, vm.courses[i].id, res.data[i].others_name)
							console.log(vm.pptfiles)
				    }
				  });
      })

  },
  created () {
	  const vm = this
    for(let course of vm.courses)
	  {
		  this.$set(this.showMoreInfo, course.id, false)
		  this.$set(this.showPPT, course.id, false)
		  this.$set(this.showTeacher, course.id, false)
      this.$set(this.showNotes, course.id, false)
		  this.$set(this.showVideo, course.id, false)
		  this.$set(this.showOther, course.id, false)
	  }
  }
};
</script>

<style>
  ul {
    list-style: none;
    width: 100%;
  }

  .course-column {
    display: flex;
    flex: 1;
    flex-direction: column;
  }

  .course-top {
    margin: 0 auto;
    width: 100%;
    height: 200px;
    border-radius: 5px;
  }

  .course-title {
    font-weight: bold;
    font-size: 22px;
    text-align: left;
    padding-left: 10px;
    margin: 20px 0;
    background-color: rgba(0,0,0,0);
  }

  .vice-title {
    display: flex;
    width: 90%;
    flex: 1;
    flex-direction: row;
    font-size: 20px;
    height: 30px;
    line-height: 30px;
    text-align: left;
    padding-left: 20px;
    margin: 10px auto;
    background-color: rgb(239, 239, 244);
    box-shadow: 0 2px 4px 0 rgba(0,0,0,0.3);
  }

  .synopsis {
    font-size: 16px;
    text-align: left;
    text-indent: 2em;
    padding: 10px 30px 5px;
    border-bottom: 1px solid rgba(0,0,0,0.2);
  }

  .course-detail {
    font-size: 18px;
    background-color: white;
    margin: 20px auto;
    border-bottom: 1px solid rgba(0,0,0,0.2);
    text-align: center;
  }

  .course-text-light {
    font-size: 18px;
    text-align: left;
    padding-left: 20px;
    padding: 10px 30px;
    border-bottom: 1px solid rgba(0,0,0,0.2);
  }

  .smallLogo {
    width: 20px;
    height: 20px;
    margin-right: 10px;
  }
  
  .arrow {
    width: 20px;
    height: 20px;
    margin-left: 60%;
    background-color: rgba(0,0,0,0);
  }
  
  .title {
    font-weight: bold;
    font-size: 20px;
    color: rgb(50, 64, 161);
    margin: 10px 0;
  }
  
	.video{
		position: relative;
		text-align: center;
	}
	
  .main-content {
    text-indent: 2em;
  }
</style>
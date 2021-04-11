<template>
  <div :class="activityStatusName" @click="showActivity">
    <h4>
      {{initActivityName}}
      <p>{{activityStatus}}</p>
    </h4>
    <img :src="activityImage" class="recPicA" />
  </div>
</template>

<script>
export default {
  name: 'Activity',
  data() {
    return {
      activityIndex: 1,
      activityImage: require('../assets/pioneercampimage.png'),
      activityStatusName: ''
    }
  },
  props: {
    activityStatus: {
      Type: String,
      default: 'processing'
    },
    initActivityName: {
      Type: String,
      default: '默认活动'
    },
    activityIndexMsg: {
      Type: Number,
      defaule: 0
    }
  },
  created() {
    this.createActivity()
  },
  methods: {
    createActivity() {
      this.activityIndex = this.activityIndexMsg
      if (this.activityStatus === '未开始') {
        this.activityStatusName = 'waiting'
      } else if (this.activityStatus === '进行中') {
        this.activityStatusName = 'processing'
      } else if (this.activityStatus === '已结束') {
        this.activityStatusName = 'over'
      }
    },
    showActivity() {
      this.$store.commit('setActivityIndex', this.activityIndex)
      this.$router.push({
        name: 'ActivityInfoForm'
      })
    }
  }
}
</script>

<style scoped>
.recPicA {
  position: relative;
  top: 0;
  left: 22%;
  width: 171px;
  height: 100px;
  object-fit: cover;
  transition: transform 0.75s;
}
.processing {
  background-image: url(../assets/processingImage.jpg);
  display: inline-block;
  height: 200px;
  width: 300px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
  cursor: pointer;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
}
.over {
  background-image: url(../assets/endImage.jpg);
  display: inline-block;
  height: 200px;
  width: 300px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
  cursor: pointer;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
}
.waiting {
  background-image: url(../assets/waitingImage.jpg);
  display: inline-block;
  height: 200px;
  width: 300px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
  cursor: pointer;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
}
h4 {
  display: block;
  position: relative;
  left: 10px;
  line-height: 1em;
  width: 180px;
  height: 10%;
  color: white;
  font-size: 20px;
}
p {
  display: inline-block;
  position: relative;
  top: -35px;
  left: 240px;
  line-height: 1em;
  width: 180px;
  color: white;
  font-size: 12px;
}
.el-image {
  position: relative;
  width: 240px;
  height: 120px;
  top: -38px;
  left: 30px;
  border: none;
  background-color: white;
}
</style>

<template>
  <div @click="showCourse" :class="campStatus">
    <h4>{{campName}}</h4>
    <img :src="lessonLabelImage" class="recPicA" />
  </div>
</template>

<script>
export default {
  name: 'LessonLabel',
  props: {
    campStatus: {
      Type: String,
      default: 'processing'
    },
    campName: {
      Type: String,
      default: '默认创新院'
    },
    campIndexMsg: {
      Type: parseInt,
      defaule: 0
    }
  },
  created() {
    if (this.campStatus == 'waiting') {
      this.chineseStatus = '（未开始）'
    } else if (this.campStatus == 'processing') {
      this.chineseStatus = '（进行中）'
    }
  },
  data() {
    return {
      chineseStatus: '',
      lessonLabelImage: require('../assets/courseLogo.png')
    }
  },
  methods: {
    showCourse() {
      this.$store.commit('setCampIndex', this.campIndexMsg)
      this.$router.push({
        name: 'CourseInfoForm'
      })
    }
  }
}
</script>

<style scoped>
.recPicA {
  position: relative;
  top: -15px;
  left: 26.5%;
  width: 151px;
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
  width: 300px;
  color: white;
  font-size: 20px;
}
.el-image {
  position: relative;
  width: 240px;
  height: 120px;
  top: -24px;
  left: -10px;
  border: none;
  background-color: white;
}
</style>

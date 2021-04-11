<template>
  <div :class="backguoundType" @click="showCampForm">
    <h4>{{campName}}</h4>
    <img fit="fill" class="el-image" :src="pioneerCampImage" />
  </div>
</template>

<script>
export default {
  name: 'PioneerCamp',
  data() {
    return {
      pioneerCampImage: require('../assets/detailIcon.png'),
      backguoundType: 'ordinary'
    }
  },
  props: {
    processingSignal: {
      type: String,
      default: 'false'
    },
    pioneerCampIndex: {
      type: Number,
      default: 0
    },
    campName: {
      type: String,
      default: '默认创新院'
    }
  },
  methods: {
    showCampForm() {
      this.$store.commit('setCampIndex', this.pioneerCampIndex)
      this.$router.push({
        name: 'PioneerCampForm'
      })
    }
  },
  created() {
    if (this.campName.length > 12) {
      this.newCampName = this.campName.slice(0, 11) + '...'
    } else if (this.campName.length <= 12) {
      this.newCampName = this.campName
    }
    if (this.processingSignal !== 'false') {
      this.backguoundType = 'processing'
    }
  }
}
</script>

<style scoped>
.ordinary {
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
.processing {
  background-image: url(../assets/canBeManage.png);
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
  width: 240px;
  color: white;
  font-size: 20px;
}
.el-image {
  position: relative;
  top: -17px;
  left: 24.5%;
  width: 162px;
  height: 100px;
  object-fit: cover;
  transition: transform 0.75s;
}
</style>

<template>
  <div>
    <h4>第一期创新院</h4>
    <el-image fit="fill" :src="pioneerCampImage"></el-image>
  </div>
</template>

<script>
export default {
  name: 'ClassForPioneerCamp',
  data() {
    return {
      pioneerCampImage: require('../assets/EdStarsLogo.jpg')
    }
  }
}
</script>

<style scoped>
div {
  background-color: steelblue;
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

<template>
  <el-header :class="status?'thisheader':'transparentheader'">
    <img v-if="isOnLoad" src="../assets/miniBlackLogo.png" class="recPicA1" />
    <img v-if="isOnLoad==false" src="../assets/miniWhiteLogo.png" class="recPicA2" />
    <span class="user-span" v-if="isOnLoad">
      <font color="#F7F7F7" size="4px">欢迎您， {{name}}</font>
    </span>
    <span class="buttonfloat" @mousemove="fun2()" @mouseleave="fun3()">
      <el-button size="small" type="primary" plain v-if="isOnLoad" @click="logout">
        注销
        <i :class="exitIcon"></i>
      </el-button>
    </span>
  </el-header>
</template>

<script>
export default {
  name: 'TitleBar',
  data() {
    return {
      name: '',
      status: false,
      exitIcon: 'el-icon-d-arrow-left el-icon--right'
    }
  },
  props: {
    isOnLoad: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    logout() {
      this.$router.push({
        name: 'Index'
      })
      this.$store.commit('setName', '')
      this.$store.commit('setPwd', '')
      this.$store.commit('setPowerCamp', 'false')
      this.$store.commit('setPowerCourse', 'false')
      this.$store.commit('setPowerActivity', 'false')
      this.$store.commit('setPowerAdministrator', 'false')
    },
    fun2() {
      this.exitIcon = 'el-icon-loading el-icon--right'
    },
    fun3() {
      this.exitIcon = 'el-icon-d-arrow-left el-icon--right'
    }
  },
  created() {
    this.name = localStorage['name']
    this.status = this.isOnLoad
  }
}
</script>

<style scoped>
.thisheader {
  background-color: rgba(179, 192, 209, 1);
  line-height: 60px;
}
.transparentheader {
  background-color: rgba(255, 255, 255, 0.3);
  line-height: 60px;
}
.title-span {
  position: absolute;
  display: inline-block;
  left: 5%;
}
.user-span {
  position: absolute;
  display: inline-block;
  font-size: 14px;
  right: 15%;
}
.el-header a {
  position: absolute;
  display: inline-block;
  right: 5%;
}
.recPicA1 {
  position: absolute;
  display: inline-block;
  top: 1.6%;
  left: 6%;
  width: 292px;
  height: 32px;
  object-fit: cover;
  transition: transform 0.75s;
}
.recPicA2 {
  position: absolute;
  display: inline-block;
  top: 1.6%;
  left: 6%;
  width: 326px;
  height: 32px;
  object-fit: cover;
  transition: transform 0.75s;
}
.buttonfloat {
  position: relative;
  right: 9%;
  float: right;
  top: -2px;
}
</style>

<template>
  <div id="app">
    <router-view />
  </div>
</template> 

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'app',
  data() {
    return {
      newName: '',
      newPwd: '',
      newPowerCamp: '',
      newPowerCourse: '',
      newPowerActivity: '',
      newPowerAdministrator: '',
      name: '',
      pwd: '',
      powerCamp: '',
      powerCourse: '',
      powerActivity: '',
      powerAdministrator: ''
    }
  },
  methods: {
    showAlert() {
      this.$alert('您的账户信息已发生变化，请重新登录！', '提示', {
        confirmButtonText: '确定'
      })
    }
  },
  mounted() {
    this.Timer = setInterval(() => {
      this.name = localStorage['name']
      this.pwd = localStorage['pwd']
      if (this.name !== '') {
        axios({
          url: 'http://117.50.34.200:8002/adminForLogin/',
          method: 'post',
          data: {
            admin_name: this.name,
            admin_password: this.pwd
          },
          transformRequest: [
            function(data) {
              return Qs.stringify(data)
            }
          ]
        }).then(response => {
          if (response.data.code === 'ok') {
            if (
              typeof localStorage['name'] === 'undefined' ||
              localStorage['name'] === ''
            ) {
              this.$store.commit('setName', '')
              this.$store.commit('setPwd', '')
              this.$store.commit('setPowerCamp', 'false')
              this.$store.commit('setPowerCourse', 'false')
              this.$store.commit('setPowerActivity', 'false')
              this.$store.commit('setPowerAdministrator', 'false')
              this.showAlert()
              this.$router.push({
                name: 'Index'
              })
            } else {
              this.powerCamp = localStorage['powerCamp']
              this.powerCourse = localStorage['powerCourse']
              this.powerActivity = localStorage['powerActivity']
              this.powerAdministrator = localStorage['powerAdministrator']
              axios({
                url: 'http://117.50.34.200:8002/specificAdministrator/',
                method: 'post',
                data: {
                  name: this.name
                },
                transformRequest: [
                  function(data) {
                    return Qs.stringify(data)
                  }
                ]
              }).then(response => {
                let power = response.data
                this.newPowerCamp = String(power[0].power_create_camp)
                this.newPowerCourse = String(power[0].power_create_course)
                this.newPowerActivity = String(power[0].power_create_activity)
                this.newPowerAdministrator = String(
                  power[0].power_create_administrator
                )
                if (this.powerCamp !== this.newPowerCamp) {
                  this.$store.commit('setName', '')
                  this.$store.commit('setPwd', '')
                  this.$store.commit('setPowerCamp', 'false')
                  this.$store.commit('setPowerCourse', 'false')
                  this.$store.commit('setPowerActivity', 'false')
                  this.$store.commit('setPowerAdministrator', 'false')
                  this.showAlert()
                  this.$router.push({
                    name: 'Index'
                  })
                } else if (this.powerCourse !== this.newPowerCourse) {
                  this.$store.commit('setName', '')
                  this.$store.commit('setPwd', '')
                  this.$store.commit('setPowerCamp', 'false')
                  this.$store.commit('setPowerCourse', 'false')
                  this.$store.commit('setPowerActivity', 'false')
                  this.$store.commit('setPowerAdministrator', 'false')
                  this.showAlert()
                  this.$router.push({
                    name: 'Index'
                  })
                } else if (this.powerActivity !== this.newPowerActivity) {
                  this.$store.commit('setName', '')
                  this.$store.commit('setPwd', '')
                  this.$store.commit('setPowerCamp', 'false')
                  this.$store.commit('setPowerCourse', 'false')
                  this.$store.commit('setPowerActivity', 'false')
                  this.$store.commit('setPowerAdministrator', 'false')
                  this.showAlert()
                  this.$router.push({
                    name: 'Index'
                  })
                } else if (
                  this.powerAdministrator !== this.newPowerAdministrator
                ) {
                  this.$store.commit('setName', '')
                  this.$store.commit('setPwd', '')
                  this.$store.commit('setPowerCamp', 'false')
                  this.$store.commit('setPowerCourse', 'false')
                  this.$store.commit('setPowerActivity', 'false')
                  this.$store.commit('setPowerAdministrator', 'false')
                  this.showAlert()
                  this.$router.push({
                    name: 'Index'
                  })
                }
              })
            }
          } else if (response.data.code === 'no') {
            this.$store.commit('setName', '')
            this.$store.commit('setPwd', '')
            this.$store.commit('setPowerCamp', 'false')
            this.$store.commit('setPowerCourse', 'false')
            this.$store.commit('setPowerActivity', 'false')
            this.$store.commit('setPowerAdministrator', 'false')
            this.showAlert()
            this.$router.push({
              name: 'Index'
            })
          }
        })
      }
    }, 3000)
  }
}
</script>

<style>
</style>


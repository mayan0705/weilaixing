import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'
import store from './store/store'
import timer from './api/timer'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.Timer = timer

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app')

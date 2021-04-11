<template>
  <div>
    <el-collapse-transition>
      <LoginPage />
    </el-collapse-transition>
  </div>
</template>

<script>
import LoginPage from '@/pages/LoginPage.vue'
export default {
  name: 'Index',
  components: {
    LoginPage
  }
}
</script>

<style scoped type="type/css">
</style>
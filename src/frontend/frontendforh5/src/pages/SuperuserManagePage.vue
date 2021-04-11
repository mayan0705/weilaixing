<template>
  <div class="superusermanagepage">
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <br />
    <h1 class="h1Style">
      <font class="fontStyle" color="grey">您拥有超级管理员身份</font>
    </h1>
    <h2 class="h2Style">
      <font class="fontStyle" color="grey">有权执行下列操作</font>
    </h2>
    <SuperUserManageTable />
  </div>
</template>

<script>
import TitleBar from '@/components/TitleBar.vue'
import NavBar from '@/components/NavBar.vue'
import SuperUserManageTable from '@/components/SuperUserManageTable.vue'
export default {
  name: 'SuperUserManagePage',
  data() {
    return {
      isOnLoad: true,
      specialColor: 5
    }
  },
  components: {
    SuperUserManageTable,
    TitleBar,
    NavBar
  }
}
</script>

<style scoped type="type/css">
.h1Style {
  text-align: center;
  font-weight: normal;
}
.fontStyle {
  font-family: '微软雅黑';
}
.h2Style {
  text-align: center;
  font-weight: normal;
}
</style>
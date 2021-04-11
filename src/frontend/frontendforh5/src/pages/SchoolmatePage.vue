<template>
  <div class="schoolmatepage">
    <title-bar :is-on-load="isOnLoad"></title-bar>
    <nav-bar :special-color="specialColor"></nav-bar>
    <br />
    <SchoolmateTable />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
  </div>
</template>

<script>
import TitleBar from '@/components/TitleBar.vue'
import NavBar from '@/components/NavBar.vue'
import SchoolmateTable from '@/components/SchoolmateTable.vue'
export default {
  name: 'SchoolmatePage',
  data() {
    return {
      isOnLoad: true,
      specialColor: 4
    }
  },
  components: {
    SchoolmateTable,
    TitleBar,
    NavBar
  },
  props: {}
}
</script>

<style scoped type="type/css">
</style>
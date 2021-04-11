<template>
  <div class="searchbox">
    <div class="inputlabel">
      <input type="text" class="StInput" id="searchbox" placeholder="  按 关 键 词 搜 索 校 友" />
      <button class="s_button" onclick="getsearchcontent()">
        <i class="Si" id="Si"></i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SchoolmateSearchBox',
  props: {}
}
</script>

<style scoped>
.StInput {
  width: 400px;
  height: 60px;
  border: 1 none black;
  font-size: 30px;
  background: 100 100;
  position: relative;
  margin: 5% 30% 2%;
}
.inputlabel {
  width: 1140px;
  position: relative;
  margin: auto;
}
.Si {
  position: absolute;
  top: 50%;
  right: 11px;
  margin-top: -8px;
  width: 16px;
  height: 16px;
  background-image: url(../assets/icon.png);
}
#Si {
  background-position: 0 -40px;
}
.s_button {
  position: relative;
  top: 5px;
  right: 390px;
  border: 0 none;
  width: 38px;
  height: 35px;
  overflow: visible;
  background: 0 0;
}
button {
  cursor: pointer;
}
</style>
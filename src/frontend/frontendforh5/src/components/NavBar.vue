<template>
  <div class="nav">
    <el-container>
      <el-header>
        <div class="newDiv">
          <el-menu
            :default-active="String(specialColor)"
            background-color="rgba(255,255,255,0)"
            active-text-color="#738ab9"
            class="menuBack el-menu-demo"
            mode="horizontal"
          >
            <el-menu-item class="width240px" @click="toRegistrationManagePage" index="1">
              <div @mousemove="activity1=1" @mouseleave="activity1=0">
                <el-collapse-transition>
                  <div v-if="activity1==0">
                    报名管理
                    <i class="el-icon-s-claim" />
                  </div>
                </el-collapse-transition>
                <el-collapse-transition>
                  <div v-if="activity1==1">
                    <i class="el-icon-d-arrow-right" /> 报 名 管 理
                    <i class="el-icon-d-arrow-left" />
                  </div>
                </el-collapse-transition>
              </div>
            </el-menu-item>
            <el-menu-item class="width240px" @click="toClassManagePage" index="2">
              <div @mousemove="activity2=1" @mouseleave="activity2=0">
                <el-collapse-transition>
                  <div v-if="activity2==0">
                    课程管理
                    <i class="el-icon-notebook-2" />
                  </div>
                </el-collapse-transition>
                <el-collapse-transition>
                  <div v-if="activity2==1">
                    <i class="el-icon-d-arrow-right" /> 课 程 管 理
                    <i class="el-icon-d-arrow-left" />
                  </div>
                </el-collapse-transition>
              </div>
            </el-menu-item>
            <el-menu-item class="width240px" @click="toActivityManagePage" index="3">
              <div @mousemove="activity3=1" @mouseleave="activity3=0">
                <el-collapse-transition>
                  <div v-if="activity3==0">
                    活动管理
                    <i class="el-icon-fork-spoon" />
                  </div>
                </el-collapse-transition>
                <el-collapse-transition>
                  <div v-if="activity3==1">
                    <i class="el-icon-d-arrow-right" /> 活 动 管 理
                    <i class="el-icon-d-arrow-left" />
                  </div>
                </el-collapse-transition>
              </div>
            </el-menu-item>
            <el-menu-item class="width240px" @click="toSchoolmatePage" index="4">
              <div @mousemove="activity4=1" @mouseleave="activity4=0">
                <el-collapse-transition>
                  <div v-if="activity4==0">
                    校友管理
                    <i class="el-icon-s-custom" />
                  </div>
                </el-collapse-transition>
                <el-collapse-transition>
                  <div v-if="activity4==1">
                    <i class="el-icon-d-arrow-right" /> 校 友 管 理
                    <i class="el-icon-d-arrow-left" />
                  </div>
                </el-collapse-transition>
              </div>
            </el-menu-item>
            <el-menu-item class="width240px" @click="toSuperuserManagePage" index="5">
              <div @mousemove="activity5=1" @mouseleave="activity5=0">
                <el-collapse-transition>
                  <div v-if="activity5==0">
                    管理员权限设置
                    <i class="el-icon-set-up" />
                  </div>
                </el-collapse-transition>
                <el-collapse-transition>
                  <div v-if="activity5==1">
                    <i class="el-icon-d-arrow-right" />管理员权限设置
                    <i class="el-icon-d-arrow-left" />
                  </div>
                </el-collapse-transition>
              </div>
            </el-menu-item>
          </el-menu>
        </div>
      </el-header>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    specialColor: {
      type: Number,
      default: 1
    }
  },
  data() {
    return {
      activity1: 0,
      activity2: 0,
      activity3: 0,
      activity4: 0,
      activity5: 0,
      activeIndex: '1'
    }
  },
  methods: {
    toRegistrationManagePage() {
      this.$router.push({
        name: 'RegistrationManagePage'
      })
    },
    toClassManagePage() {
      this.$router.push({
        name: 'ClassManagePage'
      })
    },
    toSchoolmatePage() {
      this.$router.push({
        name: 'SchoolmatePage'
      })
    },
    toActivityManagePage() {
      this.$router.push({
        name: 'ActivityManagePage'
      })
    },
    toSuperuserManagePage() {
      this.$router.push({
        name: 'SuperuserManagePage'
      })
    }
  }
}
</script>

<style scoped type="type/css">
#normalColor {
  background-color: #e9eef3;
}
#blueColor {
  background-color: #738ab9;
}
.el-header {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.subNavLi {
  line-height: 60px;
  float: left;
  font-size: 40px;
  color: #c1c1c1;
  background-color: #e9eef3;
  margin-left: 24px;
  margin-right: 24px;
  list-style: none;
  cursor: pointer;
}
.subNav {
  height: 60px;
  line-height: 60px;
  position: relative;
  margin: auto;
}
.newDiv {
  position: relative;
  margin: auto;
  width: 1200px;
}
.width240px {
  width: 240px;
  font-size: 22px;
}
.manuBack {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
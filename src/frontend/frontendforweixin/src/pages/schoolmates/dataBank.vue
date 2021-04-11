<template>
  <view class="content">
    <view class="dataBank-top">
      <view class="search-row">
        <input class="input-in-search" type="text" v-model="searchContent" placeholder="搜索校友" />
        <view class="search-btn" @tap="search">
          <img class="search-logo" src="/static/img/search.png" />
        </view>
      </view>
      <view class="select-table">
        <picker @change="classChange" :value="index" :range="array">
          <view class="">按{{array[index]}}</view>
        </picker>
      </view>
    </view>
    <view class="search-title">搜索结果：</view>
    <ul class="schoolmates-column">
      <li v-for="schoolmate in schoolmates" :key="schoolmate.id" @tap="showIntro(schoolmate.id)">
        <img class="portrait" src="/static/img/EdStarsLogo.png" />
        <view class="name">{{schoolmate.user_name}}</view>
      </li>
    </ul>
  </view>
</template>

<script>
import request from '@/static/request.js'
export default {
  data() {
    return {
      userId: 0,
      searchContent: '',
      array: ['姓名','手机','微信'],
      index: 0,
      schoolmates: [],
    };
  },
  methods: {
    search() {
      const vm = this;
      request
        .get('selectSchoolmate/', {
          type: vm.array[vm.index],
          content: vm.searchContent,
        })
        .then(res => {
          vm.schoolmates = res.data
        })
      uni.showToast({
        title: '搜索成功！',
        duration: 1000,
      })
    },
    showIntro(a) {
      let temp = this;
      uni.setStorage({
        key: 'StudentInfo',
        data: a
      });
      uni.navigateTo({
        url: '../schoolmates/student'
      });
    },
    classChange: function(e) {
      this.index = e.target.value
    }
  },
  mounted() {
    const vm = this
    request
      .get('User', {
        
      })
      .then(res => {
        this.schoolmates = res.data
      })
  },
};
</script>

<style>
  .dataBank-top {
    display: flex;
    flex-direction: row;
    position: relative;
    margin-top: 10px;
  }

  .search-row {
    display: flex;
    flex-direction: row;
    position: relative;
    border: 1px solid gray;
    padding: 5px;
    font-size: 18px;
    background-color: #ffffff;
    height: 30px;
    margin: 5px;
    width: 70%;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.3);
  }

  .search-logo {
    height: 30px;
    width: 30px;
  }

  .input-in-search {
    height: 30px;
    line-height: 30px;
    width: 87%
  }

  .search-btn {
    background-color: white;
  }

  .select-table {
    height: 30px;
    line-height: 30px;
    width: 60px;
    margin: 5px;
    padding: 5px;
    border: 1px solid grey;
    font-size: 16px;
    text-align: center;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.3);
    background-color: white;
  }

  .portrait {
    width: 100px;
    height: 100px;
    border-radius: 50px;
    z-index: 300;
    position: relative;
    border: 1px solid gray;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.3);
  }

  .name {
    width: 200px;
    height: 100px;
    border-radius: 50px;
    border: 1px solid gray;
    background-color: white;
    margin-top: -105px;
    margin-left: 18px;
    margin-bottom: 40px;
    padding-left: 100px;
    text-align: left;
    line-height: 100px;
    z-index: 200;
    position: relative;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.3);
  }

  .search-title {
    font-weight: bold;
    font-size: 18px;
    text-align: left;
    padding-left: 5px;
    margin-top: 30px;
  }
</style>

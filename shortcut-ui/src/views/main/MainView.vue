<script setup>
import {ref, computed} from "vue";

import NewCategory from "@/components/news/NewCategory.vue";
import NewSystemShortcut from "@/components/news/NewSystemShortcut.vue";
import NewVscodeShortcut from "@/components/news/NewVscodeShortcut.vue";
import NewAccotestShortcut from "@/components/news/NewAccotestShortcut.vue";

import {
  CirclePlus, Close, Guide, Printer, Search, HomeFilled, Menu, Platform, StarFilled
} from '@element-plus/icons-vue'

import CodePng from '@/assets/image/code.png'

let search = ref('')
let leftMenuDrawOpen = ref(false)
let dialog_category_add = ref(false)
let dialog_system_add = ref(false)
let dialog_vscode_add = ref(false)
let dialog_accotest_add = ref(false)


const handleAddAccotestClick = () => {
  dialog_accotest_add.value = true
}

const handleAddCategoryClick = () => {
  dialog_category_add.value = true
}


const handleAddSystemClick = () => {
  dialog_system_add.value = true
}


const handleAddVscodeClick = () => {
  dialog_vscode_add.value = true
}

</script>

<template>
  <div class="main">
    <div class="header">
      <div class="logo-container">
        <div class="logo"><img :src="CodePng" style="width:58px;height:58px;" alt=""></div>
        <div class="logo-title">VsCode 快捷键配置</div>
      </div>

      <div class="main-menu-left-button" @click="leftMenuDrawOpen = true">
        <el-icon style="font-weight: bold;">
          <font-awesome-icon :icon="['fas', 'bars']"/>
        </el-icon>
      </div>

      <div class="search-container">
        <el-input v-model="search" :suffix-icon="Search" :prefix-icon="Guide" placeholder="搜索快捷键"/>
      </div>

      <div class="exports-container">
        <el-dropdown trigger="click">
          <el-button :icon="CirclePlus" style="width: 30px;height: 30px;margin-right: 8px;" plain
                     type="primary"></el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="handleAddCategoryClick()">
                新增快捷键分类
              </el-dropdown-item>
              <el-dropdown-item divided @click="handleAddSystemClick()">
                新增操作系统快捷键
              </el-dropdown-item>
              <el-dropdown-item @click="handleAddVscodeClick()">
                新增VsCode快捷键
              </el-dropdown-item>
              <el-dropdown-item @click="handleAddAccotestClick()">
                新增Accotest快捷键
              </el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        <el-button :icon="Printer" plain type="primary" style="width: 30px;height: 30px;"></el-button>
      </div>

    </div>
    <div class="content">
      <div class="body">
        <router-view/>
      </div>
    </div>
  </div>

  <el-drawer
      v-model="leftMenuDrawOpen"
      direction="ltr"
      :size="240"
      :with-header="false"
      class="custom-drawer"
  >
    <template #default>
      <div class="aside-container">
        <div class="aside-header">
          <div class="aside-logo">
            <el-image :src="CodePng" style="height: 30px;width:30px;border-radius: 3px;"/>
            <span style="margin-left: 10px;font-weight: bold;font-size: 18px;">快捷键配置</span>
          </div>
          <div class="aside-action">
            <el-button circle :icon="Close" size="small" @click="leftMenuDrawOpen=false"></el-button>
          </div>
        </div>
        <div class="aside-body">
          <el-menu
              active-text-color="#ffd04b"
              class="main-aside-menu"
              :default-active="$route.path"
              router
          >
            <el-menu-item index="/" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <HomeFilled/>
              </el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/system/shortcuts" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <Menu/>
              </el-icon>
              <span>操作系统快捷键</span>
            </el-menu-item>
            <el-menu-item index="/vscode/shortcuts" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <Platform/>
              </el-icon>
              <span>VsCode 快捷键</span>
            </el-menu-item>
            <el-menu-item index="/accotest/shortcuts" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <StarFilled/>
              </el-icon>
              <span>Accotest 快捷键</span>
            </el-menu-item>
          </el-menu>


        </div>
      </div>
    </template>
    <template #footer>
      <div style="display: flex;">
        <el-button type="success" round plain style="width:100%;">当前版本: 0.0.1</el-button>
      </div>
    </template>
  </el-drawer>

  <el-dialog
      v-model="dialog_category_add"
      title="新增快捷键分类"
      width="75%"
  >
    <div>
      <NewCategory/>
    </div>
  </el-dialog>

  <el-dialog
      v-model="dialog_system_add"
      title="新增系统快捷键"
      width="75%"
  >
    <div>
      <NewSystemShortcut/>
    </div>
  </el-dialog>

  <el-dialog
      v-model="dialog_vscode_add"
      title="新增Vscode快捷键"
      width="75%"
  >
    <div>
      <NewVscodeShortcut/>
    </div>
  </el-dialog>

  <el-dialog
      v-model="dialog_accotest_add"
      title="新增Accotest快捷键"
      width="75%"
  >
    <NewAccotestShortcut/>
  </el-dialog>


</template>

<style scoped>

* {
  --el-switch-on-color: rgba(178, 118, 234, 0.8);
  --el-switch-border-color: rgba(64, 243, 14, 0.8);
}

.main {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
}

.header {
  width: 100%;
  height: 60px;
  border-bottom: 1px solid lightgray;
  display: flex;
  align-items: center;
  box-sizing: border-box;
}

.content {
  width: 100vw;
  height: calc(100vh - 60px);
  box-sizing: border-box;
}

.logo-container {
  display: flex;
  align-items: center;
  width: 240px;
  height: 60px;
  box-sizing: border-box;
}

.logo {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.logo-title {
  height: 60px;
  display: flex;
  align-items: center;
  font-weight: bold;
  font-size: larger;
  flex: 1;
}

.main-menu-left-button {
  width: 30px;
  height: 30px;
  border: 1px solid lightgrey;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-menu-left-button:hover {
  transition: 1s;
}

.search-container {
  display: flex;
  align-items: center;
  flex: 1;
  height: 60px;
  box-sizing: border-box;
  padding: 0 10px;
}

.exports-container {
  display: flex;
  align-items: center;
  width: 100px;
  height: 60px;
  padding-right: 20px;
  box-sizing: border-box;
  justify-content: flex-end;
}

.aside-container {
  display: flex;
  width: 100%;
  height: 100%;
  overflow-y: scroll;
  flex-direction: column;
}

.aside-header {
  width: 100%;
  height: 30px;
  display: flex;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border-bottom: 1px solid lightgrey;
}

.aside-logo {
  display: flex;
  flex: 1;
  height: 30px;
  margin: 0;
  padding: 0;
  align-items: center;
  box-sizing: border-box;

}

.aside-action {
  display: flex;
  width: 30px;
  height: 30px;
  align-items: center;
  justify-content: flex-end;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-menu-left-button {
  width: 30px;
  height: 30px;
  border: 1px solid lightgrey;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-menu-left-button:hover {
  border: 1px solid #03f2f8;
  transition: 1s;
}

.aside-body {
  flex: 1;
}

.main-aside-menu {
  border: none;
  padding: 0 !important;
  margin: 0 !important;
}

.custom-drawer {
  border: none;
  padding: 0 !important;
  margin: 0 !important;
}

.body {
  width: 100vw;
  box-sizing: border-box;
  height: calc(100vh - 60px);
  overflow-y: scroll;
}

</style>

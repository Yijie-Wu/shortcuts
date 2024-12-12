<script setup>
import {ref, onMounted, computed} from "vue";
import {useAllSystemShortcutStore} from "@/stores/shortcuts.js"
import {get_system_shortcuts} from "@/apis/shortcuts.js"
import {showMessage} from "@/utils/message.js";
import {getKey, getMouse} from "@/utils/common.js";


const search = ref("");
const system_shortcuts_store = useAllSystemShortcutStore()

onMounted(() => {
  get_system_shortcuts().then(res => {
    system_shortcuts_store.setShortcuts(res.data)
  }).catch(err => {
    showMessage('error', '获取System快捷键列表失败:'+ err.message);
  })
})


const filterTableData = computed(() =>
    system_shortcuts_store.shortcuts.filter(
        (data) =>
            !search.value ||
            data.function.toLowerCase().includes(search.value.toLowerCase())
    )
)

</script>

<template>
  <div class="shortcuts-container">
    <el-table :data="filterTableData" style="width: 100%" border striped>
      <el-table-column label="编号" prop="id" width="80" align="center" fixed="left"/>
      <el-table-column label="中文功能" prop="function" width="200" fixed="left"/>
      <el-table-column label="英文功能" prop="function_en" width="200"/>
      <el-table-column label="标签" prop="tag" width="100" align="center">
        <template #default="scope">
          <el-tag type="success" v-if="scope.row.tag !== ''" round>{{scope.row.tag}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="快捷键分类" prop="category_name" width="160" align="center">
        <template #default="scope">
          <el-tag type="primary" round>{{scope.row.category_name}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="快捷键类型" prop="type" width="120" align="center">
        <template #default="scope">
          <el-tag type="warning" round>{{scope.row.type}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="快捷键" prop="content" width="500" align="center">
        <template #default="scope">
          <div v-if="scope.row.type === '单键'">
            按下 <el-tag type="warning" round>{{getKey(scope.row.content.content[0])}}</el-tag>
          </div>
          <div v-else-if="scope.row.type === '组合键'">
            同时按下 <el-tag type="warning" style="margin: 0 3px;" v-for="i in scope.row.content.content" round>{{getKey([i])}}</el-tag>
          </div>
          <div v-else-if="scope.row.type === '级联组合键'">
            先同时按下 <el-tag type="warning" style="margin: 0 3px;" v-for="i in scope.row.content.content[0]" round>{{getKey([i])}}</el-tag>
            再按下 <el-tag type="warning" style="margin: 0 3px;" v-for="j in scope.row.content.content[1]" round>{{getKey([j])}}</el-tag>
          </div>
          <div v-else-if="scope.row.type === '鼠标'">
            <el-tag type="primary" round>{{getMouse(scope.row.content.content[0])}}</el-tag>
          </div>
          <div v-else>
            先按下 <el-tag type="warning" style="margin: 0 3px;" v-for="i in scope.row.content.content[0]" round>{{getKey([i])}}</el-tag>
            再 <el-tag type="warning" style="margin: 0 3px;" v-for="j in scope.row.content.content[1]" round>{{getMouse([j])}}</el-tag>
          </div>

        </template>
      </el-table-column>
      <el-table-column align="center" fixed="right" width="200">
        <template #header>
          <el-input v-model="search" size="small" placeholder="Type to search" />
        </template>
        <template #default="scope">
          <el-button size="small" type="success" round plain @click="">
            播放
          </el-button>
          <el-button size="small" type="warning" round plain @click="">
            编辑
          </el-button>
          <el-button size="small" type="danger" @click="" round plain>
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<style scoped>
.shortcuts-container {
  padding: 10px;
  overflow-y: scroll;
}
</style>

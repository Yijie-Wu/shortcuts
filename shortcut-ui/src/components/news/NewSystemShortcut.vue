<script setup>
import {computed, reactive, onMounted, ref} from "vue";

import {useRouter} from "vue-router";
import {useAllCategoryStore} from "@/stores/category.js";
import {get_categories} from "@/apis/category.js";
import {get_keys} from "@/apis/keys.js";
import {showMessage} from "@/utils/message.js";
import {get_mouse} from "@/apis/mouse.js";
import {useAllKeysStore} from "@/stores/keys.js";
import {useAllMouseStore} from "@/stores/mouse.js";
import {create_system_shortcut, get_system_shortcuts} from "@/apis/shortcuts.js";
import {useAllSystemShortcutStore} from "@/stores/shortcuts.js";


let router = useRouter();
let system_show_mode = ref(0)
let keys_store = useAllKeysStore()
let mouse_store = useAllMouseStore()
let category_store = useAllCategoryStore()
let system_shortcuts_store = useAllSystemShortcutStore()

const category_tags = ['全局', '面板', '块']
const shortcuts_types = ['单键', '组合键', '级联组合键', '鼠标', '键鼠组合']

const system_mode1 = ref([])
const system_mode2 = ref([])
const system_mode3_1 = ref([])
const system_mode3_2 = ref([])
const system_mode4 = ref([])
const system_mode5_1 = ref([])
const system_mode5_2 = ref([])

let system_shortcut_form_ref = ref(null)


onMounted(() => {
  get_keys().then(res => {
    keys_store.setKeys(res.data)
  }).catch(err => {
    showMessage('error', '获取键列表失败:' + err)
  })

  get_mouse().then(res => {
    mouse_store.setMouse(res.data)
  }).catch(err => {
    showMessage('error', '获取鼠标列表失败:' + err)
  })

  get_categories().then(res => {
    category_store.setCategories(res.data)
  }).catch(err => {
    showMessage('error', '获取分类列表失败:' + err)
  })

  get_system_shortcuts().then(res => {
    system_shortcuts_store.setShortcuts(res.data)
  }).catch(err => {
    showMessage('error', '获取system快捷键列表失败:' + err)
  })
})


const system_shortcut_form = reactive(
    {
      tag: '',
      type: '',
      function: '',
      function_en: '',
      category_id: null
    }
)

const system_shortcut_form_rules = reactive({
  type: [
    {required: true, message: '类型不能为空', trigger: 'blur'}
  ],
  function: [
    {required: true, message: '中文功能描述不能为空', trigger: 'blur'},
    {min: 1, max: 100, message: '中文功能描述长度必须在1到100之间', trigger: 'blur'},
  ],
  function_en: [
    {required: true, message: '英文功能描述不能为空', trigger: 'blur'},
    {min: 1, max: 100, message: '英文功能描述长度必须在1到100之间', trigger: 'blur'},
  ],
  category_id: [
    {required: true, message: '请选择分类', trigger: 'blur'},
  ]
})

const system_categories = computed(() => {
  return category_store.categories.filter(category => category.type === 'Windows')
})

const handle_system_change = (event) => {
  if (event === '单键') {
    system_show_mode.value = 1
  } else if (event === '组合键') {
    system_show_mode.value = 2
  } else if (event === '级联组合键') {
    system_show_mode.value = 3
  } else if (event === '鼠标') {
    system_show_mode.value = 4
  } else if (event === '键鼠组合') {
    system_show_mode.value = 5
  } else {
    system_show_mode.value = 0
  }
}

const createSystemShortcut = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    const data = {
      'tag': system_shortcut_form.tag,
      'type': system_shortcut_form.type,
      'function': system_shortcut_form.function,
      'function_en': system_shortcut_form.function_en,
      'category_id': system_shortcut_form.category_id,
      'content': ''
    }

    if (system_show_mode.value === 0) {
      showMessage('warning', '请选择快捷键类型')
      return
    } else if (system_show_mode.value === 1) {
      data.content = system_mode1.value
    } else if (system_show_mode.value === 2) {
      data.content = system_mode2.value
    } else if (system_show_mode.value === 3) {
      data.content = [system_mode3_1.value, system_mode3_2.value]
    } else if (system_show_mode.value === 4) {
      data.content = system_mode4.value
    } else {
      data.content = [system_mode5_1.value, system_mode5_2.value]
    }

    create_system_shortcut(data).then((res) => {
      system_shortcuts_store.addShortcut(res.data)
      router.push('/system/shortcuts')
      showMessage('success', '添加system快捷键成功')
    }).catch((err) => {
      showMessage('error', err)
    })
  })
}


</script>

<template>
  <div>
    <el-form
        label-width="auto"
        ref="system_shortcut_form_ref"
        :model="system_shortcut_form"
        :rules="system_shortcut_form_rules"
    >
      <el-form-item label="中文功能描述" prop="function">
        <el-input placeholder="中文功能描述" v-model="system_shortcut_form.function"/>
      </el-form-item>
      <el-form-item label="英文功能描述" prop="function_en">
        <el-input placeholder="英文功能描述" v-model="system_shortcut_form.function_en"/>
      </el-form-item>
      <el-form-item label="快捷键的分类" prop="category_id">
        <el-select
            placeholder="选择快捷键类型"
            style="width: 300px;"
            v-model="system_shortcut_form.category_id"
        >
          <el-option v-for="t in system_categories" :label="t.name" :value="t.id" :key="t.id"/>
        </el-select>
      </el-form-item>
      <el-form-item label="快捷键的类型" prop="type">
        <el-select
            placeholder="选择快捷键类型"
            style="width: 300px;"
            v-model="system_shortcut_form.type"
            @change="handle_system_change"
        >
          <el-option v-for="t in shortcuts_types" :label="t" :value="t" :key="t"/>
        </el-select>
      </el-form-item>
      <el-form-item label="快捷键的标签" prop="tag">
        <el-select placeholder="选择快捷键标签" v-model="system_shortcut_form.tag" style="width: 300px;">
          <el-option v-for="t in category_tags" :label="t" :value="t" :key="t"/>
        </el-select>
      </el-form-item>
      <div
          style="margin: 10px;padding:5px;border: 1px solid lightgray;border-radius: 5px;display: flex;align-items: center;justify-content: space-between;">
        <div v-if="system_show_mode === 1">
          <el-select
              v-model="system_mode1"
              placeholder="选择键"
              size="large"
              multiple
              :multiple-limit="1"
              clearable
              filterable
              style="width: 70vw;"
          >
            <el-option
                v-for="item in keys_store.keyboards"
                :key="item.id_"
                :label="item.name1"
                :value="item.id_"
            />
          </el-select>
        </div>
        <div v-else-if="system_show_mode === 2">
          <el-select
              v-model="system_mode2"
              placeholder="选择组合键"
              size="large"
              multiple
              :multiple-limit="4"
              clearable
              filterable
              style="width: 70vw;"
          >
            <el-option
                v-for="item in keys_store.keyboards"
                :key="item.id_"
                :label="item.name1"
                :value="item.id_"
            />
          </el-select>
        </div>
        <div v-else-if="system_show_mode === 3">
          <el-select
              v-model="system_mode3_1"
              placeholder="选择键"
              size="large"
              multiple
              :multiple-limit="2"
              clearable
              filterable
              style="width: 35vw;"
          >
            <el-option
                v-for="item in keys_store.keyboards"
                :key="item.id_"
                :label="item.name1"
                :value="item.id_"
            />
          </el-select>
          <el-select
              v-model="system_mode3_2"
              placeholder="选择组合键2"
              size="large"
              multiple
              :multiple-limit="2"
              clearable
              filterable
              style="width: 35vw;margin-left: 5px;"
          >
            <el-option
                v-for="item in keys_store.keyboards"
                :key="item.id_"
                :label="item.name1"
                :value="item.id_"
            />
          </el-select>
        </div>
        <div v-else-if="system_show_mode === 4">
          <el-select
              v-model="system_mode4"
              placeholder="选择鼠标"
              size="large"
              multiple
              :multiple-limit="1"
              clearable
              filterable
              style="width: 70vw;"
          >
            <el-option
                v-for="item in mouse_store.mouse"
                :key="item.id_"
                :label="item.name"
                :value="item.id_"
            />
          </el-select>
        </div>
        <div v-else-if="system_show_mode === 5">
          <el-select
              v-model="system_mode5_1"
              placeholder="选择键盘"
              size="large"
              multiple
              :multiple-limit="2"
              clearable
              filterable
              style="width: 35vw;"
          >
            <el-option
                v-for="item in keys_store.keyboards"
                :key="item.id_"
                :label="item.name1"
                :value="item.id_"
            />
          </el-select>
          <el-select
              v-model="system_mode5_2"
              placeholder="选择鼠标"
              size="large"
              multiple
              :multiple-limit="1"
              clearable
              filterable
              style="width: 35vw;margin-left: 5px;"
          >
            <el-option
                v-for="item in mouse_store.mouse"
                :key="item.id_"
                :label="item.name"
                :value="item.id_"
            />
          </el-select>
        </div>
        <div v-else><span style="color:red;font-weight: bold;">*</span> 请选择快捷键类型</div>
      </div>
      <el-form-item>
        <el-button type="primary" @click="createSystemShortcut(system_shortcut_form_ref)">创建System快捷键
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<style scoped>

</style>

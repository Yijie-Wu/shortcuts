<script setup>
import {reactive, ref} from "vue";
import {useAllCategoryStore} from "@/stores/category.js";
import {add_category} from "@/apis/category.js";
import {showMessage} from "@/utils/message.js";

const formCategoryRef = ref(null)
let category_store = useAllCategoryStore()

const category_types = ['Windows', 'Vscode', 'Accotest']

const category_form = reactive({
  type: 'Accotest',
  name: '',
  desc: '',
})

const category_rules = reactive({
  type: [
    {required: true, message: '选择快捷键分类类别', trigger: 'blur'},
  ],
  name: [
    {required: true, message: '分类名称不能为空', trigger: 'blur'},
    {min: 1, max: 60, message: '分类名称长度必须在1到60之间', trigger: 'blur'},
  ],
  desc: [
    {required: true, message: '分类描述不能为空', trigger: 'blur'},
    {min: 1, max: 300, message: '分类描述长度必须在1到300之间', trigger: 'blur'},
  ]
})

const createCategory = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    add_category(category_form).then(res => {
      category_store.addCategory(res.data)
      showMessage('success', '分类添加成功')
    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}
</script>

<template>
  <el-form
      ref="formCategoryRef"
      :model="category_form"
      :rules="category_rules"
      style="width:100%;"
      label-width="auto"
      label-position="left">
    <el-form-item style="margin-top:10px;" prop="type" label="选择属主">
      <el-select v-model="category_form.type" placeholder="选择属主" style="width:300px;">
        <el-option v-for="o in category_types" :label="o" :value="o" :key="o"/>
      </el-select>
    </el-form-item>
    <el-form-item style="margin-top:10px;" prop="name" label="分类名称">
      <el-input v-model="category_form.name" class="w-50 m-2" placeholder="分类名称" size="large" type="text"/>
    </el-form-item>
    <el-form-item style="margin-top:10px;" prop="desc" label="分类描述">
      <el-input v-model="category_form.desc" class="w-50 m-2" placeholder="分类描述" size="large"
                type="textarea"/>
    </el-form-item>

    <el-form-item style="margin-top:50px;" type="submit">
      <el-button type="primary" @click="createCategory(formCategoryRef)" plain style="width: 100%;" size="large"
                 round>创建新分类
      </el-button>
    </el-form-item>
  </el-form>
</template>

<style scoped>

</style>

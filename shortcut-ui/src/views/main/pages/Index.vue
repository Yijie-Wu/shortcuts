<script setup>
import {onMounted, computed} from 'vue'
import PlayBoard from "@/components/PlayBoard.vue";

</script>

<template>
  <div class="container">
    <div>
      <PlayBoard/>
    </div>
    <el-row>
      <el-col :span="6">
        <el-card>
          Vscode 快捷键文档
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card>
          Windows快捷键类别
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card>
           个Vscode快捷键类别
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card>
          个Accotest快捷键类别
        </el-card>
      </el-col>
    </el-row>

    <el-row>
      <el-col>
        <el-card style="height: 300px;">accotest</el-card>
      </el-col>
    </el-row>
  </div>


</template>

<style scoped>

.container {
  box-sizing: border-box;
  padding: 10px;
}

.el-col {
  box-sizing: border-box;
  padding: 10px;
}


</style>

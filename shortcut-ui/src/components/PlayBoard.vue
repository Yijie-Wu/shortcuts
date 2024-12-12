<script setup>
import Keyboard from "@/components/keyboard.vue";
import Mouse from "@/components/mouse.vue"
import {Clock} from "@element-plus/icons-vue";


</script>

<template>
  <div>
    <div class="keyboard">
      <keyboard/>
    </div>
    <div class="mouse">
      <Mouse/>
    </div>
  </div>
</template>

<style scoped>
.keyboard {
  display: flex;
  align-items: center;
  justify-content: center;
}

.mouse {
  width: 255px;
  height: 376px;
  background: white;
  position: fixed;
  top: 82px;
  right: 30px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script setup>

</script>

<template>
  <div class="mouse-container">
    <div class="mouse">
      <div class="mouse-top">
        <div class="left-key"></div>
        <div class="middle-key">
          <div class="scroll-wheel"></div>
        </div>
        <div class="right-key"></div>
      </div>
      <div class="mouse-body">LuoJi</div>
    </div>
  </div>
</template>

<style scoped>
.mouse-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}

.mouse {
  width: 240px;
  height: 350px;
  border-radius: 100px 100px 50px 50px;
  background-color: rgba(7, 253, 7, 0.17);
}

.mouse-top {
  height: 170px;
  width: 240px;
  box-sizing: border-box;
  display: flex;
  border-radius: 100px 100px 0 0;
}

.left-key {
  height: 170px;
  width: 100px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #ccc;
  border-bottom: 1px solid #ccc;
  background-color: #f65803;
  border-top-left-radius: 100px;
  border-bottom-right-radius: 30px;
}


.middle-key {
  height: 170px;
  width: 40px;
  box-sizing: border-box;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  border-top: 20px solid white;
}


.right-key {
  height: 170px;
  width: 100px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
  border-left: 1px solid #ccc;
  border-bottom: 1px solid #ccc;
  background-color: #f65803;
  border-top-right-radius: 100px;
  border-bottom-left-radius: 30px;
}


.mouse-body {
  width: 240px;
  height: 180px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 0 0 50px 50px;
  font-size: 30px;
  font-weight: bold;
}

.scroll-wheel {
  width: 30px;
  height: 100px;
  background-color: #2b2d30;
  border-radius: 15px;
  box-sizing: border-box;
  position: relative;
  top:-15px;
}


</style>

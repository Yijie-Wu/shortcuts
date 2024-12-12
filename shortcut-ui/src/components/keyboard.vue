<script setup>
import {Top, Back, Right, Bottom} from "@element-plus/icons-vue";
import WinPNG from "@/assets/image/win.png"
import ShiftPNG from "@/assets/image/shift.png"

const props = defineProps({
  activeKeys: {
    type: Array,
    default: () => []
  },
  type: {
    type: String,
    default: 'default'
  },
  actions: {
    type: Array,
    default: () => []
  }
});


</script>

<template>
  <div class="keyboard">
    <div class="area-v-left">
      <div class="area-v-left-top">
        <div>
          <div class="key">ESC</div>
        </div>
        <div class="f-container" style="margin-left: 46px;">
          <div class="key key-active">F1</div>
          <div class="key">F2</div>
          <div class="key">F3</div>
          <div class="key">F4</div>
        </div>
        <div class="f-container" style="margin: 0 32px;">
          <div class="key">F5</div>
          <div class="key">F6</div>
          <div class="key">F7</div>
          <div class="key">F8</div>
        </div>
        <div class="f-container">
          <div class="key">F9</div>
          <div class="key">F10</div>
          <div class="key">F11</div>
          <div class="key">F12</div>
        </div>
      </div>
      <div class="area-v-left-body">
        <div class="row">
          <div class="key">
            <div class="dou-top">~</div>
            <div class="dou-bottom">`</div>
          </div>
          <div class="key">
            <div class="dou-top">!</div>
            <div class="dou-bottom">1</div>
          </div>
          <div class="key">
            <div class="dou-top">@</div>
            <div class="dou-bottom">2</div>
          </div>
          <div class="key">
            <div class="dou-top">#</div>
            <div class="dou-bottom">3</div>
          </div>
          <div class="key">
            <div class="dou-top">$</div>
            <div class="dou-bottom">4</div>
          </div>
          <div class="key">
            <div class="dou-top">%</div>
            <div class="dou-bottom">5</div>
          </div>
          <div class="key">
            <div class="dou-top">^</div>
            <div class="dou-bottom">6</div>
          </div>
          <div class="key">
            <div class="dou-top">&</div>
            <div class="dou-bottom">7</div>
          </div>
          <div class="key">
            <div class="dou-top">*</div>
            <div class="dou-bottom">8</div>
          </div>
          <div class="key">
            <div class="dou-top">(</div>
            <div class="dou-bottom">9</div>
          </div>
          <div class="key">
            <div class="dou-top">)</div>
            <div class="dou-bottom">0</div>
          </div>
          <div class="key">
            <div class="dou-top">_</div>
            <div class="dou-bottom">-</div>
          </div>
          <div class="key">
            <div class="dou-top">+</div>
            <div class="dou-bottom">=</div>
          </div>
          <div class="key" style="width:104px;">Backspace</div>
        </div>
        <div class="row">
          <div class="key" style="width: 82px;">Tab</div>
          <div class="key">Q</div>
          <div class="key">W</div>
          <div class="key">E</div>
          <div class="key">R</div>
          <div class="key">T</div>
          <div class="key">Y</div>
          <div class="key">U</div>
          <div class="key">I</div>
          <div class="key">O</div>
          <div class="key">P</div>
          <div class="key">
            <div class="dou-top">{</div>
            <div class="dou-bottom">[</div>
          </div>
          <div class="key">
            <div class="dou-top">}</div>
            <div class="dou-bottom">]</div>
          </div>
          <div class="key" style="width:74px;">
            <div class="dou-top">|</div>
            <div class="dou-bottom">\</div>
          </div>
        </div>
        <div class="row">
          <div class="key" style="width: 100px;">
            <div class="dou-top">
              <span class="caps-led"></span>
            </div>
            <div class="dou-bottom">Caps Lock</div>
          </div>
          <div class="key">A</div>
          <div class="key">S</div>
          <div class="key">D</div>
          <div class="key">F</div>
          <div class="key">G</div>
          <div class="key">H</div>
          <div class="key">J</div>
          <div class="key">K</div>
          <div class="key">L</div>
          <div class="key">
            <div class="dou-top">:</div>
            <div class="dou-bottom">;</div>
          </div>
          <div class="key">
            <div class="dou-top">"</div>
            <div class="dou-bottom">'</div>
          </div>
          <div class="key" style="width:118px;">Enter</div>
        </div>
        <div class="row">
          <div class="key" style="width:140px;">
            <div style="width: 100%;display: flex;align-items: center;justify-content: flex-start;padding-left: 15px;">Shift</div>
            <div style="width: 100%;display: flex;align-items: center;justify-content: flex-start;padding-left: 15px;">
              <el-image :src="ShiftPNG" style="width: 25px; height: 25px;"></el-image>
            </div>
          </div>
          <div class="key">Z</div>
          <div class="key">X</div>
          <div class="key">C</div>
          <div class="key">V</div>
          <div class="key">B</div>
          <div class="key">N</div>
          <div class="key">M</div>
          <div class="key">
            <div class="dou-top"><</div>
            <div class="dou-bottom">,</div>
          </div>
          <div class="key">
            <div class="dou-top"><</div>
            <div class="dou-bottom">.</div>
          </div>
          <div class="key">
            <div class="dou-top">?</div>
            <div class="dou-bottom">/</div>
          </div>
          <div class="key" style="width: 140px;">
            <div style="width: 100%;display: flex;align-items: center;justify-content: flex-start;padding-left: 15px;">Shift</div>
            <div style="width: 100%;display: flex;align-items: center;justify-content: flex-start;padding-left: 15px;">
              <el-image :src="ShiftPNG" style="width: 25px; height: 25px;"></el-image>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="key" style="width: 82px;">Ctrl</div>
          <div class="key" style="width: 70px;">
            <el-image :src="WinPNG" style="width: 25px; height: 25px;"></el-image>
          </div>
          <div class="key" style="width: 70px;">Alt</div>
          <div class="key" style="width: 326px;"></div>
          <div class="key" style="width: 70px;">Alt</div>
          <div class="key" style="width: 70px;">
            <el-image :src="WinPNG" style="width: 25px; height: 25px;"></el-image>
          </div>
          <div class="key" style="width: 70px;">Fn</div>
          <div class="key" style="width: 82px;">Ctrl</div>
        </div>

      </div>
    </div>
    <div class="area-v-center">
      <div class="area-v-center-top">
        <div class="f-container">
          <div class="key">Print Screen</div>
          <div class="key">Scroll Lock</div>
          <div class="key">Pause Break</div>
        </div>
      </div>
      <div class="area-v-center-body">
        <div class="s-container">
          <div class="row">
            <div class="key">Insert</div>
            <div class="key">Home</div>
            <div class="key">PgUp</div>
          </div>
          <div class="row">
            <div class="key">Delete</div>
            <div class="key">End</div>
            <div class="key">PgDn</div>
          </div>
        </div>
        <div class="s-container" style="margin-top: 65px">
          <div class="row">
            <div class="key-none"></div>
            <div class="key">
              <el-icon :size="18">
                <Top/>
              </el-icon>
            </div>
            <div class="key-none"></div>
          </div>
          <div class="row">
            <div class="key">
              <el-icon :size="18">
                <Back/>
              </el-icon>
            </div>
            <div class="key">
              <el-icon :size="18">
                <Bottom/>
              </el-icon>
            </div>
            <div class="key">
              <el-icon :size="18">
                <Right/>
              </el-icon>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="area-v-right">
      <div class="area-v-right-top">
        <div class="light-container">
          <div class="led-container">
            <span class="led"></span>
          </div>
          <div class="light-text">
            <span>Num</span>
            <span>Lock</span>
          </div>
        </div>
        <div class="light-container">
          <div class="led-container">
            <span class="led"></span>
          </div>
          <div class="light-text">
            <span>Caps</span>
            <span>Lock</span>
          </div>
        </div>
        <div class="light-container">
          <div class="led-container">
            <span class="led"></span>
          </div>
          <div class="light-text">
            <span>Screen</span>
            <span>Lock</span>
          </div>
        </div>
      </div>
      <div class="area-v-right-body">
        <div class="area-v-right-v-left">
          <div class="row">
            <div class="key">
              <div class="dou-top">
                <span class="num-led"></span>
              </div>
              <div class="dou-bottom">Num Lock</div>
            </div>
            <div class="key">/</div>
            <div class="key">*</div>
          </div>
          <div class="row">
            <div class="key">
              <div class="dou-top">7</div>
              <div class="dou-bottom">Home</div>
            </div>
            <div class="key">
              <div class="dou-top">8</div>
              <div class="dou-bottom">
                <el-icon :size="15"><Top/></el-icon>
              </div>
            </div>
            <div class="key">
              <div class="dou-top">9</div>
              <div class="dou-bottom">PgUp</div>
            </div>
          </div>
          <div class="row">
            <div class="key">
              <div class="dou-top">4</div>
              <div class="dou-bottom"><el-icon :size="15"><Back/></el-icon></div>
            </div>
            <div class="key">5</div>
            <div class="key">
              <div class="dou-top">6</div>
              <div class="dou-bottom"><el-icon :size="15"><Right/></el-icon></div>
            </div>
          </div>
          <div class="row">
            <div class="key">
              <div class="dou-top">1</div>
              <div class="dou-bottom">End</div>
            </div>
            <div class="key">
              <div class="dou-top">2</div>
              <div class="dou-bottom"><el-icon :size="15"><Bottom/></el-icon></div>
            </div>
            <div class="key">
              <div class="dou-top">3</div>
              <div class="dou-bottom">PgDn</div>
            </div>
          </div>
          <div class="row">
            <div class="key" style="width: 114px;">
              <div class="dou-top">0</div>
              <div class="dou-bottom">Insert</div>
            </div>
            <div class="key">
              <div class="dou-top">.</div>
              <div class="dou-bottom">Delete</div>
            </div>
          </div>
        </div>
        <div class="area-v-right-v-right">
          <div class="row">
            <div class="key">-</div>
          </div>
          <div class="row">
            <div class="key" style="height: 114px;">+</div>
          </div>
          <div class="row">
            <div class="key" style="height: 114px;">Enter</div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
.keyboard {
  width: 1400px;
  height: 400px;
  border: 1px solid #ccc;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
}

.area-v-left {
  height: 380px;

}

.area-v-center {
  height: 380px;
  margin: 0 10px;
}

.area-v-right {
  height: 380px;
  display: flex;
  flex-direction: column;
}

.area-v-left-top,
.area-v-center-top,
.area-v-right-top {
  height: 60px;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  justify-content: space-evenly;
}

.row {
  display: flex;
}

.key {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  border: 1px solid #ccc;
  margin: 4px;
  border-radius: 4px;
  text-align: center;
  font-size: small;
  flex-direction: column;
  cursor: pointer;
}

.key:active {
  border: 1px solid #2cf109;
}

.key-none {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  margin: 4px;
}

.f-container {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

.s-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

.area-v-center-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

.area-v-right-body {
  display: flex;
}

.area-v-right-v-left {
  display: flex;
  flex-direction: column;
}

.area-v-right-v-right {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

.area-v-left-body {
  box-sizing: border-box;
}

.light-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
  justify-content: space-around;
  width: 100%;
  height: 100%;
}

.led-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 15px;
  box-sizing: border-box;
}

.light-text {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 45px;
  box-sizing: border-box;
  font-size: small;
}

.led {
  width: 40px;
  height: 8px;
  background: lightgray;
  border-radius: 4px;
}

.dou-top {
  width:100%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 15px;
  box-sizing: border-box;
  padding-left: 5px;
}

.dou-bottom {
  width:100%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  flex: 1;
  top: -7px;
  position: relative;
}

.num-led,
.caps-led {
  width: 6px;height: 6px;
  background: lightgray;
  border-radius: 50%;
}

.active {
  background: #2cf109;
}

.key-active {
  background: #f65803;
}



</style>

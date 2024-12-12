import {createApp} from 'vue';
import './style.css';
import App from './App.vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import 'element-plus/theme-chalk/display.css';
import router from "./router/index.js";
import {createPinia} from 'pinia';
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faBars } from '@fortawesome/free-solid-svg-icons'

library.add(faBars)

const app = createApp(App)
const pinia = createPinia()

app.use(ElementPlus).use(pinia).use(router).component('font-awesome-icon', FontAwesomeIcon).mount('#app')

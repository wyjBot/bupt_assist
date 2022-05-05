import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus';

// import vue from 'vue'
import "../node_modules/element-plus/theme-chalk/index.css"


const bbc=13;

const app = createApp(App)
app.use(ElementPlus)
app.use(router)
app.mount('#app')

export default app


// 2. 定义一些路由
// 每个路由都需要映射到一个组件。
// 我们后面再讨论嵌套路由。

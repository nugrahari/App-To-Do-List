import { createApp } from "vue";
import "./assets/styles/style.css";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import App from "./App.vue";
import router from "./router";
import { store } from "./store";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';

const app = createApp(App);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

app.component('QuillEditor', QuillEditor)
app.use(router);
app.use(ElementPlus);
app.use(store);
app.mount("#app");

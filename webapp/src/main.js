import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'

axios.defaults.baseURL = " https://smh345qw2l.execute-api.us-east-1.amazonaws.com/v1"

createApp(App).use(router).mount('#app')

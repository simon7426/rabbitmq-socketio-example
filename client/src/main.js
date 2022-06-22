import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import Socketio from './plugins/Socketio.js'

const app = createApp(App)

app.use(Socketio,{
    connection: `http://hello.world/winner`,
    options: {}
})


app.mount('#app')


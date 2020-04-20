import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/Login.vue'
import Home from './components/Home.vue'
import Welcome from './components/Welcome.vue'
import History_video from './components/History_video.vue'
import Now_video from './components/Now_video.vue'
import Device_manage from './components/Device_manage.vue'
import Device_warn from './components/Device_warn.vue'
import Pet from './components/Pet.vue'
import Plant from './components/Plant.vue'
import Information from './components/Information.vue'
import Person from './components/Person.vue'
import Room1 from './components/Room1.vue'
import Room2 from './components/Room2.vue'
import Room3 from './components/Room3.vue'
import Manage_students from "./components/Manage_students"
import Manage_exception from "./components/Manage_exception"
import Manage_home from "./components/Manage_home"
import Manage_information from "./components/Manage_information"
import Manage_Lamp from "./components/Manage_Lamp";

Vue.use(Router)

const router = new Router({
    routes: [
        { path: '/', redirect: '/login' },
        { path: '/login', component: Login },
        { path: '/students', component: Manage_students},
        { path: '/informationadmin', component: Manage_information},
        { path: '/exception', component: Manage_exception},
        { path: '/lamp', component: Manage_Lamp},
        { path: '/homeadmin', component: Manage_home},
        { path: '/manage_home', component: Manage_home},
        {
            path: '/home',
            component: Home,
            redirect: '/welcome',
            children: [
                { path: '/welcome', component: Welcome },
                { path: '/history_video', component: History_video },
                { path: '/now_video', component: Now_video },
                { path: '/device_manage', component: Device_manage },
                { path: '/device_warn', component: Device_warn },
                { path: '/room1', component: Room1 },
                { path: '/room2', component: Room2 },
                { path: '/room3', component: Room3 },
                { path: '/pet', component: Pet },
                { path: '/plant', component: Plant },
                { path: '/information', component: Information },
                { path: '/person', component: Person }
            ]
        }
    ],
    mode: "history"
})

//挂载路由导航守卫
router.beforeEach((to, form, next) => {
    //to 将要访问的路径
    //from 代表从哪个路径跳转而来
    //next 是一个函数，表示放行
    //next() 放行 next('/login') 强制跳转

    if (to.path === '/login') return next()
    //获取token
    const tokenStr = window.sessionStorage.getItem('token')
    if (!tokenStr) return next('/login')
    next()
})

export default router

import axios from 'axios'
import {
    Message,
    Loading
} from 'element-ui'
import router from './router'

let loading //定义变量loading


function startLoading() { //使用方法  Element  loading-start
    loading = Loading.service({
        lock: true,
        text: '加载中...',
        background: 'ragb(0,0,0,0.4)'
    })
}

function endLoading() { // 使用方法  Element loading-close
    loading.close()
}


// 请求拦截  设置统一header
axios.interceptors.request.use(config => {
    startLoading() //加载
    if (localStorage.eleToken)
        config.headers.Authorization = localStorage.eleToken
    return config
}, error => {
    return Promise.reject(error)
})

//响应拦截  401 token 过期处理
axios.interceptors.response.use(response => {
    endLoading()
    return response
}, error => {
    endLoading()
    Message.error(error.response.data) //错误提示
    const {
        status
    } = error.response
    if (status == 401) {
        Message.error('token值无效，请重新登录')
        localStorage.removeItem('eleToken')
        router.push('/login')
    }
    return Promise.reject(error)
})



export default axios
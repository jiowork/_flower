import axios from 'axios'
import router from './router'

//请求拦截
axios.interceptors.request.use(config => {
    if (localStorage.wxToken)
        config.headers.Authorization = localStorage.wxToken
    return config
}, error => {
    return Promise.reject(error)
})


//响应拦截
axios.interceptors.response.use(response => {
    return response
}, error => {
    const {
        status
    } = error.response
    if (status == 401) {
        alert('token值无效，请重新登录')
        localStorage.removeItem("wxToken")
        router.push('/login')
    } else
        alert(error.response.data)
    return Promise.reject(error)
})

export default axios
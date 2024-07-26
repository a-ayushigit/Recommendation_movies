import axios from 'axios'
import { ACCESS_TOKEN } from './constants'

const api = axios.create({
    baseURL:import.meta.env.VITE_API_URL
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        console.log("token" , token);
        if(token){
            config.headers.Authorization = `Bearer ${token}`
            config.headers['Content-Type'] = 'application/json'
        }
        console.log("config ",config);
        return config 
    },
    (error) =>{
        return Promise.reject(error)
    }

)

export default api ;
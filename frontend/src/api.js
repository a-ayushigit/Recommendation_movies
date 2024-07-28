import axios from 'axios'
import {  ACCESS_TOKEN } from '../src/constants/constants'
const api = axios.create({
    baseURL:import.meta.env.VITE_API_URL
    
})

api.interceptors.request.use((config)=> {
    const token = localStorage.getItem(ACCESS_TOKEN);
    console.log(token)
    if(token){
        config.headers.Authorization = `Bearer ${token}`
        config.headers['Content-Type'] = 'application/json'
    }
    //console.log(typeof(baseUrl))
    console.log(config)
    //console.log(VITE_API_URL)
    return config;
}, 
(error) => {
    return Promise.reject(error);
}
)

export default api;
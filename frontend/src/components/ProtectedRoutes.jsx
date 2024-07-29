import { useState, useEffect } from "react";
import {jwtDecode} from 'jwt-decode'
import api from '../api'
import { ACCESS_TOKEN , REFRESH_TOKEN  } from '../constants/constants'
import { Navigate } from 'react-router-dom';
//We are trying to ascertain that the user visiting the route is authorized or not , first the auth function tries to get access to the access token , if token is not present , it returns , but if token present , it is decoded and we check if it is expired or not , if expired then generate new refresh token which genrates new access token , isAuthorized maintains the state of the user 

function ProtectedRoutes({children}){
   const [isAuthorized , setIsAuthorized] = useState(null);
   useEffect(()=>{


    const refreshToken = async() => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
       try{
        const res = await api.post('/api/token/refresh', {refresh : refreshToken});
        if(res.status === 200){
            localStorage.setItem(ACCESS_TOKEN, res.data.access);
            setIsAuthorized(true);
        }
        else{
            setIsAuthorized(false);
    
        }
    
       }
       catch(error){
        console.log(error);
        setIsAuthorized(false);
       }
    
    }

    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if(!token){
            setIsAuthorized(false);
            return;
        }
        const decoded = jwtDecode(token);
        const tokenExp = decoded.exp;
        const now = Date.now()/1000; //in sec
        if(tokenExp < now){
            await refreshToken();
        }
        else {
            setIsAuthorized(true);
        }
    
        if(isAuthorized === null) return <>Loading....</>
        return isAuthorized? children : <Navigate to ='/login'/>
    }
     
    auth().catch((error)=> {
        setIsAuthorized(false);
        console.log(false);

    })
        
    
   })
}





export default ProtectedRoutes;


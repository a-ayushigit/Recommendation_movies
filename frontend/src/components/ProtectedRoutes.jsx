import { useState, useEffect } from "react";
import {jwtDecode} from 'jwt-decode'
import api from '../api'

import { Navigate } from 'react-router-dom';
//We are trying to ascertain that the user visiting the route is authorized or not , first the auth function tries to get access to the access token , if token is not present , it returns , but if token present , it is decoded and we check if it is expired or not , if expired then generate new refresh token which genrates new access token , isAuthorized maintains the state of the user 

function ProtectedRoutes({children}){
   const [isAuthorized , setIsAuthorized] = useState(null);
//    console.log({children});
   useEffect(()=>{

    const refreshToken = async() => {
        const refreshToken = localStorage.getItem(import.meta.env.VITE_REFRESH_TOKEN);
       try{
        const res = await api.post('/api/token/refresh', {refresh : refreshToken});
        
        
        if(res.status === 200){
            localStorage.setItem(import.meta.env.VITE_ACCESS_TOKEN, res.data.access);
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
        const token = localStorage.getItem(import.meta.env.VITE_ACCESS_TOKEN);
        // console.log(token);
        if(!token){
            setIsAuthorized(false);
            console.log("hello !!!")
            return;
        }
        const decoded = jwtDecode(token);
        const tokenExp = decoded.exp;
        const now = Date.now()/1000; //in sec
        if(tokenExp < now){
            await refreshToken();
            console.log("anika");
        }
        else {
            setIsAuthorized(true);
            console.log("ankita");
        }
    
      
    }
     
    auth().catch((error)=> {
        setIsAuthorized(false);
        console.log(false);

    })
        
    
   }, []);
//earlier I was rendering the below code before calling the auth function hence no authorization was taking place and the components were getting rendered beforehand only .

   if (isAuthorized === null) {
    console.log("Authorization check in progress...");
    return <div>Loading...</div>;
     }

console.log("Authorization status:", isAuthorized);
console.log(children);
if(isAuthorized) return children 
else  {<Navigate to ='/login'/>}
}
 





export default ProtectedRoutes;


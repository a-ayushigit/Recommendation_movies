import React from 'react'
import { useState } from 'react'
import api from '../api'
import { useNavigate } from 'react-router-dom'



const Form = ({route , method }) => {
    const [username , setUsername] = useState("")
    const [password , setPassword] = useState("")
    const [loading , setLoading] = useState(false)
    const navigate = useNavigate()

    const handleSubmit = async(e) =>{
        setLoading(true);
        e.preventDefault();
        try {
          const res = await api.post(route , {username , password});
          if(method === 'login'){
            localStorage.setItem(import.meta.env.ACCESS_TOKEN , res.data.access);
            localStorage.setItem(import.meta.env.REFRESH_TOKEN , res.data.refresh);
            navigate('/');
          }
          else{
            navigate('/login');
          }
        } catch (error) {
          alert(error);
        }finally{
          setLoading(false);
        }
    }
    
    const name = method === 'login' ? "Login" : "Register";
  return (
    <>
    
    <form onSubmit={handleSubmit}>
      <h1>{name}</h1>
      <input 
      type='text'
      value={username}
      onChange={(e)=> setUsername(e.target.value)}
      placeholder='Username'
      />
      <input
        type='password'
        value={password}
        onChange={(e)=> setPassword(e.target.value)}
        placeholder='password'
      
      />

      <button type="submit">{name}</button>
    </form>
    </>
  )
}

export default Form

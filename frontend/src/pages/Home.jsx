import React from 'react'
import api from '../api'
import { useState } from 'react'
const Home = () => {
  const [movie , setMovie]  = useState('movie')
  
  const handleSubmit = async  (e) =>{
     e.preventDefault();
    const route = '/movies/rec_movies_list/'
    try {
      await api.get(route , { params: { movie } }).then((response)=>{
        console.log(response.json);
        console.log(movie)
        console.log(typeof(movie))
        console.log(response.data)
        
      }).catch((error)=>{
         console.log(error)
      })
  
    } catch (error) {
      console.log(error)
    }
   
  }
  return (
    <div className="bg-slate-300">
      Home 
      <form onSubmit={handleSubmit}>
      <input value={movie}  placeholder="movie"  onChange={ev => setMovie(ev.target.value)} />
      <button type='submit' >Submit</button>
      </form>
       
      
    </div>
  )
}

export default Home

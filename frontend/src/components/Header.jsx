import React from 'react'
import {navOptions} from '../constants/constants'
import { Link } from 'react-router-dom'
const Header = () => {
  return (
    <div className="bg-blue-300 flex flex-row gap-3 justify-center items-center text-xl">
      {navOptions.map((element , i)=>(
        <div key={i} className="text-pretty font-light text-cyan-950 hover:bg-orange-300 hover:text-yellow-950 p-1 rounded-lg flex justify-around">
         <Link to={`${element.link}`}><p>{element.name}</p></Link> 
        </div>
      ))}
    </div>
  )
}

export default Header

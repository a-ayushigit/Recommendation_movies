import React, { useState, useContext } from 'react'
import { Link } from 'react-router-dom'
import { ChoiceContext } from '../context/ChoiceContext'
import api from '../api';
import { locationImg } from '../constants/constants';
import moviebg2 from '../assets/images/movieBackground2.jpg'
import useNavigationHandler from '../hooks/useNavigationHandler';
const SelectLocation = () => {
  const [location, setLocation] = useState(null);
  const [date, setDate] = useState("");

  const choice = useContext(ChoiceContext);
  const handleNavigation = useNavigationHandler(choice.choice.location);
  return (
    <div  className="h-full bg-cover bg-center  bg-inherit w-full overflow-hidden max-w-screen flex flex-col " style={{ backgroundImage: `url(${moviebg2})` }}>
      <div className="h-full relative">
      <div className="absolute inset-0  bg-black bg-opacity-75"></div>
      <p className="px-40 text-white flex relative flex-row justify-center items-center font-semibold capitalize ">Select the location of your choice </p>
      </div>
      
    
      <div className="h-full min-h-[150vh] gap-1 py-5 w-screen grid grid-cols-6 px-40 relative">
      <div className="absolute inset-0  bg-black bg-opacity-75"></div>
        {locationImg.map((locationplace, i) => (
          <div key={i} className={`flex ${location === i ? "border-4 border-green-900 bg-green-300 " : "border-4 border-transparent"} col-span-6 sm:col-span-3 md:col-span-2 items-center justify-center relative`}>

            <div className="rounded-full  h-40 w-40 bg-cover bg-center flex items-center justify-center hover:shadow-md hover:scale-95 hover:border-4 hover:border-teal-100" style={{ backgroundImage: `url(${locationplace.link})` }}>


              <p className="relative flex z-50 items-center cursor-pointer hover:opacity-100 opacity-0 justify-center hover:relative bg-white rounded-xl p-4" onClick={() => {
                setLocation(i);
                choice.addLocation(locationplace.name);
                // console.log(location);
                console.log(choice.choice.location);
              }}>{locationplace.name}</p>

            </div>
          </div>
        ))}

        
      </div>
      <div className="flex flex-col h-full min-h-[50vh] w-full min-w-screen px-40 relative">
      <div className="absolute inset-0  bg-black bg-opacity-75"></div>
        <div className=" px-40 rounded-lg relative">
        <p className="px-40 text-white flex flex-row justify-center items-center font-semibold capitalize  ">
            Choose a date for your show 
          </p>
          <div className="flex flex-row justify-center items-center  ">
          <input type="date" value={date} onChange={(e)=>{
            setDate(e.target.value);
            choice.addDate(e.target.value);
            
            }} className="flex rounded-md p-5 items-center justify-center"/>

          </div>
          <p className="flex flex-row justify-center items-center text-white p-5  ">
            Your selected date is {date}
          </p>
        </div>
        <div className="px-40 flex flex-row justify-around py-2 relative">
       <button className="bg-lime-500 p-5 rounded-md text-cyan-900 font-semibold border-2 border-blue-950" onClick={()=>handleNavigation("/booking/movies")}>
       Select Movie
       </button>
       <button className="bg-lime-500 p-5 rounded-md text-cyan-900 font-semibold border-2 border-blue-950" >
      <Link to="/booking">Return to booking page</Link>
       </button>
       <button className="bg-lime-500 p-5 rounded-md text-cyan-900 font-semibold border-2 border-blue-950" onClick={()=>handleNavigation("/booking/shows")}>
       Select Shows
       </button>
        </div>
         
        </div>


    </div>
  )
}

export default SelectLocation

import React from 'react'
import {Link} from 'react-router-dom'
import {imgList} from '../constants/constants'
import moviebg from '../assets/images/movieBackground.jpg'
import moviebg2 from '../assets/images/movieBackground2.jpg'
const BookingSubsection = () => {
    return (

        <div className="h-full bg-cover bg-center  bg-inherit w-full max-w-screen flex flex-col " style={{ backgroundImage: `url(${moviebg2})` }}>

          
            <div className="bg-cover relative bg-center h-full p-1" >
            <div className="absolute inset-0  bg-white bg-opacity-75"></div>
                
            <div className="grid grid-cols-12 px-40 gap-2 relative">
                {imgList.map((img,i)=>(
                    <div key={i} className="flex hover:scale-95 col-span-2 justify-center  border-8 border-yellow-300 rounded-lg">
                    <img src={img.link} />
                </div> 
                ))}
                
            </div>
            </div>

          

            <div className="bg-cover relative bg-center h-96 flex items-center justify-center" style={{ backgroundImage: `url(${moviebg})` }}>
            <div className="absolute inset-0 bg-black bg-opacity-75"></div>
              <div className="z-20 flex rounded-xl items-center relative inset-0 justify-center   flex-col gap-7">
              <div className="relative text-white text-xl ">
                <p><b>Cherish this journey !!!</b></p>
                <p> Book your seats <b>NOW</b> </p>
              </div>
              <div className="hover:scale-95 cursor-pointer ">
              <Link className="bg-yellow-200 rounded-lg p-5 text-3xl opacity-75" to="/booking/location">Choose your location </Link>
              </div>
              
              </div>
            </div>

        </div>

    )
}

export default BookingSubsection

import React from 'react'
import SelectLocation from './SelectLocation'
import SelectSeats from './SelectSeats'
import SelectShows from './SelectShows'
import SelectMovies from './SelectMovies'
import MakePayment from './MakePayment'
import BookingContent from './BookingContent'
import {useNavigate, useParams , Link} from 'react-router-dom'
import BookingSubsection from './BookingSubsection'




const Booking = () => {
  const {subpage} = useParams();
  const navigate = useNavigate();
  console.log(subpage)
 
  return (
    <div className="h-full min-h-screen bg-cyan-700 flex-col">
      {/* <nav>
    
      <Link to="/booking/content">Go back </Link>
      
      </nav> */}
    
    <div className={`${subpage === undefined ? "visible" :"hidden"}`}>
      <BookingSubsection/>
    </div>
    
     {subpage ? 
      <div className="h-full min-h-screen p-1">
      {subpage === "content" && <BookingContent/>}
      {subpage === "location" && <SelectLocation/>}
      {subpage === "movies" && <SelectMovies/>}
      {subpage === "shows" && <SelectShows/>}
      {subpage === "seats" && <SelectSeats/>}
      {subpage === "payment" && <MakePayment/>}
    </div>
    :
    null} 
     

    </div>
  )
}

export default Booking

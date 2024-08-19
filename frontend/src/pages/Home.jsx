import React from 'react'
import {Link} from 'react-router-dom'
const Home = () => {
  return (
    <div className="min-h-screen h-full bg-cyan-700 bg-[url('assets/images/background.jpg')] bg-cover flex flex-start p-7">
      <div className="font-serif text-2xl flex items-center justify-center flex-wrap w-[50vw] flex-col">
      <p className="font-light text-white">
      "Discover Your Next Favorite Film — Book Your Seats, Watch, and Enjoy the Magic!"
      </p>
      
       
        <ul>
          <li className="flex flex-col text-green-200 font-sans font-extralight"><span className="flex text-white font-sans font-extrabold">Step 1:</span> "Browse movies at your place " — "Browse our extensive library and find movies that catch your interest."</li>
          <li className="flex flex-col text-green-200 font-sans font-extralight"><span className="flex text-white font-sans font-extrabold">Step 2:</span>  "Select a Showtime" — "Choose your preferred time and location."</li>
          <li className="flex flex-col text-green-200 font-sans font-extralight"><span className="flex text-white font-sans font-extrabold">Step 3:</span>  "Book Your Tickets" — "Reserve your seats and enjoy the show!"</li>
        </ul>
        <Link to="/booking" className="cursor-pointer hover:scale-95 bg-green-700 text-white rounded-lg p-5"> Book Your Seats Now</Link>
      </div>
    </div>
  )
}

export default Home

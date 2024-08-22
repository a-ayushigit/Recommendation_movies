import React from 'react'

const MovieCard = ({item}) => {
  return (
    <div className="bg-green-400 text-white p-5 flex h-auto max-h-screen w-full rounded-lg">
        <ul>
        <li>Movie : {item.theatre_movie.movie.title}</li>
        <li>Date : {item.date}</li>
        <li>Start Time : {item.start_time} </li>
        <li>End Time : {item.end_time} </li>
        <li>Status : {item.status ? "Available" :"Not Available"} </li>
        <li>Address : {item.theatre_movie.theatre.name}, {item.theatre_movie.theatre.address}</li>
        </ul>
      
    </div>
  )
}

export default MovieCard

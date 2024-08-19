import React from 'react'
import {Link} from 'react-router-dom'
const SelectSeats = () => {
  return (
    <div>
      Seats
      <Link to="/booking/payment">Click me </Link>
      <Link to="/booking">Return to booking page</Link>
    </div>
  )
}

export default SelectSeats

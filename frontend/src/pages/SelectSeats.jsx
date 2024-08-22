import React ,  { useEffect , useContext , useState} from 'react'
import { Link } from 'react-router-dom'
import { ChoiceContext } from '../context/ChoiceContext'
import seat from '../assets/images/car.png'
import SeatGrid from '../components/SeatGrid'
const SelectSeats = () => {
  const choice = useContext(ChoiceContext);
  // const [seatArrangement,setSeatArrangement] = useState({});
  // const seatArrangement = choice.choice?.show?.theatre_movie?.movie_hall?.seat_arrangement;
  useEffect(()=>{
    console.log(choice)
     console.log(choice.choice.show?.theatre_movie?.movie_hall?.seat_arrangement);
    //  setSeatArrangement(choice.choice.show.theatre_movie.movie_hall.seat_arrangement);
    //  console.log(seatArrangement);
  },[])
  return (
    <div>
      Seats
     
      {/* <SeatGrid seatPlans={seatArrangement.seat_arrangement.seat_plans}/> */}

      
      <Link to="/booking/payment">Click me </Link>
      <Link to="/booking">Return to booking page</Link>
    </div>
  )
}

export default SelectSeats

import React , {useContext , useState , useEffect} from 'react'
import {Link} from 'react-router-dom'
import {ChoiceContext} from '../context/ChoiceContext'
import api from '../api';


const SelectShows = () => {

  const [data , setData] = useState([])
  const choice = useContext(ChoiceContext);
  const fetchData = async () => {
    const location = choice.choice.location;
    const movie = choice.choice.movie;
    let date = choice.choice.date;
    console.log("date ",date)
 
    console.log(location);
     const route = `/booking/shows//?place=${location ? location : ""}&theatre_movie=${movie ? movie : ""}&date=${date}`;
    const res = await api.get(route);
    setData(res.data);
    console.log(res);
    console.log(typeof(res.data[0].date))
  }
  useEffect(()=>{
    fetchData();
  },[])

  return (
    <div>
      Shows
      <Link to="/booking/seats">Click me </Link>
      <Link to="/booking">Return to booking page</Link>
    </div>
  )
}

export default SelectShows

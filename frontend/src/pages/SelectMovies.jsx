import React , {useEffect , useContext, useState} from 'react'
import {Link} from 'react-router-dom'
import {ChoiceContext} from '../context/ChoiceContext'
import api from '../api';
import PaginatedList from '../components/PaginatedList';
const SelectMovies = () => {

   const [data , setData] = useState([]);
  const choice = useContext(ChoiceContext);
  const fetchData = async () => {
    const location = choice.choice.location;
   
 
    console.log(location);
     const route = `/booking/movies//?place=${location}`;
    const res = await api.get(route);
    setData(res.data);
    console.log(res);
  }
  useEffect(()=>{
    fetchData();
  },[])
  return (
    <div>

      Movies
      <PaginatedList data={data}/>
      <Link to="/booking/shows">Click me </Link>
      <Link to="/booking">Return to booking page</Link>
    </div>
  )
}

export default SelectMovies

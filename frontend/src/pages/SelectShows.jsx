import React , {useContext , useState , useEffect} from 'react'
import {Link} from 'react-router-dom'
import {ChoiceContext} from '../context/ChoiceContext'
import api from '../api';
import MovieCard from '../components/MovieCard'
import useNavigationHandler from '../hooks/useNavigationHandler';
const SelectShows = () => {

  const [data , setData] = useState([])
  const [show, setShow] = useState(null);
  const choice = useContext(ChoiceContext);
  const handleNavigation = useNavigationHandler(choice.choice.show);
  const fetchData = async () => {
    const location = choice.choice.location;
    const movie = choice.choice.movie;
    let date = choice.choice.date;
    console.log("date ",date)
 
    console.log(location);
     const route = `/booking/shows//?place=${location ? location : ""}&theatre_movie=${movie ? movie : ""}&date=${date}`;
    const res = await api.get(route);
    setData(res.data);
    // console.log(res);
    // console.log(data.shows);
    // data && data?.shows?.map((show)=>{
    //   console.log(show)
    // })
 
    // console.log(typeof(res.data.shows[0].date))
  }
  useEffect(()=>{
    fetchData();
  },[])

  return (
    <div>
      
      {data.no_shows_for_selected_date === false ? 
      <div className="flex justify-center items-center font-bold text-blue-950">You have available shows for {choice.choice.date}</div> 
      :<div>
        <p className="flex justify-center items-center font-bold text-blue-950">
        No shows available for  {choice.choice.date}
        </p> 
        <p className="flex justify-center items-center font-bold text-blue-950">
         Check out other available shows !!!
        </p>
        </div>
      }
      <div className="min-h-[90vh] grid grid-cols-12 gap-5">
        {data.shows && data.shows.map((showData,i)=>
          <div onClick={()=>{
            setShow(i);
            choice.addShow(showData);
          }} className={`col-span-12 items-center justify-center md:col-span-4 sm:col-span-6 flex px-3 cursor-pointer object-fit ${show === i ? "border border-blue-950 bg-orange-300 scale-90" : "shadow-md hover:scale-95 "}`}>
            <div className={``}>
            <MovieCard item={showData} />
            </div>
          
          </div>
        )}

      </div>
      <div className="flex flex-row  items-end justify-between p-5">
      <button className="bg-lime-500 p-5 rounded-md text-cyan-900 font-semibold border-2 border-blue-950" >
      <Link to="/booking">Return to booking page</Link>
      </button>
      <button className="bg-lime-500 p-5 rounded-md text-cyan-900 font-semibold border-2 border-blue-950" onClick={()=>handleNavigation("/booking/seats")}>
      <Link to="/booking/seats">Book seats </Link>
      </button>
     
     
      </div>
      

    </div>
  )
}

export default SelectShows

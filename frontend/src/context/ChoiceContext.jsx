import axios from "axios"
import {createContext , useEffect , useState } from "react"


// create a context for choices taken by user 
export const ChoiceContext = createContext({
    choice:{},
    addLocation:()=>{},
    addMovie:()=>{},
    addShow:()=>{},
    addSeat:()=>{},
    addDate:()=>{},
    removeSeat:()=>{},
    removeLocation:()=>{},
    removeMovie:()=>{},
    removeShow:()=>{},
    removeDate:()=>{}


});

export default function ChoiceContextProvider({children}){
    const [choice,setChoice] = useState({});
    useEffect(()=>{
        setChoice({});
    },[])

    function addLocation(location){
        setChoice((prev)=> ({...prev,"location":location}))
    }

    function addMovie(movie){
        setChoice((prev)=> ({...prev,"movie":movie}))
    }
    function addShow(show){
        setChoice((prev)=>({...prev , "show":show}))

    }
    
    function addSeat(seat){
        setChoice((prev)=>({...prev,"seat":seat}))
    }

    function addDate(date){
        setChoice((prev)=>({...prev,"date":date}))
    }

    function removeSeat(seat){
        setChoice((prev)=>{
           const {seat , ...rest} = prev;
           return rest;
        })
    }
    function removeShow(show){
        setChoice((prev)=>{
           const {show , ...rest} = prev;
           return rest;
        })
    }
    function removeMovie(movie){
        setChoice((prev)=>{
           const {movie , ...rest} = prev;
           return rest;
        })
    }
    function removeDate(date){
        setChoice((prev)=>{
           const {date , ...rest} = prev;
           return rest;
        })
    }
    function removeLocation(location){
        setChoice((prev)=>{
           const {location , ...rest} = prev;
           return rest;
        })
    }
    
    const contextValue = {
        choice,
        addLocation,
        addMovie,
        addShow,
        addSeat,
        addDate,
        removeSeat,
        removeLocation,
        removeMovie,
        removeShow,
        removeDate
    }

    return <ChoiceContext.Provider value = {contextValue}>
        {children}
    </ChoiceContext.Provider>
}
import React, { useEffect , useContext} from 'react'
import { Link } from 'react-router-dom'
import { ChoiceContext } from '../context/ChoiceContext'
const MakePayment = () => {
  const choice = useContext(ChoiceContext);
  useEffect(()=>{
     console.log(choice)
  },[])
  return (
    <div>
      Payment
      <Link to="/booking">Return to booking page</Link>
    </div>
  )
}

export default MakePayment

import React from 'react'
import {useNavigate} from 'react-router-dom'
const useNavigationHandler = (choice) => {
    const navigate = useNavigate();
    const handleNavigation =(path) => {
        if(!choice){
            alert('Please make a selection before proceeding...')
        }
        else{
            navigate(path);
        }
    }
 

  return handleNavigation;
}

export default useNavigationHandler

import React from 'react'
import Header from '../components/Header'
import { Outlet } from 'react-router-dom'
import Footer from '../components/Footer'

const Layout = () => {
  return (
    <div className="flex flex-col ">
        
        <Header className="min-w-h-[500rem] "/>
        <Outlet className="max-h-[300rem] min-w-h-screen max-w-h-screen"/>
        <Footer className="min-w-h-[500rem] "/>
        
    </div>
  )
}

export default Layout

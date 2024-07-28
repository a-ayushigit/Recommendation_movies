import { Route ,  createBrowserRouter , createRoutesFromElements, RouterProvider , Navigate} from 'react-router-dom'
import Login from '../src/pages/Login'

import Register from '../src/pages/Register'
import NotFound from '../src/pages/NotFound'
import Layout from '../src/components/Layout'
import ProtectedRoutes from '../src/components/ProtectedRoutes'
import Home from '../src/pages/Home'


function Logout(){
  localStorage.clear();
  return <Navigate to='/login'/>
}

function RegisterandLogout(){
 localStorage.clear();
 return <Register/>
}

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
    <Route element={<Layout/>}>

    <Route index path="/" element ={<ProtectedRoutes><Home/></ProtectedRoutes>}/>
    <Route path="login" element={<Login/>}/>
    <Route path="logout" element={<Logout/>}/>
    <Route path="register" element={<RegisterandLogout/>}/>
    <Route path="*" element={<NotFound/>}/>
    </Route>
  </Route>
  )
)


function App() {
 

  return (
  <>
  <RouterProvider router={router}/>
 
  </>
  )
}

export default App

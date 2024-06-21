import { Route ,  createBrowserRouter , createRoutesFromElements, RouterProvider , Navigate} from 'react-router-dom'
import Login from './pages/Login';
import Home from './pages/Home';
import Register from './pages/Register';
import NotFound from './pages/NotFound';
import ProtectedRoute from './components/ProtectedRoutes';
import Layout from './components/Layout'


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

    <Route index path="/" element ={<ProtectedRoute><Home/></ProtectedRoute>}/>
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

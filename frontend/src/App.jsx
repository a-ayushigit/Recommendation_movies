import { Route ,  createBrowserRouter , createRoutesFromElements, RouterProvider , Navigate, Outlet} from 'react-router-dom'
import Login from './pages/Login';
import Home from './pages/Home';
import Register from './pages/Register';
import NotFound from './pages/NotFound';
import ProtectedRoutes from './components/ProtectedRoutes';
import Layout from './components/Layout'
import Booking from './pages/Booking';
import About from './pages/About';

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

    <Route index path="/" element ={<Home/>}/>
    <Route path="/about" element={<About/>}/>
    <Route path="/booking" element={<ProtectedRoutes><Booking/></ProtectedRoutes>}/>
    <Route path="/booking/:subpage" element={<ProtectedRoutes><Booking/></ProtectedRoutes>} />
    <Route path="login" element={<Login/>}/>
    <Route path="logout" element={<Logout/>}/>
    <Route path="register" element={<RegisterandLogout/>}/>
    <Route path="*" element={<NotFound/>}/>
    </Route>
  </Route>
  )
)

// const router = createBrowserRouter([
//   {
//     element: <Layout />,
//     children: [
//       {
//         path: "/",
//         element: <Home />,
//       },
//       {
//         path: "/about",
//         element: <About />,
//       },
//       // {
//       //   path:"/booking",
//       //   element:<ProtectedRoutes><Booking/></ProtectedRoutes>
//       // }
//       {
//         path:"/protected",
//         element:<ProtectedRoutes/>,
//         children:[{
//           path:"/protected/booking",
//           element:<Booking/>
//         }]
//       }
     
//     ],
//   },
//   {
//     path: "/login",
//     element: <Login />,
//   },
//   {
//     path: "/logout",
//     element: <Logout />,
//   },
//   {
//     path: "/register",
//     element: <Register />,
//   },
//   {
//     path: "*",
//     element: <NotFound />,
//   },
  
// ]);


function App() {
 

  return (
  <>
  <RouterProvider router={router}/>
 
  </>
  )
}

export default App

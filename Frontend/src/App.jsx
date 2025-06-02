import React from 'react'
import { BrowserRouter ,Route,Routes} from 'react-router-dom'
import UserLayout from './components/Layout/UserLayout.jsx'
// import AdminLayout from './components/Layout/AdminLayout.jsx'

const App = () => {
  return (
    // manages the routing of the application
    <BrowserRouter>
    <Routes>
            <Route path = "/" element = {<UserLayout/>}></Route>
       {/* <Route path = "/admin" element = {AdminLayout}></Route> */}

    </Routes>
    </BrowserRouter>
  )
}


export default App

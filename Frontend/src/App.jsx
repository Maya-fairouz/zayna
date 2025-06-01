import React from 'react'
import { BrowserRouter } from 'react-router-dom'
import UserLayout from './components/Layout/UserLayout.jsx'
// import AdminLayout from './components/Layout/AdminLayout.jsx'

const App = () => {
  return (
    // manages the routing of the application
    <BrowserRouter>
      <Route path = "/" element = {<UserLayout/>}>
      </Route>
      {/* <Route path = "/admin" element = {AdminLayout}></Route> */}
    </BrowserRouter>
  )
}


export default App

import React from 'react'
import { BrowserRouter } from 'react-router-dom'

const App = () => {
  return (
    // manages the routing of the application
    <BrowserRouter>
      <Route>{/*user layout */}</Route>
      <Route>{/*admin layout*/ }</Route>
    </BrowserRouter>
  )
}


export default App

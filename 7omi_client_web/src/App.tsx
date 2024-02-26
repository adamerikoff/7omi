import { BrowserRouter, Route, Routes } from 'react-router-dom';

import './App.css'

import NavbarLayout from './components/navbar/NavbarLayout'
import Home from './components/home/Home'
import Login from './components/login/Login'
import Signup from './components/signup/Signup'
import About from './components/statics/About'
import Contacts from './components/statics/Contacts'

function App() {

  return (
    <BrowserRouter>
      <NavbarLayout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/about" element={<About />} />
          <Route path="/contacts" element={<Contacts />} />
        </Routes>
      </NavbarLayout>
    </BrowserRouter>
  )
}

export default App




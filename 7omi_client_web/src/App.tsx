import { BrowserRouter, Route, Routes } from 'react-router-dom';

import './App.css'

import Navbar from './components/navbar/Navbar'
import Footer from './components/footer/Footer'

import Home from './components/home/Home'

import ChatLayout from './components/chat/ChatLayout'

import Login from './components/login/Login'
import Signup from './components/signup/Signup'

import About from './components/statics/About'
import Contacts from './components/statics/Contacts'
import NotFound from './components/statics/NotFound'

function App() {

  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/about" element={<About />} />
        <Route path="/contacts" element={<Contacts />} />
        <Route path="/chat" element={<ChatLayout />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
      <Footer/>
    </BrowserRouter>
  )
}

export default App




import { BrowserRouter, Route, Routes } from 'react-router-dom'


import Footer from './components/Footer'
import Header from './components/Header'

import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import Chat from './pages/Chat'

import RequireToken from './services/Auth'

import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Header/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/chat" element={<RequireToken> <Chat /> </RequireToken>} />
      </Routes>
      <Footer/>
    </BrowserRouter> 
  )
}

export default App

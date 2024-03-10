import { useState, useEffect } from 'react'
import { Routes, Route } from 'react-router-dom'

import Home from "./pages/Home"
import Register from "./pages/Register"
import Login from "./pages/Login"

import './App.css'

const BASE_URL = 'http://localhost:8000'

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </>
  )
}

export default App

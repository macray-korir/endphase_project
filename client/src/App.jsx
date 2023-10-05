import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Homepage from './Components/homepage';
import Header from './Components/header';
import Contact from './Components/Contact';

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
    <Router>
    <Header/>
    <Routes>
      <Route path="/" element={<Homepage />}/>
      <Route path="/contact" element={<Contact />} />
    </Routes>
    </Router>
    </>
  )
}

export default App

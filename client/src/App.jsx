import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Homepage from './Components/homepage';
import Header from './Components/header';
import Contact from './Components/Contact';
import Meals from './Components/meals';
import Ingredients from './Components/ingredients';
import AddMealForm from './Components/addmeal';
import Login from './Components/login';
// import SignupForm from './Components/signup';


function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
    <Router>
    <Header/>
    <Routes>
      <Route path="/" element={<Login />}/>
      {/* <Route path="/signup" element={<SignupForm />}/> */}
      <Route path="/homepage" element={<Homepage />}/>
      <Route path="/contact" element={<Contact />} />
      <Route path="/meal" element={<Meals />} />
      <Route path="/ingredient" element={<Ingredients />} />
      <Route path="/addmeal" element={<AddMealForm />} />
    </Routes>
    </Router>
    </>
  )
}

export default App

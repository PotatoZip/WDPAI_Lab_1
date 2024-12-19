import './App.css'
// import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import UserList from './components/UserList'
import Home from './components/Home.tsx'
import Navbar from './components/Navbar.tsx'

function App() {
    return (
    // <BrowserRouter>
    //   <nav>
    //     <Link to="/register">Rejestracja</Link> | <Link to="/login">Logowanie</Link> | <Link to="/users">Lista użytkowników</Link>
    //   </nav>
    //   <Routes>
    //     <Route path="/register" element={<Register />} />
    //     <Route path="/login" element={<Login />} />
    //     <Route path="/users" element={<UserList/ >} />
    //   </Routes>
    // </BrowserRouter>
    <BrowserRouter>

      <Navbar/>
      
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/users" element={<UserList/>}/>
      </Routes>

    </BrowserRouter>
  );
}

export default App;
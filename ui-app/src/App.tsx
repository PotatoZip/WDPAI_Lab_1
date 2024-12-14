import './App.css'
// import React from 'react';
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';

function App() {
    return (
    <BrowserRouter>
      <nav>
        <Link to="/register">Rejestracja</Link> | <Link to="/login">Logowanie</Link> | <Link to="/users">Lista użytkowników</Link>
      </nav>
      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
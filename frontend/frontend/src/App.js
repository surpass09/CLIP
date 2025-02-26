import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from '../src/components/login_page/login.jsx';
import LandingPage from './components/landing_page/landing/landing_page.jsx'; // Fix the import path

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<LandingPage />} /> {/* Add a route for the landing page */}
      </Routes>
    </Router>
  );
}

export default App;
// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './HomePage';
import ChatTutor from './chat_Assist1';
import ChatRoleplay from './chat_Assist2';
//since we need a home page and multiple pages to be naviggated when clicked we create routes and one these links we will have the elements associated
//so in homepage jsx file we can use navigate('route path that we created here') will take you to place
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/chat-tutor" element={<ChatTutor />} />
        <Route path="/chat-roleplay" element={<ChatRoleplay />} />
      </Routes>
    </Router>
  );
}

export default App;

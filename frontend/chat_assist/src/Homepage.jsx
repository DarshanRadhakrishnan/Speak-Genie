// src/HomePage.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';
import petAvatar from './assets/pet-avatar.gif'; // Add your animated character here
import clickSound from './assets/click-sound.mp3'; // Add a click sound

function HomePage() {
  const navigate = useNavigate();
  const [language, setLanguage] = useState('en');

  const handleClick = (path) => {
    const audio = new Audio(clickSound);
    audio.play();
    navigate(path);
  };

  return (
    <div className="home-container">
      <h1>✨ Welcome to SpeakGenie! ✨</h1>
      <p>Learn and have fun with our AI voice tutor 🎤</p>

      <img src={petAvatar} alt="Pet Avatar" className="pet-avatar" />

      <div className="points-box">
        <p>🌟 Level: 3</p>
        <p>🎁 Rewards: 2 stars</p>
        <p>🏆 Streak: 5 days!</p>
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: '60%' }}></div>
        </div>
      </div>

      <div className="language-selector">
        <span role="img" aria-label="English" onClick={() => setLanguage('en')}>
          🇺🇸
        </span>
        <span role="img" aria-label="Hindi" onClick={() => setLanguage('hi')}>
          🇮🇳
        </span>
        <span role="img" aria-label="Spanish" onClick={() => setLanguage('es')}>
          🇪🇸
        </span>
      </div>

      <div className="option-buttons">
        <button onClick={() => handleClick('./chat-tutor')}>👩‍🏫 Speak with Tutor</button>
        <button onClick={() => handleClick('/chat-roleplay')}>🎭 Roleplay Session</button>
      </div>
    </div>
  );
}

export default HomePage;

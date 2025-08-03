import React, { useState } from 'react';
import axios from 'axios';
import './chatAssist2.css';

function ChatRoleplay() {
  const [messages, setMessages] = useState([]);
  const [language, setLanguage] = useState('en');
  const [ageGroup, setAgeGroup] = useState('child');
  const [scenario, setScenario] = useState('🏫 At School');
  const [loading, setLoading] = useState(false);

  const handleMicClick = async () => {
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:5000/api/roleplay', {
        language,
        ageGroup,
        scenario,
        history: messages,
      });

      const { question, answer } = res.data;

      setMessages((prev) => [
        ...prev,
        { role: 'user', content: question },
        { role: 'assistant', content: answer },
      ]);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <div className="header">
        <input
          type="text"
          placeholder="Language (e.g., en)"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
        />
        <input
          type="text"
          placeholder="Age Group (e.g., child)"
          value={ageGroup}
          onChange={(e) => setAgeGroup(e.target.value)}
        />
        <input
          type="text"
          placeholder="Scenario (e.g., 🛒 At the Store)"
          value={scenario}
          onChange={(e) => setScenario(e.target.value)}
        />
      </div>

      <div className="chat-box">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`message ${msg.role === 'user' ? 'user' : 'ai'}`}
          >
            {msg.content}
          </div>
        ))}
        {loading && <div className="message ai">🎙️ Listening...</div>}
      </div>

      <div className="mic-container">
        <button className="mic-btn" onClick={handleMicClick} disabled={loading}>
          🎤
        </button>
      </div>
    </div>
  );
}

export default ChatRoleplay;

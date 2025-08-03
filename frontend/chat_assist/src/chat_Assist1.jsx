import React, { useState } from 'react';
import axios from 'axios';
import './chatAssist1.css';

function ChatTutor() {
  const [messages, setMessages] = useState([]); // [{ sender: 'user', text: '...' }, { sender: 'ai', text: '...' }]
  const [loading, setLoading] = useState(false);

  const handleMicClick = async () => {
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:5000/api/ask', {
        language: 'en',
        ageGroup: 'child',
      });

      const { question, answer } = res.data;

      setMessages((prev) => [
        ...prev,
        { sender: 'user', text: question },
        { sender: 'ai', text: answer },
      ]);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="message ai">🎙️ Listening...</div>}
      </div>
      <button className="mic-btn" onClick={handleMicClick} disabled={loading}>
        🎤
      </button>
    </div>
  );
}

export default ChatTutor;

# 🧠 Child-Friendly Voice Tutor using LangChain + RAG + Whisper

This project builds a **smart, interactive, child-friendly AI tutor** that:
- 🎙️ Listens to a child's voice using **Whisper**
- 🤖 Understands and responds using **OpenAI (GPT-3.5)**
- 📚 Retrieves answers from documents using **Multi-Query + Multi-Representation RAG**

---

## 📁 Folder Structure
.
├── main.py / app.py # FastAPI backend entry point
├── final_rag_chain.py # Core LangChain logic: multi-query RAG pipeline
├── data/ # Folder containing PDFs, PPTs, Markdown, and Text files
├── frontend/ # React frontend (optional)
├── requirements.txt # Python dependencies
└── README.md # You're reading it!


---

## 💡 Features

- **Voice-based Input** using Whisper or browser mic
- **Age-appropriate Questions and Answers**
- **Multi-Query Prompting**: Generates 5 alternate versions of the child’s question
- **Multi-Vector Indexing**: Indexes both summaries and original documents for deep retrieval
- **RAG-Powered Answers**: GPT generates child-friendly responses using retrieved documents

---

## 🔧 Tech Stack

| Layer       | Tech                         |
|-------------|------------------------------|
| 🎙️ STT       | Whisper (or browser mic)     |
| 🧠 LLM       | OpenAI GPT-3.5               |
| 🦜 RAG       | LangChain + Chroma           |
| 🚀 Backend   | FastAPI                      |
| ⚛️ Frontend | React                         |

---

## ⚙️ How to Run

### 1. 📄 Prepare Your Docs

Put your educational content in the `data/` folder. Supported formats:
- `.pdf`
- `.pptx`
- `.txt`
- `.md`

### 2. 📦 Install Backend Dependencies

```bash
# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install required libraries
pip install -r requirements.txt

#Start the API
uvicorn main:app --reload

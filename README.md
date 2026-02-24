# ExecutionPlanner
Web app to create and track Your Goals divided into manageable tasks.

# 🚀 Execution Planner – AI-Powered Goal Breakdown & Execution Tracker

A production-style full-stack ML web application that converts high-level goals into structured execution plans using an LLM, and tracks real-world task completion with analytics-ready logs.

Built with:
- 🧠 FastAPI (Backend API)
- 🎨 Streamlit (Frontend UI)
- 🤖 OpenAI LLM (Task Decomposition)
- 🗄 SQLite (Persistent Storage)
- 🔄 RESTful Architecture

---

## 🧩 Problem

Most people set ambitious goals but struggle with:
- Breaking them into actionable steps
- Tracking execution consistency
- Recording problems & insights
- Measuring performance over time

Execution Planner solves this by turning vague goals into structured, trackable execution systems.

---

## 💡 Solution

Users enter a goal →  
The LLM generates small, achievable tasks →  
Tasks are stored in a database →  
Users log:
- ⏱ Time spent
- ⚠ Problems faced
- 💡 Insights gained
- ✅ Completion status

All data is persistent and structured for future analytics.

---

## 🏗 Architecture
Streamlit Frontend
↓
FastAPI Backend
↓
LLM Service Layer
↓
SQLite Database


### Backend
- RESTful API
- Structured Pydantic schemas
- SQLAlchemy ORM
- LLM JSON output enforcement

### Frontend
- Clean execution UI
- Goal creation
- Task completion logging
- Real-time API interaction

---

## 📁 Project Structure
execution_planner/
│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── llm_service.py
│ └── requirements.txt
│
├── frontend/
│ ├── app.py
│ └── requirements.txt
│
└── README.md
└── LICENSE
└── gitignore

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone Repository

git clone <your-repo-url>
cd execution_planner

---

### 2️⃣ Backend Setup

cd backend
pip install -r requirements.txt

Create `.env` file:
OPENAI_API_KEY=your_api_key_here

Run backend:
uvicorn main:app --reload

Visit API docs:
http://127.0.0.1:8000/docs

---

### 3️⃣ Frontend Setup

Open new terminal:

cd frontend
pip install -r requirements.txt
streamlit run app.py


App will open in your browser.

---

## 🔍 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /goals | Create goal & auto-generate tasks |
| GET | /goals | Fetch all goals |
| PUT | /tasks/{id} | Mark task complete & log execution |

---

## 📊 Features

- ✅ LLM-based structured task generation
- 🗄 Persistent database storage
- ⏱ Time tracking per task
- ⚠ Problem logging
- 💡 Insight capture
- 🔁 Status updates
- 📘 Interactive API documentation
- 🧱 Clean separation of concerns
- 🚀 Production-style backend architecture

---

## 🧠 Technical Highlights

- Enforced JSON schema from LLM responses
- ORM-based DB layer
- Modular backend structure
- Clean service-layer separation
- Scalable design (ready for PostgreSQL / auth / Docker)

---

## 🔒 Assumptions

- Single-user local testing version
- SQLite for simplicity
- LLM availability via OpenAI API

---

## ⚠ Limitations

- No authentication (extendable)
- No background task queue
- No analytics scoring engine yet
- No deployment configuration included

---

## 🚀 Future Improvements

- JWT authentication
- Multi-user support
- Execution analytics dashboard
- Goal versioning
- Docker deployment
- Cloud hosting
- Rate limiting & caching
- Weekly performance summaries

---

## 🎯 Why This Project Matters

This project demonstrates:

- Full-stack ML system design
- LLM integration with structured outputs
- REST API development
- Database modeling
- Clean software architecture
- Real-world execution tracking system

It moves beyond “model training” and into **production-oriented ML system building**.

---

## 📽 Suggested Demo Flow

1. Create goal
2. Show LLM task breakdown
3. Complete task
4. Log insights
5. Show API docs
6. Explain architecture

---

## 🏁 Author

Built as a portfolio-grade ML systems project demonstrating end-to-end architecture, automation mindset, and scalable backend design.

---

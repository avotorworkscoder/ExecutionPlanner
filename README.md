<h1 align="center">
  🚀 Execution Planner
</h1>

<p align="center">
  <strong>An AI-Powered Goal Breakdown & Execution Tracker</strong><br>
  Turn high-level, vague goals into actionable, trackable micro-steps using Generative AI.
</p>

<p align="center">
  <!-- Place your badges here. Example: -->
  <!-- <img alt="License" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg"> -->
  <!-- <img alt="Python Version" src="https://img.shields.io/badge/Python-3.9%2B-blue"> -->
</p>

---

## 📖 Table of Contents
1. [Introduction](#1-introduction)
2. [Features](#2-features)
3. [Installation](#3-installation)
4. [Codebase Guide](#4-codebase-guide)
5. [Collaboration Guide](#5-collaboration-guide)
6. [Future Roadmap](#6-future-roadmap)
7. [Contact Us](#7-contact-us)

---

## 1. Introduction

Most people set ambitious goals but struggle with execution. **Execution Planner** is a production-grade full-stack Machine Learning web application designed to solve this by turning vague aspirations into structured execution systems.

By leveraging an LLM (Large Language Model), it automatically decomposes large tasks into 5-15 manageable tasks, and further breaks those down into 3-5 distinct micro-steps. It also seamlessly tracks your time spent, problems faced, insights gained, and completion status—providing structured data for future behavioral analytics.

<!-- Add a screenshot or demo GIF here -->
<!-- Example: `![Execution Planner Demo](./assets/demo.gif)` -->

---

## 2. Features

- **🧠 AI-Powered Breakdown:** Generates structured tasks and micro-subtasks using advanced LLMs (Gemma, Gemini).
- **🗄 Persistent Storage:** Reliable tracking via a dedicated SQLite database using SQLAlchemy ORM.
- **⏱ Time & Insight Tracking:** Log time spent (in minutes), blockers, and personal insights per task.
- **🎨 Interactive UI:** Clean, intuitive Streamlit-based frontend for goal management.
- **⚙️ RESTful API:** Robust FastAPI backend enforcing strict JSON responses from the LLM.

---

## 3. Installation

Follow these steps to set up the project locally on your machine.

### Prerequisites
- Python 3.9+ installed
- [Git](https://git-scm.com/) installed
- API Key (e.g., Gemini API Key from Google AI Studio)

### Step 1: Clone the Repository
```bash
git clone <YOUR-REPO-URL-HERE>
cd execution_planner
```

### Step 2: Set up the Backend (FastAPI)
Open a terminal and navigate to the backend directory:
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your API key
# Example content for .env:
# GEMINI_API_KEY="your_actual_api_key_here"
```

Start the FastAPI local server:
```bash
uvicorn main:app --reload
```
*The API will be available at `http://127.0.0.1:8000`. You can visit `http://127.0.0.1:8000/docs` to view the interactive Swagger API documentation.*

### Step 3: Set up the Frontend (Streamlit)
Open a *new* terminal window and navigate to the frontend directory:
```bash
cd frontend

# Install dependencies (if not already done globally)
pip install -r requirements.txt

# Run the Streamlit UI
streamlit run app.py
```
*The Streamlit web app will open automatically in your browser (usually at `http://localhost:8501`).*

---

## 4. Codebase Guide

The project strictly follows a decoupled client-server architecture. Here is a high-level overview of the most critical files to help you navigate:

```text
execution_planner/
│
├── backend/                  # ⚙️ Python FastAPI Backend Service
│ ├── main.py               # The core API entry point and route definitions.
│ ├── database.py           # Database engine & session configurations.
│ ├── models.py             # SQLAlchemy ORM models (Goal, Task, SubTask).
│ ├── schemas.py            # Pydantic schemas for data validation and serialization.
│ ├── llm_service.py        # Abstracted LLM communication (OpenAI client configured for Gemini/Gemma).
│ └── requirements.txt      # Backend Python dependencies.
│
├── frontend/                 # 🎨 Python Streamlit Frontend Client
│ ├── app.py                # Main user interface, state management, and API caller.
│ └── requirements.txt      # Frontend Python dependencies.
│
├── LICENSE                   # Apache 2.0 Open Source License
└── README.md                 # You are reading this!
```

### Key Technical Patterns
- **Database Modeling:** We use `SQLAlchemy` for handling one-to-many relationships (Goals -> Tasks -> Subtasks).
- **Data Serialization:** `Pydantic` models (`schemas.py`) define exactly what data is expected in requests and responses.
- **LLM Prompting Structure:** Due to limitations in certain models (like Gemma), the `system` prompt roles and strict JSON formatting options have been creatively adapted directly into the `user` prompts to maintain high reliability (`llm_service.py`).

---

## 5. Collaboration Guide

We welcome contributions of all kinds: bug reports, feature suggestions, or pull requests! To ensure a smooth collaborative environment, please follow these guidelines:

### How to Contribute
1. **Fork the Repository:** Create your own fork on GitHub.
2. **Clone the Fork locally:** Pull the code to your machine.
3. **Create a Feature Branch:** Always branch off `main` for your work.
   ```bash
   git checkout -b feature/your-awesome-feature
   ```
4. **Follow Coding Standards:**
   - Keep functions modular and clearly documented.
   - Separate API logic (backend) from UI logic (frontend).
   - Test your changes locally to ensure `uvicorn` and `streamlit` boot without errors.
5. **Commit Meaningfully:** Write clear, concise commit messages.
6. **Submit a Pull Request (PR):** Push your branch up and open a PR directed at our `main` branch. Provide a detailed explanation of your changes.

### Reporting Bugs
If you find a bug, please create an Issue and include:
- A descriptive title.
- Steps to reproduce the bug.
- The expected vs. actual behavior.

---

## 6. Future Roadmap

- [ ] Implement robust User Authentication (JWT).
- [ ] Add Multi-user support with isolated databases.
- [ ] Build a comprehensive execution analytics dashboard.
- [ ] Dockerize the application for easier deployment.
- [ ] Integration with background task queues (Celery/Redis) for asynchronous processing.

---

## 7. Contact Us

We are excited about the future of **Execution Planner**! If you have any questions, feedback, or want to reach out for a collaboration:

- **Lead Developer/Maintainer:** [Your Name / Alias]
- **Email:** [Your Email Address]
- **LinkedIn:** [Link to your Profile]
- **Twitter / X:** [@YourHandle](https://twitter.com/)
- **Project Link:** [Insert URL if hosted or GitHub URL]

---

<p align="center">
  <i>Built with ❤️ as a portfolio-grade ML Systems Project.</i>
</p>

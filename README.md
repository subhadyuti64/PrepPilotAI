# 🚀 PrepPilot AI

PrepPilot AI is an end-to-end AI-powered interview preparation platform that helps candidates analyze resumes, generate personalized interview questions, practice mock interviews, and receive detailed performance feedback using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

---
# 🚀 Live Demo

Frontend
https://preppilotai-j5b5us3tynu4kzhddrenwr.streamlit.app/
Backend API
https://preppilotai.onrender.com

## 🌟 Features

### 📄 Resume Analysis

* Extracts technical skills, projects, and education details.
* Identifies strengths and areas for improvement.
* Suggests suitable job roles based on resume content.

### 💬 Resume Chat (RAG)

* Chat with your resume using natural language.
* Ask questions about skills, projects, experiences, and achievements.
* Powered by FAISS vector search and OpenAI.

### ❓ Personalized Question Generator

* Generates interview questions based on:

  * Resume content
  * Skills
  * Selected domain
* Covers beginner, intermediate, and advanced levels.

### 🎤 AI Mock Interview

* Generates personalized interview questions.
* Evaluates candidate responses.
* Provides detailed feedback and follow-up questions.

### 📊 Performance Analytics

* Tracks interview scores over time.
* Displays performance trends.
* Highlights strengths and improvement areas.

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### AI & LLMs

* OpenAI GPT Models
* LangChain

### RAG Pipeline

* FAISS Vector Database
* OpenAI Embeddings
* PDF Processing

### Data Processing

* PyPDF
* Python

---

## 🏗 Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Resume Upload
 │
 ├── Resume Analysis
 │
 ├── Resume Chat (RAG)
 │
 ├── Question Generation
 │
 └── Mock Interview Evaluation
 │
 ▼
OpenAI GPT Models
 │
 ▼
FAISS Vector Store
```

---

## 🚀 Key Capabilities

### Resume Upload & Processing

* Upload PDF resumes.
* Automatically extracts and indexes content.
* Creates user-specific FAISS vector stores.

### Intelligent Resume Analysis

* Candidate overview
* Skills extraction
* Project identification
* Recommended job roles
* Improvement suggestions

### Retrieval-Augmented Resume Chat

Ask questions like:

```text
What skills are mentioned in my resume?

What projects have I worked on?

Summarize my profile.

Which technologies am I strongest in?
```

### AI-Powered Interview Preparation

Generate personalized questions for:

* Python
* Machine Learning
* Data Structures
* Algorithms
* DBMS
* Operating Systems
* Computer Networks
* OOP
* SQL
* FastAPI

### Mock Interview Evaluation

Provides:

* Overall score
* Technical accuracy
* Completeness
* Depth of understanding
* Communication score
* Missing concepts
* Ideal answer
* Follow-up questions

---

## 📂 Project Structure

```text
PrepPilot/
│
├── app/
│   ├── models/
│   │   ├── session_model.py
│   │   ├── query_model.py
│   │   ├── question_model.py
│   │   └── interview_model.py
│   │
│   ├── routes/
│   │   ├── resume_routes.py
│   │   ├── analysis_routes.py
│   │   ├── chat_routes.py
│   │   ├── question_routes.py
│   │   └── interview_routes.py
│   │
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── vector_service.py
│   │   ├── rag_service.py
│   │   ├── resume_analysis_service.py
│   │   ├── question_generator_service.py
│   │   └── interview_service.py
│   │
│   ├── utils/
│   │   └── config.py
│   │
│   └── main.py
│
├── frontend/
│   ├── Home.py
│   │
│   ├── pages/
│   │   ├── Dashboard.py
│   │   ├── Resume_Analysis.py
│   │   ├── Resume_Chat.py
│   │   ├── Question_Generator.py
│   │   ├── Mock_Interview.py
│   │   └── Performance_Report.py
│   │
│   └── utils/
│       ├── api.py
│       └── styles.py
│
├── requirements.txt
├── .env
└── README.md
```

## Author - Subhadyuti Rath

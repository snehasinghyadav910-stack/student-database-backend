# Student Database Application System – Backend

A modular backend application for managing student information using FastAPI, SQLModel, SQLite, Gemini API, LangGraph, and ChromaDB.

## Features

- Student CRUD operations
- Student search
- Input validation
- Error handling
- FastAPI REST APIs
- Swagger/OpenAPI documentation
- SQLite database
- Gemini API integration
- LangGraph chatbot
- ChromaDB vector database
- Automated API testing with Pytest
- Environment variable based API key management

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Google Gemini API
- LangGraph
- ChromaDB
- Pytest
- Uvicorn

## Project Structure

```text
student-database-backend/
│
├── app/
│   ├── api/
│   │   ├── students.py
│   │   └── chat.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── crud/
│   │   └── student.py
│   │
│   ├── db/
│   │   └── session.py
│   │
│   ├── models/
│   │   └── student.py
│   │
│   ├── schemas/
│   │   └── student.py
│   │
│   └── services/
│       ├── gemini.py
│       ├── chatbot.py
│       └── vector_db.py
│
├── tests/
│   └── test_students.py
│
├── main.py
├── .env
├── .gitignore
└── README.md

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

## Vector Database Selection

ChromaDB was selected as the vector database for this project because it provides simple Python integration, built-in similarity search, and works well with LangGraph and the Gemini-powered chatbot.

### Selection Criteria

- **Integration:** Easy integration with Python and ChromaDB client.
- **Similarity Search:** Supports semantic similarity search for retrieving relevant student information.
- **Scalability:** Suitable for the small-scale student database used in this project.
- **Complexity:** Simple to set up and maintain compared with managed vector database services.
- **Cost:** Open-source and suitable for development without additional database charges.
- **Compatibility:** Works well with the Python, LangGraph, and Gemini-based architecture.

For a larger production system, a managed vector database could be considered depending on scalability and infrastructure requirements.

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
├── .gitignore
└── README.md

from fastapi import FastAPI

from app.api.students import router as students_router
from app.api.chat import router as chat_router
from app.db.session import create_db_and_tables


app = FastAPI(
    title="Student Database Backend",
    description="Backend API for Student Database Application",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(students_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {"message": "Student Database Backend is running!"}
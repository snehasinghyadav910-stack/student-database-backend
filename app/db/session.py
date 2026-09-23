from sqlmodel import SQLModel, Session, create_engine

from app.models.student import Student


DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
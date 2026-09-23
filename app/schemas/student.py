from pydantic import EmailStr, Field
from sqlmodel import SQLModel


class StudentCreate(SQLModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=1, le=100)
    course: str = Field(min_length=2, max_length=100)
    year: int = Field(ge=1, le=5)


class StudentRead(SQLModel):
    id: int
    name: str
    email: EmailStr
    age: int
    course: str
    year: int


class ValidationError(SQLModel):
    detail: str
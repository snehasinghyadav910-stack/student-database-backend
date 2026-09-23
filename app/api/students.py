from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud.student import (
    create_student,
    get_student,
    get_students,
    update_student,
    delete_student,
    search_students,
)
from app.schemas.student import StudentCreate, StudentRead
from app.db.session import get_session


router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=StudentRead)
def create_student_api(
    student: StudentCreate,
    session: Session = Depends(get_session),
):
    return create_student(session, student)


@router.get("/", response_model=list[StudentRead])
def get_students_api(
    session: Session = Depends(get_session),
):
    return get_students(session)

@router.get("/search/", response_model=list[StudentRead])
def search_students_api(
    keyword: str,
    session: Session = Depends(get_session),
):
    return search_students(session, keyword)


@router.get("/{student_id}", response_model=StudentRead)
def get_student_api(
    student_id: int,
    session: Session = Depends(get_session),
):
    student = get_student(session, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return student


@router.put("/{student_id}", response_model=StudentRead)
def update_student_api(
    student_id: int,
    student_data: StudentCreate,
    session: Session = Depends(get_session),
):
    student = get_student(session, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return update_student(session, student, student_data)


@router.delete("/{student_id}")
def delete_student_api(
    student_id: int,
    session: Session = Depends(get_session),
):
    student = get_student(session, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    delete_student(session, student)

    return {"message": "Student deleted successfully"}


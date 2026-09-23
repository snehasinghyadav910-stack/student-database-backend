from sqlmodel import Session, select

from app.models.student import Student
from app.schemas.student import StudentCreate


def create_student(session: Session, student_data: StudentCreate):
    student = Student.model_validate(student_data)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


def get_students(session: Session):
    statement = select(Student)
    return session.exec(statement).all()


def get_student(session: Session, student_id: int):
    return session.get(Student, student_id)


def update_student(
    session: Session,
    student: Student,
    student_data: StudentCreate
):
    student.name = student_data.name
    student.email = student_data.email
    student.age = student_data.age
    student.course = student_data.course
    student.year = student_data.year

    session.add(student)
    session.commit()
    session.refresh(student)
    return student


def delete_student(session: Session, student: Student):
    session.delete(student)
    session.commit()

def search_students(session: Session, keyword: str):
    statement = select(Student).where(
        Student.name.contains(keyword)
    )

    return session.exec(statement).all()

def search_students_by_name(session: Session, name: str):
    statement = select(Student).where(Student.name.contains(name))
    return session.exec(statement).all()
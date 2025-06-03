from sqlalchemy.orm import Session
from sqlalchemy import Numeric, cast, func, desc
from database.models import Student, Group, Subject, Grade

avg_grade = func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg_grade")


# 1. 5 студентів із найбільшим середнім балом з усіх предметів
def select_1(session: Session):
    return (
        session.query(
            Student.first_name,
            Student.last_name,
            avg_grade,
        )
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc(avg_grade))
        .limit(5)
        .all()
    )


# 2. Студент із найвищим середнім балом з певного предмета
def select_2(session: Session, subject_id: int):
    return (
        session.query(
            Student.first_name,
            Student.last_name,
            avg_grade,
        )
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc(avg_grade))
        .first()
    )


# 3. Середній бал у групах з певного предмета
def select_3(session: Session, subject_id: int):
    return (
        session.query(
            Group.name,
            func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student, Student.id == Grade.student_id)
        .join(Group, Group.id == Student.group_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.name)
        .all()
    )


# 4. Середній бал на потоці (по всій таблиці оцінок)
def select_4(session: Session):
    return session.query(func.round(cast(func.avg(Grade.grade), Numeric), 2)).scalar()


# 5. Які курси читає певний викладач
def select_5(session: Session, teacher_id: int):
    return (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .order_by(Subject.name)
        .all()
    )


# 6. Список студентів у певній групі
def select_6(session: Session, group_id: int):
    return (
        session.query(Student.first_name, Student.last_name)
        .filter(Student.group_id == group_id)
        .order_by(Student.last_name, Student.first_name)
        .all()
    )


# 7. Оцінки студентів у окремій групі з певного предмета
def select_7(session: Session, group_id: int, subject_id: int):
    return (
        session.query(Student.first_name, Student.last_name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .order_by(Student.last_name, Student.first_name)
        .all()
    )


# 8. Середній бал, який ставить певний викладач зі своїх предметів
def select_8(session: Session, teacher_id: int):
    return (
        session.query(func.round(cast(func.avg(Grade.grade), Numeric), 2))
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )


# 9. Список курсів, які відвідує певний студент
def select_9(session: Session, student_id: int):
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .order_by(Subject.name)
        .all()
    )


# 10. Курси, які певному студенту читає певний викладач
def select_10(session: Session, student_id: int, teacher_id: int):
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .distinct()
        .order_by(Subject.name)
        .all()
    )

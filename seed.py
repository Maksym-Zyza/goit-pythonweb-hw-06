import random
from faker import Faker
from sqlalchemy.orm import Session
from database.models import Student, Group, Teacher, Subject, Grade
from database.db import engine

fake = Faker()

GROUPS = 3
TEACHERS = random.randint(3, 5)
SUBJECTS = random.randint(5, 8)
STUDENTS = random.randint(30, 50)
GRADES = random.randint(10, 20)
GRADE = random.uniform(60, 100)

with Session(engine) as session:
    # Groups
    groups = [Group(name=f"Group {i+1}") for i in range(GROUPS)]
    session.add_all(groups)
    session.commit()

    # Teachers
    teachers = [
        Teacher(first_name=fake.first_name(), last_name=fake.last_name())
        for _ in range(TEACHERS)
    ]
    session.add_all(teachers)
    session.commit()

    # Subjects
    subjects = [
        Subject(name=fake.word().capitalize(), teacher=random.choice(teachers))
        for _ in range(SUBJECTS)
    ]
    session.add_all(subjects)
    session.commit()

    # Students
    students = [
        Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group=random.choice(groups),
        )
        for _ in range(STUDENTS)
    ]
    session.add_all(students)
    session.commit()

    # Grades
    for student in students:
        for subject in subjects:
            for _ in range(GRADES):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=round(GRADE, 2),
                    date_received=fake.date_time_between(
                        start_date="-1y", end_date="now"
                    ),
                )
                session.add(grade)
    session.commit()

print("Database seeded successfully!")

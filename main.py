from database.db import get_db
from database.my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def main():
    MENU = """
    Виберіть запит для виконання:
    1 - 5 студентів із найбільшим середнім балом з усіх предметів
    2 - Студент із найвищим середнім балом з певного предмета
    3 - Середній бал у групах з певного предмета
    4 - Середній бал на потоці (по всій таблиці оцінок)
    5 - Які курси читає певний викладач
    6 - Список студентів у певній групі
    7 - Оцінки студентів у окремій групі з певного предмета
    8 - Середній бал, який ставить певний викладач зі своїх предметів
    9 - Список курсів, які відвідує певний студент
    10 - Курси, які певному студенту читає певний викладач
    0 - Вихід
    """

    def input_int(prompt: str) -> int:
        while True:
            value = input(prompt)
            try:
                return int(value)
            except ValueError:
                print("Введіть коректне число!")

    for db in get_db():
        while True:
            print(MENU)
            try:
                choice = input_int(">>> ")
            except ValueError:
                print("Введіть число!")
                continue

            if choice == 0:
                print("Вихід...")
                break

            match choice:
                case 1:
                    results = select_1(db)
                    for r in results:
                        print(r)
                case 2:
                    subject_id = input_int("Введіть subject_id: ")
                    r = select_2(db, subject_id)
                    print(r)
                case 3:
                    subject_id = input_int("Введіть subject_id: ")
                    results = select_3(db, subject_id)
                    for r in results:
                        print(r)
                case 4:
                    avg = select_4(db)
                    print(f"Середній бал по всьому потоку: {avg}")
                case 5:
                    teacher_id = input_int("Введіть teacher_id: ")
                    results = select_5(db, teacher_id)
                    for r in results:
                        print(r)
                case 6:
                    group_id = input_int("Введіть group_id: ")
                    results = select_6(db, group_id)
                    for r in results:
                        print(r)
                case 7:
                    group_id = input_int("Введіть group_id: ")
                    subject_id = input_int("Введіть subject_id: ")
                    results = select_7(db, group_id, subject_id)
                    for r in results:
                        print(r)
                case 8:
                    teacher_id = input_int("Введіть teacher_id: ")
                    avg = select_8(db, teacher_id)
                    print(f"Середній бал, який ставить викладач: {avg}")
                case 9:
                    student_id = input_int("Введіть student_id: ")
                    results = select_9(db, student_id)
                    for r in results:
                        print(r)
                case 10:
                    student_id = input_int("Введіть student_id: ")
                    teacher_id = input_int("Введіть teacher_id: ")
                    results = select_10(db, student_id, teacher_id)
                    for r in results:
                        print(r)
                case _:
                    print("Невірний вибір. Спробуйте ще.")


if __name__ == "__main__":
    main()

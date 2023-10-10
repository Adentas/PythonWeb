import sqlite3
from faker import Faker
import random

def create_data():
    
    # Створення бази даних та підключення до неї
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    # Створення таблиць
    c.execute('''CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, group_id INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS groups
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS teachers
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS subjects
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, teacher_id INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS grades
                (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, subject_id INTEGER, grade INTEGER, date TEXT)''')

    # Наповнення таблиць випадковими даними
    fake = Faker()

    # Додавання груп
    groups = ['101', '102', '103']
    c.executemany("INSERT INTO groups (name) VALUES (?)", [(group,) for group in groups])

    # Додавання студентів
    for _ in range(50):
        name = fake.name()
        group_id = random.randint(1, len(groups))
        c.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

    # Додавання викладачів
    teachers = [fake.name() for _ in range(5)]
    c.executemany("INSERT INTO teachers (name) VALUES (?)", [(teacher,) for teacher in teachers])

    # Додавання предметів та зв'язок із викладачами
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
    for subject in subjects:
        teacher_id = random.randint(1, len(teachers))
        c.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

    # Додавання оцінок
    for _ in range(200):
        student_id = random.randint(1, 50)
        subject_id = random.randint(1, len(subjects))
        grade = random.randint(60, 100)
        date = fake.date_this_decade().strftime('%Y-%m-%d')
        c.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date))

    # Збереження змін
    conn.commit()
    conn.close()

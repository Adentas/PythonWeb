from faker import Faker
from sqlalchemy import create_engine

def seed_database():
    fake = Faker()
    engine = create_engine('sqlite:///university.db')  # Вкажіть правильний URL для вашої бази даних SQLite
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Додавання груп
    group_names = ['101', '102', '103']
    groups = [Group(name=name) for name in group_names]
    session.add_all(groups)
    session.commit()

    # Додавання студентів
    students = []
    for _ in range(random.randint(30, 50)):
        fullname = fake.name()
        group = random.choice(groups)
        student = Student(fullname=fullname, group=group)
        students.append(student)
        session.add(student)
    session.commit()

    # Додавання викладачів
    teachers = []
    for _ in range(random.randint(3, 5)):
        fullname = fake.name()
        teacher = Teacher(fullname=fullname)
        teachers.append(teacher)
        session.add(teacher)
    session.commit()

    # Додавання предметів
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
    subjects_objects = []
    for subject_name in subjects:
        teacher = random.choice(teachers)
        subject = Subject(name=subject_name, teacher=teacher)
        subjects_objects.append(subject)
        session.add(subject)
    session.commit()

    # Додавання оцінок
    for student in students:
        for subject in subjects_objects:
            for _ in range(random.randint(1, 20)):
                grade = random.randint(60, 100)
                date = fake.date_this_decade()
                grade_entry = Grade(student=student, subject=subject, grade=grade, date=date)
                session.add(grade_entry)
    session.commit()

    session.close()

if __name__ == '__main__':
    seed_database()

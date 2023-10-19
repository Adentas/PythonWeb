import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade

# Підключення до бази даних
engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def create_record(model, name):
    if model == "Student":
        new_student = Student(fullname=name)
        session.add(new_student)
    elif model == "Group":
        new_group = Group(name=name)
        session.add(new_group)
    elif model == "Teacher":
        new_teacher = Teacher(name=name)
        session.add(new_teacher)
    elif model == "Subject":
        new_subject = Subject(name=name)
        session.add(new_subject)
    elif model == "Grade":
        print("To add a grade, please provide student_id, subject_id, and grade value.")
    else:
        print("Invalid model name.")

def list_records(model):
    if model == "Student":
        students = session.query(Student).all()
        for student in students:
            print(f"Student ID: {student.id}, Name: {student.fullname}")
    elif model == "Group":
        groups = session.query(Group).all()
        for group in groups:
            print(f"Group ID: {group.id}, Name: {group.name}")
    elif model == "Teacher":
        teachers = session.query(Teacher).all()
        for teacher in teachers:
            print(f"Teacher ID: {teacher.id}, Name: {teacher.name}")
    elif model == "Subject":
        subjects = session.query(Subject).all()
        for subject in subjects:
            print(f"Subject ID: {subject.id}, Name: {subject.name}")
    elif model == "Grade":
        grades = session.query(Grade).all()
        for grade in grades:
            print(f"Grade ID: {grade.id}, Student ID: {grade.student_id}, Subject ID: {grade.subject_id}, Grade: {grade.grade}")
    else:
        print("Invalid model name.")

def update_record(model, record_id, name):
    if model == "Student":
        student = session.query(Student).filter_by(id=record_id).first()
        if student:
            student.fullname = name
        else:
            print("Student not found.")
    elif model == "Group":
        group = session.query(Group).filter_by(id=record_id).first()
        if group:
            group.name = name
        else:
            print("Group not found.")
    elif model == "Teacher":
        teacher = session.query(Teacher).filter_by(id=record_id).first()
        if teacher:
            teacher.name = name
        else:
            print("Teacher not found.")
    elif model == "Subject":
        subject = session.query(Subject).filter_by(id=record_id).first()
        if subject:
            subject.name = name
        else:
            print("Subject not found.")
    elif model == "Grade":
        print("To update a grade, please provide new grade value.")
    else:
        print("Invalid model name.")

def remove_record(model, record_id):
    if model == "Student":
        student = session.query(Student).filter_by(id=record_id).first()
        if student:
            session.delete(student)
        else:
            print("Student not found.")
    elif model == "Group":
        group = session.query(Group).filter_by(id=record_id).first()
        if group:
            session.delete(group)
        else:
            print("Group not found.")
    elif model == "Teacher":
        teacher = session.query(Teacher).filter_by(id=record_id).first()
        if teacher:
            session.delete(teacher)
        else:
            print("Teacher not found.")
    elif model == "Subject":
        subject = session.query(Subject).filter_by(id=record_id).first()
        if subject:
            session.delete(subject)
        else:
            print("Subject not found.")
    elif model == "Grade":
        grade = session.query(Grade).filter_by(id=record_id).first()
        if grade:
            session.delete(grade)
        else:
            print("Grade not found.")
    else:
        print("Invalid model name.")

def main():
    parser = argparse.ArgumentParser(description="CRUD Operations CLI")
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], required=True,
                        help="Action to perform: create, list, update, or remove")
    parser.add_argument("-m", "--model", choices=["Teacher", "Group", "Student", "Subject", "Grade"], required=True,
                        help="Model on which the action will be performed")
    parser.add_argument("-n", "--name", help="Name for creating or updating")
    parser.add_argument("--id", type=int, help="ID of the record to update or remove")

    args = parser.parse_args()

    action = args.action
    model = args.model
    name = args.name
    record_id = args.id

    if action == "create":
        create_record(model, name)
    elif action == "list":
        list_records(model)
    elif action == "update":
        if record_id and name:
            update_record(model, record_id, name)
        else:
            print("Both ID and name are required for update operation.")
    elif action == "remove":
        if record_id:
            remove_record(model, record_id)
        else:
            print("ID is required for remove operation.")
    else:
        print("Invalid action.")

    session.commit()

if __name__ == "__main__":
    main()

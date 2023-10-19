from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject, Teacher, Group, engine

Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')). \
        join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

def select_2(subject_id):
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')). \
        join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id). \
        order_by(func.avg(Grade.grade).desc()).first()
    return result

def select_3(subject_id):
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')). \
        join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    return result

def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()
    return result

def select_5(teacher_name):
    result = session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()
    return result

def select_6(group_name):
    result = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    return result

def select_7(group_name, subject_id):
    result = session.query(Student.fullname, Grade.grade).join(Group).join(Grade). \
        filter(Group.name == group_name, Grade.subject_id == subject_id).all()
    return result

def select_8(teacher_name):
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')). \
        join(Subject).join(Teacher).filter(Teacher.fullname == teacher_name).scalar()
    return result

def select_9(student_name):
    result = session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).all()
    return result

def select_10(student_name, teacher_name):
    result = session.query(Subject.name).join(Grade).join(Student).join(Teacher). \
        filter(Student.fullname == student_name, Teacher.fullname == teacher_name).all()
    return result

def select_11(teacher_name, student_id):
    average_grade = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')). \
        join(Student).join(Subject).join(Teacher). \
        filter(Teacher.fullname == teacher_name, Student.id == student_id).scalar()
    return average_grade

def select_12(group_name, subject_id):
    subquery = session.query(func.max(Grade.date).label('max_date')).join(Student).join(Group). \
        filter(Group.name == group_name, Grade.subject_id == subject_id).group_by(Student.id).subquery()

    grades = session.query(Student.fullname, Grade.grade).join(subquery, Grade.date == subquery.c.max_date).all()
    return grades

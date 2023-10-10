import sqlite3
from data_creator import create_data

# Підключення до бази даних
conn = sqlite3.connect('university.db')
c = conn.cursor()

# Функція для виконання запиту без параметрів
def execute_query_without_params(query_number):
    with open(f'query_{query_number}.sql', 'r') as file:
        query = file.read()

    c.execute(query)
    result = c.fetchall()
    print(f"Query {query_number} Result:")
    print(result)

# Функція для виконання запиту з одним параметром
def execute_query_with_one_param(query_number, param1):
    with open(f'query_{query_number}.sql', 'r') as file:
        query = file.read()

    c.execute(query, (param1,))
    result = c.fetchall()
    print(f"Query {query_number} Result:")
    print(result)

# Функція для виконання запиту з двома параметрами
def execute_query_with_two_params(query_number, param1, param2):
    with open(f'query_{query_number}.sql', 'r') as file:
        query = file.read()

    c.execute(query, (param1, param2))
    result = c.fetchall()
    print(f"Query {query_number} Result:")
    print(result)

# Функція для виводу таблиці
def execute_query_table(query_number):
    with open(f'query_{query_number}.sql', 'r') as file:
        queries = file.read().split(';')

    for query in queries:
        if query.strip():  # Ігноруємо порожні запити
            c.execute(query)
            result = c.fetchall()
            print(f"Query Result:")
            print(result)

# Головне меню програми
while True:
    print("Menu:")
    print("0. Вивести таблицю university.db")
    print("1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
    print("2. Знайти студента із найвищим середнім балом з певного предмета. (параметр subject_id)")
    print("3. Знайти середній бал у групах з певного предмета. (параметр subject_id)")
    print("4. Знайти середній бал на потоці (по всій таблиці оцінок).")
    print("5. Знайти, які курси читає певний викладач. (параметр teacher_name)")
    print("6. Знайти список студентів у певній групі. (параметр group_name)")
    print("7. Знайти оцінки студентів в окремій групі з певного предмета. (параметр1 group_name)(параметр2 subject_id)")
    print("8. Знайти середній бал, який ставить певний викладач зі своїх предметів. (параметр teacher_name)")
    print("9. Знайти список курсів, які відвідує студент. (параметр student_name)")
    print("10.Список курсів, які певному студенту читає певний викладач. (параметр1 student_name)(параметр2 teacher_name)")
    print("11.Середній бал, який певний викладач ставить певному студентові. (параметр1 teacher_name)(параметр2 student_id)")
    print("12.Оцінки студентів у певній групі з певного предмета на останньому занятті. (параметр1 group_name)(параметр2 subject_name)")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice.isdigit():
        choice = int(choice)
        if choice == 13:
            break
        elif 0 <= choice <= 12:
            if choice in [2, 3, 5, 6, 8, 9]:
                param1 = input("Enter parameter: ")
                execute_query_with_one_param(choice, param1)
            elif choice in [7, 10, 11, 12]:
                param1 = input("Enter first parameter: ")
                param2 = input("Enter second parameter: ")
                execute_query_with_two_params(choice, param1, param2)
            elif choice in [0]:
                execute_query_table(choice)
            else:
                execute_query_without_params(choice)
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid input. Please enter a number.")

file.close()

# Закрийте з'єднання
conn.close()

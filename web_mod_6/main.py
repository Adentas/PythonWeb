import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
c = conn.cursor()

# Виконання SQL запитів
with open('query_1.sql', 'r') as file:
    query_1 = file.read()

c.execute(query_1)
result_1 = c.fetchall()
print("Query 1 Result:")
print(result_1)

file.close()

with open('query_2.sql', 'r') as file:
    query_2 = file.read()

param_value = input("Write subject... ")
c.execute(query_2, (param_value,))
result_2 = c.fetchall()
print("Query 2 Result:")
print(result_2)

file.close()

with open('query_3.sql', 'r') as file:
    query_3 = file.read()

param_value = input("Write subject... ")
c.execute(query_3, (param_value,))
result_3 = c.fetchall()
print("Query 3 Result:")
print(result_3)

file.close()

with open('query_4.sql', 'r') as file:
    query_4 = file.read()

c.execute(query_4)
result_4 = c.fetchall()
print("Query 4 Result:")
print(result_4)

file.close()

with open('query_5.sql', 'r') as file:
    query_5 = file.read()

param_value = input("Write teachers... ")
c.execute(query_5, (param_value,))
result_5 = c.fetchall()
print("Query 5 Result:")
print(result_5)

file.close()

with open('query_6.sql', 'r') as file:
    query_6 = file.read()

param_value = input("Write group... ")
c.execute(query_6, (param_value,))
result_6 = c.fetchall()
print("Query 6 Result:")
print(result_6)

file.close()

with open('query_7.sql', 'r') as file:
    query_7 = file.read()

param1_value = input("Write group... ")
param2_value = input("Write subject... ")
c.execute(query_7, (param1_value, param2_value))
result_7 = c.fetchall()
print("Query 7 Result:")
print(result_7)

file.close()

with open('query_8.sql', 'r') as file:
    query_8 = file.read()

param_value = input("Write teacher... ")
c.execute(query_8, (param_value,))
result_8 = c.fetchall()
print("Query 8 Result:")
print(result_8)

file.close()

with open('query_9.sql', 'r') as file:
    query_9 = file.read()

param_value = input("Write student... ")
c.execute(query_9, (param_value,))
result_9 = c.fetchall()
print("Query 9 Result:")
print(result_9)

file.close()

with open('query_10.sql', 'r') as file:
    query_10 = file.read()

param1_value = input("Write student... ")
param2_value = input("Write teacher... ")
c.execute(query_10, (param1_value, param2_value))
result_10 = c.fetchall()
print("Query 10 Result:")
print(result_10)

file.close()

# Закрийте з'єднання
conn.close()

# Data Generator and Query Executor

## Overview

This project aims to generate a SQLite database with fake data and execute SQL queries on it. The project consists of multiple Python files and SQL query files to handle the database creation, data generation, and query execution.

## Files Description

### Python Files

- `main.py`: The main entry point to the program. It imports functions from other Python files to create a database and fill it with data. Contains a menu for managing functionality.
- `data_creator.py`: Contains functions for generating fake data for the database using the Faker library.

### SQL Files
- `query_1.sql, query_2.sql, query_3.sql, query_4.sql, query_5.sql, query_6.sql, query_7.sql, query_8.sql, query_9.sql, query_10.sql, query_11.sql and query_12.sql`: These files contain various SQL queries to perform specific tasks in the database.
- `query_0.sql`: This file contains a simple output of the generated table


## SQL Query Descriptions
`query_1.sql`: Identifies the top 5 students with the highest GPAs in all subjects.
`query_2.sql`: Identifies the student with the highest GPA in a particular subject.
`query_3.sql`: Calculates the average score for groups in a particular subject.
`query_4.sql`: Calculates the grade point average for the entire grade table.
`query_5.sql`: Displays a list of courses taught by a particular teacher.
`query_6.sql`: Displays the list of students in a particular group.
`query_7.sql`: Displays the grades of students in a particular group for a particular subject.
`query_8.sql`: Finds the average grade given by a particular teacher for all subjects.
`query_9.sql`: Displays the list of courses taken by a specific student.
`query_10.sql`: Displays the list of courses taught by a specific teacher to a specific student.
`query_11.sql`: Calculates the average grade that a particular teacher gives to a particular student.
`query_12.sql`: Displays the grades of students in a particular group in a particular subject for the last lesson.


## How to Use

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run `python main.py` to create, populate the database and execute SQL queries...

## Dependencies

- Python 3.11.4
- SQLite
- Faker library

## Author

[Illya Hryhoriev]

## License

MIT License
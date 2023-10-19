
# University Database Management

A Python application designed to manage and seed a university's database with entities such as teachers, students, groups, and subjects. The project utilizes SQLAlchemy for ORM, Alembic for database migrations, and is containerized using Docker.

## Database Models:

1. **Group**: Represents university groups or classes.
2. **Student**: Represents individual students associated with groups.
3. **Teacher**: Represents individual teachers.
4. **Subject**: Represents subjects taught in the university.

## Features:

- Seeding the database with fake data for testing purposes.
- Alembic migrations for database version control.
- Dockerized setup for consistent environment.

## Query and Data Display:

The project includes a module `my_select.py` with functionalities such as:

1. **Queries**: Retrieve specific data from the database, like the top five students based on their average grades.

## Getting Started:

1. **Docker Setup**: Build and run the Docker container using the provided `Dockerfile`.
2. **Configurations**: Modify the `config.ini` file for database credentials.
3. **Database Setup**: Use Alembic to handle migrations and set up the database structure.
4. **Seeding**: Run `main.py` to populate the database with initial data.
5. **Queries**: Use functions from `my_select.py` to execute and display specific queries.
# Use an official Python runtime as a parent image
FROM python:3.10.8

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in poetry.lock
RUN poetry install


# Run our application inside the container
ENTRYPOINT ["python", "main.py"]
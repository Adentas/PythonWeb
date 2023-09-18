# The Docker command FROM specifies the base image of the container.
# Our base image is Linux with Python 3.10 pre-installed.
FROM python:3.10.8

# Set an environment variable
ENV APP_HOME /app

ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory inside the container
WORKDIR $APP_HOME

# Copy the other files to the working directory of the container
COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock

# Install dependencies inside the container
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main

COPY . .

# Specify the port on which the application runs inside the container
EXPOSE 5000

# Run our application inside the container
ENTRYPOINT ["python", "src/main.py"]
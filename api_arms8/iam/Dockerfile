# # FROM python:3.12.2-bullseye
# # COPY ./requirements.txt .
# # RUN pip3 install -r requirements.txt
# # COPY . .
# # RUN python3 manage.py migrate
# # RUN python3 manage.py test
# # EXPOSE 8000
# # CMD python3 manage.py runserver 0.0.0.0:8000

# # Use the official Python image as a base image
# FROM python:3.12.2-bullseye

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt /app/

# # Install dependencies
# RUN pip3 install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app/

# # Run migrations
# CMD python3 manage.py migrate

# # Start the Django development server
# CMD python3 manage.py runserver 0.0.0.0:8000
# Use the official Python image as a base image
FROM python:3.12.2-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Run migrations
RUN python3 manage.py migrate

# Start the Django development server
CMD python3 manage.py runserver 0.0.0.0:8000

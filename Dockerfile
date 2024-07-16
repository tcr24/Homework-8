# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run tests before running the application
RUN pytest tests/test_app.py

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["python", "app/main.py"]


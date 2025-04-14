# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to the container's /app directory
COPY . /app

# Expose the port the app will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

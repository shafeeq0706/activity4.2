# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (Flask default is 5000)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

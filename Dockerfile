# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all the project files to the container
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "main.py"]

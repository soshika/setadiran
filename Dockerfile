# Use the official Python image as a parent image
FROM python:3.9

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]

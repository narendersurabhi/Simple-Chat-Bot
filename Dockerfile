# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variable for the port
ENV PORT=3050

# Expose the port that the app runs on
EXPOSE ${PORT}

# Specify the command to run the app
CMD ["sh", "-c", "python app.py"]

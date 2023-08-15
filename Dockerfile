# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org scikit-learn pandas

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME SentimentAnalysis

# Run sentiment_analysis.py when the container launches
CMD ["python", "sentiment_analysis.py"]

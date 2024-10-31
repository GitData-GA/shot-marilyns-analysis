# Use the official Python 3.10.12 image from Docker Hub
FROM python:3.10.12

# Set the working directory
WORKDIR /

# Copy the requirements.txt file to the container
COPY src/requirements.txt requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Set the command to run your application
CMD ["python", "main.py"]

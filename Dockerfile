FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Change to the project directory
WORKDIR /app/vapecraft-parser

# Copy repository files
COPY . .

# Install the required dependencies
RUN pip install -r requirements.txt

# Set the entrypoint to run the application
ENTRYPOINT ["python", "parser.py"]
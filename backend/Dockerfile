FROM python:3.9-slim

FROM python:3.9  # Ensure you're using an official Python base image

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libsqlite3-dev

COPY requirements.txt .

# Update pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p uploads

# Your remaining Dockerfile commands...
#CMD ["gunicorn", "app:app"]  # Example command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

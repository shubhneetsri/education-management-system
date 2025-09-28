# ✅ Use official Python image with specific version
FROM python:3.13.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=2.1.3
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/app"

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry pinned version
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION

# Copy only pyproject.toml and poetry.lock first (for Docker layer caching)
COPY pyproject.toml poetry.lock ./

# Install dependencies system-wide (no virtual environment)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction

# Install poetry export plugin to generate requirements.txt
RUN poetry self add poetry-plugin-export

# Export requirements.txt for CI/CD or AWS Lambda
RUN poetry export -f requirements.txt --without-hashes --output requirements.txt

# Copy full project files
COPY . .

# Expose the port Uvicorn will run on
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "education_management_system.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

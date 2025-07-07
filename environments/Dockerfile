FROM python:3.12-slim

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY environments/.env* ./environments/
COPY pyproject.toml uv.lock ./

RUN uv venv
RUN uv sync

COPY . .

# CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "-p", "8000"]
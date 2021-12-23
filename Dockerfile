FROM python:3.9

LABEL description="A simple bank core app for mentoring purpose" \
      author="Oleksandr6676" \
      contributor="JanMate" \
      app="happy-bank-core" \
      version=1.0.0

ENV PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    POETRY_VERSION=1.1.2 \
    USER_NAME=core

# Create system user with less privileges than root
RUN adduser --system "${USER_NAME}"
USER "${USER_NAME}"

# Update path env var with path to user's binaries
ENV PATH="${PATH}:/home/${USER_NAME}/.local/bin"

# Install poetry
RUN pip install --no-cache-dir --upgrade pip \
    && curl -sSL "https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py" | python -

WORKDIR /app

# Add source code
COPY pyproject.toml poetry.lock .
COPY core core

# Setup app deps
RUN poetry install --no-dev --no-interaction --no-ansi

# Run flask app via poetry in generated venv
ENTRYPOINT ["poetry", "run"]
CMD ["python3", "core/app.py"]
